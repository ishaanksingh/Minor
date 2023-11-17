import tkinter as tk
from tkinter import ttk

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

def validate_radio_selection(radio_group, var):
    if not any(option.get() for option in radio_group):
        error_label = tk.Label(second_tab, text="Please select an option.", fg="red")
        error_label.grid(row=14, column=0, sticky="w")
        root.update_idletasks()
        error_label.after(2000, error_label.destroy)  # Destroy label after 2 seconds

root = tk.Tk()
root.title("Rapid Visual Screening")

# Create StringVars
seismic_zone_var = tk.StringVar()
occupancy_var = tk.StringVar()

# Tab Control
notebook = ttk.Notebook(root)
notebook.pack(fill="both", expand=True)

# Starting Tab
starting_tab = ttk.Frame(notebook)
starting_tab_label = ttk.Label(starting_tab, text="Welcome to the Rapid Visual Screening Model", font=("Arial", 14, "bold"))
starting_tab_label.grid(row=0, column=0, padx=10, pady=10)
continue_button = ttk.Button(starting_tab, text="Continue", command=on_continue_button_click)
continue_button.grid(row=1, column=0, padx=10, pady=10)

# Second Tab
second_tab = ttk.Frame(notebook)
second_tab_heading_label = ttk.Label(second_tab, text="Select the Type of Structure to Perform RVS On", font=("Arial", 14, "bold"))
second_tab_heading_label.grid(row=0, column=0, padx=10, pady=10)

structure_type_label = ttk.Label(second_tab, text="Please select the type of structure for which the RVS is conducted:")
structure_type_label.grid(row=1, column=0, sticky="w", padx=10, pady=5)

structure_type_var = tk.StringVar()
structure_type_concrete = ttk.Radiobutton(
    second_tab, text="Concrete Structure", variable=structure_type_var, value="Concrete Structure"
)
structure_type_rc = ttk.Radiobutton(
    second_tab, text="Rigid Frame Structure (RC)", variable=structure_type_var, value="Rigid Frame Structure (RC)"
)
structure_type_masonry = ttk.Radiobutton(
    second_tab, text="Masonry Structure", variable=structure_type_var, value="Masonry Structure"
)
structure_type_other = ttk.Radiobutton(
    second_tab, text="Other (Please Specify)", variable=structure_type_var, value="Other (Please Specify)"
)

structure_type_concrete.grid(row=2, column=0, sticky="w", padx=10)
structure_type_rc.grid(row=3, column=0, sticky="w", padx=10)
structure_type_masonry.grid(row=4, column=0, sticky="w", padx=10)
structure_type_other.grid(row=5, column=0, sticky="w", padx=10)

other_structure_type_label = ttk.Label(
    second_tab, text="Please specify the structure type if you selected 'Other' above:"
)
other_structure_type_label.grid(row=6, column=0, sticky="w", padx=10, pady=5)
other_structure_type_entry = ttk.Entry(second_tab, width=50)
other_structure_type_entry.grid(row=7, column=0, sticky="w", padx=10, pady=5)

# Add the starting tab to the notebook
notebook.add(starting_tab, text="Welcome")

# Add the second tab to the notebook
notebook.add(second_tab, text="Structure Type")

# Section 1: Siting Issues
def section1_siting_issues():
    section1_label = ttk.Label(second_tab, text="1. Siting Issues")
    section1_label.grid(row=2, column=0, sticky="w", columnspan=3, padx=10, pady=5)

    subpart1_1_label = ttk.Label(second_tab, text="1.1 Building is resting on ground that has failed due to Landslide/Fissures and Liquefaction.")
    subpart1_1_label.grid(row=3, column=0, sticky="w", padx=10, pady=5)

    subpart1_1_var = tk.StringVar()
    subpart1_1_yes = ttk.Radiobutton(
        second_tab,
        text="Yes",
        variable=subpart1_1_var,
        value="Yes",
        command=lambda: validate_radio_selection(
            [subpart1_1_yes, subpart1_1_no], subpart1_1_var
        ),
    )
    subpart1_1_no = ttk.Radiobutton(
        second_tab,
        text="No",
        variable=subpart1_1_var,
        value="No",
        command=lambda: validate_radio_selection(
            [subpart1_1_yes, subpart1_1_no], subpart1_1_var
        ),
    )
    subpart1_1_yes.grid(row=3, column=1)
    subpart1_1_no.grid(row=3, column=2)

