  
import numpy as np
import streamlit as st
import pickle
import pandas as pd

from PIL import Image

pickle_in = open("int_det_model.pkl","rb")
model=pickle.load(pickle_in)


def predict_intrusion(src_bytes,dst_host_srv_count,service,dst_bytes,logged_in,dst_host_serror_rate):
    
    prediction=model.predict([[src_bytes,dst_host_srv_count,service,dst_bytes,logged_in,dst_host_serror_rate]])
    print(prediction)
    return prediction



def main():
   
    html_temp = """
    <div style="background-colour:black;padding:15px">
    <h1 style="color:white;text-align:center;">Intrusion detection</h1>
    """
    st.markdown(html_temp,unsafe_allow_html=True)
    src_bytes = st.text_input("src bytes(No.of data bytes transferred from source to destination)",placeholder="Range:0 to 1379963888")
    dst_host_srv_count = st.text_input("No.of connections having the same port number",placeholder="Range:0 to 255")
    service = st.text_input("Destination network service used",placeholder="Range:0 to 69")
    dst_bytes = st.text_input("No.of data bytes transferred from destination to source in single connection",placeholder="Range:0 to 1309937401")
    logged_in = st.text_input("Login Status",placeholder="Range:0 or 1")
    dst_host_serror_rate = st.text_input("The percentage of connections that have activated the flag ",placeholder="Range:0 to 1")
    result=""
    if st.button("Predict"):
        result=predict_intrusion(src_bytes,dst_host_srv_count,service,dst_bytes,logged_in,dst_host_serror_rate)
    st.success('The attack type is {}'.format(result))
    if st.button("Attack types"):
        st.text("1.normal\n2.neptune\n3.warezclient\n4.ipsweep\n5.portsweep\n6.Teardrop\n7.nmap\n8.satan\n9.smurf\n10.pod\n11.back\n12.guess_passwd\n13.ftp_write\n14.multihop\n15.rootkit\n16.buffer_overflow\n17.imap\n18.warezmaster\n19.phf\n20.land\n21.loadmodule\n22.spy\n23.perl")
        
        
       




if __name__ == "__main__":
    main()
