import tkinter as tk
from tkinter import ttk
import pandas as pd
import matplotlib.pyplot as plt

# Function to update the graph based on user selections
def update_graph():
    selected_parameter = parameter_var.get()
    selected_month = month_var.get()
    selected_year = year_var.get()
    
    # Filter data based on user selections
    filtered_data = data[
                         (data['Month'] == selected_month) &
                         (data['Year'] == selected_year)]
    
    # Plot the data
    plt.figure(figsize=(10, 6))
    x_values = range(1, len(filtered_data) + 1)
    print(len(filtered_data))
    plt.bar(x_values, filtered_data[selected_parameter].astype(float))
    plt.xlabel('Day')
    plt.ylabel(selected_parameter)
    plt.title(f'{selected_parameter} for {selected_month} {selected_year}')
    plt.xticks(rotation=45)
    plt.show()
    print("Selected Parameter:", selected_parameter)
    print("Selected Month:", selected_month)
    print("Selected Year:", selected_year)
    print("Filtered Data:")
    print(filtered_data)

# Load CSV data
data1 = pd.read_csv('YVR/en_climate_daily_BC_1108395_2017_P1D.csv')  
data2 = pd.read_csv('YHZ/en_climate_daily_NS_8202251_2017_P1D.csv')  
print(data1['Mean Temp (°C)'])
# Concatenate the two datasets
# data = pd.concat([data1, data2], ignore_index=True)
data = data1
# Create tkinter window
root = tk.Tk()
root.title('Weather Comparison')

# Create labels and dropdowns for category, month, and year selection
parameter_label = ttk.Label(root, text='Parameter:')
parameter_label.pack()
parameters = ['Max Temp (°C)', 'Min Temp (°C)', 'Mean Temp (°C)', 'Total Rain (mm)', 'Total Snow (cm)', 'Total Precip (mm)', 'Snow on Grnd (cm)']
parameter_var = ttk.Combobox(root, values=parameters)
parameter_var.pack()

month_label = ttk.Label(root, text='Month:')
month_label.pack()
month_var = ttk.Combobox(root, values=data['Month'].unique())
month_var.pack()

year_label = ttk.Label(root, text='Year:')
year_label.pack()
year_var = ttk.Combobox(root, values=data['Year'].unique())
year_var.pack()

# Create update button
update_button = ttk.Button(root, text='Update Graph', command=update_graph)
update_button.pack()

# Start tkinter main loop
root.mainloop()