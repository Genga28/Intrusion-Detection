import numpy as np
import streamlit as st
import pickle
import pandas as pd

from PIL import Image

pickle_in = open("C:\\Users\\kgeng\\Downloads\\Projects\\Intrusion detection\\intrusion_det_model.pkl","rb")
model=pickle.load(pickle_in)

def predict_intrusion(src_bytes,dst_host_srv_count,service,dst_bytes):
    
    prediction=model.predict([[src_bytes,dst_host_srv_count,service,dst_bytes]])
    print(prediction)
    return prediction



def main():
    st.title("Intrusion detection")
    html_temp = """
    <div style="background-colour:black;padding:15px">
    <h2 style="color:white;text-align:center;">Intrusion detection</h2>
    """
    st.markdown(html_temp,unsafe_allow_html=True)
    src_bytes = st.text_input("src_bytes","Type Here")
    dst_host_srv_count = st.text_input("dst_host_srv_count","Type Here")
    service = st.text_input("service","Type Here")
    dst_bytes = st.text_input("dst_bytes","Type Here")
    result=""
    if st.button("Predict"):
        result=predict_intrusion(src_bytes,dst_host_srv_count,service,dst_bytes)
    st.success('The output is {}'.format(result))
    if st.button("About"):
        st.text("Lets LEarn")
        st.text("Built with Streamlit")





if __name__ == "__main__":
    main()