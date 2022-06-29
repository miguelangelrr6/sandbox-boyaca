# -*- coding: utf-8 -*-
"""
Created on Mon Jun 27 14:50:45 2022

@author: Miguelangel
"""

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
df = pd.read_csv("datasetcompletofinal.csv", sep = ";", encoding = "unicode_escape", parse_dates = ['Fecha_entrega','Fecha_creacion', 'Fecha_vencimiento'])



#Side Bar
st.sidebar.markdown("## Panel de Control")
st.sidebar.markdown("Puedes **cambiar** los valores de los *gráficos*")
st.sidebar.markdown("### Rango de Fechas")

#min_date = dt.datetime(2010,1,1)
#max_date = dt.date(2023,1,1)

a_date = st.sidebar.date_input("Selecciona la fecha inicial", value = dt.datetime(2010,1,1), key= "1", min_value = dt.datetime(2010,1,1), max_value = dt.datetime(2023,1,1))
b_date = st.sidebar.date_input("Selecciona la fecha final", value = dt.datetime(2023,1,1), key= "2", min_value = dt.datetime(2010,1,1), max_value = dt.datetime(2023,1,1))
mask_fe1 = df["Fecha_entrega"]> np.datetime64(a_date)
mask_fe2 = df["Fecha_entrega"]< np.datetime64(b_date)

#"The date selected:", a_date
#"The type", type(a_date)
#"Fecha Inicial", a_date[0]
#"Fecha Final", a_date[1]

# Row A
a1, a2, a3 = st.columns(3)
a1.image(Image.open('gobernacion_boyaca_logo.png'))
a2.metric("Pasaportes Entregados", len(df[df["Entregado"]==1]), None)
a3.metric("Pasaportes Sin Entregar", len(df[df["Entregado"]==0]), None)

#Row B
b1, b2, b3, b4 = st.columns(4)
b1.metric("Pasaportes Vencidos", df["Fecha_vencimiento"].value_counts().sort_index().loc["2021-01-08":pd.to_datetime("today")].sum(), None)
b2.metric("Pasaportes por vencerse (3) meses", df["Fecha_vencimiento"].value_counts().sort_index().loc[pd.to_datetime("today"):pd.to_datetime("today") + pd.DateOffset(months = 3)].sum(), None)
b3.metric("Pasaportes", "N", "M")
b4.metric("Pasaportes", "N", "M")
#Row C
graficas = st.container()
with graficas:
    st.subheader('Entregas por Año')
    graph_fecha_entrega_count = pd.DataFrame(df[mask_fe1 & mask_fe2]["Fecha_entrega"].dt.year.value_counts().sort_index())
    st.bar_chart(graph_fecha_entrega_count)
    
    st.subheader('Entregas por Mes')
    graph_fecha_entrega_count_month = pd.DataFrame(df[mask_fe1 & mask_fe2]["Fecha_entrega"].dt.month.value_counts().sort_index())
    st.bar_chart(graph_fecha_entrega_count_month)


#Row C
#c1, c2 = st.columns((7,3))
#with c1:
#    st.header('Grafica 1')
#    st.text('Texto Grafica 1')
#with c2:
#    st.header('Grafica 2')
#    st.text('Texto Grafica 2')
