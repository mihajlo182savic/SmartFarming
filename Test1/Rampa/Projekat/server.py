from flask import Flask,render_template,request,redirect
import userValidation
import profileEdit
import json
app = Flask(__name__)

@app.route('/')
def userLoginPage():
	return render_template('userLogin.html')

@app.route('/userLogin', methods=['POST'])
def userLogin():
	if (request.method=='POST'):
		user = request.json
		if (userValidation.validation(str(user['username']),str(user['password'])) == 1):
			return '1'
		else:
			return '0'

@app.route('/profileEditUsername',methods=['POST'])
def userChangeUsername():
	if (request.method=='POST'):
		edit = request.json
		if(profileEdit.changeUsername(str(edit['oldUsername']),str(edit['newUsername']))=='1'):
			return '1'
		else:
			return '0'

@app.route('/profileEditPassword',methods=['POST'])
def userChangePassword():
	if(request.method=='POST'):
		edit = request.json
		if(profileEdit.changePassword(str(edit['username']),str(edit['newPassword']))=='1'):
			return '1'
		else:
			return '0'

@app.route('/profileEditInsertPhone',methods=['POST'])
def userInsertPhone():
	if(request.method=='POST'):
		edit = request.json
		if(profileEdit.insertPhone(str(edit['username']),str(edit['phone']))=='1'):
			return '1'
		else:
			return '0'

@app.route('/getPhone',methods=['POST'])
def userPhone():
	if(request.method=='POST'):
		info = request.json
		return json.dumps(profileEdit.showPhoneNumbers(str(info['username'])))

@app.route('/admin')
def adminLoginPage():
	return render_template('adminLogin.html')

	
@app.route('/adminLogin',methods=['POST'])
def adminLogin():	
	if (request.method=='POST'):
		admin = request.json
		if (userValidation.validation(str(admin['username']),str(admin['password'])) == '1'):
			return redirect('admin.html', code=302)
		else:
			return '0'


if __name__=="__main__":
	app.run()
