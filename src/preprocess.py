import pandas as pd

def compute_attendance(df):
    df["sem1_attendance"] = df["sem1_attended"] / df["sem1_total"] * 100
    df["sem2_attendance"] = df["sem2_attended"] / df["sem2_total"] * 100
    return df
