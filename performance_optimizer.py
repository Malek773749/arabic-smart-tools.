import os
from PIL import Image
import htmlmin
import rjsmin
import rcssmin

print("🚀 بدء تحسين الموقع...")

# تحسين HTML
if os.path.exists("templates/index.html"):
    with open("templates/index.html", "r", encoding="utf-8") as f:
        html = f.read()
    minified = htmlmin.minify(html, remove_comments=True)
    with open("templates/index.html", "w", encoding="utf-8") as f:
        f.write(minified)
    print("✅ تم تحسين HTML")

# تحسين JS
js_path = "static/js/main.js"
if os.path.exists(js_path):
    with open(js_path, "r", encoding="utf-8") as f:
        js = f.read()
    min_js = rjsmin.jsmin(js)
    with open(js_path, "w", encoding="utf-8") as f:
        f.write(min_js)
    print("✅ تم تحسين JavaScript")

# تحسين CSS
css_path = "static/css/style.css"
if os.path.exists(css_path):
    with open(css_path, "r", encoding="utf-8") as f:
        css = f.read()
    min_css = rcssmin.cssmin(css)
    with open(css_path, "w", encoding="utf-8") as f:
        f.write(min_css)
    print("✅ تم تحسين CSS")

print("🎉 انتهى التحسين بنجاح")
