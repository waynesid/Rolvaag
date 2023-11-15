import csv

while True:
    # Collect user input
    home_odds = input("Enter the home odds (or type 'done' to finish): ")

    # Check if the user wants to exit
    if home_odds.lower() == "done":
        break

    try:
        home_odds = float(home_odds)
        draw_odds = float(input("Enter the draw odds: "))
        away_odds = float(input("Enter the away odds: "))
        label = int(input("Enter the label (1 for home win, 0 for draw, 2 for away win): "))

        # Validate the label input
        if label not in [0, 1, 2]:
            print("Invalid label. Please enter 0, 1, or 2 for the label.")
        else:
            # Create or open the CSV file for writing
            with open('data.csv', 'a', newline='') as csv_file:
                # Define the CSV writer
                csv_writer = csv.writer(csv_file)

                # Write the data to the CSV file
                csv_writer.writerow([home_odds, draw_odds, away_odds, label])

            print("Data saved to data.csv.")
    except ValueError:
        print("Invalid input. Please enter valid numeric values for odds.")