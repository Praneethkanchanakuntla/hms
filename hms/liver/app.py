import streamlit as st
import pickle
model=pickle.load(open('liver.pkl','rb'))
def liver():
    html_temp="""
    <div style='background-color:yellow;padding:13px'>
    <h1 style='color:black;text-align:center;'>liver patient predictor </h1>
    </div>
    """
    #Age	Gender	Total_Bilirubin	Direct_Bilirubin	Alkaline_Phosphotase	Alamine_Aminotransferase	Aspartate_Aminotransferase	Total_Protiens	Albumin	Albumin_and_Globulin_Ratio
    st.markdown(html_temp,unsafe_allow_html=True)
    l1=st.number_input('Age')
    l2=st.selectbox('gender',['Male','Female'])
    l3=st.number_input('TotalBilirubin')
    l4=st.number_input('Direct_Bilirubin')
    l5=st.number_input('Alkaline_Phosphotase')
    l6=st.number_input('Alamine_Aminotransferase')
    l7=st.number_input('Aspartate_Aminotransferase')
    l8=st.number_input('Total_Protiens')
    l9=st.number_input('Albumin')
    l10=st.number_input('Albumin_and_Globulin_Ratio')
    if l2=='Male':
        l2=1
    else:
        l2=0
    if st.button('predict'):
        result=model.predict([[l1,l2,l3,l4,l5,l6,l7,l8,l9,l10]])
        if result==1:
            st.title('You are a Liver Patient, please be careful')
        else:
            st.title('you are not liver Patient')
if __name__=='__main__':
    liver()