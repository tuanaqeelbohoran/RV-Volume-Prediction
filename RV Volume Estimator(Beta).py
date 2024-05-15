import tkinter as tk
import numpy as np
import torch
import os, sys
import datetime
from tab_transformer_pytorch import FTTransformer
import warnings
import ctypes
warnings.filterwarnings("ignore")

# Check if GPU is available
if torch.cuda.is_available():
    device = torch.device("cuda")
    print("PyTorch is running on GPU")
else:
    device = torch.device("cpu")
    print("PyTorch is running on CPU")
    
  

model_best = torch.load("model_best.pth").to(device)
model_best.eval()

def validate_input(P):
    if P.isdigit() or (P.count(".") == 1 and P.replace(".", "").isdigit()) or P == "\b":
        return True
    else:
        return False

    

def show_inputs():

    
    inputs = [var_phase.get(), var_sex.get(), var_age.get(), var_fourC.get(), var_PLAX.get(),
              var_PSAX_AV.get(), var_PSAXbase.get(), var_PSAXdistal.get(), var_PSAXmid.get(),
              var_Rinflow.get(), var_SubC.get()]
    
    inputs = np.array(inputs)  
    print(inputs)
    if inputs[0] == "ED":
        inputs[0] = 0
    if inputs[0] == "ES":
        inputs[0] = 1    
    if inputs[1] == "F":
        inputs[1] = 0
    if inputs[1] == "M":
        inputs[1] = 1 
        
    inputs_new = inputs
    inputs = []
    for i in range(11):
        input_str = inputs_new[i]
        if input_str.strip() == '':
            inputs.append(0)
        else:
            inputs.append(float(input_str))


    inputs = np.array(inputs, dtype=np.float32)  
    
    print(inputs)
    
    x_categ_val = torch.Tensor([[2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]]).long().to(device)
    inputs = torch.Tensor([inputs]).to(device)
    y_pred = model_best(x_categ_val,inputs)
    output = y_pred[0][0].data.detach().cpu().numpy()
    print(output)
    display_label.config(text=str(var_phase.get()) + " Volume " + str(round(output,2)) + "cm\u00b3")


root = tk.Tk()
root.title("RV Volume Estimator")

var_phase = tk.StringVar()
var_sex = tk.StringVar()
var_age = tk.StringVar()
var_fourC = tk.StringVar()
var_PLAX = tk.StringVar()
var_PSAX_AV = tk.StringVar()
var_PSAXbase = tk.StringVar()
var_PSAXdistal = tk.StringVar()
var_PSAXmid = tk.StringVar()
var_Rinflow = tk.StringVar()
var_SubC = tk.StringVar()

phase_label = tk.Label(root, text="Phase")
phase_label.grid(row=0, column=0)

phase_dropdown = tk.OptionMenu(root, var_phase, "ES", "ED")
phase_dropdown.grid(row=0, column=1)

sex_label = tk.Label(root, text="Sex")
sex_label.grid(row=1, column=0)

sex_dropdown = tk.OptionMenu(root, var_sex, "M", "F")
sex_dropdown.grid(row=1, column=1)

age_label = tk.Label(root, text="Age")
age_label.grid(row=2, column=0)

age_entry = tk.Entry(root, textvariable=var_age, validate="key", validatecommand=(root.register(validate_input), "%P"))
age_entry.grid(row=2, column=1)

fourC_label = tk.Label(root, text="FourC")
fourC_label.grid(row=3, column=0)

fourC_entry = tk.Entry(root, textvariable=var_fourC, validate="key", validatecommand=(root.register(validate_input), "%P"))
fourC_entry.grid(row=3, column=1)

PLAX_label = tk.Label(root, text="PLAX")
PLAX_label.grid(row=4, column=0)

PLAX_entry = tk.Entry(root, textvariable=var_PLAX, validate="key", validatecommand=(root.register(validate_input), "%P"))
PLAX_entry.grid(row=4, column=1)

PSAX_AV_label = tk.Label(root, text="PSAX_AV")
PSAX_AV_label.grid(row=5, column=0)

PSAX_AV_entry = tk.Entry(root, textvariable=var_PSAX_AV, validate="key", validatecommand=(root.register(validate_input), "%P"))
PSAX_AV_entry.grid(row=5, column=1)

PSAXbase_label = tk.Label(root, text="PSAXbase")
PSAXbase_label.grid(row=6, column=0)

PSAXbase_entry = tk.Entry(root, textvariable=var_PSAXbase, validate="key", validatecommand=(root.register(validate_input), "%P"))
PSAXbase_entry.grid(row=6, column=1)

PSAXdistal_label = tk.Label(root, text="PSAXdistal")
PSAXdistal_label.grid(row=7, column=0)

PSAXdistal_entry = tk.Entry(root, textvariable=var_PSAXdistal, validate="key", validatecommand=(root.register(validate_input), "%P"))
PSAXdistal_entry.grid(row=7, column=1)

PSAXmid_label = tk.Label(root, text="PSAXmid")
PSAXmid_label.grid(row=8, column=0)

PSAXmid_entry = tk.Entry(root, textvariable=var_PSAXmid, validate="key", validatecommand=(root.register(validate_input), "%P"))
PSAXmid_entry.grid(row=8, column=1)

Rinflow_label = tk.Label(root, text="RVinflow")
Rinflow_label.grid(row=9, column=0)

Rinflow_entry = tk.Entry(root, textvariable=var_Rinflow, validate="key", validatecommand=(root.register(validate_input), "%P"))
Rinflow_entry.grid(row=9, column=1)

SubC_label = tk.Label(root, text="SubC")
SubC_label.grid(row=10, column=0)

SubC_entry = tk.Entry(root, textvariable=var_SubC, validate="key", validatecommand=(root.register(validate_input), "%P", 'reset'))
SubC_entry.grid(row=10, column=1)

submit_button = tk.Button(root, text="Submit", command=show_inputs)
submit_button.grid(row=11, column=0)

display_label = tk.Label(root)
display_label.grid(row=12, column=0, columnspan=2)

name_label = tk.Label(root, text="Creator: Tuan Aqeel Bohoran \n Supervisor: Archontis Giannakidis \n Nottingham Trent University ")
name_label.grid(row=13, column=0, columnspan=2)

# Set the expiration date
expiration_date = datetime.datetime(2023, 3, 14)

# Get the current date and time
current_date = datetime.datetime.now()

# Check if the current date is after the expiration date
if current_date > expiration_date:
    print("Software has expired")
    # Create the message box
    title = "License Expired"
    message = "Your license has expired!"
    style = 0x10 | 0x0  # 0x10 is the icon for the critical message box, 0x0 is the OK button
    ctypes.windll.user32.MessageBoxW(0, message, title, style)
else:
    print("Software is still valid")
    root.mainloop()



