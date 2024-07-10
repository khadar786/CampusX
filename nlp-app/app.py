from tkinter import *
from mydb import Database
from tkinter import messagebox
from myapi import API

class NLPApp:
    
    def __init__(self):
        #create db object
        self.dbo=Database()
        self.apio=API()
        
        
        # login ka gui load karna
        self.root=Tk()
        self.root.title('NLPAPP')
        self.root.iconbitmap('resources/favicon.ico')
        self.root.geometry('350x600')
        self.root.configure(bg='#99A1B7')
        
        self.login_gui()
        
        self.root.mainloop()
    
    def login_gui(self):
        self.clear()
            
        heading=Label(self.root,text='NLPApp',bg='#99A1B7',fg='#ffffff')
        heading.pack(pady=(30,30))
        heading.configure(font=('verdana',24,'bold'))
        
        label1=Label(self.root,text='Enter Email')
        label1.pack(pady=(10,10))
        
        self.email_input=Entry(self.root,width=50)
        self.email_input.pack(pady=(5,10),ipady=4)
        
        label2=Label(self.root,text='Enter Password')
        label2.pack(pady=(10,10))
        
        self.password_input=Entry(self.root,width=50,show='*')
        self.password_input.pack(pady=(5,10),ipady=4)
        
        login_btn=Button(self.root,text='Login',width=30,height=2,command=self.perform_login)
        login_btn.pack(pady=(10,10))

        label3=Label(self.root,text='Not a member ?')
        label3.pack(pady=(20,10))
        
        redirect_btn=Button(self.root,text='Register Now',command=self.register_gui)
        redirect_btn.pack(pady=(10,10))
    
    def register_gui(self):
        self.clear()
        
        heading=Label(self.root,text='NLPApp',bg='#99A1B7',fg='#ffffff')
        heading.pack(pady=(30,30))
        heading.configure(font=('verdana',24,'bold'))
        
        label0=Label(self.root,text='Enter Name')
        label0.pack(pady=(10,10))
        
        self.name_input=Entry(self.root,width=50)
        self.name_input.pack(pady=(5,10),ipady=4)
        
        label1=Label(self.root,text='Enter Email')
        label1.pack(pady=(10,10))
        
        self.email_input=Entry(self.root,width=50)
        self.email_input.pack(pady=(5,10),ipady=4)
        
        label2=Label(self.root,text='Enter Password')
        label2.pack(pady=(10,10))
        
        self.password_input=Entry(self.root,width=50,show='*')
        self.password_input.pack(pady=(5,10),ipady=4)
        
        register_btn=Button(self.root,text='Register',width=30,height=2,command=self.perform_registration)
        register_btn.pack(pady=(10,10))

        label3=Label(self.root,text='Already a member ?')
        label3.pack(pady=(20,10))
        
        redirect_btn=Button(self.root,text='Login Now',command=self.login_gui)
        redirect_btn.pack(pady=(10,10))
        
    def clear(self):
        #clear the existing gui
        for i in self.root.pack_slaves():
            i.destroy()
    
    def perform_registration(self):
        # fetch data from the gui
        name=self.name_input.get()
        email=self.email_input.get()
        password=self.password_input.get()
        
        response=self.dbo.add_data(name,email,password)
        
        if response:
            messagebox.showinfo('Success','Registration successful. You can login now')
        else:
            messagebox.showerror('Error','Email already exists')
    
    def perform_login(self):
        email=self.email_input.get()
        password=self.password_input.get()
        
        response=self.dbo.search(email,password)
        
        if response==1:
            messagebox.showinfo('Success','Login successful')
            self.home_gui()
        else:
            messagebox.showerror('Error','Incorrect email or password')
    
    def home_gui(self):
        self.clear()
        
        heading=Label(self.root,text='NLPApp',bg='#99A1B7',fg='#ffffff')
        heading.pack(pady=(30,30))
        heading.configure(font=('verdana',24,'bold'))
        
        sentiment_btn=Button(self.root,text='Sentiment Analysis',width=30,height=4,command=self.sentiment_gui)
        sentiment_btn.pack(pady=(10,10))
        
        ner_btn=Button(self.root,text='Named Entity Recognition',width=30,height=4,command=self.ner_gui)
        ner_btn.pack(pady=(10,10))
        
        emotion_btn=Button(self.root,text='Emotion Prediction',width=30,height=4,command=self.emotion_gui)
        emotion_btn.pack(pady=(10,10))
        
        logout_btn=Button(self.root,text='Logout',command=self.login_gui)
        logout_btn.pack(pady=(10,10))
    
    def sentiment_gui(self):
        self.clear()
        heading=Label(self.root,text='NLPApp',bg='#99A1B7',fg='#ffffff')
        heading.pack(pady=(30,30))
        heading.configure(font=('verdana',24,'bold'))
        
        heading2=Label(self.root,text='Sentiment Analysis',bg='#99A1B7',fg='#ffffff')
        heading2.pack(pady=(10,20))
        heading2.configure(font=('verdana',20))
        
        label1=Label(self.root,text='Enter the text')
        label1.pack(pady=(20,10))
        
        self.sentiment_input=Entry(self.root,width=50)
        self.sentiment_input.pack(pady=(5,10),ipady=4)
        
        sentiment_btn=Button(self.root,text='Analyze Sentiment',width=30,height=4,command=self.do_sentiment_analysis)
        sentiment_btn.pack(pady=(10,10))
        
        self.sentiment_result=Label(self.root,text='',bg='#99A1B7',fg='#ffffff')
        self.sentiment_result.pack(pady=(20,10))
        self.sentiment_result.configure(font=('verdana',16))
        
        goback_btn=Button(self.root,text='Go Back',width=30,height=4,command=self.home_gui)
        goback_btn.pack(pady=(10,10))
        
    
    def ner_gui(self):
        self.clear()
        heading=Label(self.root,text='NLPApp',bg='#99A1B7',fg='#ffffff')
        heading.pack(pady=(30,30))
        heading.configure(font=('verdana',24,'bold'))
        
        heading2=Label(self.root,text='Named Entity Recognition',bg='#99A1B7',fg='#ffffff')
        heading2.pack(pady=(10,20))
        heading2.configure(font=('verdana',20))
        
        label1=Label(self.root,text='Enter the text')
        label1.pack(pady=(20,10))
        
        self.ner_input=Entry(self.root,width=50)
        self.ner_input.pack(pady=(5,10),ipady=4)
        
        ner_btn=Button(self.root,text='Recognize Entity',width=30,height=4,command=self.do_ner)
        ner_btn.pack(pady=(10,10))
        
        self.ner_result=Label(self.root,text='',bg='#99A1B7',fg='#ffffff')
        self.ner_result.pack(pady=(20,10))
        self.ner_result.configure(font=('verdana',16))
        
        goback_btn=Button(self.root,text='Go Back',width=30,height=4,command=self.home_gui)
        goback_btn.pack(pady=(10,10))
    
    def emotion_gui(self):
        self.clear()
        heading=Label(self.root,text='NLPApp',bg='#99A1B7',fg='#ffffff')
        heading.pack(pady=(30,30))
        heading.configure(font=('verdana',24,'bold'))
        
        heading2=Label(self.root,text='Emotion Prediction',bg='#99A1B7',fg='#ffffff')
        heading2.pack(pady=(10,20))
        heading2.configure(font=('verdana',20))
        
        label1=Label(self.root,text='Enter the text')
        label1.pack(pady=(20,10))
        
        self.emotion_input=Entry(self.root,width=50)
        self.emotion_input.pack(pady=(5,10),ipady=4)
        
        emotion_btn=Button(self.root,text='Predict Emotion',width=30,height=4,command=self.do_emotion)
        emotion_btn.pack(pady=(10,10))
        
        self.emotion_result=Label(self.root,text='',bg='#99A1B7',fg='#ffffff')
        self.emotion_result.pack(pady=(20,10))
        self.emotion_result.configure(font=('verdana',16))
        
        goback_btn=Button(self.root,text='Go Back',width=30,height=4,command=self.home_gui)
        goback_btn.pack(pady=(10,10))

    
    def do_sentiment_analysis(self):
        #Come on, lets play together
        text=self.sentiment_input.get()
        result=self.apio.sentiment_analysis(text)
        
        #print(result)
        txt=''
        for i in result['sentiment']:
            #self.sentiment_result['text']=
            txt+=i+' -> '+str(result['sentiment'][i])+'\n'
            #print(i)
        
        self.sentiment_result['text']=txt
    
    def do_ner(self):
        #Apple was founded by Steve Jobs.
        text=self.ner_input.get()
        result=self.apio.ner(text)
        
        #{'name': 'Apple', 'category': 'group', 'confidence_score': 0.9758293629}
        txt=''
        for i in result['entities']:
            txt+='=======\n'
            txt+='name : '+i['name']+'\n'+' category :'+i['category']+'\n'+' confidence_score :'+str(i['confidence_score'])+'\n'
            txt+='=======\n'
        
        self.ner_result['text']=txt
    
    def do_emotion(self):
        #I had great expectations from my new phone but it turned out to be another hyped up model with average features.
        text=self.emotion_input.get()
        result=self.apio.emotion_prediction(text)
        print(result)
            
nlp=NLPApp()