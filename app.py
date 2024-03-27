import streamlit as st
import numpy as np
from prediction import predict, predict_regg
import json

# # Load options from JSON file
with open("item_type.json", "r") as f:
    data = json.load(f)
    # options = data["options"]

# # Extract keys from the loaded data
options = list(data.keys())

st.title('Industrial Copper Application')

# Create tabs using st.sidebar
tabs = st.sidebar.radio("Navigate to :", ["Predict price", "Predict status"])

# Depending on the selected tab, show different content
if tabs == "Predict price":
    col3, col4 = st.columns(2)
    with col3:       
      # Create a number textbox
      quantity_tons = st.number_input("Enter quantity tons")
      cust_no = st.number_input("Enter the customer number")
      country_no = st.number_input("Enter the country number")     
      # Create a dropdown box with options
      selected_option = st.selectbox("Select an item type", options)
      selected_value = data[selected_option]
      # # Display the selected option
      # st.write("You selected:", selected_option, " Value is -", selected_value)
    with col4:
      app_no = st.number_input("Enter the application number")
      thick_no = st.number_input("Enter the thickness")      
      width_no = st.number_input("Enter the width")
      prod_ref = st.number_input("Enter the product reference number")
      if st.button("Predict price"):
            result_price = predict_regg(np.array([[quantity_tons, cust_no,	country_no,	selected_value,	app_no,	thick_no,	width_no,	prod_ref]]))
            st.write("Price is : ", result_price[0])
    
elif tabs == "Predict status":
    # # Create two columns
    col1, col2 = st.columns(2)
    # st.write("## Tab 2 Content")
    with col1:
      # Create a number textbox
      quantity_tons = st.number_input("Enter quantity tons") 
      cust_no = st.number_input("Enter the customer number") 
      country_no = st.number_input("Enter the country number")     
      # Create a dropdown box with options
      selected_option = st.selectbox("Select an item type", options)
      selected_value = data[selected_option]
      # # Display the selected option
      # st.write("You selected:", selected_option, " Value is -", selected_value)
    with col2: 
      app_no = st.number_input("Enter the application number", placeholder="Enter the number")
      thick_no = st.number_input("Enter the thickness")      
      width_no = st.number_input("Enter the width")
      prod_ref = st.number_input("Enter the product reference number")

      if st.button("Predict status"):
            result = predict(np.array([[quantity_tons, cust_no,	country_no,	selected_value,	app_no,	thick_no,	width_no,	prod_ref]]))
            if result[0] == 1:
              st.text('Status is Won')
            else:
              st.text('Status is Loss')      

