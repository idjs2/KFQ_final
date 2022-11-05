from flask import Flask, request, render_template, redirect, url_for, flash
from werkzeug.utils import secure_filename
app = Flask(__name__)
app.secret_key = '1234'
import os

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/daum')
def daum() :
    return render_template(url_for('https://www.daum.net'))

@app.route('/method', methods=['GET','POST'])
def method() :
    if request.method == 'GET':
        return "GET으로 전달"
    else:
        return "POST로 전달"

# @app.route('/upload')
# def upload_file() :
#     return render_template('13_upload.html')

@app.route('/uploader', methods=['GET', 'POST'])
def uploader_file() :
    # file_name = [] # 파일이름 리스트 생성
    global file # 전역변수로 호출
    f = request.files.getlist('file[]')
    for file in f :
        file.save('./static/upload_files/' + secure_filename(file.filename))
    flash("업로드가 완료되었습니다.") 
    IMG_LIST = os.listdir('static/upload_files') # 폴더 속 파일리스트
    imagelist = ['upload_files/' + i for i in IMG_LIST]
    # file_name.append(f.filename) # 파일이름 리스트 추가
    # IMG_LIST = os.listdir('static/upload_files') # 폴더 속 파일리스트
    # IMG_LIST = ['upload_files/' + i for i in IMG_LIST]
    return render_template('solution.html', file_name = file.filename, IMG_LIST = IMG_LIST, imagelist = imagelist)
    # return redirect(url_for('solution'), file_name = file.filename, imagelist = IMG_LIST)


# 클릭한 사진 뽑아내기
@app.route('/yolo', methods=['GET', 'POST'])
def yolo() :
    global file
    # click_file = request.file('file')
    IMG_LIST = os.listdir('static/upload_files') # 폴더 속 파일리스트
    IMG_LIST = ['upload_files/' + i for i in IMG_LIST]
    return render_template('solution.html', file_name = file.filename, imagelist = IMG_LIST)

# 여러 이미지 띄우기

IMG_FOLDER = os.path.join('static', 'img/upload_files')

@app.route('/showIMG')
def showIMG() :
    IMG_LIST = os.listdir('static/img/upload_files')
    IMG_LIST = ['static/img/upload_files/' + i for i in IMG_LIST]
    return render_template('solution.html', imagelist = IMG_LIST)


@app.route('/solution', methods = ['GET', 'POST'])
def solution() :
    return render_template('solution.html')
 

if __name__ == '__main__' :
    with app.test_request_context() :
        print(url_for('daum'))
    app.run(debug = True)