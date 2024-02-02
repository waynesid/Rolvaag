import os
import pandas as pd

def preprocess_data():
    # Specify the directory you want to use
    directory = r"C:\Users\USER\Wayne\Rolvaag\FootballData"
    output_file = 'final_output.csv'

    # Specify the columns you want to keep
    columns = ["FTHG","FTAG","HST","AST","B365H","B365D","B365A","FTR"]

    # Create an empty DataFrame to store all data
    all_data = pd.DataFrame()

    # Loop through every CSV file in the directory and its subdirectories
    for subdir, dirs, files in os.walk(directory):
        for filename in files:
            if filename.endswith(".csv"):
                try:
                    # Load the CSV file
                    data = pd.read_csv(os.path.join(subdir, filename), delimiter=',')
                    
                    # Check if all columns exist in the DataFrame
                    if set(columns).issubset(data.columns):
                        # Keep only the specified columns
                        data = data[columns]
                        
                        # Fill NaN values with the column mean
                        for i in data.columns[data.isnull().any(axis=0)]:
                            data[i].fillna(data[i].mean(), inplace=True)
                        
                        # Append the data to the all_data DataFrame
                        all_data = pd.concat([all_data, data])
                except pd.errors.ParserError:
                    print(f"Skipping file due to parsing error: {filename}")

    # Save the DataFrame to the CSV file
    all_data.to_csv(output_file, index=False)

if __name__ == '__main__':
    preprocess_data()
