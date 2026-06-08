from flask import Flask, request, render_template_string
import cloudinary
import cloudinary.uploader
import os

app = Flask(__name__)

cloudinary.config(
    cloud_name="dcpybmrzb",
    api_key="786263534259259",
    api_secret="Wnt_Ve_rAxyKtXepSqhaEwOTEHs"
)

HTML = '''
<!DOCTYPE html>
<html dir="rtl">
<head><meta charset="UTF-8"><title>مشاركة ملفات</title>
<style>
body { font-family: Arial; max-width: 600px; margin: 50px auto; padding: 20px; }
h1 { color: #333; }
input, button { padding: 10px; margin: 10px 0; width: 100%; }
button { background: #0066cc; color: white; border: none; cursor: pointer; border-radius: 5px; }
.file-link { display: block; margin: 10px 0; padding: 10px; background: #f0f0f0; border-radius: 5px; }
</style></head>
<body>
<h1>مشاركة الملفات</h1>
<form method="POST" enctype="multipart/form-data">
  <input type="file" name="file" required>
  <button type="submit">رفع الملف</button>
</form>
{% if url %}
<p>تم رفع الملف! رابط التحميل:</p>
<a class="file-link" href="{{ url }}" target="_blank">{{ url }}</a>
{% endif %}
</body></html>
'''

@app.route('/', methods=['GET', 'POST'])
def home():
    url = None
    if request.method == 'POST':
        file = request.files['file']
        result = cloudinary.uploader.upload(file, resource_type="auto")
        url = result['secure_url']
    return render_template_string(HTML, url=url)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)