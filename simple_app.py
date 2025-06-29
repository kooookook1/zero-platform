#!/usr/bin/env python3
"""
ZERO Platform - Cybersecurity Testing Platform (Simplified Version)
© 2025 ZERO Platform. All rights reserved.

This platform provides various cybersecurity testing tools for educational purposes only.
"""

from flask import Flask, render_template, request, jsonify, session, redirect, url_for, flash, Response
from flask_cors import CORS
import subprocess
import threading
import json
import os
import uuid
import time
from datetime import datetime
import logging
from werkzeug.utils import secure_filename

app = Flask(__name__)
CORS(app, origins="*")
app.secret_key = 'zero-platform-2025-secret-key'

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Configuration
UPLOAD_FOLDER = '/tmp/zero-uploads'
RESULTS_FOLDER = '/tmp/zero-results'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(RESULTS_FOLDER, exist_ok=True)

# Tool configurations (same as before)
TOOLS_CONFIG = {
    'web_testing': {
        'name': 'اختبار الويب والثغرات',
        'tools': {
            'sqlmap': {
                'name': 'SQLMap - اختبار حقن SQL',
                'description': 'أداة قوية لاكتشاف واستغلال ثغرات حقن SQL',
                'command': 'sqlmap',
                'params': ['--url', '--batch', '--level=3', '--risk=2']
            },
            'nikto': {
                'name': 'Nikto - فحص ثغرات الويب',
                'description': 'فحص شامل لثغرات خوادم الويب',
                'command': 'nikto',
                'params': ['-h']
            },
            'dirb': {
                'name': 'DirB - اكتشاف المجلدات المخفية',
                'description': 'البحث عن مجلدات وملفات مخفية في المواقع',
                'command': 'dirb',
                'params': []
            },
            'whatweb': {
                'name': 'WhatWeb - تحليل تقنيات الموقع',
                'description': 'اكتشاف التقنيات والإضافات المستخدمة',
                'command': 'whatweb',
                'params': ['--aggression=3']
            },
            'wpscan': {
                'name': 'WPScan - فحص ووردبريس',
                'description': 'فحص متخصص لمواقع ووردبريس',
                'command': 'wpscan',
                'params': ['--url', '--enumerate', 'vp,vt,tt,cb,dbe']
            }
        }
    },
    'network_scanning': {
        'name': 'فحص الشبكات والخدمات',
        'tools': {
            'nmap': {
                'name': 'Nmap - مسح الشبكات',
                'description': 'أداة مسح الشبكات والبورتات الأكثر شهرة',
                'command': 'nmap',
                'params': ['-sS', '-sV', '-O', '--script=vuln']
            },
            'masscan': {
                'name': 'Masscan - مسح سريع',
                'description': 'مسح سريع جداً للبورتات',
                'command': 'masscan',
                'params': ['-p1-65535', '--rate=1000']
            },
            'hping3': {
                'name': 'Hping3 - اختبار الاستجابة',
                'description': 'اختبار استجابة الشبكة وفحص الجدران النارية',
                'command': 'hping3',
                'params': ['-S', '-p', '80', '-c', '10']
            },
            'dnsenum': {
                'name': 'DNSEnum - تعداد DNS',
                'description': 'جمع معلومات DNS والنطاقات الفرعية',
                'command': 'dnsenum',
                'params': ['--enum']
            },
            'snmpcheck': {
                'name': 'SNMP-Check - فحص SNMP',
                'description': 'فحص خدمات SNMP واستخراج المعلومات',
                'command': 'snmp-check',
                'params': ['-c', 'public']
            }
        }
    },
    'password_attacks': {
        'name': 'هجمات كلمات المرور',
        'tools': {
            'hydra': {
                'name': 'Hydra - هجوم القوة الغاشمة',
                'description': 'هجمات brute-force على خدمات مختلفة',
                'command': 'hydra',
                'params': ['-l', 'admin', '-P']
            },
            'john': {
                'name': 'John the Ripper - كسر الهاش',
                'description': 'كسر كلمات المرور المشفرة',
                'command': 'john',
                'params': ['--wordlist=/usr/share/wordlists/rockyou.txt']
            },
            'hashid': {
                'name': 'Hash-Identifier - تحديد نوع الهاش',
                'description': 'تحديد نوع التشفير المستخدم',
                'command': 'hash-identifier',
                'params': []
            },
            'cewl': {
                'name': 'CeWL - توليد قوائم كلمات',
                'description': 'توليد قوائم كلمات مرور من المواقع',
                'command': 'cewl',
                'params': ['-d', '2', '-m', '5']
            },
            'crunch': {
                'name': 'Crunch - توليد كلمات مخصصة',
                'description': 'توليد قوائم كلمات مرور مخصصة',
                'command': 'crunch',
                'params': ['8', '8', 'abcdefghijklmnopqrstuvwxyz0123456789']
            }
        }
    }
}

