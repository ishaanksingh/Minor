import pandas as pd

# Set the Google Sheet URL
import pandas as pd

sheet_url = "C:\Users\ISHANK\Desktop\testtted\dbsolve.xlsx"
data = pd.read_excel(sheet_url, engine='openpyxl')

# Create a dictionary to store parameter counts for each building
parameter_counts = {}
for building in data['Building'].unique():
    parameter_counts[building] = {}
    for parameter in range(2, 23):  # Range of parameters from 2 to 22
        parameter_counts[building][parameter] = 0

# Count the occurrences of each parameter in each building
for index, row in data.iterrows():
    building = row['Building']
    parameters = row['Parameters'].split(',')
    for parameter in parameters:
        if type(parameter) == str:
            parameter = int(parameter)
        parameter_counts[building][parameter] += 1

# Calculate the percentage of occurrence of each parameter for each building
for building in parameter_counts:
    for parameter, count in parameter_counts[building].items():
        total_parameters = sum(data[data['Building'] == building]['Parameters'].str.split(',').str.len())
        parameter_counts[building][parameter] = (count / total_parameters) * 100

# Print parameter percentages for each building
for building in parameter_counts:
    print(f"Building: {building}")
    for parameter, percentage in parameter_counts[building].items():
        print(f"    Parameter: {parameter}, Percentage: {percentage:.2f}%")