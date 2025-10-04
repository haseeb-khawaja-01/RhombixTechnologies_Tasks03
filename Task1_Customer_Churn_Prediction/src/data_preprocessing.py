import pandas as pd
import numpy as np

def load_data_from_url(url, save_path=None):
    
    df = pd.read_csv(url)
    if save_path:
        df.to_csv(save_path, index=False)
    return df

def basic_cleaning(df):
    df = df.copy()

    if 'TotalCharges' in df.columns:
        df['TotalCharges'] = pd.to_numeric(df['TotalCharges'], errors='coerce')
        df['TotalCharges'] = df['TotalCharges'].fillna(df['TotalCharges'].median( ))


    if 'customerID' in df.columns:
        df.drop(columns=['customerID'], inplace=True)
    return df
