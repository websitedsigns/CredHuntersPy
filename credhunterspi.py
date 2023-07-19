import tkinter as tk
from tkinter import messagebox
from tkinter import ttk


def load_data(file_path):
    with open(file_path, 'r') as file:
        data = [line.strip() for line in file]
    return data


def add_coaster():
    coaster = coaster_entry.get()
    manufacturer = manufacturer_combobox.get()
    theme_park = theme_park_combobox.get()
    country = country_combobox.get()

    if coaster and manufacturer and theme_park and country:
        # Check for duplicate entries
        if coaster in coaster_data:
            if messagebox.askyesno("Duplicate Entry", "This coaster already exists. Do you want to update it?"):
                coaster_data[coaster] = {'manufacturer': manufacturer, 'theme_park': theme_park, 'country': country}
        else:
            coaster_data[coaster] = {'manufacturer': manufacturer, 'theme_park': theme_park, 'country': country}

        # Update coaster listbox and running total
        update_coaster_listbox()
        update_running_total()

        # Clear input fields
        coaster_entry.delete(0, tk.END)
        manufacturer_combobox.set('')
        theme_park_combobox.set('')
        country_combobox.set('')

    else:
        messagebox.showerror("Error", "Please fill in all fields.")


def update_coaster_listbox():
    coaster_listbox.delete(0, tk.END)
    for coaster in coaster_data.keys():
        coaster_listbox.insert(tk.END, coaster)


def update_running_total():
    total_count = len(coaster_data)
    coaster_count_label.config(text=f"# {total_count}")


def remove_coaster():
    selected_coaster = coaster_listbox.get(tk.ACTIVE)
    if selected_coaster:
        if messagebox.askyesno("Remove Coaster", "Are you sure you want to remove this coaster?"):
            del coaster_data[selected_coaster]
            update_coaster_listbox()
            update_running_total()
    else:
        messagebox.showerror("Error", "No coaster selected.")


def edit_coaster():
    selected_coaster = coaster_listbox.get(tk.ACTIVE)
    if selected_coaster:
        data = coaster_data[selected_coaster]
        coaster_entry.delete(0, tk.END)
        manufacturer_combobox.set(data['manufacturer'])
        theme_park_combobox.set(data['theme_park'])
        country_combobox.set(data['country'])
        coaster_entry.insert(tk.END, selected_coaster)
        remove_coaster()
    else:
        messagebox.showerror("Error", "No coaster selected.")


def on_manufacturer_key_press(event):
    current_text = manufacturer_combobox.get()
    matching_values = [value for value in manufacturer_values if value.lower().startswith(current_text.lower())]
    manufacturer_combobox['values'] = matching_values


def on_theme_park_key_press(event):
    current_text = theme_park_combobox.get()
    matching_values = [value for value in theme_park_values if value.lower().startswith(current_text.lower())]
    theme_park_combobox['values'] = matching_values


def on_country_key_press(event):
    current_text = country_combobox.get()
    matching_values = [value for value in country_values if value.lower().startswith(current_text.lower())]
    country_combobox['values'] = matching_values


# Specify the file names
manufacturers_file = 'manufacturers.txt'
theme_parks_file = 'themeparks.txt'
countries_file = 'countries.txt'

# Load manufacturers, theme parks, and countries from the files
manufacturer_values = load_data(manufacturers_file)
theme_park_values = load_data(theme_parks_file)
country_values = load_data(countries_file)


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

# Create the coaster count label
coaster_count_label = ttk.Label(main_frame, text="Total Coasters: 0", font=("Arial", 14, "bold"))
coaster_count_label.pack()

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
manufacturer_combobox = ttk.Combobox(input_frame, width=27)
manufacturer_combobox.grid(row=1, column=1, padx=5, pady=5)
manufacturer_combobox['values'] = manufacturer_values
manufacturer_combobox.bind("<KeyRelease>", on_manufacturer_key_press)

theme_park_label = ttk.Label(input_frame, text="Theme Park:")
theme_park_label.grid(row=2, column=0, sticky=tk.E, padx=5, pady=5)
theme_park_combobox = ttk.Combobox(input_frame, width=27)
theme_park_combobox.grid(row=2, column=1, padx=5, pady=5)
theme_park_combobox['values'] = theme_park_values
theme_park_combobox.bind("<KeyRelease>", on_theme_park_key_press)

country_label = ttk.Label(input_frame, text="Country:")
country_label.grid(row=3, column=0, sticky=tk.E, padx=5, pady=5)
country_combobox = ttk.Combobox(input_frame, width=27)
country_combobox.grid(row=3, column=1, padx=5, pady=5)
country_combobox['values'] = country_values
country_combobox.bind("<KeyRelease>", on_country_key_press)

# Create the Add Coaster button
add_button = ttk.Button(main_frame, text="Add Coaster", command=add_coaster)
add_button.pack(pady=10)

# Create the remove and edit buttons
button_frame = ttk.Frame(main_frame)
button_frame.pack(pady=10)

remove_button = ttk.Button(button_frame, text="Remove Coaster", command=remove_coaster)
remove_button.pack(side=tk.LEFT, padx=1)

edit_button = ttk.Button(button_frame, text="Edit Coaster", command=edit_coaster)
edit_button.pack(side=tk.LEFT, padx=1)

# Create the coaster listbox
coaster_data = {}
coaster_listbox = tk.Listbox(main_frame, width=40)
coaster_listbox.pack(pady=10)

# Update initial state
update_coaster_listbox()
update_running_total()

# Run the main loop
root.mainloop()
