import pandas

# you’ll need to capture the full path where the Excel file is stored on your computer,
# Don’t forget include the file name
# include the Excel file extension
# #place "r" before the path string to address special character, such as '\'
excel_data_df = pandas.read_excel(r'C:\Users\eshet\OneDrive\Desktop\Database export file\ecommerce5.xlsx', sheet_name='sheet1')
a = excel_data_df.keys()

# print sheet data from the excel
print(excel_data_df)

print("-"*100)
# if you want to select a specific column or columns from the Excel file
data = pandas.read_excel(r'C:\Users\eshet\OneDrive\Desktop\Database export file\ecommerce5.xlsx', sheet_name='sheet1')
excel_data_df = pandas.DataFrame(data, columns= ['CustomerID', 'CustomerName'])
print(excel_data_df)