import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt



def show_explore_page():
    st.title("Yarn Properties :- ")

    st.write("""### A.   Lea strength (kg) : """)
    st.write("""##### - The Lea strength of yarn is one of the major properties on which the suitability of yarn for its ultimate end use depends. It is the standard method of measuring the strength of the yarn. The frictional forces rendered to the yarn in the lea test reduce the sensitivity of the test to detect weak places in the yarn. A weak yarn can also produce a low strength, but presence of an abnormally weak place in one of the treads may not be detected.""")
    st.text("")
    st.text("")
    st.write("""### B.   Count Strength Product (CSP) :  """) 
    st.write("""##### - This indicator is used to assess the strength of a yarn. Technically, this is the product of count of the yarn and its tensile strength measured using a machine. The higher CSP indicates higher strength of the yarn.""")
    st.text("")
    st.text("")
    st.write("""### C.   CV% of count : """)
    st.write("""##### - The variation in yarn count from one lea to another lea can be measured by the co-efficient of variation( C.V.) which is merely the standard deviation ( SD) expressed as a percentage of the average.""")
    st.text("")
    st.text("")
    st.write("""### D.   Unevenness (CV) : """)
    st.write("""##### - Unevenness is a measure of variation in weight per unit length of the yarn or the variation in thickness of the yarn.""")
    st.text("")
    st.text("")
    st.write("""### E.   Total imperfections (per km) : """)
    st.write("""##### - The imperfection index (IPI) is the sum of yarn thin places/ km (-50%), thick places/km (+50%) and neps/km (+200%) per kilometer of tested yarn for ring spun yarn.""")
    st.text("")
    st.text("")
    st.write("""### F.   Yarn irregularity : """)
    st.write("""##### - The irregularity or unevenness of a yarn is commonly deﬁned as the variation in ﬁneness along its length.""")
    st.text("")
    st.text("")
    st.write("""### G.   Yarn tenacity : """)
    st.write("""##### - Tenacity is the standard way of assessing the strength of textile products such as yarn and fibre ropes.""")
    st.text("")
    st.text("")
    st.write("""### H.   Breaking strength and elongation : """)
    st.write("""##### - The force at material rupture is known as ultimate tensile strength, which is commonly shortened to tensile strength or tensile. Elongation is measured by applying tensile force, or stretching the material in the same manner as described previously, and determining the change in length from original.""")
    

    
    
    st.title("Fibre Properties :- ")
    
    st.write("""### A.   Nominal yarn count : """)
    st.write("""##### - Sometimes it may be slightly finer say 10.2s and sometimes it may be slightly coarser say, 9.8s count. This resulting count will be written as a 10s count. Therefore this count will not be an actual count of yarn. It is called the nominal count of yarn.""")
    st.text("") 
    st.text("")
    st.write("""### B.   Uniformity Ratio : """)
    st.write("""##### - Uniformity ratio of cotton fibre is determined by the formula: Uniformity ratio = 50% span length / 2.5% span length x 100 Uniformity ratio is determined in percentage. If it less than 47% there is increasing short fibres.""")
    st.text("") 
    st.text("")
    st.write("""### C.   2.5% span length : """)
    st.write("""##### - It is defined as the distance spanned by 2.5% of fibres in the specimen being tested when the fibres are parallelized and randomly distributed and where the initial starting point of the scanning in the test is considered 100%. This length is measured using "DIGITAL FIBROGRAPH".""")
    st.text("") 
    st.text("")
    st.write("""### D.   Blend ratio : """)
    st.write("""##### - Blending is a process of mixing two or more different fiber in desired percentage.""")
    st.text("") 
    st.text("")
    st.write("""### E.   Mean fibre length : """)
    st.write("""##### - It is defined as the average length of all fibers in the sample, based on weight – length or relative number – length distribution.""")
    st.text("") 
    st.text("")
    st.write("""### F.   Upper quartile length : """)
    st.write("""##### - It is defined as the length that exceeded by 25% of fibers by weight (resp. by number).""")
    st.text("") 
    st.text("")
    st.write("""### G.   First and second nozzle pressure : """)
    st.write("""##### - Nozzle pressure drop is the key parameter determining the kinetic energy of the jet, and the kinetic energy of the jet directly affects the flow field.""")
    st.text("") 
    st.text("")
    st.write("""### H.   Upper half mean length for fibres : """)
    st.write("""##### - Staple length is reported as the average length of the longer half of the fibers (normally called “upper-half-mean” length).""")
    
     
             



