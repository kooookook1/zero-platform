# 🤝 المساهمة في ZERO Platform

مرحباً بك في مجتمع **ZERO Platform**! نحن نرحب بمساهماتك في تطوير وتحسين المنصة.

---

## 🎯 كيفية المساهمة

### 1. 🍴 Fork المستودع
```bash
# انقر على زر Fork في GitHub أو استخدم:
gh repo fork kooookook1/zero-platform
```

### 2. 📥 استنساخ المستودع
```bash
git clone https://github.com/YOUR_USERNAME/zero-platform.git
cd zero-platform
```

### 3. 🌿 إنشاء branch جديد
```bash
git checkout -b feature/new-tool
# أو
git checkout -b fix/bug-description
```

### 4. 💻 تطوير التغييرات
- اكتب الكود مع التوثيق المناسب
- اتبع معايير الكود المحددة
- اختبر التغييرات محلياً

### 5. 📤 إرسال Pull Request
```bash
git add .
git commit -m "إضافة أداة جديدة: اسم الأداة"
git push origin feature/new-tool
```

---

## 🛠️ أنواع المساهمات المرحب بها

### ✨ إضافة أدوات جديدة
- أدوات اختراق أخلاقي مشهورة
- أدوات تحليل الأمان
- أدوات فحص الثغرات

### 🐛 إصلاح الأخطاء
- أخطاء في الكود
- مشاكل في الواجهة
- تحسين الأداء

### 📚 تحسين التوثيق
- إضافة أمثلة
- تحسين الشرح
- ترجمة المحتوى

### 🎨 تحسين التصميم
- تحسين الواجهة
- إضافة تأثيرات بصرية
- تحسين التجربة

---

## 📋 معايير الكود

### 🐍 Python
```python
# استخدم أسماء متغيرات واضحة
tool_name = "nmap"
target_ip = "192.168.1.1"

# أضف تعليقات للكود المعقد
def run_nmap_scan(target, ports):
    """
    تشغيل فحص nmap على الهدف المحدد
    
    Args:
        target (str): عنوان IP أو النطاق
        ports (str): البورتات المراد فحصها
    
    Returns:
        dict: نتائج الفحص
    """
    # الكود هنا...
```

### 🌐 HTML/CSS
```html
<!-- استخدم فئات Bootstrap RTL -->
<div class="container-fluid" dir="rtl">
    <div class="row">
        <div class="col-md-6">
            <!-- المحتوى -->
        </div>
    </div>
</div>
```

### 📱 JavaScript
```javascript
// استخدم const/let بدلاً من var
const toolName = 'sqlmap';
let results = [];

// أضف تعليقات للوظائف
/**
 * تشغيل أداة الفحص
 * @param {string} tool - اسم الأداة
 * @param {object} params - معاملات الفحص
 */
function runTool(tool, params) {
    // الكود هنا...
}
```

---

## 🔧 إضافة أداة جديدة

### 1. 📁 إنشاء ملف الأداة
```python
# في ملف tools/new_tool.py
def run_new_tool(target, options=None):
    """
    تشغيل الأداة الجديدة
    
    Args:
        target (str): الهدف
        options (dict): خيارات إضافية
    
    Returns:
        dict: نتائج الفحص
    """
    try:
        # منطق تشغيل الأداة
        result = subprocess.run([
            'new_tool_command',
            target
        ], capture_output=True, text=True, timeout=300)
        
        return {
            'success': True,
            'output': result.stdout,
            'error': result.stderr
        }
    except Exception as e:
        return {
            'success': False,
            'error': str(e)
        }
```

### 2. 🌐 إضافة واجهة الأداة
```html
<!-- في templates/tools.html -->
<div class="tool-card" id="new-tool">
    <h3>🔧 الأداة الجديدة</h3>
    <p>وصف مختصر للأداة وما تفعله</p>
    
    <form id="new-tool-form">
        <div class="mb-3">
            <label class="form-label">الهدف:</label>
            <input type="text" class="form-control" name="target" required>
        </div>
        <button type="submit" class="btn btn-primary">تشغيل الفحص</button>
    </form>
    
    <div id="new-tool-results" class="results-container"></div>
</div>
```

