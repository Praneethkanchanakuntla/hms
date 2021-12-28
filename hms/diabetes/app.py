import streamlit as st
import pickle
model=pickle.load(open('diabetes.pkl','rb'))
def diabetes():
    html_temp="""
    <div style='background-color:yellow;padding:13px'>
    <h1 style='color:black;text-align:center;'>Diabetes predictor </h1>
    </div>
    """
    st.markdown(html_temp,unsafe_allow_html=True)
    d1=st.text_input("Pregancies")
    d2=st.text_input('Glucose')
    d3=st.text_input('bloodpressure')
    d4=st.text_input('skinthickness')
    d5=st.text_input('Insulin')
    d6=st.text_input('bmi')
    d7=st.text_input('diabetes pedrige ratio (0 to 1)')
    d8=st.text_input('age')
    if st.button('Predict'):
        result=model.predict([[d1,d2,d3,d4,d5,d6,d7,d8]])
        if result==0:
            st.write(' # You dont have diabetes ')
            
        else:
            st.write(' # You might have diabetes consult Doctor Please......')
if __name__=='__main__':
    diabetes()
