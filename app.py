# -*- coding: utf-8 -*-
"""
Created on Fri Jul  1 21:31:41 2022

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
                div.css-79elbk.e1fqkh3o8 {
                    visibility: collapse;
                    }
                .css-k0sv6k.e8zbici2 {
                    background-color: #349D60;
                    color: white;
                    }
                .css-1siy2j7.e1fqkh3o3 {
                    background-color: rgba(52, 157, 96, 0.2);
                    }
                </style>
                """, unsafe_allow_html=True)

# ####################################MAIN PAGE


def main_page():
    st.markdown("# Panel de Control :pushpin:")
    # Dataset
    df = pd.read_csv("data/datasetcompletofinal.csv", sep = ";", encoding = "utf-8", parse_dates = ['Fecha_entrega','Fecha_creacion', 'Fecha_vencimiento'])
    df.drop("Unnamed: 0", axis = 1, inplace = True)
    df.columns = ["Ciudadano", "Pasaporte", "Status", "Entrega", "Paquete", "Serie", "Guia", "Creacion", "Vencimiento", "Tiempo"]
    df = df[["Ciudadano", "Pasaporte", "Status", "Paquete", "Serie", "Guia", "Creacion", "Entrega", "Vencimiento", "Tiempo"]]
    
    df_pqr = pd.read_csv("data/ps_PQRSD.csv", sep = ';',
                    encoding= 'unicode_escape',
                     header = 0,
                     names = ["No_Expediente", "Tipo_Documental", "No_Radicado", "Titulo_asunto","Archivado",
                              "Fecha_creacion","Dependencia","Origen","Usuario_creador","Expediente_asociado"],
                     parse_dates = ['Fecha_creacion'])
    
    #Variables
    today = pd.to_datetime("today")
    thisyear = today.date().year
    lastyear = today.date().year - 1
    dif = len(df[df["Creacion"].dt.year == thisyear]) - len(df[df["Creacion"].dt.year == lastyear])
    delta = dif / len(df[df["Creacion"].dt.year == lastyear])
    deltapor = delta*100
    #np.round(deltapor, decimals=2)
    
    #tiempo = df["Entrega"] - df["Creacion"]
    #df["Tiempo"] = tiempo.dt.days
        
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
    c1, c2, c3, c4 = st.columns(4)
    c1.metric("Total PQRS", len(df_pqr), None)
    c2.metric("Solicitud de Información", df_pqr["Expediente_asociado"].value_counts()["76.5. Solicitudes de  Información"], None)
    c3.metric("Quejas", df_pqr["Expediente_asociado"].value_counts()["76.2. Quejas"], None)
    c4.metric("Denuncias", df_pqr["Expediente_asociado"].value_counts()["76.4. Denuncias"], None)

#####################################PASAPORTES PAGE

def page2():
    
    import streamlit as st
    import pandas as pd
    import datetime as dt
    import numpy as np
    from PIL import Image
    
        
    #styles
    #st.set_page_config(layout="wide")
    st.markdown("# Pasaportes :closed_book:")
    # m = st.markdown("""
    #                 <style>
    #                 div.css-1r6slb0.e1tzin5v2{
    #                     background-color: #DCDCDC;
    #                     padding: 3% 3% 3% 3%;
    #                     border-radius: 5px;
    #                     }
    #                 div.css-12w0qpk.e1tzin5v2{
    #                     background-color: #DCDCDC;
    #                     padding: 3% 3% 3% 3%;
    #                     border-radius: 5px;
    #                     }
    #                 footer.css-qri22k.egzxvld0 {
    #                     visibility: hidden;
    # }
    #                 </style>
    #                 """, unsafe_allow_html=True)
    
    df = pd.read_csv("data/datasetcompletofinal.csv", sep = ";", encoding = "utf-8", parse_dates = ['Fecha_entrega','Fecha_creacion', 'Fecha_vencimiento'])
    df.drop("Unnamed: 0", axis = 1, inplace = True)
    df.columns = ["Ciudadano", "Pasaporte", "Status", "Entrega", "Paquete", "Serie", "Guia", "Creacion", "Vencimiento"]
    df = df[["Ciudadano", "Pasaporte", "Status", "Paquete", "Serie", "Guia", "Creacion", "Entrega", "Vencimiento"]]
    
    #Variables
    a_date = dt.datetime(2010,1,1)
    b_date = dt.datetime(2023,1,1)
    
    #Side Bar
    # st.sidebar.markdown("## Panel de Control")
    # st.sidebar.markdown("Puedes **cambiar** los valores de los *gráficos*")
    st.sidebar.markdown("### Rango de Fechas")
    
    #min_date = dt.datetime(2010,1,1)
    #max_date = dt.date(2023,1,1)
    
    
    
    a_date = st.sidebar.date_input("Selecciona la fecha inicial", value = dt.datetime(2010,1,1), key= "1", min_value = dt.datetime(2010,1,1), max_value = dt.datetime(2023,1,1))
    b_date = st.sidebar.date_input("Selecciona la fecha final", value = dt.datetime(2023,1,1), key= "2", min_value = dt.datetime(2010,1,1), max_value = dt.datetime(2023,1,1))
    mask_fe1 = df["Entrega"]> np.datetime64(a_date)
    mask_fe2 = df["Entrega"]< np.datetime64(b_date)
    
    # Row A
    a1, a2, a3 = st.columns(3)
    a1.image(Image.open('gobernacion_boyaca_logo.png'))
    a2.metric("Pasaportes Entregados", len(df[df["Status"]==1]), None)
    a3.metric("Pasaportes Sin Entregar", len(df[df["Status"]==0]), None)
    
    #Row C
    graficas = st.container()
    with graficas:
        st.subheader('Entregas por Año')
        graph_fecha_entrega_count = pd.DataFrame(df[mask_fe1 & mask_fe2]["Entrega"].dt.year.value_counts().sort_index())
        st.bar_chart(graph_fecha_entrega_count)
        
        st.subheader('Entregas por Mes')
        graph_fecha_entrega_count_month = pd.DataFrame(df[mask_fe1 & mask_fe2]["Entrega"].dt.month.value_counts().sort_index())
        st.bar_chart(graph_fecha_entrega_count_month)

