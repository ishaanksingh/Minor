import tkinter as tk

def submit_form():
    project_location = project_location_entry.get()
    input_data = input_data_entry.get()

    # Process the project location and input data
    print("Project location:", project_location)
    print("Input data:", input_data)

root = tk.Tk()
root.title("RVS Model")

# Create a label for the title
title_label = tk.Label(root, text="Welcome to RVS Model")
title_label.pack()

# Create a label for the project location
project_location_label = tk.Label(root, text="Project Location:")
project_location_label.pack()

# Create an entry box for the project location
project_location_entry = tk.Entry(root)
project_location_entry.pack()


# Create a button to submit the form
submit_button = tk.Button(root, text="Submit", command=submit_form)
submit_button.pack()

root.mainloop()
