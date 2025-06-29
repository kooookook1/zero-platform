#!/bin/bash
# ZERO Platform Startup Script
# © 2025 ZERO Platform. All rights reserved.

echo "🔥 بدء تشغيل منصة ZERO Platform..."
echo "© 2025 ZERO Platform. All rights reserved."
echo ""

# Kill any existing processes
echo "إيقاف العمليات السابقة..."
pkill -f simple_app.py 2>/dev/null || true
sleep 2

# Start the main application
echo "تشغيل الخادم الرئيسي..."
cd /workspace/zero-platform
python3 simple_app.py > server.log 2>&1 &
SERVER_PID=$!

# Wait for server to start
echo "انتظار بدء الخادم..."
sleep 5

# Check if server is running
if curl -s http://localhost:5000/ > /dev/null; then
    echo "✅ تم تشغيل ZERO Platform بنجاح!"
    echo ""
    echo "🌐 روابط الوصول:"
    echo "   - المحلي: http://localhost:5000"
    echo "   - الشبكة: http://10.2.32.34:5000"
    echo ""
    echo "📋 الأدوات المتوفرة:"
    echo "   ✓ اختبار الويب (SQLMap, Nikto, DirB, WhatWeb, WPScan)"
    echo "   ✓ فحص الشبكات (Nmap, Masscan, Hping3, DNSEnum)"
    echo "   ✓ كلمات المرور (Hydra, John, Hash-Identifier, CeWL, Crunch)"
    echo ""
    echo "⚠️  تذكر: استخدم الأدوات للأغراض التعليمية والاختبار الأخلاقي فقط"
    echo ""
    echo "📝 لإيقاف الخادم: pkill -f simple_app.py"
    echo "📊 لمراقبة السجلات: tail -f server.log"
else
    echo "❌ فشل في تشغيل الخادم"
    echo "تحقق من السجلات: cat server.log"
    exit 1
fi