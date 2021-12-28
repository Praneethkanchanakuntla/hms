import streamlit as st
import pickle
model=pickle.load(open('kidney.pkl','rb'))
def kidney():
    k1=st.number_input('age')
    k2=st.number_input('Blood Pressure')
    k3=st.number_input('specific gravity')
    k4=st.number_input('albumin')
    k5=st.number_input('sugar')
    k6=st.selectbox('red blood cells',['Normal','Abnormal'])
    k7=st.selectbox('puss cells',['normal','Abnormal'])
    k8=st.selectbox('pus cells clumps',['Not pressent','present'])
    k9=st.selectbox('Bacteria',['Not present','present'])
    k10=st.number_input('blood glucose random')
    k11=st.number_input('blood urea')
    k12=st.number_input('serum creatinine')
    k13=st.number_input('sodium')
    k14=st.number_input('potassium')
    k15=st.number_input('hemoglobin')
    k16=st.number_input('packed cell volume')
    k17=st.number_input('white blood cell count')
    k18=st.number_input('red blood cell count')
    k19=st.selectbox('hypertension',['no','yes'])
    k20=st.selectbox('diabetes mellitus',['no','yes'])
    k21=st.selectbox('coronary artery disease',['no','yes'])
    k22=st.selectbox('appetite',['no','yes'])
    k23=st.selectbox('pedal edema',['no','yes'])
    k24=st.selectbox('anemia',['no','yes'])
    if k6=='Normal':
        k6=1
    else:
        k6=0
    if k7=='normal':
        k7=1
    else:
        k7=0
    if k8=='Not present':
        k8=0
    else:
        k8=1
    if k9=='Not present':
        k9=0
    else:
        k9=1
    if k19=='no':
        k19=0
    else:
        k19=1
    if k20=='no':
        k20=0
    else:
        k20=1
    if k21=='no':
        k21=0
    else:
        k21=1
    if k22=='good':
        k22=0
    else:
        k22=1
    if k23=='no':
        k23=0
    else:
        k23=1
    if k24=='no':
        k24=0
    else:
        k24=1
    result=model.predict([[k1,k2,k3,k4,k5,k6,k7,k8,k9,k10,k11,k12,k13,k14,k15,k16,k17,k18,k19,k20,k21,k22,k23,k24]])
    if st.button('predict'):
        if result==1:
            st.title('You have chronic kidney disease')
        else:
            st.title('You dont have Chronic Kidney Disease')
if __name__=='__main__':
    kidney()
        