def run_tool_command(tool_category, tool_name, params):
    """Execute a tool command and return output"""
    try:
        tool_config = TOOLS_CONFIG[tool_category]['tools'][tool_name]
        
        # Check if real tool exists, otherwise use demo
        real_command = tool_config['command']
        if subprocess.run(['which', real_command], capture_output=True).returncode != 0:
            # Use demo tool
            command = ['python3', 'demo_tools.py', tool_name] + params
            logger.info(f"Real tool {real_command} not found, using demo")
        else:
            command = [real_command] + params
        
        # Log the command
        logger.info(f"Executing: {' '.join(command)}")
        
        # Run the process
        process = subprocess.run(
            command,
            capture_output=True,
            text=True,
            timeout=60  # 60 second timeout
        )
        
        return {
            'success': True,
            'stdout': process.stdout,
            'stderr': process.stderr,
            'returncode': process.returncode,
            'command': ' '.join(command)
        }
        
    except subprocess.TimeoutExpired:
        return {
            'success': False,
            'error': 'انتهت مهلة تشغيل الأداة (60 ثانية)',
            'command': ' '.join(command) if 'command' in locals() else 'Unknown'
        }
    except Exception as e:
        logger.error(f"Error executing tool: {str(e)}")
        return {
            'success': False,
            'error': str(e),
            'command': ' '.join(command) if 'command' in locals() else 'Unknown'
        }

@app.route('/')
def index():
    """Main landing page with disclaimer"""
    return render_template('simple.html')

@app.route('/full')
def full_index():
    """Full featured landing page"""
    return render_template('index.html')

@app.route('/disclaimer')
def disclaimer():
    """Disclaimer page"""
    return render_template('disclaimer.html')

@app.route('/accept_disclaimer', methods=['POST'])
def accept_disclaimer():
    """Accept disclaimer and proceed to dashboard"""
    session['disclaimer_accepted'] = True
    session['user_id'] = str(uuid.uuid4())
    return redirect(url_for('dashboard'))

@app.route('/dashboard')
def dashboard():
    """Main dashboard with tool categories"""
    if not session.get('disclaimer_accepted'):
        return redirect(url_for('disclaimer'))
    
    return render_template('dashboard.html', tools_config=TOOLS_CONFIG)

@app.route('/tools/<category>')
def tools_page(category):
    """Individual tool category page"""
    if not session.get('disclaimer_accepted'):
        return redirect(url_for('disclaimer'))
    
    if category not in TOOLS_CONFIG:
        flash('فئة الأدوات غير موجودة', 'error')
        return redirect(url_for('dashboard'))
    
    return render_template('simple_tools.html', 
                         category=category, 
                         tools=TOOLS_CONFIG[category])

@app.route('/run_tool', methods=['POST'])
def run_tool():
    """Execute a tool with given parameters"""
    if not session.get('disclaimer_accepted'):
        return jsonify({'error': 'يجب قبول إخلاء المسؤولية أولاً'}), 403
    
    data = request.get_json()
    category = data.get('category')
    tool_name = data.get('tool')
    params = data.get('params', [])
    
    if not category or not tool_name:
        return jsonify({'error': 'معاملات مفقودة'}), 400
    
    if category not in TOOLS_CONFIG or tool_name not in TOOLS_CONFIG[category]['tools']:
        return jsonify({'error': 'أداة غير موجودة'}), 404
    
    # Execute the tool
    result = run_tool_command(category, tool_name, params)
    
    return jsonify(result)

@app.route('/api/status')
def api_status():
    """API status endpoint"""
    return jsonify({
        'status': 'online',
        'platform': 'ZERO Platform',
        'version': '1.0.0',
        'tools_available': len([tool for category in TOOLS_CONFIG.values() for tool in category['tools']]),
        'disclaimer_required': True
    })

if __name__ == '__main__':
    # Run the application
    print("🔥 ZERO Platform Starting...")
    print("© 2025 ZERO Platform. All rights reserved.")
    print(f"Server running on: http://0.0.0.0:5000")
    print(f"Local access: http://localhost:5000")
    print(f"Network access: http://10.2.32.34:5000")
    app.run(host='0.0.0.0', port=5000, debug=False, threaded=True)