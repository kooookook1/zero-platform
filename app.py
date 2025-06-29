#!/usr/bin/env python3
"""
ZERO Platform - Cybersecurity Testing Platform
© 2025 ZERO Platform. All rights reserved.

This platform provides various cybersecurity testing tools for educational purposes only.
"""

from flask import Flask, render_template, request, jsonify, session, redirect, url_for, flash
from flask_socketio import SocketIO, emit
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
app.secret_key = 'zero-platform-2025-secret-key'
socketio = SocketIO(app, cors_allowed_origins="*")

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Configuration
UPLOAD_FOLDER = '/tmp/zero-uploads'
RESULTS_FOLDER = '/tmp/zero-results'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(RESULTS_FOLDER, exist_ok=True)

# Tool configurations
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
    },
    'android_tools': {
        'name': 'أدوات أندرويد',
        'tools': {
            'msfvenom': {
                'name': 'MSFVenom - توليد APK ملغم',
                'description': 'توليد تطبيقات أندرويد مع backdoor',
                'command': 'msfvenom',
                'params': ['-p', 'android/meterpreter/reverse_tcp', '-f', 'raw']
            },
            'apktool': {
                'name': 'APKTool - تفكيك APK',
                'description': 'تفكيك وإعادة بناء تطبيقات أندرويد',
                'command': 'apktool',
                'params': ['d']
            },
            'objection': {
                'name': 'Objection - تخطي الحمايات',
                'description': 'تخطي حمايات التطبيقات وتشغيل أوامر',
                'command': 'objection',
                'params': ['--gadget']
            },
            'drozer': {
                'name': 'Drozer - استغلال التطبيقات',
                'description': 'استغلال ثغرات تطبيقات أندرويد',
                'command': 'drozer',
                'params': ['console', 'connect']
            },
            'jadx': {
                'name': 'JADX - ديكومبايل Java',
                'description': 'تحويل ملفات APK إلى كود Java',
                'command': 'jadx',
                'params': ['-d']
            }
        }
    },
    'wifi_attacks': {
        'name': 'هجمات الواي فاي',
        'tools': {
            'aircrack': {
                'name': 'Aircrack-ng - كسر WPA/WPA2',
                'description': 'كسر كلمات مرور الواي فاي',
                'command': 'aircrack-ng',
                'params': ['-w']
            },
            'reaver': {
                'name': 'Reaver - هجوم WPS',
                'description': 'هجوم brute-force على WPS',
                'command': 'reaver',
                'params': ['-i', '-b', '-vv']
            },
            'wifite': {
                'name': 'Wifite - هجوم آلي',
                'description': 'أداة آلية لهجمات الواي فاي',
                'command': 'wifite',
                'params': ['--kill']
            },
            'hcxdumptool': {
                'name': 'HCXDumpTool - PMKID Attack',
                'description': 'هجوم PMKID المباشر',
                'command': 'hcxdumptool',
                'params': ['-i', '-o']
            },
            'bettercap': {
                'name': 'Bettercap - MITM WiFi',
                'description': 'هجمات MITM على الواي فاي',
                'command': 'bettercap',
                'params': ['-iface']
            }
        }
    },
    'bluetooth_attacks': {
        'name': 'هجمات البلوتوث',
        'tools': {
            'bluelog': {
                'name': 'Bluelog - مسح البلوتوث',
                'description': 'مسح أجهزة البلوتوث القريبة',
                'command': 'bluelog',
                'params': ['-i', 'hci0']
            },
            'blue_hydra': {
                'name': 'Blue Hydra - مسح BLE',
                'description': 'مسح متطور لأجهزة البلوتوث',
                'command': 'blue_hydra',
                'params': []
            },
            'btscanner': {
                'name': 'BTScanner - معلومات الأجهزة',
                'description': 'جمع معلومات متقدمة عن أجهزة البلوتوث',
                'command': 'btscanner',
                'params': ['-i', 'hci0']
            },
            'ubertooth': {
                'name': 'Ubertooth - هجمات متقدمة',
                'description': 'هجمات على الطبقات المنخفضة',
                'command': 'ubertooth-btle',
                'params': ['-f']
            },
            'carwhisperer': {
                'name': 'Car Whisperer - استغلال الصوت',
                'description': 'استغلال أجهزة البلوتوث الصوتية',
                'command': 'carwhisperer',
                'params': []
            }
        }
    },
    'mitm_attacks': {
        'name': 'هجمات MITM والتحكم',
        'tools': {
            'ettercap': {
                'name': 'Ettercap - MITM وتسميم ARP',
                'description': 'هجمات MITM وتسميم ARP',
                'command': 'ettercap',
                'params': ['-T', '-M', 'arp:remote']
            },
            'dsniff': {
                'name': 'Dsniff - التقاط كلمات المرور',
                'description': 'التقاط كلمات المرور والبروتوكولات',
                'command': 'dsniff',
                'params': ['-i']
            },
            'mitmproxy': {
                'name': 'MITMProxy - اعتراض HTTP/HTTPS',
                'description': 'اعتراض وتعديل طلبات HTTP/HTTPS',
                'command': 'mitmproxy',
                'params': ['-s']
            },
            'sslstrip': {
                'name': 'SSLStrip - تحويل HTTPS',
                'description': 'تحويل HTTPS إلى HTTP لسرقة البيانات',
                'command': 'sslstrip',
                'params': ['-l', '8080']
            },
            'netsniff': {
                'name': 'Netsniff-ng - تحليل الشبكات',
                'description': 'أدوات متقدمة لتحليل الشبكات',
                'command': 'netsniff-ng',
                'params': ['--in']
            }
        }
    }
}