#####################################INCONSISTENCIAS PAGE

def page3():
    import streamlit as st
    import pandas as pd
    import datetime as dt
    import numpy as np
    from PIL import Image
    
    #styles
    #st.set_page_config(layout="wide")
    st.markdown("# Inconsistencias :exclamation:")
    # m = st.markdown("""
    #                 <style>
    #                 div.css-1r6slb0.e1tzin5v2{
    #                     background-color: #DCDCDC;
    #                     padding: 3% 3% 3% 3%;
    #                     border-radius: 5px;
    #                     }
    #                 div.css-12w0qpk.e1tzin5v2{
    #                     background-color: #DCDCDC;
    #                     padding: 3% 3% 3% 3%;
    #                     border-radius: 5px;
    #                     }
    #                 footer.css-qri22k.egzxvld0 {
    #                     visibility: hidden;
    # }
    #                 </style>
    #                 """, unsafe_allow_html=True)
    
    df = pd.read_csv("data/datasetcompletofinal.csv", sep = ";", encoding = "utf-8", parse_dates = ['Fecha_entrega','Fecha_creacion', 'Fecha_vencimiento'])
    df.drop("Unnamed: 0", axis = 1, inplace = True)
    df.columns = ["Ciudadano", "Pasaporte", "Status", "Entrega", "Paquete", "Serie", "Guia", "Creacion", "Vencimiento"]
    df = df[["Ciudadano", "Pasaporte", "Status", "Paquete", "Serie", "Guia", "Creacion", "Entrega", "Vencimiento"]]
    
    #Variables
    c_date = dt.datetime(2010,1,1)
    d_date = dt.datetime(2023,1,1)
    tiemponegativo = df[df["Tiempo"] < 0]
    mask3 = df["Tiempo"].isnull()
    mask4 = df["Status"] == 1
    
    
    #Side Bar
    # st.sidebar.markdown("## Panel de Control")
    # st.sidebar.markdown("Puedes **cambiar** los valores de los *gráficos*")
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

