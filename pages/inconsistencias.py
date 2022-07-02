# -*- coding: utf-8 -*-
"""
Created on Fri Jul  1 22:05:37 2022

@author: Miguelangel
"""

import streamlit as st
import pandas as pd
import datetime as dt
import numpy as np
from app import df
from PIL import Image

#styles
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
             
tiemponegativo = df[df["tiempo"] < 0]
mask3 = df["tiempo"].isnull()
mask4 = df["Status"] == 1


#Side Bar
st.sidebar.markdown("## Panel de Control")
st.sidebar.markdown("Puedes **cambiar** los valores de los *gráficos*")
st.sidebar.markdown("### Rango de Fechas")

#min_date = dt.datetime(2010,1,1)
#max_date = dt.date(2023,1,1)

c_date = st.sidebar.date_input("Selecciona la fecha inicial", value = dt.datetime(2010,1,1), key= "1", min_value = dt.datetime(2010,1,1), max_value = dt.datetime(2023,1,1))
d_date = st.sidebar.date_input("Selecciona la fecha final", value = dt.datetime(2023,1,1), key= "2", min_value = dt.datetime(2010,1,1), max_value = dt.datetime(2023,1,1))
mask_fc1 = df["Creacion"]> np.datetime64(c_date)
mask_fc2 = df["Creacion"]< np.datetime64(d_date)

# Row A
a1, a2, a3 = st.columns(3)
a1.image(Image.open('gobernacion_boyaca_logo.png'))
a2.metric("Pasaportes Tiempo Negativo", len(tiemponegativo), None)
a3.metric("Pasaportes Entregados sin Registro", len(df[mask3 & mask4]), None)

graficas = st.container()
with graficas:
    st.subheader('Pasaportes con tiempo negativo')
    graph_pasaportes_negativos = pd.DataFrame(tiemponegativo[mask_fc1 & mask_fc2]["Creacion"].dt.year.value_counts().sort_index())
    st.bar_chart(graph_pasaportes_negativos)
    
tabla = st.container()
with tabla:
    tiemponegativo[mask_fc1 & mask_fc2]
    
    df[mask3 & mask4]
    
