import pandas as pd
import yfinance as yf
import pandas_datareader as pdr
from datetime import datetime

class DataLoader:
    def load_local_file(self, file_path):
        try:
            if hasattr(file_path, 'name'):
                name = file_path.name
            else:
                name = file_path

            if name.endswith('.csv'):
                df = pd.read_csv(file_path)
            elif name.endswith(('.xls', '.xlsx')):
                df = pd.read_excel(file_path)
            else:
                return None, "Непідтримуваний формат файлу."
            
            print(f"Файл {file_path} успішно завантажено.")
            return df, None
        except Exception as e:
            return None, str(e)

    def fetch_stock_data(self, ticker, start_date, end_date):
        try:
            df = yf.download(ticker, start=start_date, end=end_date)
            if df.empty:
                return None, "Дані не знайдено для цього тікера."
            return df, None
        except Exception as e:
            return None, str(e)

    def fetch_macro_fred(self, series_id, start_date):
        try:
            df = pdr.get_data_fred(series_id, start=start_date)
            return df, None
        except Exception as e:
            return None, str(e)