### 3. ⚙️ إضافة المعالج في Flask
```python
# في app.py
@app.route('/run_new_tool', methods=['POST'])
def run_new_tool_endpoint():
    try:
        data = request.get_json()
        target = data.get('target')
        
        if not target:
            return jsonify({'error': 'الهدف مطلوب'})
        
        # تشغيل الأداة
        result = run_new_tool(target)
        
        return jsonify(result)
    except Exception as e:
        return jsonify({'error': str(e)})
```

---

## 🧪 اختبار التغييرات

### 🔍 اختبار محلي
```bash
# تشغيل المشروع محلياً
python3 simple_app.py

# اختبار الأداة الجديدة
curl -X POST http://localhost:5000/run_new_tool \
  -H "Content-Type: application/json" \
  -d '{"target": "example.com"}'
```

### ✅ قائمة التحقق
- [ ] الأداة تعمل بشكل صحيح
- [ ] الواجهة تعرض النتائج
- [ ] لا توجد أخطاء في الكونسول
- [ ] التصميم متجاوب
- [ ] النصوص باللغة العربية

---

## 📝 كتابة Commit Messages

### ✅ أمثلة جيدة
```
إضافة أداة Gobuster لفحص الأدلة المخفية
إصلاح مشكلة عرض النتائج في SQLMap
تحسين تصميم صفحة أدوات الشبكات
تحديث التوثيق لإضافة أمثلة جديدة
```

### ❌ أمثلة سيئة
```
update
fix bug
new feature
changes
```

---

## 🔒 الأمان والمسؤولية

### ⚠️ تنبيهات مهمة
- تأكد من أن الأداة للاستخدام الأخلاقي فقط
- أضف تحذيرات مناسبة في الواجهة
- لا تضيف أدوات ضارة أو مدمرة
- احترم حقوق الملكية الفكرية

### 🛡️ فحص الأمان
```python
# تحقق من صحة المدخلات
def validate_input(target):
    if not target or len(target) > 255:
        raise ValueError("هدف غير صالح")
    
    # منع الحقن
    if any(char in target for char in [';', '&', '|', '`']):
        raise ValueError("أحرف غير مسموحة")
```

---

## 📋 قوالب المساهمة

### 🐛 تقرير خطأ
```markdown
## وصف المشكلة
وصف واضح ومختصر للمشكلة

## خطوات إعادة الإنتاج
1. اذهب إلى '...'
2. انقر على '...'
3. شاهد الخطأ

## السلوك المتوقع
ما كان يجب أن يحدث

## لقطات الشاشة
إذا كان ذلك مناسباً

## البيئة
- نظام التشغيل: [مثل iOS]
- المتصفح: [مثل chrome, safari]
- الإصدار: [مثل 22]
```

### ✨ طلب ميزة جديدة
```markdown
## وصف الميزة
وصف واضح ومختصر للميزة المطلوبة

## المشكلة المحلولة
ما هي المشكلة التي تحلها هذه الميزة؟

## الحل المقترح
وصف الحل الذي تريده

## بدائل أخرى
أي حلول بديلة فكرت فيها

## معلومات إضافية
أي معلومات أخرى مفيدة
```

---

## 🏆 الاعتراف بالمساهمين

جميع المساهمين سيتم ذكرهم في:
- 📋 ملف CONTRIBUTORS.md
- 🎉 صفحة الشكر والتقدير
- 📱 واجهة المنصة (اختياري)

---

## 📞 التواصل

### 💬 للأسئلة والمناقشات
https://github.com/kooookook1/zero-platform/discussions

### 🐛 للإبلاغ عن مشاكل
https://github.com/kooookook1/zero-platform/issues

### 📧 للتواصل المباشر
يرجى استخدام GitHub Issues أو Discussions

---

## 📜 رخصة المساهمة

بمساهمتك في هذا المشروع، أنت توافق على:
- منح ZERO Platform حقوق استخدام مساهمتك
- أن مساهمتك أصلية ولا تنتهك حقوق الآخرين
- أن مساهمتك للأغراض التعليمية والأخلاقية فقط

---

**شكراً لك على اهتمامك بالمساهمة في ZERO Platform! 🔥**

**© 2025 ZERO Platform. All rights reserved.**

*للأغراض التعليمية واختبار الاختراق الأخلاقي فقط*