section1_siting_issues()

# Run the GUIṇ
root.mainloop()
root = tk.Tk()
root.title("Rapid Visual Screening")

# Starting Tab
starting_tab = tk.Frame(root)
starting_tab_label = tk.Label(starting_tab, text="Welcome to the Rapid Visual Screening Model", font=("Arial", 14, "bold"))
starting_tab_label.pack()
continue_button = tk.Button(starting_tab, text="Continue", command=on_continue_button_click)
continue_button.pack()

# Tab Control
notebook = ttk.Notebook(root)
notebook.pack(fill="both", expand=True)

# Add the starting tab to the notebook
notebook.add(starting_tab, text="Welcome")

# Add the rest of your tabs and code here

# Second Tab
second_tab = tk.Frame(root)
second_tab_label = tk.Label(second_tab, text="This is the second tab", font=("Arial", 14, "bold"))
second_tab_label.pack()

# Add the second tab to the notebook
notebook.add(second_tab, text="Second Tab")

root.mainloop()

root.mainloop()

root = tk.Tk()
root.title("Rapid Visual Screening")

header_label = tk.Label(root, text="Rapid Visual Screening Model Created by Ishank Singh", font=("Arial", 14, "bold"))
header_label.grid(row=0, column=0, columnspan=2)

seismic_zone_label = tk.Label(root, text="1. Select Seismic Zone:")
seismic_zone_label.grid(row=1, column=0, sticky="w")

seismic_zone_var = tk.StringVar()

seismic_zone_options = ["Seismic Zone II", "Seismic Zone III", "Seismic Zone IV", "Seismic Zone V"]
seismic_zone_dropdown = ttk.Combobox(root, textvariable=seismic_zone_var, values=seismic_zone_options)
seismic_zone_dropdown.grid(row=1, column=1)
seismic_zone_dropdown.bind("<<ComboboxSelected>>", on_seismic_zone_select)

occupancy_label = tk.Label(root, text="2. Select Type of Occupancy:")
occupancy_label.grid(row=2, column=0, sticky="w")

occupancy_var = tk.StringVar()

occupancy_options = [
    "Individual House / Apartments",
    "EDUCATIONAL: School / College / Institute/University",
    "LIFELINE: Hospital / Police Station / Fire Station",
    "Power Station / Water Plant / Sewage Plant",
    "COMMERCIAL: Hotel / Shopping / Recreational",
    "OFFICE: Government / Private",
    "MIXED USE: Residential and Commercial / Residential and Industrial",
    "INDUSTRIAL: Agriculture / Live Stock",
    "OTHER: _________________"
]

occupancy_dropdown = ttk.Combobox(root, textvariable=occupancy_var, values=occupancy_options)
occupancy_dropdown.grid(row=2, column=1)
occupancy_dropdown.bind("<<ComboboxSelected>>", on_occupancy_select)

section1_label = tk.Label(root, text="1. Siting Issues")
section1_label.grid(row=3, column=0, sticky="w", columnspan=3)

subpart1_1_label = tk.Label(root, text="1.1 Building is resting on ground that has failed due to Landslide/Fissures and Liquefaction.")
subpart1_1_label.grid(row=4, column=0, sticky="w")
subpart1_1_var = tk.StringVar()
subpart1_1_yes = tk.Radiobutton(root, text="Yes", variable=subpart1_1_var, value="Yes", command=lambda: on_yes_no_select(1, 1, subpart1_1_var.get()))
subpart1_1_no = tk.Radiobutton(root, text="No", variable=subpart1_1_var, value="No", command=lambda: on_yes_no_select(1, 1, subpart1_1_var.get()))
subpart1_1_yes.grid(row=4, column=1)
subpart1_1_no.grid(row=4, column=2)



