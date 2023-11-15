import os
import csv


def concatenate_csv_files(folder_path, output_file):
    with open(output_file, 'w', newline='') as output_csvfile:
        csv_writer = csv.writer(output_csvfile)

        for root, dirs, files in os.walk(folder_path):
            for file in files:
                if file.endswith(".csv"):
                    file_path = os.path.join(root, file)
                    with open(file_path, 'r') as input_csvfile:
                        csv_reader = csv.reader(input_csvfile)
                        for row in csv_reader:
                            csv_writer.writerow(row)


if __name__ == "__main__":
    folder_path = "/home/wayne/Datasets/FootballData"
    output_file = "allPdfs.csv"

    concatenate_csv_files(folder_path, output_file)
    print(f"Concatenated all CSV files into {output_file}")
