import pandas as pd

def load_jtl(file_path):
    df = pd.read_csv(file_path)
    return df