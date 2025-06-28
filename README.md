# 🛡️ WAVS - Web Application Vulnerability Scanner | أداة فحص ثغرات تطبيقات الويب

## 🧠 Overview | نظرة عامة

WAVS is an open-source Python tool designed to scan web applications for common vulnerabilities such as SQL Injection and XSS.  
WAVS هي أداة مفتوحة المصدر مكتوبة بلغة بايثون، صممت لفحص تطبيقات الويب واكتشاف ثغرات مثل SQL Injection وXSS.

It uses powerful tools like **Nmap**, **Nikto**, and brute-force testing to simulate real-world attacks.  
تستخدم أدوات قوية مثل **Nmap** و**Nikto**، وتنفذ هجمات تجريبية مثل brute-force لمحاكاة الهجمات الواقعية.

---

## ⚙️ Installation and Running | التثبيت والتشغيل

```bash
# 1. Clone the repository | استنساخ المشروع
git clone https://github.com/Alahmadiamjad/WAVS-.git

# 2. Enter the project directory | الدخول إلى مجلد المشروع
cd WAVS-

# 3. Install required libraries | تثبيت المكتبات المطلوبة
pip install -r requirments.txt

# 4. Run the tool | تشغيل الأداة
python main.py

Enter the IP or URL (without http/https) when prompted.
عند التشغيل، ستطلب منك الأداة إدخال عنوان IP أو رابط الموقع بدون http/https


📁 Project Files | ملفات المشروع
File	Description	الملف	الوصف
main.py	Main entry point	main.py	ملف التشغيل الرئيسي
SQLi.py	SQL Injection detection	SQLi.py	فحص ثغرات SQL Injection
XSS_checker.py	XSS detection	XSS_checker.py	فحص ثغرات XSS
Login_brute.py	Brute-force login testing	Login_brute.py	تجربة تسجيل الدخول بالقوة
Web_Scanner.py	Web page scanner	Web_Scanner.py	فحص الصفحات المفتوحة
crawler.py	Internal link crawler	crawler.py	الزاحف لاستخراج روابط الصفحات
bruteforce.txt	Password wordlist	bruteforce.txt	قائمة كلمات مرور لتجربة الدخول
requirments.txt	Required libraries	requirments.txt	مكتبات Python المطلوبة

![Screenshot 2025-06-28 113438](https://github.com/user-attachments/assets/de44a5dd-677d-4552-92dd-01a7fd9ea5ea)
![Screenshot 2025-06-28 113412](https://github.com/user-attachments/assets/0fc20122-da2c-47a1-ae66-1f4a591ab4f6)
![Screenshot 2025-06-28 113350](https://github.com/user-attachments/assets/b7b7f8f1-b8ed-4e8a-a4ad-33685af77c90)

✅ What It Does | ما الذي تفعله الأداة
Checks if the host is alive
تتحقق من أن الموقع يعمل

Scans open ports with Nmap
تفحص المنافذ المفتوحة باستخدام Nmap

Detects login pages and performs brute-force login attempts
تكتشف صفحات تسجيل الدخول وتجرب كلمات مرور عبر brute-force

Tests for SQL Injection in login forms
تفحص نماذج الدخول لاكتشاف SQL Injection

Crawls the website and collects all links
تزحف على الموقع وتجمع روابط جميع الصفحات

Tests each page for XSS vulnerabilities
تفحص الصفحات المكتشفة لثغرات XSS

Uses Nikto to scan server configuration
تستخدم Nikto لتحليل إعدادات السيرفر

Generates a report file with scan results
تنشئ ملف تقرير يحتوي على نتائج الفحص النهائية

⭐ Features | المميزات
Simple and automatic scanning
فحص سهل وتلقائي

Uses powerful tools (Nmap, Nikto)
يستخدم أدوات قوية ومعروفة

Saves results into a text file
يحفظ نتائج الفحص في ملف تلقائيًا

Great for students, learning, and testing
مناسب للطلاب والتعلم ومشاريع التخرج

💡 Future Improvements | تطويرات مستقبلية
Add a graphical user interface (GUI)
إضافة واجهة رسومية GUI

Support more vulnerabilities (e.g., CSRF, LFI)
دعم أنواع ثغرات إضافية مثل CSRF وLFI

Improve detection accuracy and reduce false positives
تحسين دقة الكشف وتقليل الإنذارات الخاطئة

Export results as PDF/HTML
إمكانية توليد تقارير بصيغة PDF أو HTML

Official support for Windows
دعم رسمي لنظام ويندوز

👨‍💻 Developer | المطور
Amjad Alahmadi

🔗 LinkedIn Profile : 
https://www.linkedin.com/in/amjad-alahmadi-b04106280 


⚠️ Disclaimer | تنبيه
This tool is for educational purposes only. Do not use it without permission.
الأداة تعليمية فقط، ولا يجوز استخدامها ضد أي موقع بدون إذن صريح.




