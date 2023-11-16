import tkinter as tk
from tkinter import ttk

# Define the on_yes_no_select function
def on_yes_no_select(section, subpart, value):
    print(f"Section {section}.{subpart} selected: {value}")

def on_seismic_zone_select(event):
    selected_zone = seismic_zone_var.get()
    print(f"Selected Seismic Zone: {selected_zone}")

def on_occupancy_select(event):
    selected_occupancy = occupancy_var.get()
    print(f"Selected Occupancy Type: {selected_occupancy}")

def on_continue_button_click():
    notebook.select(1)

root = tk.Tk()
root.title("Rapid Visual Screening")

# Create StringVars
seismic_zone_var = tk.StringVar()
occupancy_var = tk.StringVar()

seismic_zone_label = tk.Label(root, text="1. Select Seismic Zone:")
seismic_zone_label.grid(row=0, column=0, sticky="w")

seismic_zone_options = ["Seismic Zone II", "Seismic Zone III", "Seismic Zone IV", "Seismic Zone V"]
seismic_zone_dropdown = ttk.Combobox(root, textvariable=seismic_zone_var, values=seismic_zone_options)
seismic_zone_dropdown.grid(row=0, column=1)
seismic_zone_dropdown.bind("<<ComboboxSelected>>", on_seismic_zone_select)

occupancy_label = tk.Label(root, text="2. Select Type of Occupancy:")
occupancy_label.grid(row=1, column=0, sticky="w")

occupancy_options = [
    "Individual House / Apartments",
    "EDUCATIONAL: School / College / Institute/University",
    "LIFELINE: Hospital / Police Station / Fire Station",
    "Power Station / Water Plant / Sewage Plant",
    "COMMERCIAL: Hotel / Shopping / Recreational",
    "OFFICE: Government / Private",
    "MIXED USE: Residential and Commercial / Residential and Industrial",
    "INDUSTRIAL: Agriculture / Live Stock",
    "OTHER: ___"
]

occupancy_dropdown = ttk.Combobox(root, textvariable=occupancy_var, values=occupancy_options)
occupancy_dropdown.grid(row=1, column=1)
occupancy_dropdown.bind("<<ComboboxSelected>>", on_occupancy_select)

def create_section(subpart, label_text):
    subpart_label = tk.Label(root, text=label_text)
    subpart_label.grid(row=subpart, column=0, sticky="w")

    subpart_var = tk.StringVar()
    subpart_yes = tk.Radiobutton(root, text="Yes", variable=subpart_var, value="Yes", command=lambda: on_yes_no_select(1, subpart, subpart_var.get()))
    subpart_no = tk.Radiobutton(root, text="No", variable=subpart_var, value="No", command=lambda: on_yes_no_select(1, subpart, subpart_var.get()))
    subpart_yes.grid(row=subpart, column=1)
    subpart_no.grid(row=subpart, column=2)

# Create Sections and Subparts
create_section(2, "2. Soil & Foundation Conditions")
create_section(3, "3. Structural Aspects")
create_section(4, "4. Structure Joints (Select multiple options if applicable):")

# Create variables to store the selected structure joints
u_joint_var = tk.IntVar()
v_joint_var = tk.IntVar()
h_joint_var = tk.IntVar()
t_joint_var = tk.IntVar()

# Create Checkbuttons for U, V, H, T joints
u_joint_checkbutton = tk.Checkbutton(root, text="U Joint", variable=u_joint_var)
v_joint_checkbutton = tk.Checkbutton(root, text="V Joint", variable=v_joint_var)
h_joint_checkbutton = tk.Checkbutton(root, text="H Joint", variable=h_joint_var)
t_joint_checkbutton = tk.Checkbutton(root, text="T Joint", variable=t_joint_var)

u_joint_checkbutton.grid(row=5, column=0, sticky="w")
v_joint_checkbutton.grid(row=5, column=1, sticky="w")
h_joint_checkbutton.grid(row=6, column=0, sticky="w")
t_joint_checkbutton.grid(row=6, column=1, sticky="w")

# Function to get selected structure joints
def get_structure_joints():
    selected_joints = []
    if u_joint_var.get():
        selected_joints.append("U Joint")
    if v_joint_var.get():
        selected_joints.append("V Joint")
    if h_joint_var.get():
        selected_joints.append("H Joint")
    if t_joint_var.get():
        selected_joints.append("T Joint")

    return selected_joints

root.mainloop()