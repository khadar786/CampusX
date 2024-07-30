import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(layout='wide',page_title='StartUp Analysis')
df=pd.read_csv('startup_cleaned.csv')
df['date']=pd.to_datetime(df['date'],errors='coerce')
df['month']=df['date'].dt.month
df['year']=df['date'].dt.year
#data cleaning
#df['Investors Name']=df['Investors Name'].fillna('Undisclosed')

def load_investor_details(investor):
    st.title(investor)
    #load the recent 5 investments of the investor 
    last5_df=df[df['investors'].str.contains(investor)].head()[['date','startup','vertical','city','round','amount']]
    st.subheader('Most Recent Investments')
    st.dataframe(last5_df)
    
    
    col1,col2=st.columns(2)
    col3,col4=st.columns(2)
    col5,col6=st.columns(2)
    
    with col1:
        #biggest investments
        big_series=df[df['investors'].str.contains(investor)].groupby('startup')['amount'].sum().sort_values(ascending=False).head()
        st.subheader('Biggest Investments')
        st.dataframe(big_series)
    
    with col2:
        st.subheader('Biggest Chart')
        fig,ax=plt.subplots()
        ax.bar(big_series.index,big_series.values)
        st.pyplot(fig)
        
    
    with col3:
        st.subheader('Sectors invested in')
        verical_series=df[df['investors'].str.contains(investor)].groupby('vertical')['amount'].sum()
        fig1,ax1=plt.subplots()
        ax1.pie(verical_series,labels=verical_series.index,autopct='%0.01f%%')
        st.pyplot(fig1)
    
    with col4:
        st.subheader('Sectors invested in')
        round_series=df[df['investors'].str.contains(investor)].groupby('round')['amount'].sum()
        fig2,ax2=plt.subplots()
        ax2.pie(round_series,labels=round_series.index,autopct='%0.01f%%')
        st.pyplot(fig2)
    
    with col5:
        st.subheader('YoY investment')
        df['year']=df['date'].dt.year
        year_series=df[df['investors'].str.contains(investor)].groupby('year')['amount'].sum()
        fig3,ax3=plt.subplots(figsize=(10, 6))
        ax3.plot(year_series.index,year_series.values)
        st.pyplot(fig3)
    
    with col6:
        st.subheader('Invested in cities')
        city_series=df[df['investors'].str.contains(investor)].groupby('city')['amount'].sum()
        fig4,ax4=plt.subplots()
        ax4.pie(city_series,labels=city_series.index,autopct='%0.01f%%')
        st.pyplot(fig4)

def load_overall_analysis():
    st.title('Overall Analysis')
    col1,col2,col3,col4=st.columns(4)
    #total invested amount
    total=round(df['amount'].sum())
    
    #max amount infused in startup
    max_funding=df.groupby("startup")['amount'].max().sort_values(ascending=False).head(1).values[0]
    
    #av ticket size
    avg_funding=df.groupby("startup")['amount'].sum().mean()
    
    #total funded startups
    num_startups=df['startup'].nunique()
      
    with col1:
        st.metric('Total',str(total)+' Cr')
    
    with col2:
        st.metric('Max',str(max_funding)+' Cr')
        
    with col3:
        st.metric('Avg',str(round(avg_funding))+' Cr')
    
    with col4:
        st.metric('Funded Startups',num_startups)
    
    st.header('MoM graph')
    selected_option=st.selectbox('Select Type',['Total','Count'])
    if selected_option=='Total':
        temp_df=df.groupby(['year','month'])['amount'].sum().reset_index()
    else:
        temp_df=df.groupby(['year','month'])['amount'].count().reset_index()
        
    temp_df['x_axis']=temp_df['month'].astype('str')+'-'+temp_df['year'].astype('str')
    #temp_df[['amount','x_axis']]
    fig4,ax4=plt.subplots()
    ax4.plot(temp_df['x_axis'],temp_df['amount'])
    st.pyplot(fig4)
    

st.sidebar.title('Startup Funding Analysis')
option=st.sidebar.selectbox('Select One',['Overall Analysis','StartUp','Investor'])

if option=='Overall Analysis':
    #btn0=st.sidebar.button('Show Overall Analysis')
    
    #if btn0:
    load_overall_analysis()
elif option=='StartUp':
    st.sidebar.selectbox('Select StartUp',sorted(df['startup'].unique().tolist()))
    btn1=st.sidebar.button('Find StartUp Details')
    st.title('StartUp Analysis')
else:
    selected_investor=st.sidebar.selectbox('Select Investor',sorted(set(df['investors'].str.split(',').sum())))
    btn2=st.sidebar.button('Find Investor Details')
    
    if btn2:
        load_investor_details(selected_investor)
    else:
        st.title('Investor Analysis')
    

