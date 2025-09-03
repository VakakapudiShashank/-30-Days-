# Day 23 — CSV Data Analyzer
# pip install pandas

import os
import pandas as pd

SAMPLE_FILE = "data.csv"

def create_sample_csv():
    data = {
        "Category": ["Food", "Transport", "Food", "Bills", "Shopping", "Transport"],
        "Amount": [250, 80, 150, 1200, 600, 40],
        "PaymentMode": ["Cash", "UPI", "UPI", "Card", "Card", "Cash"]
    }
    df = pd.DataFrame(data)
    df.to_csv(SAMPLE_FILE, index=False)
    print(f"✅ Sample CSV created: {SAMPLE_FILE}")

def analyze_csv(file_path=SAMPLE_FILE):
    if not os.path.exists(file_path):
        create_sample_csv()

    df = pd.read_csv(file_path)
    print("\n📄 Basic Info")
    print("Shape:", df.shape)
    print("Columns:", list(df.columns))
    print("\nData Types:")
    print(df.dtypes)

    print("\n🔎 First 5 rows:")
    print(df.head())

    print("\n📊 Numeric Summary:")
    print(df.describe())

    if "Category" in df.columns and "Amount" in df.columns:
        print("\n💡 Spend by Category:")
        print(df.groupby("Category")["Amount"].sum())

    print("\n🧮 Missing Values:")
    print(df.isna().sum())

if __name__ == "__main__":
    analyze_csv()
