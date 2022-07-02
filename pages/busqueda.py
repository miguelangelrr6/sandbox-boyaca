# -*- coding: utf-8 -*-
"""
Created on Fri Jul  1 22:31:49 2022

@author: Miguelangel
"""

import streamlit as st
import pandas as pd
from app import df
from PIL import Image

# Page Settings
st.set_page_config(layout="wide")     
m = st.markdown("""
                <style>
                div.css-1r6slb0.e1tzin5v2{
                    background-color: #DCDCDC;
                    padding: 3% 3% 3% 3%;
                    border-radius: 5px;
                    }
                div.css-12w0qpk.e1tzin5v2{
                    background-color: #DCDCDC;
                    padding: 3% 3% 3% 3%;
                    border-radius: 5px;
                    }
                footer.css-qri22k.egzxvld0 {
                    visibility: hidden;
}
                </style>
                """, unsafe_allow_html=True)
                
# Row A
a1, a2, a3 = st.columns(3)
a1.image(Image.open('gobernacion_boyaca_logo.png'))
a2.metric("Pasaportes Entregados", len(df[df["Status"]==1]), None)
a3.metric("Pasaportes Sin Entregar", len(df[df["Status"]==0]), None)