section2_label = tk.Label(root, text="2. Soil & Foundation Conditions")
section2_label.grid(row=5, column=0, sticky="w", columnspan=3)
subpart2_1_label = tk.Label(root, text="2.1 Building is resting on river terraces that have cracked soil.")
subpart2_1_label.grid(row=5, column=0, sticky="w")
subpart2_1_var = tk.StringVar()
subpart2_1_yes = tk.Radiobutton(root, text="Yes", variable=subpart2_1_var, value="Yes", command=lambda: on_yes_no_select(2, 1, subpart2_1_var.get()))
subpart2_1_no = tk.Radiobutton(root, text="No", variable=subpart2_1_var, value="No", command=lambda: on_yes_no_select(2, 1, subpart2_1_var.get()))
subpart2_1_yes.grid(row=5, column=1)
subpart2_1_no.grid(row=5, column=2)

# Subpart 2.2
subpart2_2_label = tk.Label(root, text="2.2 Building has sustained uneven settlement of the ground.")
subpart2_2_label.grid(row=6, column=0, sticky="w")
subpart2_2_var = tk.StringVar()
subpart2_2_yes = tk.Radiobutton(root, text="Yes", variable=subpart2_2_var, value="Yes", command=lambda: on_yes_no_select(2, 2, subpart2_2_var.get()))
subpart2_2_no = tk.Radiobutton(root, text="No", variable=subpart2_2_var, value="No", command=lambda: on_yes_no_select(2, 2, subpart2_2_var.get()))
subpart2_2_yes.grid(row=6, column=1)
subpart2_2_no.grid(row=6, column=2)



section3_label = tk.Label(root, text="3. Structural Aspects")
section3_label.grid(row=6, column=0, sticky="w", columnspan=3)
# Subpart 2.3
subpart2_3_label = tk.Label(root, text="2.3 Building is resting on liquefied soil.")
subpart2_3_label.grid(row=7, column=0, sticky="w")
subpart2_3_var = tk.StringVar()
subpart2_3_yes = tk.Radiobutton(root, text="Yes", variable=subpart2_3_var, value="Yes", command=lambda: on_yes_no_select(2, 3, subpart2_3_var.get()))
subpart2_3_no = tk.Radiobutton(root, text="No", variable=subpart2_3_var, value="No", command=lambda: on_yes_no_select(2, 3, subpart2_3_var.get()))
subpart2_3_yes.grid(row=7, column=1)
subpart2_3_no.grid(row=7, column=2)

# Subpart 2.4
subpart2_4_label = tk.Label(root, text="2.4 Uneven Settlement of building leading to visual damage.")
subpart2_4_label.grid(row=8, column=0, sticky="w")
subpart2_4_var = tk.StringVar()
subpart2_4_yes = tk.Radiobutton(root, text="Yes", variable=subpart2_4_var, value="Yes", command=lambda: on_yes_no_select(2, 4, subpart2_4_var.get()))
subpart2_4_no = tk.Radiobutton(root, text="No", variable=subpart2_4_var, value="No", command=lambda: on_yes_no_select(2, 4, subpart2_4_var.get()))
subpart2_4_yes.grid(row=8, column=1)
subpart2_4_no.grid(row=8, column=2)

# Subpart 3.1 (Starting section 3)
section3_label = tk.Label(root, text="3. Structural Aspects")
section3_label.grid(row=9, column=0, sticky="w", columnspan=3)

