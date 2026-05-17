from flask import Flask, request, send_file
from weasyprint import HTML
import os

app = Flask(__name__)

@app.route('/convert', methods=['POST'])
def convert():
    html_content = request.data.decode('utf-8')
    temp_html = '/tmp/input.html'
    temp_pdf = '/tmp/output.pdf'
    
    with open(temp_html, 'w', encoding='utf-8') as f:
        f.write(html_content)
    
    HTML(filename=temp_html).write_pdf(temp_pdf)
    
    return send_file(temp_pdf, as_attachment=True, download_name='试卷.pdf')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
