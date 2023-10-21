import pandas as pd
import streamlit as st
data= pd.read_csv('historico_resultados_pruebas_saber_11.csv')
data

# Filtro 1
st.header("Filtro 1")
st.write ("Mostrar todos los puntajes de matematicas")
filtro1 = data["puntaje_matematicas"]
st.dataframe(filtro1)

# Filtro 2
st.header("filtro 2")
st.write("Mostrar prestacion de servicios contratacion en establecimiento col gente unida jovenes por la paz - luz de oriente")
filtro5 = data[(data['prestacion_servicio'] == 'contratacion') & (data['establecimiento'] == 'col gente unida jovenes por la paz - luz de oriente')] 
st.dataframe(filtro5)

# Filtro 3
st.header("Filtro 3")
st.write ("Mostrar todos los promedios de lenguaje")
filtro2 = data["puntaje_lectura"] 
st.dataframe(filtro2)

# Filtro 4
st.header("filtro 4")
st.write("Mostrar puntajes de institucion  santa teresa")
filtro3 = data[(data['establecimiento'] =='inst educ santa teresa')] 
st.dataframe(filtro3)

# Filtro 5
st.header("filtro 5")
st.write("Mostrar puntaje naturales mayor que 50")
filtro1 = data[data['puntaje_naturales'] > 50]
st.dataframe(filtro1)