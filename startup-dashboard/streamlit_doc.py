import streamlit as st
import pandas as pd
import time

st.title('Startup Dashboard')
st.header('I am learning Streamlit')
st.subheader('And I am loving it!')
st.write('This is my normal text')

st.markdown("""
### My favorite movies
- Race 3
- Humshakals
- Housefull
"""
)

st.code("""
def foo(input):
    return foo**2

x=foo(2)
""")

st.latex('x^2+y^2+2=0')

df=pd.DataFrame({
    'name':['Nitish','Ankit','Anupam'],
    'marks':[50,60,70],
    'package':[10,12,14]
})

st.dataframe(df)

st.metric('Revenue','Rs 3L','-3%')

st.json({
    'name':['Nitish','Ankit','Anupam'],
    'marks':[50,60,70],
    'package':[10,12,14]
})

st.image('JEE90-S1.JPEG')
st.video('http://commondatastorage.googleapis.com/gtv-videos-bucket/sample/BigBuckBunny.mp4')

st.sidebar.title('Sidebar ka title')
col1,col2=st.columns(2)

with col1:
    st.image('JEE90-S1.JPEG')
    
with col2:
    st.image('JEE90-S1.JPEG')


st.error('login failed')
st.success('login successful')
st.info('login successful')
st.warning('login successful')

bar=st.progress(0)

for i in range(1,101):
    #time.sleep(0.1)
    bar.progress(i)


email=st.text_input('Enter email')
number=st.number_input('Enter age')
st.date_input('Enter regis date')



email=st.text_input('Enter email')
password=st.text_input('Enter password',type='password')
gender=st.selectbox('Select gender',['male','female','others'])
st.file_uploader('')
btn=st.button('Login karo')


#if the button click
if btn:
    if email=='nitish@gmail.com' and password=='1234':
        #st.success('Login successful')
        st.balloons()
        st.write(gender)
    else:
        st.error('Login Failed')

file=st.file_uploader('Upload a csv file')


if file is not None:
    df=pd.read_csv(file)
    st.dataframe(df.describe())