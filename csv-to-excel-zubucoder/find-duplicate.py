# import pandas as pd

# # Load the Excel file
# file_path = 'customers.xlsx'
# df = pd.read_excel(file_path)

# # Identify duplicated phone numbers
# duplicated_phones = df[df.duplicated(subset=['Phone'], keep=False)]

# # Extract the relevant information
# output_df = duplicated_phones[['BP ID','BP Name', 'Customer Name', 'Phone','Interested To Buy','Date','Time']]

# # Save to a new CSV file
# output_csv_path = 'duplicated.csv'
# output_df.to_csv(output_csv_path, index=False)

# print(f"Output saved to {output_csv_path}")




# ========================== only interested yes =========================
import pandas as pd

# Load the Excel file
file_path = 'filtered_customers.xlsx'
df = pd.read_excel(file_path)

# Identify duplicated phone numbers
duplicated_phones = df[df.duplicated(subset=['Phone'], keep=False)]

# Further filter the rows where 'Interested To Buy' is 'yes'
<<<<<<< HEAD
# filtered_duplicated_phones = duplicated_phones[(duplicated_phones['Interested To Buy'].str.lower() == 'no') | (duplicated_phones['Interested To Buy'].str.lower() == 'yes')]
filtered_duplicated_phones = duplicated_phones[(duplicated_phones['Interested To Buy'].str.lower() == 'yes')]
=======
filtered_duplicated_phones = duplicated_phones[(duplicated_phones['Interested To Buy'].str.lower() == 'no')]
# filtered_duplicated_phones = duplicated_phones[(duplicated_phones['Interested To Buy'].str.lower() == 'yes') | (duplicated_phones['Interested To Buy'].str.lower() == 'no')]
>>>>>>> ed25b0f (new convertion code update)

# Extract the relevant information
output_df = filtered_duplicated_phones[['BP ID', 'BP Name', 'Customer Name', 'Phone', 'Interested To Buy', 'Date', 'Time']]

# Save to a new CSV file
output_csv_path = 'duplicated.csv'
output_df.to_csv(output_csv_path, index=False)

print(f"Output saved to {output_csv_path}")
