#!/usr/bin/env python3
"""
ZERO Platform - خادم التحميل المباشر
© 2025 ZERO Platform. All rights reserved.
"""

from flask import Flask, send_file, Response
import os

app = Flask(__name__)

@app.route('/')
@app.route('/download')
def download_direct():
    """تحميل مباشر للمشروع"""
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

@app.route('/info')
def info():
    """معلومات المشروع"""
    return """
    <html dir="rtl">
    <head><meta charset="UTF-8"><title>ZERO Platform</title></head>
    <body style="font-family: Arial; background: #0f0f23; color: white; text-align: center; padding: 50px;">
        <h1>🔥 ZERO Platform</h1>
        <p>رابط التحميل المباشر: <a href="/download" style="color: #4ecdc4;">اضغط هنا</a></p>
        <p>© 2025 ZERO Platform. All rights reserved.</p>
    </body>
    </html>
    """

if __name__ == '__main__':
    print("🔥 ZERO Platform Direct Download Server")
    print("© 2025 ZERO Platform. All rights reserved.")
    print("رابط التحميل المباشر: http://10.2.32.34:9000/")
    print("رابط التحميل المباشر: http://10.2.32.34:9000/download")
    app.run(host='0.0.0.0', port=9000, debug=False)