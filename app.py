from flask import Flask, request, render_template, redirect, url_for, flash
from werkzeug.utils import secure_filename
app = Flask(__name__)
app.secret_key = '1234'
import os

# 파일업로드 출력 테스트
# from flaskext.mysql import MySQL
import os
# mysql = MySQL()
###여기까지



@app.route('/') 
def hello():
    return 'Hello, World!'

@app.route('/method',methods = ['GET','POST']) 
def method():
    if request.method == 'GET' :
        return 'GET으로 전달'
    else :
        return 'POST로 전달'


# 새 창 열기 = html 열기
@app.route('/login')
def login() :
    return render_template('login.html')

@app.route('/naver')
def naver() :
    return render_template('naver.html')  # html을 통해 사이트 열기

@app.route('/daum')
def daum() :
    return redirect('https://www.daum.net/')  # html없이 사이트 열기

@app.route('/urltest')
def url_test():
    return redirect(url_for('daum'))

@app.errorhandler(404)  # error 메시지 
def page_not_found(error):
    return "페이지가 없습니다. URL를 확인 하세요", 404

@app.route('/input/<int:num>')
def input(num):
    name = ''
    if num == 1:
        name = '도라에몽'
    elif num == 2:
        name = '진구'
    elif num == 3:
        name = '퉁퉁이'
    return "hello {}".format(name)

@app.route('/myimage')
def myimage() :
    return render_template('myimage.html')

@app.route('/index')
def index() :
    return render_template('index.html')



@app.route('/upload')
def upload_file() :
    return render_template('13_upload.html')

@app.route('/uploader', methods=['GET', 'POST'])
def uploader_file() :
    # file_name = [] # 파일이름 리스트 생성
    global file # 전역변수로 호출
    f = request.files.getlist('file[]')
    for file in f :
        file.save('./static/upload_files/' + secure_filename(file.filename))
    flash("업로드가 완료되었습니다.") 
    IMG_LIST = os.listdir('static/upload_files') # 폴더 속 파일리스트
    IMG_LIST = ['upload_files/' + i for i in IMG_LIST]
    # file_name.append(f.filename) # 파일이름 리스트 추가
    # IMG_LIST = os.listdir('static/upload_files') # 폴더 속 파일리스트
    # IMG_LIST = ['upload_files/' + i for i in IMG_LIST]
    return render_template('solution.html', file_name = file.filename, imagelist = IMG_LIST)
    # return redirect(url_for('solution'), file_name = file.filename, imagelist = IMG_LIST)


# 클릭한 사진 뽑아내기
@app.route('/yolo', methods=['GET', 'POST'])
def yolo() :
    global file
    # click_file = request.file('file')
    IMG_LIST = os.listdir('static/upload_files') # 폴더 속 파일리스트
    IMG_LIST = ['upload_files/' + i for i in IMG_LIST]
    return render_template('solution.html', file_name = file.filename, imagelist = IMG_LIST)



# 파일 업로드 출력 테스트
# @app.route('/fileUpload', methods = ['GET', 'POST'])
# def file_upload():
#     if request.method == 'POST':
#         f = request.files['file']
#         f.save('static/uploads/' + secure_filename(f.filename))
#         files = os.listdir("static/uploads")
 
#         conn = mysql.connect()
#         cursor = conn.cursor()
#         # 파일명과 파일경로를 데이터베이스에 저장함
#         sql = "INSERT INTO images (image_name, image_dir) VALUES ('%s', '%s')" % (secure_filename(f.filename), 'uploads/'+secure_filename(f.filename))
#         cursor.execute(sql)
#         data = cursor.fetchall()
 
#         if not data:
#             conn.commit()
#             return redirect(url_for("main"))
 
#         else:
#             conn.rollback()
#             return 'upload failed'
 
#         cursor.close()
#         conn.close()
 
# @app.route('/view', methods = ['GET', 'POST'])
# def view():
#     conn = mysql.connect()  # DB와 연결
#     cursor = conn.cursor()  # connection으로부터 cursor 생성 (데이터베이스의 Fetch 관리)
#     sql = "SELECT image_name, image_dir FROM images"  # 실행할 SQL문
#     cursor.execute(sql)  # 메소드로 전달해 명령문을 실행
#     data = cursor.fetchall()  # 실행한 결과 데이터를 꺼냄
 
