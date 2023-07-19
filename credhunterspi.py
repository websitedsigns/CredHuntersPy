import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from ttkthemes import ThemedStyle

def add_coaster(*args):
    coaster = coaster_entry.get()
    manufacturer = manufacturer_entry.get()
    theme_park = theme_park_entry.get()
    country = country_entry.get()

    if coaster and manufacturer and theme_park and country:
        # Check for duplicate entries
        if coaster in coaster_count:
            if messagebox.askyesno("Duplicate Entry", "This coaster already exists. Do you want to add it again?"):
                coaster_count[coaster] += 1
        else:
            coaster_count[coaster] = 1

        # Update coaster listbox and running total
        update_coaster_listbox()
        update_running_total()

        # Clear input fields
        coaster_entry.delete(0, tk.END)
        manufacturer_entry.delete(0, tk.END)
        theme_park_entry.delete(0, tk.END)
        country_entry.delete(0, tk.END)

def update_coaster_listbox():
    coaster_listbox.delete(0, tk.END)
    for item, count in coaster_count.items():
        coaster_listbox.insert(tk.END, item)

def update_running_total():
    total_count = sum(coaster_count.values())
    total_label.config(text=f"Total Coasters: {total_count}")

root = tk.Tk()
root.geometry("800x600")
root.title("CredHunters")

style = ThemedStyle(root)
style.set_theme("plastik")

# Title label
title_label = ttk.Label(root, text="CredHunters", font=("Arial", 24, "bold"), foreground="white", background="darkblue")
title_label.pack(pady=20)

# Coaster input frame
input_frame = tk.Frame(root, padx=10, pady=10)
input_frame.pack()

# Coaster input fields
coaster_label = ttk.Label(input_frame, text="Coaster:")
coaster_label.grid(row=0, column=0, sticky=tk.W)
coaster_entry = ttk.Entry(input_frame, width=30)
coaster_entry.grid(row=0, column=1, padx=5)

manufacturer_label = ttk.Label(input_frame, text="Manufacturer:")
manufacturer_label.grid(row=1, column=0, sticky=tk.W)
manufacturer_entry = ttk.Entry(input_frame, width=30)
manufacturer_entry.grid(row=1, column=1, padx=5)

theme_park_label = ttk.Label(input_frame, text="Theme Park:")
theme_park_label.grid(row=2, column=0, sticky=tk.W)
theme_park_entry = ttk.Entry(input_frame, width=30)
theme_park_entry.grid(row=2, column=1, padx=5)

country_label = ttk.Label(input_frame, text="Country:")
country_label.grid(row=3, column=0, sticky=tk.W)
country_entry = ttk.Entry(input_frame, width=30)
country_entry.grid(row=3, column=1, padx=5)
country_entry.bind("<Return>", add_coaster)

# Button frame
button_frame = tk.Frame(root, pady=10)
button_frame.pack()

# Add Coaster button
add_button = ttk.Button(button_frame, text="Add Coaster", command=add_coaster)
add_button.pack(side=tk.LEFT, padx=5)

# Remove Coaster button
remove_button = ttk.Button(button_frame, text="Remove Coaster", command=remove_coaster)
remove_button.pack(side=tk.LEFT, padx=5)

# Analyze Data button
analyze_button = ttk.Button(button_frame, text="Analyze Data", command=analyze_data)
analyze_button.pack(side=tk.LEFT, padx=5)

# Generate Statistics button
statistics_button = ttk.Button(button_frame, text="Generate Statistics", command=generate_statistics)
statistics_button.pack(side=tk.LEFT, padx=5)

# Coaster listbox
coaster_count = {}
coaster_listbox = tk.Listbox(root, width=40)
coaster_listbox.pack(pady=10)

# Running total label
total_label = ttk.Label(root, text="Total Coasters: 0")
total_label.pack()

root.mainloop()
