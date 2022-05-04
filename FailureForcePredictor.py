import pickle
with open("Compression_Failure_Force_Predictor (5)","rb") as f:
  model= pickle.load(f)


import streamlit as st
st.title("Compressive Failure Force Predictor Machine Learning App")
a=st.number_input("Infill_Density")
b=st.number_input("Yeild Strength")
c= st.number_input("Young's Modulus")
d = st.number_input("Poisson's Ratio")

    
Infill_Pattern= st.selectbox("Select Infill_Pattern", ["Hexagonal","Cubic","Concentric"])

h=i=0
if Infill_Pattern=="Cubic":
    h=1
if Infill_Pattern=="Hexagonal":
    i=1


    
prediction=model.predict([[a,b,c,d,h,i]])
button_pressed=st.button("Predict")

if button_pressed:
        
        st.write("Failure Force : " ,prediction[0])
   
