import streamlit as st
from src.data_loader import DataLoader

loader = DataLoader()

def handle_file_upload(uploaded_file):
    if uploaded_file is not None:
        df, err = loader.load_local_file(uploaded_file)
        if not err:
            st.session_state.raw_data = df
            st.success("Файл успішно завантажено")
        else:
            st.error(f"Помилка: {err}")

def handle_api_download(ticker, start_date, end_date):
    with st.spinner(f'Завантаження даних для {ticker}...'):
        df, err = loader.fetch_stock_data(ticker, start_date, end_date)
        if not err:
            st.session_state.raw_data = df
            st.success(f"Дані {ticker} отримано")
        else:
            st.error(f"Помилка Yahoo API: {err}")

def handle_fred_download(series_id, start_date):
    with st.spinner(f'Завантаження серії {series_id} з бази FRED...'):
        df, err = loader.fetch_macro_fred(series_id, start_date)
        
        if not err:
            df.columns = [series_id]
            st.session_state.raw_data = df
            st.success(f"Макропоказник {series_id} успішно завантажено!")            
            st.info("💡 Дані завантажено. Перейдіть на вкладку обробки для аналізу.")
        else:
            st.error(f"Помилка FRED API: {err}")