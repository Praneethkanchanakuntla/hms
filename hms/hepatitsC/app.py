import streamlit as st
import pickle
files=open('hepat.pkl', 'rb')
classifier=pickle.load(files)
files.close();


def predict():
    html_temp="""
    <div style='background-color:yellow;padding:13px'>
    <h1 style='color:black;text-align:center;'>Hepatitis predictor </h1>
    </div>
    """
    #Age	Sex	AST	BIL	CHE	CREA	GGT	ALPmean	CHOLmean	ALBmean	PROTmean	ALTmean
    st.markdown(html_temp,unsafe_allow_html=True)
    h1=st.text_input('Age')
    h2=st.selectbox('sex',['male','female'])
    h3=st.number_input('Aspartate Transaminase')
    h4=st.number_input('Bilirubin')
    h5=st.number_input('Acetylcholinesterase')
    h6=st.number_input('Creatinine')
    h7=st.number_input('Gamma-Glutamyl Transferase')
    h8=st.number_input('Alkaline phosphatase')
    h9=st.number_input('cholesterol')
    h10=st.number_input('Albumin Blood Test')
    h11=st.number_input('Proteins')
    h12=st.number_input('Alanine Transaminase')
    if h2=='male':
        gen=1;
    else:
        gen=0;
    if st.button('Predict'):
       re=[[h1,gen,h3,h4,h5,h6,h7,h8,h9,h10,h11,h12]]
       result=classifier.predict(re)
       if result==0:
            st.write(' # Blood Donor')
       elif result==1:
            st.write(' # Suspected Blood Donor')
       elif result==2:
            st.write('# Hepatitis')
       elif result==3:
          st.write('# Fibrosis')
       else:
           st.write('Cirrhosis ')
       st.write('')
if __name__=='__main__':
    st.title('Hepatitis disease')
    st.text('\n')
    predict()