# Subpart 3.1
subpart3_1_label = tk.Label(root, text="3.1 Building has pounding damage from adjoining building or structure.")
subpart3_1_label.grid(row=10, column=0, sticky="w")
subpart3_1_var = tk.StringVar()
subpart3_1_yes = tk.Radiobutton(root, text="Yes", variable=subpart3_1_var, value="Yes", command=lambda: on_yes_no_select(3, 1, subpart3_1_var.get()))
subpart3_1_no = tk.Radiobutton(root, text="No", variable=subpart3_1_var, value="No", command=lambda: on_yes_no_select(3, 1, subpart3_1_var.get()))
subpart3_1_yes.grid(row=10, column=1)
subpart3_1_no.grid(row=10, column=2)
# Subpart 3.2
subpart3_2_label = tk.Label(root, text="3.2 Building has collapsed/damaged staircase/mumty or blockade of staircase.")
subpart3_2_label.grid(row=11, column=0, sticky="w")
subpart3_2_var = tk.StringVar()
subpart3_2_yes = tk.Radiobutton(root, text="Yes", variable=subpart3_2_var, value="Yes", command=lambda: on_yes_no_select(3, 2, subpart3_2_var.get()))
subpart3_2_no = tk.Radiobutton(root, text="No", variable=subpart3_2_var, value="No", command=lambda: on_yes_no_select(3, 2, subpart3_2_var.get()))
subpart3_2_yes.grid(row=11, column=1)
subpart3_2_no.grid(row=11, column=2)

# Subpart 3.3
subpart3_3_label = tk.Label(root, text="3.3 Building has an Open storey (at ground / other level) with columns having shear cracks.")
subpart3_3_label.grid(row=12, column=0, sticky="w")
subpart3_3_var = tk.StringVar()
subpart3_3_yes = tk.Radiobutton(root, text="Yes", variable=subpart3_3_var, value="Yes", command=lambda: on_yes_no_select(3, 3, subpart3_3_var.get()))
subpart3_3_no = tk.Radiobutton(root, text="No", variable=subpart3_3_var, value="No", command=lambda: on_yes_no_select(3, 3, subpart3_3_var.get()))
subpart3_3_yes.grid(row=12, column=1)
subpart3_3_no.grid(row=12, column=2)

# Subpart 3.4
subpart3_4_label = tk.Label(root, text="3.4 Building has Floating Columns with cracked supporting beams.")
subpart3_4_label.grid(row=13, column=0, sticky="w")
subpart3_4_var = tk.StringVar()
subpart3_4_yes = tk.Radiobutton(root, text="Yes", variable=subpart3_4_var, value="Yes", command=lambda: on_yes_no_select(3, 4, subpart3_4_var.get()))
subpart3_4_no = tk.Radiobutton(root, text="No", variable=subpart3_4_var, value="No", command=lambda: on_yes_no_select(3, 4, subpart3_4_var.get()))
subpart3_4_yes.grid(row=13, column=1)
subpart3_4_no.grid(row=13, column=2)

# Subpart 3.5
subpart3_5_label = tk.Label(root, text="3.5 Building has main load-resisting columns with shear cracks.")
subpart3_5_label.grid(row=14, column=0, sticky="w")
subpart3_5_var = tk.StringVar()
subpart3_5_yes = tk.Radiobutton(root, text="Yes", variable=subpart3_5_var, value="Yes", command=lambda: on_yes_no_select(3, 5, subpart3_5_var.get()))
subpart3_5_no = tk.Radiobutton(root, text="No", variable=subpart3_5_var, value="No", command=lambda: on_yes_no_select(3, 5, subpart3_5_var.get()))
subpart3_5_yes.grid(row=14, column=1)
subpart3_5_no.grid(row=14, column=2)
# Subpart 3.6
subpart3_6_label = tk.Label(root, text="3.6 Building has main load-resisting short columns with shear cracks.")
subpart3_6_label.grid(row=15, column=0, sticky="w")
subpart3_6_var = tk.StringVar()
subpart3_6_yes = tk.Radiobutton(root, text="Yes", variable=subpart3_6_var, value="Yes", command=lambda: on_yes_no_select(3, 6, subpart3_6_var.get()))
subpart3_6_no = tk.Radiobutton(root, text="No", variable=subpart3_6_var, value="No", command=lambda: on_yes_no_select(3, 6, subpart3_6_var.get()))
subpart3_6_yes.grid(row=15, column=1)
subpart3_6_no.grid(row=15, column=2)

