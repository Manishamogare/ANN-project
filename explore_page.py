import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt



def show_explore_page():
    st.title("Properties :- ")

    st.write("""### A.  Lea strength (kg) : """)
    st.write("""##### - The Lea strength of yarn is one of the major properties on which the suitability of yarn for its ultimate end use depends. It is the standard method of measuring the strength of the yarn. The frictional forces rendered to the yarn in the lea test reduce the sensitivity of the test to detect weak places in the yarn. A weak yarn can also produce a low strength, but presence of an abnormally weak place in one of the treads may not be detected.""")
    st.write("""### B.  Count Strength Product (CSP) :  """) 
    st.write("""##### -    This indicator is used to assess the strength of a yarn. Technically, this is the product of count of the yarn and its tensile strength measured using a machine. The higher CSP indicates higher strength of the yarn.""")
    st.write("""### C.  CV% of count :""")
    st.write("""##### - The variation in yarn count from one lea to another lea can be measured by the co-efficient of variation( C.V.) which is merely the standard deviation ( SD) expressed as a percentage of the average.
    st.write("""### D.  Unevenness(CV) : """)
    st.write("""#### - Unevenness is a measure of variation in weight per unit length of the yarn or the variation in thickness of the yarn.""")
    st.write("""### E.  Total imperfections(per km) : """)
    st.write("""#### - The imperfection index (IPI) is the sum of yarn thin places/ km (-50%), thick places/km (+50%) and neps/km (+200%) per kilometer of tested yarn for ring spun yarn.""")
     
             



