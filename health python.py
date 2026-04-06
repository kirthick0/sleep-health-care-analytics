import pandas as pd
file_path = "data.csv"   
df = pd.read_csv(r"C:\Users\kirthick\Downloads\archive (1)\sleep_health_dataset.csv")

print("Original Data:")
print(df.head())
df = df.drop_duplicates()
df = df.dropna()
df.columns = df.columns.str.strip()        
df.columns = df.columns.str.lower()       
df.columns = df.columns.str.replace(" ", "_")
numeric_cols = df.select_dtypes(include=['int64', 'float64']).columns

for col in numeric_cols:
    Q1 = df[col].quantile(0.25)
    Q3 = df[col].quantile(0.75)
    IQR = Q3 - Q1

    df = df[
        (df[col] >= Q1 - 1.5 * IQR) &
        (df[col] <= Q3 + 1.5 * IQR)
    ]
df.to_csv("cleaned_data.csv", index=False)
print("\nCleaned Data Saved as cleaned_data.csv")
print(df.head())