import pandas as pd
import matplotlib.pyplot as plt
import sys

def analyze_column(file_path, column_name):
    try:
        #file path to be put manually
        df = pd.read_excel(r'C:\Users\meher\Downloads\test.xlsx')
    except Exception as e:
        print(f"Error reading Excel file: {e}")
        return

    if column_name not in df.columns:
        print(f"Column '{column_name}' not found in the dataset.")
        return

    column = df[column_name].dropna()

    if not pd.api.types.is_numeric_dtype(column):
        print(f"Column '{column_name}' is not numeric.")
        return

    print(f"Statistical analysis for column: {column_name}")
    print(f"Mean: {column.mean()}")
    print(f"Median: {column.median()}")
    print(f"Mode: {column.mode().tolist()}")
    print(f"Standard Deviation: {column.std()}")
    print(f"Minimum: {column.min()}")
    print(f"Maximum: {column.max()}")

    # Plotting
    plt.figure(figsize=(10, 6))
    plt.hist(column, bins=30, color='skyblue', edgecolor='black')
    plt.title(f"Distribution of {column_name}")
    plt.xlabel(column_name)
    plt.ylabel("Frequency")
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python analyze_excel_column.py <excel_file_path> <column_name>")
    else:
        dispfile=sys.argv[1]
        print("this is the excel file we putting- " + dispfile)
        dispcol=sys.argv[2]
        print("this is the col we putting- " + dispcol)
        analyze_column(sys.argv[1], sys.argv[2])
