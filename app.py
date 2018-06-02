from flask import Flask, render_template, Response, request, redirect
import sys, json

sys.path.append("include")
from camera import AnyCamera
from db import animals
from db import Users

#######################################################################################################
app = Flask(__name__, static_folder='site', static_url_path='', template_folder='site')

@app.route('/') # Map page
def index():
	return render_template('index.html')

@app.route('/zoo') # Zoo demo page
def zoo():
	return render_template('zoo.html')

@app.route('/animals') # Animals List
def list():
	data = animals['animals']
	return render_template('list.html', post_names=data)

#/////////////////////////////////////////////////////////////////////////////////////////////////////#

@app.route('/regMe', methods=['POST'])
def reg():
	username = request.form['username']
	password = request.form['password']
	email = request.form['email']
	phone = request.form['phone']
	Users.regMe(username, password, email, phone)
	return redirect('/animals')

#######################################################################################################
def gen(camera):
	while True:
		frame = camera.get_frame()
		yield (b'--frame\r\n'
			b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')

@app.route('/video_feed')
def video_feed():
	return Response(gen(AnyCamera()), mimetype='multipart/x-mixed-replace; boundary=frame')
#######################################################################################################

def Main():
	app.run(host='0.0.0.0', debug=True)

Main()
