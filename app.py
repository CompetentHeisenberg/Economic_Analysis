import pandas as pd
import streamlit as st
from src.configs.config import init_folders, DATA_PROCESSED
from src.data_services.data_service import handle_file_upload, handle_api_download, handle_fred_download
from src.preprocessor import Preprocessor
from src.ui.ui_comp import render_sidebar, render_welcome_page 
import os

st.set_page_config(page_title="Економічний Аналіз", layout="wide", page_icon="src\\ui\\pngwing.com.png")
init_folders()
preprocessor = Preprocessor()

if 'raw_data' not in st.session_state:
    st.session_state.raw_data = None

source = render_sidebar()

if source == "Завантажити файл":
    uploaded_file = st.sidebar.file_uploader("Оберіть CSV/Excel")
    if uploaded_file:
        handle_file_upload(uploaded_file)

elif source == "Yahoo Finance":
    ticker = st.sidebar.text_input("Тікер", "UAH=X")
    if st.sidebar.button("Завантажити"):
        handle_api_download(ticker, "2024-01-01", "2025-01-01")

elif source == "FRED API":
    st.sidebar.info("Приклади кодів FRED:\n- **GDP**: ВВП США\n- **CPIAUCSL**: Інфляція (CPI)\n- **UNRATE**: Безробіття\n- **M2SL**: Грошова маса M2")
    
    series_id = st.sidebar.text_input("Код показника (Series ID)", "GDP")
    start_date = st.sidebar.date_input("Початкова дата", pd.to_datetime("2010-01-01"))
    
    if st.sidebar.button("Завантажити з FRED"):
        handle_fred_download(series_id, start_date)

if st.session_state.raw_data is None:
    render_welcome_page()

else:
    st.subheader("Вихідні дані")
    st.dataframe(st.session_state.raw_data.head())

    cleaned = preprocessor.clean_data(st.session_state.raw_data)
    scaled = preprocessor.scale_data(cleaned)
    
    st.divider()
    st.subheader("Дані для багатовимірного аналізу (Нормовані)")
    st.dataframe(scaled.head())

    if st.button("Зберегти у data/processed"):
        save_path = os.path.join(DATA_PROCESSED, "prepared_data.csv")
        scaled.to_csv(save_path)
        st.success(f"Файл збережено успішно: {save_path}")