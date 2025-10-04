import pandas as pd
import numpy as np

def load_data_from_url(url, save_path=None):
    """Load dataset from a raw URL (CSV). Optionally save to save_path."""
    df = pd.read_csv(url)
    if save_path:
        df.to_csv(save_path, index=False)
    return df

def basic_cleaning(df):
    df = df.copy()
    # Example cleaning for Telco dataset
    if 'TotalCharges' in df.columns:
        df['TotalCharges'] = pd.to_numeric(df['TotalCharges'], errors='coerce')
        df['TotalCharges'].fillna(df['TotalCharges'].median(), inplace=True)
    # Drop customerID if present
    if 'customerID' in df.columns:
        df.drop(columns=['customerID'], inplace=True)
    return df
