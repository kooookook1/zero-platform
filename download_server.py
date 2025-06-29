#!/usr/bin/env python3
"""
ZERO Platform - خادم تحميل المشروع
© 2025 ZERO Platform. All rights reserved.
"""

from flask import Flask, send_file, render_template_string
import os

app = Flask(__name__)

DOWNLOAD_TEMPLATE = """
<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>تحميل ZERO Platform</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background: linear-gradient(135deg, #0f0f23 0%, #1a1a2e 50%, #16213e 100%);
            color: #ffffff;
            min-height: 100vh;
            display: flex;
            align-items: center;
            justify-content: center;
            margin: 0;
            direction: rtl;
        }
        
        .container {
            background: rgba(255, 255, 255, 0.1);
            padding: 40px;
            border-radius: 20px;
            backdrop-filter: blur(10px);
            border: 1px solid rgba(255, 255, 255, 0.2);
            text-align: center;
            max-width: 600px;
            width: 90%;
        }
        
        .logo {
            font-size: 3rem;
            font-weight: bold;
            margin-bottom: 20px;
            background: linear-gradient(45deg, #ff6b6b, #4ecdc4, #45b7d1);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
        }
        
        .subtitle {
            font-size: 1.2rem;
            opacity: 0.8;
            margin-bottom: 30px;
        }
        
        .download-btn {
            background: linear-gradient(45deg, #ff6b6b, #4ecdc4);
            color: white;
            padding: 15px 30px;
            border: none;
            border-radius: 25px;
            cursor: pointer;
            font-size: 1.2rem;
            text-decoration: none;
            display: inline-block;
            transition: all 0.3s ease;
            margin: 10px;
        }
        
        .download-btn:hover {
            transform: scale(1.05);
            box-shadow: 0 5px 15px rgba(255, 107, 107, 0.4);
        }
        
        .info {
            background: rgba(40, 167, 69, 0.2);
            color: #28a745;
            padding: 20px;
            border-radius: 10px;
            margin: 20px 0;
            border: 1px solid #28a745;
        }
        
        .instructions {
            background: rgba(255, 255, 255, 0.05);
            padding: 20px;
            border-radius: 10px;
            margin: 20px 0;
            text-align: right;
        }
        
        .code {
            background: rgba(0, 0, 0, 0.3);
            padding: 10px;
            border-radius: 5px;
            font-family: monospace;
            margin: 10px 0;
            direction: ltr;
            text-align: left;
        }
        
        .copyright {
            margin-top: 30px;
            font-size: 0.9rem;
            opacity: 0.7;
        }
    </style>
</head>
<body>
    <div class="container">
        <div class="logo">🔥 ZERO Platform</div>
        <div class="subtitle">تحميل المشروع الكامل</div>
        
        <div class="info">
            ✅ المشروع جاهز للتحميل - حجم الملف: 36 KB<br>
            📦 يحتوي على جميع الملفات والأدوات
        </div>
        
        <a href="/download" class="download-btn">
            ⬇️ تحميل مباشر - ZERO Platform
        </a>
        
        <div style="margin: 20px 0;">
            <strong>🔗 رابط التحميل المباشر:</strong><br>
            <div class="code">http://10.2.32.34:8000/download</div>
            <small style="opacity: 0.7;">انسخ هذا الرابط واستخدمه في أي متصفح</small>
        </div>
        
        <div class="instructions">
            <h3>📋 تعليمات التشغيل المحلي:</h3>
            
            <p><strong>1. فك الضغط:</strong></p>
            <div class="code">tar -xzf zero-platform-complete.tar.gz</div>
            
            <p><strong>2. الدخول للمجلد:</strong></p>
            <div class="code">cd zero-platform</div>
            
            <p><strong>3. تثبيت المتطلبات:</strong></p>
            <div class="code">pip install flask flask-cors</div>
            
            <p><strong>4. تشغيل المشروع:</strong></p>
            <div class="code">python3 simple_app.py</div>
            
            <p><strong>5. فتح المتصفح:</strong></p>
            <div class="code">http://localhost:5000</div>
        </div>
        
        <div class="info">
            ⚠️ للأغراض التعليمية واختبار الاختراق الأخلاقي فقط
        </div>
        
        <div class="copyright">
            © 2025 ZERO Platform. All rights reserved.
        </div>
    </div>
</body>
</html>
"""

@app.route('/')
def index():
    """صفحة التحميل الرئيسية"""
    return render_template_string(DOWNLOAD_TEMPLATE)

@app.route('/download')
def download_project():
    """تحميل ملف المشروع"""
    file_path = '/workspace/zero-platform-complete.tar.gz'
    if os.path.exists(file_path):
        return send_file(
            file_path,
            as_attachment=True,
            download_name='zero-platform-complete.tar.gz',
            mimetype='application/gzip'
        )
    else:
        return "الملف غير موجود", 404

if __name__ == '__main__':
    print("🔥 ZERO Platform Download Server")
    print("© 2025 ZERO Platform. All rights reserved.")
    print("رابط التحميل: http://10.2.32.34:8000")
    app.run(host='0.0.0.0', port=8000, debug=False)