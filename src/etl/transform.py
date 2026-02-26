import pandas as pd

def transform_data(df):
    # Increase salary by 10%
    df["salary"] = df["salary"] * 1.10
    
    # Create age group column
    df["age_group"] = df["age"].apply(lambda x: "Young" if x < 30 else "Senior")
    
    return df