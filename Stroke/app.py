import streamlit as st
import pickle
model=pickle.load(open('stroke.pkl','rb'))
def stroke():
    html_temp="""
    <div style='background-color:grey;padding:13px'>
    <h1 style='color:black;text-align:center;'>Stroke predictor </h1>
    </div>
    """
    st.markdown(html_temp,unsafe_allow_html=True)
    s1=st.text_input('Age')
    s2=st.selectbox('Do you have hypertension',['yes','no'])
    s3=st.selectbox('Do you have blood pressure',['yes','no'])
    s4=st.text_input('Glucose level')
    s5=st.text_input('BMI')
    s6=st.selectbox('Gender',['male','female'])
    s7=st.selectbox('married',['yes','no'])
    s8=st.selectbox('category',['never wroked','private','self employed','children','government job'])
    s9=st.selectbox('home location',['urban','rural'])
    s10=st.selectbox('smoking habit',['used smoke','never smoked','smokes'])
    if s2=='yes':
        s2=1
    else:
        s2=0
    if s3=='yes':
        s3=1
    else:
        s3=0
    if s6=='male':
        s6=1
    else :
        s6=0
    if s7=='yes':
        s7=1
    else:
        s7=0
    if s8=='never wroked':
        s8=1
    elif s8=='private':
        s8=2
    elif s8=='self employed':
        s8=3
    elif s8=='childern':
        s8=4
    else:
        s8=0
    if s9=='urban':
        s9=1
    else:
        s9=0
    if s10=='used to smoke':
        s10=1
    elif s10=='never smoked':
        s10=2
    elif s10=='smokes':
        s10=3
    else:
        s10=0
    if st.button('Predict'):
        result=model.predict([[s1,s2,s3,s4,s5,s6,s7,s8,s9,s10]])
        
        if result==0:
            st.write(' # There is no chance of stroke in near future ')
        else:
            st.write(' # You might get  stroke consult Doctor Please......')
if __name__=='__main__':
    stroke()
    