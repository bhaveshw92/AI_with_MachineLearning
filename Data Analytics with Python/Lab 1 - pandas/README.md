### AI with Machine Learning - Data Analytics Lab

**Lab 1: Data Manipulation with Pandas**

**Salaries.csv Dataset**

1. **Read the Dataset:**  
   - Use `pd.read_csv('Salaries.csv')` to load the dataset into a DataFrame named `df_data`.
   
2. **View Data Types:**  
   - Execute `print(df_data.dtypes)` to view the data types of each column.
   
3. **Slice First Two Columns:**  
   - Use `df_data.loc[:, :'EmployeeName']` to slice the first two columns of the dataset.
   
4. **Slice First Two Rows:**  
   - Slice the first two rows using `df_data.loc[:1, :]`.
   
5. **Slice Rows 0, 4, 6 and Columns 'invoice time' and 'price':**  
   - Slice specific rows and columns using `df_data.loc[[0, 4, 6], ['invoice time', 'price']]`.
   
6. **Store Number of Rows:**  
   - Calculate the number of rows and store it in a variable: `num_rows = len(df_data)`.
   
7. **Print Last Row:**  
   - Retrieve and print the last row of the dataset using `df_data.iloc[-1]`.
   
8. **Compute Average and Max TotalPay:**  
   - Calculate the average and maximum values of the 'TotalPay' column: `avg_TotalPay = df_data['TotalPay'].mean()` and `max_TotalPay = df_data['TotalPay'].max()`.
   
9. **Create 'final' Column:**  
   - Create a new column named 'final' by multiplying the 'BasePay' column by 2.
