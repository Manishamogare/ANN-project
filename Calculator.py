import streamlit as st
import math
import time
from conversion_page import conversion
from yarn_count import yarn_count


def calculator():
 
    st.title("Textile Calculator")
    
    select = st.selectbox('What do you want to calculate',options=("Select","Unit Conversions","Yarn Count","Draft"))
    

    if select == "Unit Conversions":
        # creates a horizontal line
        st.write("---")  
        
        conversion()
        
    
       

    if select == "Yarn Count":
        # creates a horizontal line
        st.write("---")
       
        yarn_count()

        
