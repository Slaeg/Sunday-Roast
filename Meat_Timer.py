from tkinter import *
from tkinter import ttk  # needed for Combobox

root = Tk()
root.title("Roasting Timer")
root.geometry("500x300")

# UI Improvements
root.configure(bg='light grey') # Changes the background color

# Center the grid
root.grid_columnconfigure(0, weight=1)
root.grid_rowconfigure(0, weight=1) 

# Label modification
label1 = Label(root, text="Roasting Timer", bg='light grey', font=("Helvetica", 16))
label1.grid(row=0, column=0, pady=10) # Add padding for the label

label2 = Label(root, text="Enter the weight in grams:", bg='light grey')
label2.grid(row=2, column=0, pady=10)

# Add a dropdown menu to select the type of meat
label3 = Label(root, text="Select the type of meat:", bg='light grey')
label3.grid(row=1, column=0, pady=10)

meat_var = StringVar()
meat_dropdown = ttk.Combobox(root, textvariable=meat_var)
meat_dropdown['values'] = ('Chicken', 'Beef', 'Pork')
meat_dropdown.grid(row=1, column=1)
meat_dropdown.current(0)  # sets the default value

# Entry for weight input
entry1 = Entry(root)
entry1.grid(row=2, column=1, pady=10)

# Creating the text box
text1 = Text(root, height=5, width=40, wrap=WORD)
text1.grid(row=4, column=0, columnspan=2, pady=10)

# Modify the error handling and calculation for different meats
def calculate():
    try:
        grams = int(entry1.get())

        if grams <= 0:
            raise ValueError("Please enter a value greater than 0.")
        
        # Determine which calculation and temperature to use
        if meat_var.get() == 'Chicken':
            time = (grams/1000)*45+20
            temperature = "200 degrees centigrade (180 fan) or gas mark 6."
        elif meat_var.get() == 'Beef':
            time = (grams/1000)*60+30
            temperature = "180 degrees centigrade (160 fan) or gas mark 4."  # Modify as needed
        elif meat_var.get() == 'Pork':
            time = (grams/1000)*70+35
            temperature = "190 degrees centigrade (170 fan) or gas mark 5."  # Modify as needed
        else:
            raise ValueError("Please select a type of meat.")
        
        time = round(time)
        text1.delete(0.0, END)
        text1.insert(0.0, str(time) + " minutes at " + temperature)  
    except ValueError as e:
        text1.delete(0.0, END)
        text1.insert(0.0, "Please enter a numeric value in the weight box.")

# Create the buttons
button1 = Button(root, text="Calculate", command=calculate)
button1.grid(row=3, column=0, pady=10)

button2 = Button(root, text="Exit", command=root.destroy)
button2.grid(row=3, column=1, pady=10)

root.mainloop()
