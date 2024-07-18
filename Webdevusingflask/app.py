from flask import Flask,render_template,request,redirect,session
from db import Database

app=Flask(__name__)

dbo=Database()

@app.route('/')
def index():
    return render_template('login.html')


@app.route('/register')
def register():
    return render_template('register.html')

@app.route('/dologin',methods=['POST'])
def dologin():
    email=request.form.get('email')
    password=request.form.get('password')
    
    response=dbo.search(email,password)
    if response==1:
        session['logged_in']=1
        return redirect('/dashboard')
    else:
        return render_template('login.html',invalidmsg='Incorrect email/password')

@app.route('/doregister',methods=['POST'])
def doregister():
    uname=request.form.get('uname')
    email=request.form.get('email')
    password=request.form.get('password')
    response=dbo.insert(uname,email,password)
    
    if response==1:
        return render_template('login.html',message='Registration successful.Kindly login to proceed')
    else:
        return render_template('register.html',message='email already exists')

@app.route('/dashboard',methods=['GET'])
def dashboard():
    if session['logged_in']==1:
        return render_template('dashboard.html')
    else:
        return redirect('/login')

@app.route('/ner',methods=['GET'])
def ner():
    if session['logged_in']==1:
        return render_template('ner.html')
    else:
        return redirect('/login')
    
@app.route('/sentiment',methods=['GET'])
def sentiment():
    return render_template('sentiment.html')

@app.route('/emotion',methods=['GET'])
def emotion():
    return render_template('emotion.html')

@app.route('/doner',methods=['POST'])
def do_ner():
    pass

@app.route('/dosentimentanalysis',methods=['POST'])
def do_sentiment_analysis():
    pass

@app.route('/doemotion',methods=['POST'])
def doemotion():
    pass

if __name__=='__main__':
    app.run(debug=True)