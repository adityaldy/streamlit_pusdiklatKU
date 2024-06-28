"""
import altair as alt
import numpy as np
import pandas as pd
import streamlit as st


# Welcome to Streamlit!

Edit `/streamlit_app.py` to customize this app to your heart's desire :heart:.
If you have any questions, checkout our [documentation](https://docs.streamlit.io) and [community
forums](https://discuss.streamlit.io).

In the meantime, below is an example of what you can do with just a few lines of code:


num_points = st.slider("Number of points in spiral", 1, 10000, 1100)
num_turns = st.slider("Number of turns in spiral", 1, 300, 31)

indices = np.linspace(0, 1, num_points)
theta = 2 * np.pi * num_turns * indices
radius = indices

x = radius * np.cos(theta)
y = radius * np.sin(theta)

df = pd.DataFrame({
    "x": x,
    "y": y,
    "idx": indices,
    "rand": np.random.randn(num_points),
})

st.altair_chart(alt.Chart(df, height=700, width=700)
    .mark_point(filled=True)
    .encode(
        x=alt.X("x", axis=None),
        y=alt.Y("y", axis=None),
        color=alt.Color("idx", legend=None, scale=alt.Scale()),
        size=alt.Size("rand", legend=None, scale=alt.Scale(range=[1, 150])),
    ))
"""

import streamlit as st 
import pandas as pd 
import requests
from st_aggrid import AgGrid, GridOptionsBuilder

house = pd.read_csv('https://raw.githubusercontent.com/adityaldy/streamlit_pusdiklatKU/main/house_clean.csv')

gb = GridOptionsBuilder.from_dataframe(house)
gb.configure_pagination(paginationAutoPageSize=False, paginationPageSize=10)
gb.configure_default_column(editable=True, groupable=True, filter=True, sortable=True)
gb.configure_side_bar()
gb.configure_grid_options(domLayout='normal', autoSizeColumns=True)
grid_options = gb.build()

def main() : 
  st.header('This is Halaman Streamlit Aldy')
  st.subheader('Setjen LPDP')
  st.markdown('# rendering markdown')
  st.write('Some phytagorean equation : ')
  st.latex('c^2 = a^2+b^2')
  st.write('Metrics')
  st.metric(label="Temperature", value="70 F", delta="-1.2 F")
  st.markdown('# dataframe biasa')
  st.dataframe(house)
  st.markdown('# Aggrid')
  AgGrid(house, gridOptions=grid_options, enable_enterprise_modules=True, theme='streamlit')
  #st.table([x for x in range(1,5)])

  click_me_btn = st.button('Click Me')
  st.write(click_me_btn) #Return True kalo di Click 
  check_btn = st.checkbox('Klik Jika Setuju')
  if check_btn :
    st.write('Anda Setuju')
    
    
  radio_button= st.radio('Choose below',[x for x in range(1,3)])
  st.write('Anda Memilih',radio_button)
    
  #slider 
  age_slider = st.slider('Berapa Usia Anda',0,100)
  st.write('Usia Anda',age_slider)
    
  #Input (Typing)
  num_input = st.number_input('Input Berapapun')
  st.write('Kuadrat dari {} adalah {}'.format(num_input,num_input**2))

if __name__ == '__main__' : 
  main()