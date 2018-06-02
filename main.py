from flask import Flask, render_template, Response, request, redirect
from camera import VideoCamera
import sqlite3 as lite
import sys

app = Flask(__name__, static_folder='static', static_url_path='')

@app.route('/')
def index():
	return render_template('map.html')

@app.route('/animals')
def animals():
	con = lite.connect('ecodb.db')
	lite.connect(":memory:", check_same_thread = False)
	cur = con.cursor()
	cur.execute("SELECT * FROM animals")
	data = cur.fetchall()
	return render_template('animals.html', post_names=data)

@app.route('/mystream')
def mystream():
	return render_template('stream.html')

@app.route('/auth', methods=['POST'])
def auth():
	# ----------------------------------------------------#
	user = request.form['username']
	passw = request.form['password']
	email = request.form['email']
	phone = request.form['phone']
	# ----------------------------------------------------#
	con = lite.connect('ecodb.db')
	lite.connect(":memory:", check_same_thread = False)
	cur = con.cursor()
	cur.execute("INSERT INTO user VALUES(null, '" + str(user) + "', '" + str(passw) + "', '" + str(email) + "', '" + str(phone) + "')")
	con.commit()
	# ----------------------------------------------------#
	print("reg: done.")
	return redirect('/animals')

@app.route('/dologin', methods=['POST'])
def dologin():
	# ----------------------------------------------------#
	email = request.form['email']
	passw = request.form['password']
	# ----------------------------------------------------#
	con = lite.connect('ecodb.db')
	lite.connect(":memory:", check_same_thread = False)
	cur = con.cursor()
	cur.execute("SELECT password FROM user WHERE email='" + str(email) + "'")
	data = cur.fetchone()
	try:
		if str(passw) == data[0]:
			print("login: done.")
			return redirect('/animals')
		else:
			print("login: failed(pass)")
	except:
			print("login: failed(email)")

@app.route('/animals_data', methods=['POST'])
def animals_data():
	con = lite.connect('ecodb.db')
	lite.connect(":memory:", check_same_thread = False)
	cur = con.cursor()
	cur.execute("SELECT password FROM user WHERE email='" + str(email) + "'")
	data = cur.fetchone()
	try:
		if str(passw) == data[0]:
			print("login: done.")
			return redirect('/animals')
		else:
			print("login: failed(pass)")
	except:
			print("login: failed(email)")

def gen(camera):
    while True:
        frame = camera.get_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')

@app.route('/video_feed')
def video_feed():
    return Response(gen(VideoCamera()),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)