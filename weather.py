import tkinter as tk
from tkinter import ttk
import pandas as pd
import matplotlib.pyplot as plt
from enum import Enum
import os


# Function to update the graph based on user selections
def update_graph():
    selected_parameter = parameter_var.get()
    selected_month = month_var.get()
    selected_year = year_var.get()
    selected_year = int(selected_year)
    try:
        month_enum = Month[selected_month]
        month_code = month_enum.value
        month_code = int(month_code)
    except KeyError:
        print("Invalid Key")

    # Filter data based on user selections
    filtered_data1 = data1[
        (data1["Month"] == month_code) & (data1["Year"] == selected_year)
    ]
    filtered_data2 = data2[
        (data2["Month"] == month_code) & (data2["Year"] == selected_year)
    ]
    # Plot the data
    plt.figure(figsize=(10, 6))
    x_values = range(1, len(filtered_data1) + 1)
    plt.plot(
        x_values,
        filtered_data1[selected_parameter].astype(float),
        label=subfolder1_name,
        color="blue",
        marker="o",
    )
    plt.plot(
        x_values,
        filtered_data2[selected_parameter].astype(float),
        label=subfolder2_name,
        color="red",
        marker="o",
    )
    plt.xlabel("Day")
    plt.ylabel(selected_parameter)
    plt.title(f"{selected_parameter} for {selected_month} {selected_year}")
    plt.xticks(rotation=45)
    plt.legend()
    plt.show()


# Load CSV data
subfolder1_name = "YVR"
subfolder1_path = os.path.join(".", subfolder1_name)
data1_files = [file for file in os.listdir(subfolder1_path) if file.endswith(".csv")]
data1 = pd.DataFrame()

subfolder2_name = "YHZ"
subfolder2_path = os.path.join(".", subfolder2_name)
data2_files = [file for file in os.listdir(subfolder2_path) if file.endswith(".csv")]
data2 = pd.DataFrame()

# Load and concatenate data from all CSV files into a two DataFrames
print("Importing .csv files from", subfolder1_name)
for file1 in data1_files:
    file1_path = os.path.join(subfolder1_path, file1)
    file_data1 = pd.read_csv(file1_path)
    data1 = pd.concat([data1, file_data1], ignore_index=True)
print("Importing .csv files from", subfolder2_name)
for file2 in data2_files:
    file2_path = os.path.join(subfolder2_path, file2)
    file_data2 = pd.read_csv(file2_path)
    data2 = pd.concat([data2, file_data2], ignore_index=True)


# Create tkinter window
root = tk.Tk()
root.title("Weather Comparison")

# Create labels and dropdowns for category, month, and year selection
parameter_label = ttk.Label(root, text="Parameter:")
parameter_label.pack()
parameters = [
    "Max Temp (°C)",
    "Min Temp (°C)",
    "Mean Temp (°C)",
    "Total Rain (mm)",
    "Total Snow (cm)",
    "Total Precip (mm)",
    "Snow on Grnd (cm)",
]
parameter_var = ttk.Combobox(root, values=parameters)
parameter_var.pack()

month_label = ttk.Label(root, text="Month:")
month_label.pack()
months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December",
]
month_var = ttk.Combobox(root, values=months)  # values=data["Month"].unique())
month_var.pack()


class Month(Enum):
    January = "01"
    February = "02"
    March = "03"
    April = "04"
    May = "05"
    June = "06"
    July = "07"
    August = "08"
    September = "09"
    October = "10"
    November = "11"
    December = "12"


year_label = ttk.Label(root, text="Year:")
year_label.pack()
years = ["2017", "2018", "2019", "2020", "2021", "2022", "2023"]
year_var = ttk.Combobox(root, values=years)  # values=data["Year"].unique())
year_var.pack()

# Create update button
update_button = ttk.Button(root, text="Update Graph", command=update_graph)
update_button.pack()

# Start tkinter main loop
root.mainloop()
