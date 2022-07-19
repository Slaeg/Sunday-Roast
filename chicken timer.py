#ChickenTimer.py
#A calculator for the time it takes to roast a chicken.
#with a simple GUI made with tkinter.

#Importing tkinter
from tkinter import *

#Creating the window
root = Tk()
root.title("Chicken Timer")
root.geometry("500x300")

#Creating the labels
label1 = Label(root, text="Chicken Timer")
label1.grid(row=0, column=0)
label2 = Label(root, text="Enter the number of grams of chicken:")
label2.grid(row=1, column=0)


#Creating the entry boxes
entry1 = Entry(root)
entry1.grid(row=1, column=1)


#Creating the buttons
button1 = Button(root, text="Calculate", command=lambda: calculate(entry1))
button1.grid(row=3, column=0)
button2 = Button(root, text="Exit", command=root.destroy)
button2.grid(row=3, column=1)

#Creating the text box
text1 = Text(root, height=5, width=40)
text1.grid(row=4, column=0)

#Creating the function to calculate the time
#and display the result
def calculate(entry1):
    try:
        #Converting the entry box to an integer
        grams = int(entry1.get())
        
        #Calculating the time
        time = (grams/1000)*45+(20)
        #rounding the time to the nearest whole number
        time = round(time)

        #Displaying the result
        text1.delete(0.0, END)
        text1.insert(0.0,  str(time) + " minutes at 200 degrees centigrade \n (180 fan) or gas mark 6.")   
    except ValueError:
        #Displaying the error message
        text1.delete(0.0, END)
        text1.insert(0.0, "Please enter a numeric value in the entry box.")

#Running the window
root.mainloop()
#end of chicken timer.py
