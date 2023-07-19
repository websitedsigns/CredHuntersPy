import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

# Function to handle adding a coaster
def add_coaster():
    coaster = coaster_entry.get()
    manufacturer = manufacturer_entry.get()
    theme_park = theme_park_entry.get()
    country = country_entry.get()

    if coaster and manufacturer and theme_park and country:
        # Check for duplicate entries
        if coaster in coaster_data:
            if messagebox.askyesno("Duplicate Entry", "This coaster already exists. Do you want to add it again?"):
                coaster_data[coaster] = {'manufacturer': manufacturer, 'theme_park': theme_park, 'country': country}
        else:
            coaster_data[coaster] = {'manufacturer': manufacturer, 'theme_park': theme_park, 'country': country}

        # Update coaster listbox and running total
        update_coaster_listbox()
        update_running_total()

        # Clear input fields
        coaster_entry.delete(0, tk.END)
        manufacturer_entry.delete(0, tk.END)
        theme_park_entry.delete(0, tk.END)
        country_entry.delete(0, tk.END)

    else:
        messagebox.showerror("Error", "Please fill in all fields.")

# Function to update the coaster listbox
def update_coaster_listbox():
    coaster_listbox.delete(0, tk.END)
    for coaster in coaster_data.keys():
        coaster_listbox.insert(tk.END, coaster)

# Function to update the running total
def update_running_total():
    total_count = len(coaster_data)
    total_label.config(text=f"Total Coasters: {total_count}")

# Function to filter coasters based on park, country, or manufacturer
def filter_coasters():
    selected_filter = filter_combobox.get()
    search_query = search_entry.get().lower()

    # Clear the listbox
    coaster_listbox.delete(0, tk.END)

    # Filter and display the matching coasters
    for coaster, data in coaster_data.items():
        if selected_filter == "Park" and data['theme_park'].lower() == search_query:
            coaster_listbox.insert(tk.END, coaster)
        elif selected_filter == "Country" and data['country'].lower() == search_query:
            coaster_listbox.insert(tk.END, coaster)
        elif selected_filter == "Manufacturer" and data['manufacturer'].lower() == search_query:
            coaster_listbox.insert(tk.END, coaster)

# Create the main window
root = tk.Tk()
root.title("CredHunters")
root.geometry("800x600")
root.resizable(False, False)

# Create a style for the GUI elements
style = ttk.Style()
style.theme_use("clam")

# Configure style options
style.configure("TLabel", foreground="black", background="#F0F0F0", font=("Arial", 12))
style.configure("TEntry", fieldbackground="#FDFDFD", font=("Arial", 12))
style.configure("TButton", background="#4E96B0", foreground="white", font=("Arial", 12))
style.configure("TCombobox", font=("Arial", 12))

# Create the title label
title_label = ttk.Label(root, text="Cred Hunters", font=("Arial", 18, "bold"))
title_label.pack(pady=20)

# Create the main frame
main_frame = ttk.Frame(root, padding=20)
main_frame.pack(fill=tk.BOTH, expand=True)

# Create the input frame
input_frame = ttk.Frame(main_frame)
input_frame.pack(pady=20)

# Create the coaster input fields
coaster_label = ttk.Label(input_frame, text="Coaster:")
coaster_label.grid(row=0, column=0, sticky=tk.E, padx=5, pady=5)
coaster_entry = ttk.Entry(input_frame, width=30)
coaster_entry.grid(row=0, column=1, padx=5, pady=5)

manufacturer_label = ttk.Label(input_frame, text="Manufacturer:")
manufacturer_label.grid(row=1, column=0, sticky=tk.E, padx=5, pady=5)
manufacturer_entry = ttk.Entry(input_frame, width=30)
manufacturer_entry.grid(row=1, column=1, padx=5, pady=5)

theme_park_label = ttk.Label(input_frame, text="Theme Park:")
theme_park_label.grid(row=2, column=0, sticky=tk.E, padx=5, pady=5)
theme_park_entry = ttk.Entry(input_frame, width=30)
theme_park_entry.grid(row=2, column=1, padx=5, pady=5)

country_label = ttk.Label(input_frame, text="Country:")
country_label.grid(row=3, column=0, sticky=tk.E, padx=5, pady=5)
country_entry = ttk.Entry(input_frame, width=30)
country_entry.grid(row=3, column=1, padx=5, pady=5)
country_entry.bind("<Return>", lambda event: add_coaster())

# Create the Add Coaster button
add_button = ttk.Button(main_frame, text="Add Coaster", command=add_coaster)
add_button.pack(pady=10)

# Create the filter frame
filter_frame = ttk.Frame(main_frame)
filter_frame.pack(pady=20)

# Create the filter combobox
filter_combobox = ttk.Combobox(filter_frame, values=["Park", "Country", "Manufacturer"], state="readonly")
filter_combobox.current(0)
filter_combobox.pack(side=tk.LEFT, padx=5)
filter_combobox.configure(style="TCombobox")

# Create the search entry
search_entry = ttk.Entry(filter_frame, width=20)
search_entry.pack(side=tk.LEFT, padx=5)
search_entry.configure(style="TEntry")
search_entry.bind("<Return>", lambda event: filter_coasters())

# Create the search button
search_button = ttk.Button(filter_frame, text="Search", command=filter_coasters)
search_button.pack(side=tk.LEFT)
search_button.configure(style="TButton")

# Create the coaster listbox
coaster_data = {}
coaster_listbox = tk.Listbox(main_frame, width=40)
coaster_listbox.pack(pady=10)

# Create the running total label
total_label = ttk.Label(main_frame, text="Total Coasters: 0", font=("Arial", 14, "bold"))
total_label.pack()

