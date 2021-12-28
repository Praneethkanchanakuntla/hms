import streamlit as st
import pickle as pt
model=pt.load(open('breast.pkl','rb'))
def breast():
    x=['radius_mean','texture_mean', 'perimeter_mean', 'area_mean',
       'smoothness_mean', 'compactness_mean', 'concavity_mean',
       'concave points_mean', 'symmetry_mean', 'fractal_dimension_mean',
       'radius_se', 'texture_se', 'perimeter_se', 'area_se', 'smoothness_se',
       'compactness_se', 'concavity_se', 'concave points_se', 'symmetry_se',
       'fractal_dimension_se', 'radius_worst', 'texture_worst',
       'perimeter_worst', 'area_worst', 'smoothness_worst',
       'compactness_worst', 'concavity_worst', 'concave points_worst','symmetry_worst', 'fractal_dimension_worst']
    lst=[]
    for i in x:
        x=st.number_input(i)
        lst.append(x)
    if st.button('predict'):
        result=model.predict([lst])
        if result==1:
            st.title('you are cancer is  Malignant ')
        else:
            st.title('you are cancer is Benign tumor')
if __name__=="__main__":
    breast()
        
         