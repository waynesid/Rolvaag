import csv

# Define a mapping from values to labels
value_to_label = {1: "home", 2: "away", 0: "draw"}

# Input and output file paths
input_file_path = 'data.csv'  # Replace with the path to your input CSV file
output_file_path = 'output.csv'  # Replace with the desired output file path

# Read the input CSV file and write the modified data to the output CSV file
with open(input_file_path, 'r', newline='') as input_file, open(output_file_path, 'w', newline='') as output_file:
    csv_reader = csv.reader(input_file)
    csv_writer = csv.writer(output_file)

    for row in csv_reader:
        # Check if the row has at least one element
        if len(row) > 0:
            # Convert the last column to the corresponding label
            last_column_value = int(row[-1])
            if last_column_value in value_to_label:
                row[-1] = value_to_label[last_column_value]
            else:
                # Handle unknown values (optional)
                row[-1] = "unknown"

            # Write the modified row to the output CSV file
            csv_writer.writerow(row)

print("Conversion completed. Output saved to:", output_file_path)