#     data_list = []
 
#     for obj in data:  # 튜플 안의 데이터를 하나씩 조회해서
#         data_dic = {  # 딕셔너리 형태로
#             # 요소들을 하나씩 넣음
#             'name': obj[0],
#             'dir': obj[1]
#         }
#         data_list.append(data_dic)  # 완성된 딕셔너리를 list에 넣음
 
#     cursor.close()
#     conn.close()
 
#     return render_template('view.html', data_list=data_list)  # html을 렌더하며 DB에서 받아온 값들을 넘김

# 페이징 구현
# @bp.route('/list/')
# def _list():
#     page = request.args.get('page', type=int, default=1)  # 페이지
#     img_list = 
#     question_list = question_list.paginate(page=page, per_page=10)
#     return render_template('question/question_list.html', question_list=question_list)

# 여러 이미지 띄우기

IMG_FOLDER = os.path.join('static', 'img/upload_files')

@app.route('/showIMG')
def showIMG() :
    IMG_LIST = os.listdir('static/img/upload_files')
    IMG_LIST = ['static/img/upload_files/' + i for i in IMG_LIST]
    return render_template('solution.html', imagelist = IMG_LIST)

## 업로드 파일 출력


# 데이터베이스 값 설정
# app.config['MYSQL_DATABASE_USER'] = 'root'
# app.config['MYSQL_DATABASE_PASSWORD'] = '0000'
# app.config['MYSQL_DATABASE_DB'] = 'image'
# app.config['MYSQL_DATABASE_HOST'] = 'localhost'
# app.secret_key = "ABCDEFG"
# mysql.init_app(app)

@app.route('/solution', methods = ['GET', 'POST'])
def solution() :
    return render_template('solution.html')
 
# @app.route('/fileUpload', methods = ['GET', 'POST'])
# def file_upload():
#     if request.method == 'POST':
#         f = request.files['file']
#         f.save('static/img/upload_files/' + secure_filename(f.filename))
#         files = os.listdir("static/img/upload_files")
 
#         conn = mysql.connect()
#         cursor = conn.cursor()
#         # 파일명과 파일경로를 데이터베이스에 저장함
#         sql = "INSERT INTO images (image_name, image_dir) VALUES ('%s', '%s')" % (secure_filename(f.filename), 'uploads/'+secure_filename(f.filename))
#         cursor.execute(sql)
#         data = cursor.fetchall()
 
#         if not data:
#             conn.commit()
#             flash("업로드가 완료되었습니다.")
#             return render_template('solution.html')
 
#         else:
#             conn.rollback()
#             flash("!!업로드하는데 실패했습니다.!!")
#             return render_template('solution.html')
 
#         cursor.close()
#         conn.close()
 
# @app.route('/view', methods = ['GET', 'POST'])
# def view():
#     conn = mysql.connect()  # DB와 연결
#     cursor = conn.cursor()  # connection으로부터 cursor 생성 (데이터베이스의 Fetch 관리)
#     sql = "SELECT image_name, image_dir FROM images"  # 실행할 SQL문
#     cursor.execute(sql)  # 메소드로 전달해 명령문을 실행
#     data = cursor.fetchall()  # 실행한 결과 데이터를 꺼냄
 
#     data_list = []
 
#     for obj in data:  # 튜플 안의 데이터를 하나씩 조회해서
#         data_dic = {  # 딕셔너리 형태로
#             # 요소들을 하나씩 넣음
#             'name': obj[0],
#             'dir': obj[1]
#         }
#         data_list.append(data_dic)  # 완성된 딕셔너리를 list에 넣음
 
#     cursor.close()
#     conn.close()
 
#     return render_template('solution.html', data_list=data_list)  # html을 렌더하며 DB에서 받아온 값들을 넘김


if __name__ == '__main__' :
    with app.test_request_context() :
        print(url_for('daum'))
    app.run(debug = True)




