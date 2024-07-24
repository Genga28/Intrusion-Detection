import numpy as np
import streamlit as st
import pickle
import pandas as pd
from PIL import Image

# Load the model
try:
    with open("int_det_model.pkl", "rb") as pickle_in:
        model = pickle.load(pickle_in)
except FileNotFoundError:
    st.error("Model file not found. Please ensure the model file is in the correct path.")
    st.stop()

# Define the prediction function
def predict_intrusion(src_bytes, dst_host_srv_count, service, dst_bytes, logged_in, dst_host_serror_rate):
    try:
        # Ensure all inputs are converted to the correct data type
        src_bytes = int(src_bytes)
        dst_host_srv_count = int(dst_host_srv_count)
        service = int(service)
        dst_bytes = int(dst_bytes)
        logged_in = int(logged_in)
        dst_host_serror_rate = float(dst_host_serror_rate)
        
        prediction = model.predict([[src_bytes, dst_host_srv_count, service, dst_bytes, logged_in, dst_host_serror_rate]])
        print(prediction)
        return prediction[0]  # Assuming the prediction is an array and returning the first element
    except ValueError as e:
        st.error(f"Input values are not in the expected format: {e}")
        return None

# Main function for the Streamlit app
def main():
    html_temp = """
    <div style="background-colour:black;padding:15px">
    <h1 style="color:white;text-align:center;">Intrusion Detection</h1>
    </div>
    """
    st.markdown(html_temp, unsafe_allow_html=True)

    # Get user input
    src_bytes = st.text_input("src bytes (No. of data bytes transferred from source to destination)", placeholder="Range: 0 to 1379963888")
    dst_host_srv_count = st.text_input("No. of connections having the same port number", placeholder="Range: 0 to 255")
    service = st.text_input("Destination network service used", placeholder="Range: 0 to 69")
    dst_bytes = st.text_input("No. of data bytes transferred from destination to source in a single connection", placeholder="Range: 0 to 1309937401")
    logged_in = st.text_input("Login Status", placeholder="Range: 0 or 1")
    dst_host_serror_rate = st.text_input("The percentage of connections that have activated the flag", placeholder="Range: 0 to 1")

    result = ""
    if st.button("Predict"):
        result = predict_intrusion(src_bytes, dst_host_srv_count, service, dst_bytes, logged_in, dst_host_serror_rate)
        if result is not None:
            st.success(f'The attack type is {result}')
    
    if st.button("Attack types"):
        st.text(""" 1. normal
                    2. neptune
                    3. warezclient
                    4. ipsweep
                    5. portsweep
                    6. Teardrop
                    7. nmap
                    8. satan
                    9. smurf
                    10. pod
                    11. back
                    12. guess_passwd
                    13. ftp_write
                    14. multihop
                    15. rootkit
                    16. buffer_overflow
                    17. imap
                    18. warezmaster
                    19. phf
                    20. land
                    21. loadmodule
                    22. spy
                    23. perl""")

if __name__ == "__main__":
    main()
