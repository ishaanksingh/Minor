import pandas as pd

# Set the Excel file path
excel_file_path = "/Users/charvi/Minor-1/dbsolve.xlsx"  # Update the path

# Read the Excel file using pandas
data = pd.read_excel(excel_file_path)

# Check the column names
print("Column Names:", data.columns)

# Ensure 'Tag' is in the columns
tag_column = 'Tag'  # Change this to the actual Tag column name
if tag_column not in data.columns:
    raise ValueError(f"The '{tag_column}' column is not found in the DataFrame.")

# Create a dictionary to store total counts for each parameter
total_counts = {}

# Iterate over rows in the dataset
for index, row in data.iterrows():
    # Check if 'Tag' is not NaN
    if pd.notna(row[tag_column]):
        parameter = row[tag_column]
        if parameter not in total_counts:
            total_counts[parameter] = 0
        total_counts[parameter] += 1

# Calculate the overall percentage of occurrence for each parameter
total_buildings = len(data)
parameter_percentages = {}

for parameter, count in total_counts.items():
    parameter_percentages[parameter] = (count / total_buildings) * 100

# Print overall parameter percentages
print("Overall Parameter Percentages:")
for parameter, percentage in parameter_percentages.items():
    print(f"    Parameter: {parameter}, Percentage: {percentage:.2f}%")

# Save the result to a CSV file
result_df = pd.DataFrame(list(parameter_percentages.items()), columns=['Parameter', 'Percentage'])
result_df.to_csv('res1.csv', index=False)
print("Result saved to res1.csv")