# Subpart 3.7
subpart3_7_label = tk.Label(root, text="3.7 Building has Flat Slab with punching shear failure.")
subpart3_7_label.grid(row=16, column=0, sticky="w")
subpart3_7_var = tk.StringVar()
subpart3_7_yes = tk.Radiobutton(root, text="Yes", variable=subpart3_7_var, value="Yes", command=lambda: on_yes_no_select(3, 7, subpart3_7_var.get()))
subpart3_7_no = tk.Radiobutton(root, text="No", variable=subpart3_7_var, value="No", command=lambda: on_yes_no_select(3, 7, subpart3_7_var.get()))
subpart3_7_yes.grid(row=16, column=1)
subpart3_7_no.grid(row=16, column=2)

# Subpart 3.8
subpart3_8_label = tk.Label(root, text="3.8 Building has spalling of cover concrete in main load-resisting columns.")
subpart3_8_label.grid(row=17, column=0, sticky="w")
subpart3_8_var = tk.StringVar()
subpart3_8_yes = tk.Radiobutton(root, text="Yes", variable=subpart3_8_var, value="Yes", command=lambda: on_yes_no_select(3, 8, subpart3_8_var.get()))
subpart3_8_no = tk.Radiobutton(root, text="No", variable=subpart3_8_var, value="No", command=lambda: on_yes_no_select(3, 8, subpart3_8_var.get()))
subpart3_8_yes.grid(row=17, column=1)
subpart3_8_no.grid(row=17, column=2)

# Subpart 3.9
subpart3_9_label = tk.Label(root, text="3.9 Building has extensive X cracking or out-of-plane collapse of infills.")
subpart3_9_label.grid(row=18, column=0, sticky="w")
subpart3_9_var = tk.StringVar()
subpart3_9_yes = tk.Radiobutton(root, text="Yes", variable=subpart3_9_var, value="Yes", command=lambda: on_yes_no_select(3, 9, subpart3_9_var.get()))
subpart3_9_no = tk.Radiobutton(root, text="No", variable=subpart3_9_var, value="No", command=lambda: on_yes_no_select(3, 9, subpart3_9_var.get()))
subpart3_9_yes.grid(row=18, column=1)
subpart3_9_no.grid(row=18, column=2)

# Subpart 3.10
subpart3_10_label = tk.Label(root, text="3.10 No seismic separation between staircase and building.")
subpart3_10_label.grid(row=19, column=0, sticky="w")
subpart3_10_var = tk.StringVar()
subpart3_10_yes = tk.Radiobutton(root, text="Yes", variable=subpart3_10_var, value="Yes", command=lambda: on_yes_no_select(3, 10, subpart3_10_var.get()))
subpart3_10_no = tk.Radiobutton(root, text="No", variable=subpart3_10_var, value="No", command=lambda: on_yes_no_select(3, 10, subpart3_10_var.get()))

# Subpart 3.10
subpart3_10_label = tk.Label(root, text="3.10 No seismic separation between staircase and building.")
subpart3_10_label.grid(row=19, column=0, sticky="w")
subpart3_10_var = tk.StringVar()
subpart3_10_yes = tk.Radiobutton(root, text="Yes", variable=subpart3_10_var, value="Yes", command=lambda: on_yes_no_select(3, 10, subpart3_10_var.get()))
subpart3_10_no = tk.Radiobutton(root, text="No", variable=subpart3_10_var, value="No", command=lambda: on_yes_no_select(3, 10, subpart3_10_var.get()))
subpart3_10_yes.grid(row=19, column=1)
subpart3_10_no.grid(row=19, column=2)
structure_joints_label = tk.Label(root, text="4. Structure Joints (Select multiple options if applicable):")
structure_joints_label.grid(row=30, column=0, sticky="w")

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

u_joint_checkbutton.grid(row=31, column=0, sticky="w")
v_joint_checkbutton.grid(row=31, column=1, sticky="w")
h_joint_checkbutton.grid(row=32, column=0, sticky="w")
t_joint_checkbutton.grid(row=32, column=1, sticky="w")

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