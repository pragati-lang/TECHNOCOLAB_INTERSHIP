# Done by Mentor(Action not considered)
import pandas as pd
import numpy as np
import pickle
import streamlit as st

pickle_in = open('stock_log_reg.pkl', 'rb')
classifier = pickle.load(pickle_in)

def predict_vol(X):
    pred = classifier.predict(X)
    output = np.argmax(pred)
    return output

def main():

    st.title("Predicting Market Volatility")

    html_temp = """
	<div style ="background-color:yellow;padding:13px">
	<h1 style ="color:black;text-align:center;">Streamlit Market Prediction Logistic Regression ML App </h1>
	</div>
	"""
    
    st.markdown(html_temp, unsafe_allow_html = True)
    open = st.number_input('open')
    high = st.number_input('high')
    low = st.number_input('low')
    close = st.number_input('close')
    volume = st.number_input('volume')      
    cont_len = st.number_input('comment length')
    cont_pol = st.number_input('comment polarity')           
    date = st.date_input('date')    
    date_year = date.year
    date_month = date.month
    date_day = date.day
    sentiment = st.selectbox('sentiment', ['postive','neutral','negative'])
    
    sent_pos = 0
    sent_neu = 0
    sent_neg = 0
    if sentiment =='negative':
        sent_pos = 0
        sent_neu = 0
        sent_neg = 1
    elif sentiment =='neutral':
        sent_pos = 0
        sent_neu = 1
        sent_neg = 0
    elif sentiment =='positive':
        sent_pos = 1
        sent_neu = 0
        sent_neg = 0
    df = pd.DataFrame({'open':open,
    'high':high,
    'low':low,
    'close':close,
    'volume':volume,
    'cont_len':cont_len,
    'cont_pol':cont_pol,
    'date_year':date_year,
    'date_month':date_month,
    'date_day':date_day,
    'sent_neg':sent_neg,
    'sent_neu':sent_neu,
    'sent_pos':sent_pos},index=[0],
    columns=['open',
     'high',
     'low',
     'close',
     'volume',
     'cont_len',
     'cont_pol',
     'date_year',
     'date_month',
     'date_day',
     'sent_neg',
     'sent_neu',
     'sent_pos'])
    
    features = ['open',
     'high',
     'low',
     'close',
     'volume',
     'cont_len',
     'cont_pol',
     'date_year',
     'date_month',
     'date_day',
     'sent_neg',
     'sent_neu',
     'sent_pos']

	
    X = df[features]
    if st.button("Predict"):
        output = predict_vol(X)
        if output == 1:
            st.success('Up')
        else:
            st.success('Down')  
            
if __name__=='__main__':
	main()