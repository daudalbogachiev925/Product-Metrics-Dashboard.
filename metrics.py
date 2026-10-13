import pandas as pd
import numpy as np

def generate_sample_data(days=180, users=1000):
    np.random.seed(42)
    dates = pd.date_range(end=pd.Timestamp.today(), periods=days)
    data = []
    base_users = users
    for i, d in enumerate(dates):
        growth = 1 + 0.005 * i
        dau = int(base_users * growth * np.random.uniform(0.6, 0.9))
        new = int(dau * np.random.uniform(0.05, 0.15))
        churned = int(dau * np.random.uniform(0.02, 0.08))
        data.append({
            "date": d,
            "dau": dau,
            "new_users": new,
            "churned_users": churned,
            "revenue": round(dau * np.random.uniform(0.5, 2.0), 2)
        })
    return pd.DataFrame(data)

def calc_retention(df):
    df = df.copy()
    df["retention"] = 1 - df["churned_users"] / df["dau"]
    return df

def calc_ltv_cac(df, cac=5.0):
    df = df.copy()
    avg_revenue_per_user = df["revenue"].sum() / df["dau"].sum()
    ltv = avg_revenue_per_user * 12
    df["ltv"] = ltv
    df["cac"] = cac
    df["ltv_cac_ratio"] = ltv / cac
    return df

def calc_mau(df):
    return df["dau"].rolling(30).mean().iloc[-1]
