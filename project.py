import streamlit as st
import requests

st.markdown('<iframe src="https://embed.lottiefiles.com/animation/78969"></iframe>',
 unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)
with col1:
    currency1 = st.selectbox('Currency 1', ['EUR', 'USD', 'GBP', 'CNY', 'JPY', 'KRW'])
with col2:
    if currency1 == 'EUR':
        st.markdown('<iframe src="https://embed.lottiefiles.com/animation/54010"></iframe>', unsafe_allow_html=True)
    elif currency1 == 'USD':
        st.markdown('<iframe src="https://embed.lottiefiles.com/animation/28999"></iframe>', unsafe_allow_html=True)
    elif currency1 == 'JPY':
        st.markdown('<iframe src="https://embed.lottiefiles.com/animation/103127"></iframe>', unsafe_allow_html=True)
    elif currency1 == 'CNY':
        st.markdown('<iframe src="https://embed.lottiefiles.com/animation/103205"></iframe>', unsafe_allow_html=True)
    elif currency1 == 'GBP':
        st.markdown('<iframe src="https://embed.lottiefiles.com/animation/103212"></iframe>', unsafe_allow_html=True)
    else:
        st.markdown('<iframe src="https://embed.lottiefiles.com/animation/103133"></iframe>', unsafe_allow_html=True)
with col3:
    currency2 = st.selectbox('Currency 2', ['EUR', 'USD', 'GBP', 'CNY', 'JPY', 'KRW'])

url = f'https://api.exchangerate.host/convert?from={currency1}&to={currency2}'
re = requests.get(url)
re = re.json()
result = re['result']


url2 = f'https://api.exchangerate.host/convert?from={currency2}&to={currency1}'
re2 = requests.get(url2)
re2 = re2.json()
result2 = re2['result']
print(url)
print(url2)
print(re)
print("hasil 1 = ", result)
print("hasil 2 = ", result2)

col1, col2 = st.columns(2)
with col1:
    st.write(f'1 {currency1} to {currency2}')
    st.success(result)
with col2:
    st.write(f'1 {currency2} to {currency1}')
    st.success(result2)
col1, col2 = st.columns(2)
with col1:
    amount = st.number_input(currency1)
with col2:
    converted = amount*result
    st.write(f'Converted Amount')
    st.success(f'{converted:.5f}')
st.markdown('<style> body{text-align:center;} #Mainmenu, footer{visibility: hidden;} .css-fg4pbf {background-color: #A5C9CA;} </style>', 
 unsafe_allow_html=True)
# step 1 function looping 2x return array [], result = [1,2] hasil ini 
# step 2 col1 = [index yg pertama]
# step 3 col2 = [index array yg kedua]
# google search = python function looping output array
