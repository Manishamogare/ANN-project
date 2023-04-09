import streamlit as st
import math
import time
from conversion_page import conversion

def yarn_count():
    # input 1       
        select1 = st.selectbox('Select length in',options=("km","m","cm","mm","yd","ft","inch"))
        num1 = st.number_input(label="Enter length")
        
        
        # input 2
        select2 = st.selectbox('Select weight in',options=("kg","gm","mg","pounds"))
        num2 = st.number_input(label="Enter weight")

        st.write("#### Different Types Yarn Counts")
        
        if select1 == "km":
            yd = num1 * 1093.61
            m = num1 * 1000
            cm = num1 * 100000
            mm = num1 * 1000000
            ft = num1 * 3280.8399
            inch = num1 * 39370.0787

        operation = st.radio("Select a type of yarn count:",
                            ("Tex", "Den", "Ne", "Nm","Grains/yd"))

        ans = 0

        def calculate():
            if operation == "Tex":
                
                    
                
                ans = num1 + num2
            elif operation == "DEn":
                ans = num1 - num2
            elif operation == "Ne":
                ans = num1 * num2
            elif operation=="Divide" and num2!=0:
                ans = num1 / num2
            else:
                st.warning("Division by 0 error. Please enter a non-zero number.")
                ans = "Not defined"

            st.success(f"Answer = {ans}")

        if st.button("Calculate result"):
            calculate()
            
  
        
