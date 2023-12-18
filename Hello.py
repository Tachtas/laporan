import streamlit as st
import pandas as pd
import numpy as np
from surrealdb import Surreal

st.title('Uber pickups in NYC')

@st.cache_data
