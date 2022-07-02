# -*- coding: utf-8 -*-
"""
Created on Fri Jul  1 21:31:41 2022

@author: Miguelangel
"""

import streamlit as st

import streamlit as st
import pandas as pd
import datetime as dt
import numpy as np
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
    
#Dataset
df = pd.read_csv("data/datasetcompletofinal.csv", sep = ";", encoding = "utf-8", parse_dates = ['Fecha_entrega','Fecha_creacion', 'Fecha_vencimiento'])
df.drop("Unnamed: 0", axis = 1, inplace = True)
df.columns = ["Ciudadano", "Pasaporte", "Status", "Entrega", "Paquete", "Serie", "Guia", "Creacion", "Vencimiento"]
df = df[["Ciudadano", "Pasaporte", "Status", "Paquete", "Serie", "Guia", "Creacion", "Entrega", "Vencimiento"]]


#Variables
today = pd.to_datetime("today")
thisyear = today.date().year
lastyear = today.date().year - 1
dif = len(df[df["Creacion"].dt.year == thisyear]) - len(df[df["Creacion"].dt.year == lastyear])
delta = dif / len(df[df["Creacion"].dt.year == lastyear])
deltapor = delta*100
#np.round(deltapor, decimals=2)

tiempo = df["Entrega"] - df["Creacion"]
df["Tiempo"] = tiempo.dt.days

def main():
    st.title("Streamlit Multi-Page")
    st.subheader("Main Page")
    
if __name__ == "__main__":
    main()
    
# Row A
a1, a2, a3 = st.columns(3)
a1.image(Image.open('gobernacion_boyaca_logo.png'))
a2.metric("Pasaportes Entregados", len(df[df["Status"]==1]), None)
a3.metric("Pasaportes Sin Entregar", len(df[df["Status"]==0]), None)

#Row B
b1, b2, b3, b4 = st.columns(4)
b1.metric("Pasaportes Vencidos", df["Vencimiento"].value_counts().sort_index().loc["2021-01-08":pd.to_datetime("today")].sum(), None)
b2.metric("Pasaportes por vencerse (3) meses", df["Vencimiento"].value_counts().sort_index().loc[pd.to_datetime("today"):pd.to_datetime("today") + pd.DateOffset(months = 3)].sum(), None)
b3.metric("Pasaportes Año Pasado", len(df[df["Creacion"].dt.year == lastyear]), None)
b4.metric("Pasaportes este Año", len(df[df["Creacion"].dt.year == thisyear]), str(np.round(deltapor, decimals=2)) + " %")
#Row C
