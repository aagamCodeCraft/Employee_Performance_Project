import pandas as pd

# Load the dataset
file_path = 'E:\\employees record\\data\\XYZ_Employees.xlsx'
data = pd.read_excel(file_path)

# Preview first 5 rows
print("Dataset Preview:")
print(data.head())

# Basic info
print("\nDataset Info:")
print(data.info())

# Summary statistics
print("\nSummary Statistics:")
print(data.describe())


# Calculate Performance Score (weights are customizable)
data['Performance_Score'] = (data['Attendance (%)'] * 0.3 +
                             data['Projects_Completed'] * 0.3 +
                             data['Customer_Feedback_Score'] * 10 * 0.2 +  # Scaled for balance
                             data['Work_Hours'] * 0.2)

# Display Employee Performance Scores
print("\nEmployee Performance Scores:")
print(data[['Employee_ID', 'Name', 'Performance_Score']])


# Define the full path where the processed file will be saved
output_file_path = 'E:/employees record/processed_employee_data.xlsx'

# Save processed data
data.to_excel(output_file_path, index=False)
print(f"\nProcessed data saved as '{output_file_path}'")

