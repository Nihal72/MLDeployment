

# this is my first streamlit app

import streamlit as st
import numpy as np
import time

progress_bar = st.sidebar.progress(0)
status_text = st.sidebar.empty()
last_rows = np.random.randn(1 , 1)
chart = st.line_chart(last_rows)

for i in range(1, 101):
    new_rows = last_rows[-1] + np.random.randn(5 , 1).cumsum(axis = 0)
    chart.add_rows(new_rows)
    status_text.text(f"{i}% is completed.")
    progress_bar.progress(i)
    time.sleep(0.1)
    
progress_bar.empty()

st.button("Re-run")


