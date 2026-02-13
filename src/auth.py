"""
Authentication Module
User authentication, JWT tokens, and role-based access control
"""

import os
import sqlite3
from datetime import datetime, timedelta
from typing import Optional, Dict, List
from pathlib import Path
from passlib.context import CryptContext
from jose import JWTError, jwt
from enum import Enum


class UserRole(Enum):
    """User roles for RBAC"""
    ADMIN = "admin"
    ANALYST = "analyst"
    VIEWER = "viewer"


# Password hashing (using argon2 - more secure and modern than bcrypt)
pwd_context = CryptContext(schemes=["argon2"], deprecated="auto")

# JWT settings
SECRET_KEY = os.getenv("JWT_SECRET_KEY", "your-secret-key-change-in-production-please")
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 1440  # 24 hours


class UserAuth:
    """User authentication and management"""
    
    def __init__(self, db_path: str = "data/users.db"):
        """Initialize user authentication system"""
        self.db_path = db_path
        Path(db_path).parent.mkdir(parents=True, exist_ok=True)
        self.conn = sqlite3.connect(db_path, check_same_thread=False)
        self.conn.row_factory = sqlite3.Row
        self._initialize_db()
        
    def _initialize_db(self):
        """Create users table if it doesn't exist"""
        cursor = self.conn.cursor()
        
        # Users table
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT UNIQUE NOT NULL,
                email TEXT UNIQUE NOT NULL,
                full_name TEXT,
                hashed_password TEXT NOT NULL,
                role TEXT NOT NULL,
                is_active BOOLEAN DEFAULT 1,
                created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
                last_login DATETIME
            )
        """)
        
        # API Keys table
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS api_keys (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id INTEGER NOT NULL,
                key_name TEXT NOT NULL,
                api_key TEXT NOT NULL,
                created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
                last_used DATETIME,
                FOREIGN KEY (user_id) REFERENCES users(id)
            )
        """)
        
        # Create default admin if no users exist
        cursor.execute("SELECT COUNT(*) FROM users")
        if cursor.fetchone()[0] == 0:
            self._create_default_admin()
        
        self.conn.commit()
    
    def _create_default_admin(self):
        """Create default admin user"""
        cursor = self.conn.cursor()
        hashed_password = self.hash_password("admin123")
        
        cursor.execute("""
            INSERT INTO users (username, email, full_name, hashed_password, role)
            VALUES (?, ?, ?, ?, ?)
        """, ("admin", "admin@securitymonitor.local", "System Administrator", 
              hashed_password, UserRole.ADMIN.value))
        
        self.conn.commit()
        print("✅ Default admin user created: username='admin', password='admin123'")
    
    def hash_password(self, password: str) -> str:
        """Hash a password"""
        return pwd_context.hash(password)
    
    def verify_password(self, plain_password: str, hashed_password: str) -> bool:
        """Verify a password against its hash"""
        return pwd_context.verify(plain_password, hashed_password)
    
    def create_access_token(self, data: dict) -> str:
        """Create JWT access token"""
        to_encode = data.copy()
        expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
        to_encode.update({"exp": expire})
        encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
        return encoded_jwt
    
    def verify_token(self, token: str) -> Optional[Dict]:
        """Verify and decode JWT token"""
        try:
            payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
            return payload
        except JWTError:
            return None
    
    def authenticate_user(self, username: str, password: str) -> Optional[Dict]:
        """Authenticate user with username and password"""
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM users WHERE username = ? AND is_active = 1", (username,))
        user = cursor.fetchone()
        
        if not user:
            return None
        
        if not self.verify_password(password, user['hashed_password']):
            return None
        
        # Update last login
        cursor.execute("UPDATE users SET last_login = ? WHERE id = ?", 
                      (datetime.utcnow(), user['id']))
        self.conn.commit()
        
        return {
            'id': user['id'],
            'username': user['username'],
            'email': user['email'],
            'full_name': user['full_name'],
            'role': user['role']
        }
    
    def register_user(self, username: str, email: str, password: str, 
                     full_name: str, role: str = UserRole.ANALYST.value) -> Dict:
        """Register a new user"""
        cursor = self.conn.cursor()
        
        # Check if username or email exists
        cursor.execute("SELECT id FROM users WHERE username = ? OR email = ?", 
                      (username, email))
        if cursor.fetchone():
            raise ValueError("Username or email already exists")
        
        # Validate role
        if role not in [r.value for r in UserRole]:
            raise ValueError("Invalid role")
        
        hashed_password = self.hash_password(password)
        
        cursor.execute("""
            INSERT INTO users (username, email, full_name, hashed_password, role)
            VALUES (?, ?, ?, ?, ?)
        """, (username, email, full_name, hashed_password, role))
        
        self.conn.commit()
        user_id = cursor.lastrowid
        
        return {
            'id': user_id,
            'username': username,
            'email': email,
            'full_name': full_name,
            'role': role
        }
    
    def get_user_by_id(self, user_id: int) -> Optional[Dict]:
        """Get user by ID"""
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM users WHERE id = ?", (user_id,))
        user = cursor.fetchone()
        
        if not user:
            return None
        
        return {
            'id': user['id'],
            'username': user['username'],
            'email': user['email'],
            'full_name': user['full_name'],
            'role': user['role'],
            'is_active': user['is_active'],
            'created_at': user['created_at'],
            'last_login': user['last_login']
        }
    
    def get_all_users(self) -> List[Dict]:
        """Get all users (Admin only)"""
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM users ORDER BY created_at DESC")
        users = cursor.fetchall()
        
        return [{
            'id': user['id'],
            'username': user['username'],
            'email': user['email'],
            'full_name': user['full_name'],
            'role': user['role'],
            'is_active': user['is_active'],
            'created_at': user['created_at'],
            'last_login': user['last_login']
        } for user in users]
    
    def update_user_role(self, user_id: int, new_role: str) -> bool:
        """Update user role (Admin only)"""
        if new_role not in [r.value for r in UserRole]:
            raise ValueError("Invalid role")
        
        cursor = self.conn.cursor()
        cursor.execute("UPDATE users SET role = ? WHERE id = ?", (new_role, user_id))
        self.conn.commit()
        return cursor.rowcount > 0
    
    def deactivate_user(self, user_id: int) -> bool:
        """Deactivate user (Admin only)"""
        cursor = self.conn.cursor()
        cursor.execute("UPDATE users SET is_active = 0 WHERE id = ?", (user_id,))
        self.conn.commit()
        return cursor.rowcount > 0
    
    def activate_user(self, user_id: int) -> bool:
        """Activate user (Admin only)"""
        cursor = self.conn.cursor()
        cursor.execute("UPDATE users SET is_active = 1 WHERE id = ?", (user_id,))
        self.conn.commit()
        return cursor.rowcount > 0
    
    def add_api_key(self, user_id: int, key_name: str, api_key: str) -> bool:
        """Add API key for user"""
        cursor = self.conn.cursor()
        cursor.execute("""
            INSERT INTO api_keys (user_id, key_name, api_key)
            VALUES (?, ?, ?)
        """, (user_id, key_name, api_key))
        self.conn.commit()
        return True
    
    def get_user_api_keys(self, user_id: int) -> List[Dict]:
        """Get all API keys for a user"""
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM api_keys WHERE user_id = ?", (user_id,))
        keys = cursor.fetchall()
        
        return [{
            'id': key['id'],
            'key_name': key['key_name'],
            'api_key': key['api_key'][:20] + '...' if len(key['api_key']) > 20 else key['api_key'],
            'created_at': key['created_at'],
            'last_used': key['last_used']
        } for key in keys]
    
    def delete_api_key(self, key_id: int, user_id: int) -> bool:
        """Delete API key"""
        cursor = self.conn.cursor()
        cursor.execute("DELETE FROM api_keys WHERE id = ? AND user_id = ?", 
                      (key_id, user_id))
        self.conn.commit()
        return cursor.rowcount > 0


# Global auth instance
auth = UserAuth()
