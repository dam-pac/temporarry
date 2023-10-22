from flask import *
import os
app = Flask(__name__)

@app.route('/upload')
def upload():
    return render_template("file_upload_form.html") 
@app.route('/')
def list_files():
    files = os.listdir('/home/user/')
    file_list = '<br>'.join(files)
    return f'Список файлов:<br>{file_list}'
@app.route('/success', methods=['GET', 'POST'])
def success():
    if request.method == 'POST': 
        f = request.files['file']
        f.save(f.filename)
        return render_template("success.html", name = f.filename) 

@app.route('/download/<filename>', methods=['GET', 'POST'])
def download_file(filename):
    return send_file(filename, as_attachment=True)

if __name__ == '__main__':
    app.run()
