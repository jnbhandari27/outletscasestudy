#openpyxl needed to run this code if not present install using pip
import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt

#To select the columns needed and ignore the columns with questions in the original excel file
data = pd.read_excel("Frequency of Purchase Analysis Data Question.xlsx", engine = "openpyxl")
columns = list(data.columns.values)
columns = columns[0:4]

#New dataframe with relevant columns
df = data[columns]

outlets_count = df['Outlet ID'].value_counts()
count_results = {}
total_sales_value = {}
sales_value_per_outlet = {}
for i in range(1,10): 
    count = outlets_count.where(outlets_count==i).dropna()
    count_results[i]= count.size
    outlet_ids = count.index.tolist()
    count_df = df[df['Outlet ID'].isin(outlet_ids)]
    total_sales_value[i] = round(count_df["Sales Value"].sum(),2)    
    sales_value_per_outlet[i] = total_sales_value[i]/count_results[i]

print("Count of outlet ids with their respective values of frequency counts are as follows:\n",count_results)

print("The total sales values of frequency counts are as follows:\n",total_sales_value) 

print("Average Sales Value per Outlet:", sales_value_per_outlet)

x = range(1,10)
y = list(sales_value_per_outlet.values())
plt.plot(x, y)  
plt.xlabel('Frequency of Outlet ID')
plt.ylabel('Average Sales Value per Outlet')
plt.grid()
plt.show()