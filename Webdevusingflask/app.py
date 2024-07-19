from flask import Flask,render_template,request,redirect,session
from db import Database
from myapi import API
import json

app=Flask(__name__)
app.secret_key="NLPAPP#2024"

dbo=Database()
apio=API()

@app.route('/')
@app.route('/login')
def index():
    if 'logged_in' in session:
        return redirect('/dashboard')
    
    return render_template('login.html')


@app.route('/register')
def register():
    if 'logged_in' in session:
        return redirect('/dashboard')
    
    return render_template('register.html')

@app.route('/dologin',methods=['POST'])
def dologin():
    if 'logged_in' in session:
        return redirect('/dashboard')
    
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
    if 'logged_in' in session:
        return redirect('/dashboard')
    
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
    if 'logged_in' in session:
        return render_template('dashboard.html')
    else:
        return redirect('/login')

@app.route('/ner',methods=['GET'])
def ner():
    if 'logged_in' in session:
        return render_template('ner.html')
    else:
        return redirect('/login')
    
@app.route('/sentiment',methods=['GET'])
def sentiment():
    if 'logged_in' in session:
        return render_template('sentiment.html')
    else:
        return redirect('/login')

@app.route('/emotion',methods=['GET'])
def emotion():
    if 'logged_in' in session:
        return render_template('emotion.html')
    else:
        return redirect('/login')

@app.route('/doner',methods=['POST'])
def do_ner():
    #Apple was founded by Steve Jobs.
    ner_text=request.form.get('ner_text')
    result=apio.ner(ner_text)
    return render_template('ner.html',result=result,txt=ner_text)

@app.route('/dosentimentanalysis',methods=['POST'])
def do_sentiment_analysis():
    #Come on, lets play together
    #{'sentiment': {'negative': 0.068, 'neutral': 0.46, 'positive': 0.472}}
    sentiment_text=request.form.get('sentiment_text')
    result=apio.sentiment_analysis(sentiment_text)
    print(result)
    return render_template('sentiment.html',result=result,txt=sentiment_text)

@app.route('/doemotion',methods=['POST'])
def doemotion():
    #I had great expectations from my new phone but it turned out to be another hyped up model with average features.
    #text=["I had great expectations from my new phone but it turned out to be another hyped up model with average features.","This is shit."]
    emoticon_text=request.form.get('emoticon_text')
    result=apio.emotion_prediction(emoticon_text)
    print(result)
    return render_template('emotion.html',result=result,txt=emoticon_text)

@app.route('/logout',methods=['GET'])
def logout():
    session.pop('logged_in',None)
    return redirect('/login')

if __name__=='__main__':
    #app.run(debug=True)
    app.run()