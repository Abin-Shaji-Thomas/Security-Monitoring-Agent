"""
Export Utilities
Export analysis results to multiple formats (CSV, JSON, Excel)
"""

import csv
import json
import io
from typing import Dict, List, Any
from datetime import datetime
import xlsxwriter


class DataExporter:
    """
    Export analysis data to various formats
    """
    
    def __init__(self):
        self.last_analysis = None
    
    def store_analysis(self, analysis_data: Dict[str, Any]):
        """Store the latest analysis for export"""
        self.last_analysis = analysis_data
    
    def export_to_csv(self) -> str:
        """
        Export threats to CSV format
        
        Returns:
            CSV string
        """
        if not self.last_analysis:
            raise ValueError("No analysis data available")
        
        output = io.StringIO()
        writer = csv.writer(output)
        
        # Write header
        writer.writerow([
            'Threat Type',
            'Severity',
            'Risk Score',
            'Confidence',
            'Description',
            'Recommendation',
            'Source IP',
            'Country',
            'Affected Resources'
        ])
        
        # Write threat data
        threats = self.last_analysis.get('threats', [])
        for threat in threats:
            writer.writerow([
                threat.get('type', ''),
                threat.get('severity', ''),
                threat.get('risk_score', ''),
                threat.get('confidence', ''),
                threat.get('description', ''),
                threat.get('recommendation', ''),
                threat.get('source_ip', ''),
                threat.get('country', ''),
                ', '.join(threat.get('affected', []))
            ])
        
        return output.getvalue()
    
    def export_to_json(self) -> str:
        """
        Export full analysis to JSON format
        
        Returns:
            JSON string
        """
        if not self.last_analysis:
            raise ValueError("No analysis data available")
        
        export_data = {
            'timestamp': datetime.now().isoformat(),
            'analysis': self.last_analysis,
            'metadata': {
                'version': '2.0.0',
                'export_format': 'json'
            }
        }
        
        return json.dumps(export_data, indent=2)
    
    def export_to_excel(self) -> bytes:
        """
        Export comprehensive analysis to Excel format
        
        Returns:
            Excel file as bytes
        """
        if not self.last_analysis:
            raise ValueError("No analysis data available")
        
        output = io.BytesIO()
        workbook = xlsxwriter.Workbook(output, {'in_memory': True})
        
        # Formats
        header_format = workbook.add_format({
            'bold': True,
            'bg_color': '#4472C4',
            'font_color': 'white',
            'border': 1
        })
        
        critical_format = workbook.add_format({
            'bg_color': '#FFC7CE',
            'font_color': '#9C0006'
        })
        
        high_format = workbook.add_format({
            'bg_color': '#FFF3CD',
            'font_color': '#856404'
        })
        
        # Summary Sheet
        summary_sheet = workbook.add_worksheet('Summary')
        summary_sheet.set_column('A:B', 30)
        
        row = 0
        summary_sheet.write(row, 0, 'Security Analysis Report', header_format)
        summary_sheet.write(row, 1, '', header_format)
        row += 2
        
        overall = self.last_analysis.get('overall_security', {})
        summary_sheet.write(row, 0, 'Overall Security Score')
        summary_sheet.write(row, 1, f"{overall.get('health_score', 0):.1f}/100")
        row += 1
        
        summary_sheet.write(row, 0, 'Health Status')
        summary_sheet.write(row, 1, overall.get('health_status', 'Unknown'))
        row += 1
        
        summary_sheet.write(row, 0, 'Total Threats Detected')
        summary_sheet.write(row, 1, len(self.last_analysis.get('threats', [])))
        row += 2
        
        # Compression Stats
        stats = self.last_analysis.get('compression_stats', {})
        summary_sheet.write(row, 0, 'Original Tokens', header_format)
        summary_sheet.write(row, 1, stats.get('original_tokens', 0))
        row += 1
        
        summary_sheet.write(row, 0, 'Compressed Tokens', header_format)
        summary_sheet.write(row, 1, stats.get('compressed_tokens', 0))
        row += 1
        
        summary_sheet.write(row, 0, 'Tokens Saved', header_format)
        summary_sheet.write(row, 1, stats.get('tokens_saved', 0))
        row += 1
        
        savings = self.last_analysis.get('cost_savings', {})
        summary_sheet.write(row, 0, 'Percentage Saved', header_format)
        summary_sheet.write(row, 1, f"{savings.get('percentage_saved', 0):.1f}%")
        
        # Threats Sheet
        threats_sheet = workbook.add_worksheet('Threats')
        threats_sheet.set_column('A:A', 25)
        threats_sheet.set_column('B:B', 12)
        threats_sheet.set_column('C:C', 12)
        threats_sheet.set_column('D:D', 50)
        threats_sheet.set_column('E:E', 50)
        threats_sheet.set_column('F:F', 15)
        threats_sheet.set_column('G:G', 20)
        
        headers = ['Threat Type', 'Severity', 'Risk Score', 'Description', 
                   'Recommendation', 'Source IP', 'Country']
        
        for col, header in enumerate(headers):
            threats_sheet.write(0, col, header, header_format)
        
        threats = self.last_analysis.get('threats', [])
        for row, threat in enumerate(threats, start=1):
            severity = threat.get('severity', '').upper()
            row_format = critical_format if severity == 'CRITICAL' else \
                        high_format if severity == 'HIGH' else None
            
            threats_sheet.write(row, 0, threat.get('type', ''), row_format)
            threats_sheet.write(row, 1, threat.get('severity', ''), row_format)
            threats_sheet.write(row, 2, threat.get('risk_score', ''), row_format)
            threats_sheet.write(row, 3, threat.get('description', ''), row_format)
            threats_sheet.write(row, 4, threat.get('recommendation', ''), row_format)
            threats_sheet.write(row, 5, threat.get('source_ip', ''), row_format)
            threats_sheet.write(row, 6, threat.get('country', ''), row_format)
        
        # IP Intelligence Sheet (if available)
        ip_data = self.last_analysis.get('ip_intelligence', {})
        if ip_data and ip_data.get('threat_ips'):
            ip_sheet = workbook.add_worksheet('IP Intelligence')
            ip_sheet.set_column('A:D', 20)
            
            ip_headers = ['IP Address', 'Country', 'Threat Level', 'ISP']
            for col, header in enumerate(ip_headers):
                ip_sheet.write(0, col, header, header_format)
            
            for row, ip_info in enumerate(ip_data.get('threat_ips', []), start=1):
                ip_sheet.write(row, 0, ip_info.get('ip', ''))
                ip_sheet.write(row, 1, ip_info.get('country', ''))
                ip_sheet.write(row, 2, ip_info.get('threat_level', ''))
                ip_sheet.write(row, 3, ip_info.get('isp', ''))
        
        workbook.close()
        output.seek(0)
        return output.getvalue()


# Global exporter instance
exporter = DataExporter()
