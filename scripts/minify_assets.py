import os
import glob

def minify_js():
    for file in glob.glob('static/js/*.js'):
        with open(file, 'r', encoding='utf-8') as f:
            content = f.read()
        # إزالة التعليقات // و /* */
        import re
        content = re.sub(r'/\*.*?\*/', '', content, flags=re.DOTALL)
        content = re.sub(r'//.*', '', content)
        # إزالة المسافات البيضاء
        content = re.sub(r'\s+', ' ', content)
        min_file = file.replace('.js', '.min.js')
        with open(min_file, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"✅ تم تصغير {file} → {min_file}")

def minify_css():
    for file in glob.glob('static/css/*.css'):
        with open(file, 'r', encoding='utf-8') as f:
            content = f.read()
        # إزالة التعليقات /* */
        import re
        content = re.sub(r'/\*.*?\*/', '', content, flags=re.DOTALL)
        # إزالة المسافات البيضاء
        content = re.sub(r'\s+', ' ', content)
        min_file = file.replace('.css', '.min.css')
        with open(min_file, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"✅ تم تصغير {file} → {min_file}")

if __name__ == '__main__':
    minify_js()
    minify_css()
    print("🎉 جميع ملفات JS وCSS تم تصغيرها بنجاح!")