def run_tool_command(tool_category, tool_name, params, session_id):
    """Execute a tool command and stream output via WebSocket"""
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
        
        # Create results directory for this session
        session_dir = os.path.join(RESULTS_FOLDER, session_id)
        os.makedirs(session_dir, exist_ok=True)
        
        # Log the command
        logger.info(f"Executing: {' '.join(command)}")
        
        # Start the process
        process = subprocess.Popen(
            command,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            universal_newlines=True,
            bufsize=1
        )
        
        # Stream output
        output_lines = []
        while True:
            output = process.stdout.readline()
            if output == '' and process.poll() is not None:
                break
            if output:
                output_lines.append(output.strip())
                socketio.emit('tool_output', {
                    'session_id': session_id,
                    'output': output.strip(),
                    'type': 'stdout'
                })
        
        # Get any remaining stderr
        stderr_output = process.stderr.read()
        if stderr_output:
            socketio.emit('tool_output', {
                'session_id': session_id,
                'output': stderr_output,
                'type': 'stderr'
            })
        
        # Save results to file
        result_file = os.path.join(session_dir, f"{tool_name}_{int(time.time())}.txt")
        with open(result_file, 'w', encoding='utf-8') as f:
            f.write(f"ZERO Platform - {tool_config['name']}\n")
            f.write(f"Command: {' '.join(command)}\n")
            f.write(f"Timestamp: {datetime.now()}\n")
            f.write("=" * 50 + "\n\n")
            f.write('\n'.join(output_lines))
            if stderr_output:
                f.write(f"\n\nErrors:\n{stderr_output}")
        
        # Notify completion
        socketio.emit('tool_complete', {
            'session_id': session_id,
            'result_file': result_file,
            'exit_code': process.returncode
        })
        
    except Exception as e:
        logger.error(f"Error executing tool: {str(e)}")
        socketio.emit('tool_error', {
            'session_id': session_id,
            'error': str(e)
        })

@app.route('/')
def index():
    """Main landing page with disclaimer"""
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
    
    return render_template('tools.html', 
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
    
    # Generate session ID for this execution
    session_id = str(uuid.uuid4())
    
    # Start tool execution in background thread
    thread = threading.Thread(
        target=run_tool_command,
        args=(category, tool_name, params, session_id)
    )
    thread.daemon = True
    thread.start()
    
    return jsonify({
        'success': True,
        'session_id': session_id,
        'message': 'تم بدء تشغيل الأداة'
    })

@socketio.on('connect')
def handle_connect():
    """Handle WebSocket connection"""
    logger.info('Client connected')

@socketio.on('disconnect')
def handle_disconnect():
    """Handle WebSocket disconnection"""
    logger.info('Client disconnected')

if __name__ == '__main__':
    # Run the application
    socketio.run(app, host='0.0.0.0', port=12000, debug=True, allow_unsafe_werkzeug=True, async_mode='gevent')