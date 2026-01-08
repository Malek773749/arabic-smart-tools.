from flask import Flask, render_template, send_from_directory, Response
from flask_compress import Compress  # لضغط Gzip
import os

app = Flask(__name__)
Compress(app)  # تفعيل ضغط Gzip لجميع الاستجابات

# ---- صفحة رئيسية ----
@app.route('/')
def index():
    return render_template('index.html')

# ---- فحص كلمة المرور ----
@app.route('/password-check')
def password_check():
    return render_template('password-check.html')

# ---- توليد كلمة المرور ----
@app.route('/password-generate')
def password_generate():
    return render_template('password-generate.html')

# ---- معلومات IP ----
@app.route('/ip-info')
def ip_info():
    return render_template('ip-info.html')

# ---- إرسال ملفات static (CSS, JS, الصور) ----
@app.route('/static/<path:filename>')
def static_files(filename):
    return send_from_directory('static', filename)

# ---- ضغط HTML تلقائي ----
@app.after_request
def compress_html(response):
    if response.content_type == u'text/html; charset=utf-8':
        content = response.get_data(as_text=True)
        # إزالة التعليقات HTML
        import re
        content = re.sub(r'<!--.*?-->', '', content, flags=re.DOTALL)
        # إزالة المساحات البيضاء الزائدة
        content = re.sub(r'>\s+<', '><', content)
        response.set_data(content)
    return response

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