#####################################BUSQUEDA PAGE
def page4():
    import streamlit as st
    import pandas as pd
    from PIL import Image

    
    # Page Settings
    #st.set_page_config(layout="wide")   
    st.markdown("# Búsqueda :mag_right:")  
    # m = st.markdown("""
    #                 <style>
    #                 div.css-1r6slb0.e1tzin5v2{
    #                     background-color: #DCDCDC;
    #                     padding: 3% 3% 3% 3%;
    #                     border-radius: 5px;
    #                     }
    #                 div.css-12w0qpk.e1tzin5v2{
    #                     background-color: #DCDCDC;
    #                     padding: 3% 3% 3% 3%;
    #                     border-radius: 5px;
    #                     }
    #                 footer.css-qri22k.egzxvld0 {
    #                     visibility: hidden;
    # }
    #                 </style>
    #                 """, unsafe_allow_html=True)
    
    df = pd.read_csv("data/datasetcompletofinal.csv", sep = ";", encoding = "utf-8", parse_dates = ['Fecha_entrega','Fecha_creacion', 'Fecha_vencimiento'])
    df.drop("Unnamed: 0", axis = 1, inplace = True)
    df.columns = ["Ciudadano", "Pasaporte", "Status", "Entrega", "Paquete", "Serie", "Guia", "Creacion", "Vencimiento"]
    df = df[["Ciudadano", "Pasaporte", "Status", "Paquete", "Serie", "Guia", "Creacion", "Entrega", "Vencimiento"]]
    
    
    # Side Bar
    
    # Variables
    range_tiempo = df["Tiempo"].dropna().sort_values()
    range_tiempo_low = range_tiempo.min()
    range_tiempo_high = range_tiempo.max()
    mask_ciudadano = "None"
    mask_pasaporte = "None"
    status_filter = "None"
    # Filters
    ciudadano_filter = st.sidebar.text_input('No de Ciudadano', '')
    pasaporte_filter = st.sidebar.text_input('No de Pasaporte', '')
    status_filter = st.sidebar.radio(
         "Estado de entrega",
         ('Ambos', 'Entregado', 'No Entregado'))
    time_filter_initial, time_filter_end = st.sidebar.select_slider(
         'Selecciona el rango de tiempo',
         options=range_tiempo,
         value=(range_tiempo_low, range_tiempo_high))
    st.sidebar.write('Se va a filtrar desde el tiempo de entrega', time_filter_initial, ' hasta', time_filter_end, " días")
    
    # mask_ciudadano = df["Ciudadano"] == ciudadano_filter
    # mask_pasaporte = df["Pasaporte"] == pasaporte_filter
    if ciudadano_filter == '':
        mask_ciudadano = df["Ciudadano"].notnull()
    else:
        mask_ciudadano = df["Ciudadano"] == ciudadano_filter
    
    if pasaporte_filter == '':
        mask_pasaporte = df["Pasaporte"].notnull()
    else:
        mask_pasaporte = df["Pasaporte"] == pasaporte_filter
    
    if status_filter == "Entregado":
        status_filter = 1
    elif status_filter == "No Entregado":
        status_filter = 0
    else:
        status_filter = None
    
    mask_status_filter = df["Status"] == status_filter
    
    # if status_filter != "Ambos":
    #     mask_status_filter = df["Status"] == status_filter
    # else:
    #     mask_status_filter = df["Status"].notnull()
    
    
    mask_time_low = df["Tiempo"] > time_filter_initial
    mask_time_high = df["Tiempo"] < time_filter_end
    mask_time_null = df["Tiempo"].isnull()
    
    df_busqueda = df[(mask_time_low & mask_time_high) | mask_time_null]
    # Row A
    a1, a2, a3 = st.columns(3)
    a1.image(Image.open('gobernacion_boyaca_logo.png'))
    a2.metric("Pasaportes Entregados", len(df[df["Status"]==1]), None)
    a3.metric("Pasaportes Sin Entregar", len(df[df["Status"]==0]), None)
    
    tabla = st.container()
    with tabla:
        if status_filter == None:
            df_busqueda[mask_ciudadano & mask_pasaporte]
        else:
            df_busqueda[(mask_status_filter & mask_ciudadano) & mask_pasaporte]    
#####################################EDA PQRS
def page5():
    import pandas as pd
    import streamlit as st
    import matplotlib.pyplot as plt
    st.markdown("# PQRS :telephone_receiver:")
    
    # Dataset
    df_pqr = pd.read_csv("data/ps_PQRSD.csv", sep = ';',
                    encoding= 'unicode_escape',
                     header = 0,
                     names = ["No_Expediente", "Tipo_Documental", "No_Radicado", "Titulo_asunto","Archivado",
                              "Fecha_creacion","Dependencia","Origen","Usuario_creador","Expediente_asociado"],
                     parse_dates = ['Fecha_creacion'])
    # Variables
    pie1_label = df_pqr["Expediente_asociado"].value_counts().index
    pie1_values = df_pqr["Expediente_asociado"].value_counts().values
    pie1_explode = (0, 0.1, 0, 0, 0, 0)
    fig1, ax1 = plt.subplots()
    ax1.pie(pie1_values, explode=pie1_explode, labels=None, autopct='%1.1f%%',
        shadow=True, startangle=90)
    ax1.axis('equal')
    df_pqr_count = df_pqr["Expediente_asociado"].value_counts().to_frame()
    df_pqr_count["Porcentaje"] = df_pqr_count["Expediente_asociado"]/df_pqr_count["Expediente_asociado"].sum()
    
    df_pqr_count["Porcentaje"] = df_pqr_count["Porcentaje"] * 100
    
    # Row A
    a1, a2, a3 = st.columns(3)
    a1.image(Image.open('gobernacion_boyaca_logo.png'))
    a2.metric("Total PQRS", len(df_pqr), None)
    a3.metric("Solicitud de Información", df_pqr["Expediente_asociado"].value_counts()["76.5. Solicitudes de  Información"], None)
    
    #Row B
    graph1, graph2 = st.columns(2)
    with graph1:
        st.pyplot(fig1)
    with graph2:
        df_pqr_count
        
    # Row C
    graph3 = st.container()
    with graph3:
        st.line_chart(data = df_pqr["Fecha_creacion"].value_counts().sort_index(), width=0, height=0, use_container_width=True)
    # Row D
    graph4, graph5 = st.columns(2)
    with graph4:
        st.bar_chart(data = df_pqr["Archivado"].value_counts(), width=0, height=0, use_container_width=True)
    with graph5: 
        st.bar_chart(data = df_pqr["Tipo_Documental"].value_counts(), width=0, height=475, use_container_width=True)

#####################################INTRO

page_names_to_funcs = {
    "Panel de Control": main_page,
    "Pasaportes": page2,
    "Inconsistencias": page3,
    "Búsqueda": page4,
    "PQRS": page5,
}
st.sidebar.image("gobernacion_boyaca_logo.png", use_column_width=True)
selected_page = st.sidebar.selectbox("Navegación", page_names_to_funcs.keys())
page_names_to_funcs[selected_page]()

