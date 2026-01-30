from sklearn.preprocessing import StandardScaler
import pandas as pd

class Preprocessor:
    def clean_data(self, df):
        df_cleaned = df.dropna()
        df_numeric = df_cleaned.select_dtypes(include=['number'])
        return df_numeric

    def scale_data(self, df):
        scaler = StandardScaler()
        scaled_data = scaler.fit_transform(df)
        return pd.DataFrame(scaled_data, columns=df.columns, index=df.index)