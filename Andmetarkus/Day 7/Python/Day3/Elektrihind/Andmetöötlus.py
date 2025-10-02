import pandas as pd
# Lae elektrihindade graafikud

df = pd.read_json('day-3/elektrihind/el_data_2025.json')
df_expanded = pd.json_normalize(df["data"])

if "timestamp" in df_expanded.columns:
    df_expanded = df_expanded.drop(columns=["timestamp"])

print(df_expanded)

