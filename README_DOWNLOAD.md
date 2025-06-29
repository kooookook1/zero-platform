# 🔥 ZERO Platform - دليل التحميل والتشغيل المحلي

## 📥 رابط التحميل المباشر

### 🌐 الرابط الأساسي
```
http://10.2.32.34:8000/
```

### 📱 روابط بديلة
```
http://localhost:8000/
http://127.0.0.1:8000/
```

---

## 📋 تعليمات التشغيل المحلي

### 1️⃣ تحميل المشروع
- اذهب إلى الرابط: `http://10.2.32.34:8000/`
- اضغط على زر "تحميل ZERO Platform"
- سيتم تحميل ملف: `zero-platform-complete.tar.gz`

### 2️⃣ فك الضغط
```bash
tar -xzf zero-platform-complete.tar.gz
cd zero-platform
```

### 3️⃣ تثبيت المتطلبات
```bash
# Python 3.6+ مطلوب
pip install flask flask-cors

# أو باستخدام pip3
pip3 install flask flask-cors
```

### 4️⃣ تشغيل المشروع
```bash
python3 simple_app.py
```

### 5️⃣ فتح المتصفح
```
http://localhost:5000
```

---

## 🛠️ متطلبات النظام

### البرمجيات المطلوبة
- **Python 3.6+** (مطلوب)
- **pip** (لتثبيت المكتبات)
- **متصفح ويب** (Chrome, Firefox, Safari, Edge)

### المكتبات المطلوبة
- `Flask 2.3.3+`
- `Flask-CORS 4.0.0+`

### أنظمة التشغيل المدعومة
- ✅ **Windows 10/11**
- ✅ **macOS 10.15+**
- ✅ **Linux** (Ubuntu, Debian, CentOS, etc.)
- ✅ **WSL** (Windows Subsystem for Linux)

---

## 🔧 استكشاف الأخطاء

### مشكلة: Python غير مثبت
```bash
# Windows
# تحميل من: https://python.org/downloads/

# macOS
brew install python3

# Ubuntu/Debian
sudo apt update && sudo apt install python3 python3-pip

# CentOS/RHEL
sudo yum install python3 python3-pip
```

### مشكلة: pip غير موجود
```bash
# تثبيت pip
curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
python3 get-pip.py
```

### مشكلة: المنفذ 5000 مشغول
```bash
# تغيير المنفذ في simple_app.py
# السطر الأخير: app.run(host='0.0.0.0', port=8080)
```

### مشكلة: صلاحيات الوصول
```bash
# Linux/macOS
chmod +x simple_app.py
sudo python3 simple_app.py  # إذا كان المنفذ < 1024
```

---

## 📁 هيكل المشروع

```
zero-platform/
├── simple_app.py              # الخادم الرئيسي
├── templates/                 # قوالب HTML
│   ├── simple.html           # الصفحة الرئيسية
│   ├── index.html            # الصفحة الكاملة
│   ├── base.html             # القالب الأساسي
│   ├── disclaimer.html       # صفحة إخلاء المسؤولية
│   ├── dashboard.html        # لوحة التحكم
│   └── tools.html            # صفحة الأدوات
├── static/                   # الملفات الثابتة
│   └── css/                  # ملفات CSS
│       ├── bootstrap.rtl.min.css
│       └── fontawesome.min.css
├── download_server.py        # خادم التحميل
├── README_DOWNLOAD.md        # هذا الملف
├── FINAL_SOLUTION.md         # التوثيق الكامل
└── server.log               # سجل الخادم
```

---

## 🎯 الميزات المتاحة

### 🛡️ فئات الأدوات
1. **اختبار الويب**: SQLMap, Nikto, DirB, WhatWeb, WPScan
2. **فحص الشبكات**: Nmap, Masscan, Hping3, DNSEnum
3. **كلمات المرور**: Hydra, John, Hash-ID, CeWL, Crunch
4. **أندرويد**: MSFVenom, APKTool, Objection
5. **واي فاي**: Aircrack-ng, Reaver, Wifite
6. **بلوتوث**: Blue_Hydra, BTScanner
7. **MITM**: Ettercap, MITMProxy, SSLStrip

### 🌐 واجهة المستخدم
- ✅ تصميم عربي RTL كامل
- ✅ متجاوب مع جميع الشاشات
- ✅ تأثيرات بصرية جذابة
- ✅ سهولة الاستخدام

### 🔒 الأمان
- ✅ إخلاء مسؤولية واضح
- ✅ تسجيل جلسات المستخدمين
- ✅ حماية من الاستخدام غير المصرح
- ✅ تشفير الاتصالات

---

## ⚠️ تنبيهات مهمة

### القانونية
- 🚨 **للأغراض التعليمية فقط**
- 🚨 **لا تستخدم على أنظمة غير مملوكة لك**
- 🚨 **احترم القوانين المحلية والدولية**
- 🚨 **ZERO Platform غير مسؤولة عن سوء الاستخدام**

### الأمان
- 🔒 لا تشغل على خوادم الإنتاج
- 🔒 استخدم في بيئة معزولة
- 🔒 احذف البيانات الحساسة بعد الانتهاء
- 🔒 لا تحفظ كلمات مرور حقيقية

---

## 📞 الدعم الفني

### المشاكل الشائعة
1. **الخادم لا يبدأ**: تحقق من Python وpip
2. **الصفحة لا تظهر**: تحقق من المنفذ 5000
3. **الأدوات لا تعمل**: تحقق من صلاحيات النظام
4. **خطأ في المكتبات**: أعد تثبيت flask

### معلومات الاتصال
- **المشروع**: ZERO Platform
- **الإصدار**: 1.0.0
- **التاريخ**: 2025
- **الترخيص**: للأغراض التعليمية

---

## 🎉 شكر خاص

شكراً لاستخدامك ZERO Platform!

هذا المشروع تم تطويره لأغراض تعليمية لمساعدة المتخصصين في الأمان السيبراني على تعلم واختبار الأدوات بطريقة آمنة وقانونية.

---

**© 2025 ZERO Platform. All rights reserved.**

*للأغراض التعليمية واختبار الاختراق الأخلاقي فقط*