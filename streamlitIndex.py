import streamlit as st
from datetime import time
from datetime import datetime

st.text('Primera APP de prueba')

with st.form(key='my_form'):
  username = st.text_input('Username: ')
  password = st.text_input('Password: ')
  submitted = st.form_submit_button("Ingresar")
  if submitted:
    st.write("Usuario enviado: ", username, ", contraseña: ", password)

st.text('----------------------------------------')

age = st.slider('Cuantos años tienes?', 0, 130, 25)
st.write("Tengo ", age, ' años')

values = st.slider('Select un rango de valores', 0.0, 100.0, (25.0, 75.0))
st.write('Values:', values)

appointment = st.slider("Schedule your appointment:", value=(time(11, 30), time(12, 45)))
st.write("You're scheduled for:", appointment)

start_time = st.slider("Cuando inicia?", value=datetime(2020, 1, 1, 9, 30), format="MM/DD/YY - hh:mm")
st.write("Inicio:", start_time)
