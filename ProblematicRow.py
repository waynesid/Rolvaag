# Find the problematic row
problematic_row = None
for index, row in data.iterrows():
    if len(row) != 4:  # Adjust 4 to the expected number of columns in your data
        problematic_row = index
        break

# Print the index of the problematic row
print("Problematic Row Index:", problematic_row)



# Find rows where the last column is not 'home', 'draw', or 'away'
problematic_rows = []
valid_labels = ['home', 'draw', 'away']

for index, row in data.iterrows():
    if row.iloc[-1] not in valid_labels:
        problematic_rows.append(index)

# Print the indices of the problematic rows
print("Problematic Row Indices:", problematic_rows)