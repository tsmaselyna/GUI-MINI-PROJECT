#Assign Variable
x = 0
SumGrade = 0
SumCredit = 0
Count = int(input("Enter Number Of Subject: "))

#While Loop
while x < Count:
    Subject = input("Enter Subject: ")
    Credit = int(input("Enter Credit: "))
    SumCredit = SumCredit + Credit
    Grade = float(input("Enter Grade: "))
    SumGrade = SumGrade + (Grade * Credit)

    #Increment
    x +=1

    #Formula
    Formula = SumGrade  / SumCredit

#Function 
def Cal_Value(Formula):
  "This function calculate CGPA by input user"
  if Formula >= 3.67 and Formula <=4.00: return "Dean List"
  elif Formula >= 2.75 and Formula <=3.66: return "Pass"
  elif Formula >= 2.00 and Formula <=2.74: return "Conditional Pass"
  else : return "Fail"

#Output
print("CGPA is {:0.2f} and Result is {}. Total Credit is {}".format(Formula,Cal_Value(Formula),SumCredit))



#Coding Combine With Python tkinter
import tkinter as tk

# Assign Tkinter
wd = tk.Tk()

# Window Size
wd.geometry("850x250")

# Assign Title
wd.title("MINI PROJECT")
title1=tk.Label(text="CGPA CALCULATOR",bg="#80ff00")
title1.grid(column=2,row=0)

# Function Grade
def Display():

    # Declare Objects For Entering Data 
    D0 = tk.Entry(wd) # Name
    D1 = tk.Entry(wd) # Matric
    D2 = tk.Entry(wd) # Number Of Subject
    D3 = tk.Entry(wd) # Subject
    D4 = tk.Entry(wd) # Credit
    D5 = tk.Entry(wd) # Grade
    D6 = tk.Entry(wd) # Total Credit // Entry Location
    D7 = tk.Entry(wd) # Total CGPA // Entry Location
    D8 = tk.Entry(wd) # Result // Entry Location

    # Assign Variables
    x = 0
    SumGrade = 0
    SumCredit = 0
    Credit = 0
    Grade = 0.00
    while x == D2:
        #Subject = input("Enter Subject: ") *D3
        #Credit = int(input("Enter Credit: ")) *D4
        #SumCredit = SumCredit + D4
        #Grade = float(input("Enter Grade: ")) *D5
        ## SumGrade = SumGrade + (D5 * D4) *Location Entry *D7 ##
        x +=1
        ## Formula = SumGrade  / SumCredit *Location Entry ##
    
    # D2 [NUMBER OF SUBJECT]
    if D2.get() == D2 :
        tk.Label(wd, text = D2).grid(row=5, column=4) 
        D2 = D2
    
    # D4 [CREDIT]
    if D4.get() == D4 : 
        tk.Label(wd, text = SumCredit).grid(row=5, column=4) 
        SumCredit = SumCredit + Credit

    # D5 [GRADE]
    if D5.get() == "A": 
        tk.Label(wd, text =4.00).grid(row=5, column=4) 
        SumGrade += 4.00
    if D5.get() == "A-": 
        tk.Label(wd, text =3.75).grid(row=5, column=4) 
        SumGrade += 3.75
    if D5.get() == "B+": 
        tk.Label(wd, text =3.50).grid(row=5, column=4) 
        SumGrade += 3.50
    if D5.get() == "B": 
        tk.Label(wd, text =3.00).grid(row=5, column=4) 
        SumGrade += 3.00
    if D5.get() == "B-": 
        tk.Label(wd, text =2.75).grid(row=5, column=4) 
        SumGrade += 2.75
    if D5.get() == "C+": 
        tk.Label(wd, text =2.50).grid(row=5, column=4) 
        SumGrade += 250
    if D5.get() == "C": 
        tk.Label(wd, text =2.00).grid(row=5, column=4) 
        SumGrade += 2.00
    if D5.get() == "C-": 
        tk.Label(wd, text =1.75).grid(row=5, column=4) 
        SumGrade += 1.75
    if D5.get() == "D": 
        tk.Label(wd, text =1.50).grid(row=5, column=4) 
        SumGrade += 1.50
    if D5.get() == "E": 
        tk.Label(wd, text =1.00).grid(row=5, column=4) 
        SumGrade += 1.00
    if D5.get() == "F": 
        tk.Label(wd, text =0.00).grid(row=5, column=4) 
        SumGrade += 0.00
    
    # Label [CREDIT]
    tk.Label(wd, text="Credit").grid(row=3, column=0)
    D4 = tk.Entry(wd).grid(row=3, column=1)

    # Label [GRADE]
    tk.Label(wd, text="Grade").grid(row=4, column=0)
    D5 = tk.Entry(wd).grid(row=4, column=1)

    # Label [TOTAL CREDIT]
    tk.Label(wd, text="Total Credit :").grid(row=3, column=3)
    tk.Label(wd, text=SumCredit + Credit).grid(row=3, column=4)
    #D6 = tk.Entry(wd).grid(row=3, column=4)

    # Label [TOTAL CGPA]
    tk.Label(wd, text="Total CGPA :").grid(row=4, column=3)
    tk.Label(wd, text=SumGrade + Grade).grid(row=4, column=4)
    #D7 = tk.Entry(wd).grid(row=4, column=4)

    # Label [RESULT]
    tk.Label(wd, text="Result :").grid(row=5, column=3)
    tk.Label(wd, text=(SumGrade/SumCredit)).grid(row=5, column=4)
    #D8 = tk.Entry(wd).grid(row=5, column=4)

#Function Result
#def Cal_Value():
    #"This function calculate CGPA by input user"
    #if SumGrade/SumCredit >= 3.67 and SumGrade/SumCredit <=4.00: return "Dean List"
    #elif SumGrade/SumCredit >= 2.75 and SumGrade/SumCredit <=3.66: return "Pass"
    #elif SumGrade/SumCredit >= 2.00 and SumGrade/SumCredit <=2.74: return "Conditional Pass"
    #else : return "Fail"

# Label [NAME]
tk.Label(wd, text="Name").grid(row=1, column=0)
D0 = tk.Entry(wd).grid(row=1, column=1)

# Label [MATRIC]
tk.Label(wd, text="Matric").grid(row=1, column=3)
D1 = tk.Entry(wd).grid(row=1, column=4)

# Label [NUMBER OF SUBJECT]
tk.Label(wd, text="Number of Subject").grid(row=2, column=0)
D2 = tk.Entry(wd).grid(row=2, column=1)

# Label [BUTTON]
button=tk.Button(wd, text="submit", bg="#ffbf00", command=Display) 
button.grid(row=9, column=5)

# Label [BUTTON1]
button1=tk.Button(wd, text="Exit", bg="#E74C3C", command=exit) 
button1.grid(row=9, column=7)

# Label [BUTTON2]
#button2=tk.Button(wd, text="Back", bg="#FF00FF", command=) 
#button2.grid(row=9, column=6)

wd.mainloop()


#helmy latest update 3 button with 3windows
from tkinter import*
import tkinter.messagebox
from tkinter import ttk
import random
import time
import datetime

def main():
    root = Tk()
    application=Rental_Inventory(root)
    root.mainloop()

#blank windows 1
class Window1:
    def __init__ (self,master):
        self.master.title("CGPA Calculator")
        self.master.geometry("1350x750+0+0")
        self.master.config(bg="powder blue")
        self.frame = Frame(self.master, bg="powder blue")
        self.frame.pack()

#3 buttons 
        self.btnLogin = Button(self.frame,text ="login", width =17, command =self.new_windows)
        self.btnlogin.grid(row=3,column=0)

        self.btnReset = Button(self.frame,text ="login", width =17, command =self.new_windows)
        self.btnReset.grid(row=3,column=0)

        self.btnExit = Button(self.frame,text ="login", width =17, command =self.new_windows)
        self.btnExit.grid(row=3,column=0)

    def new_window(self):
        self.newWindow = Toplevel(self.master)
        self.app = Window2(self.newWindow)


class Window2:
    def __init__ (self,master):
        self.master.title("CGPA Calculator")
        self.master.geometry("1350x750+0+0")
        self.master.config(bg="cadet blue")
        self.frame = Frame(self.master, bg="powder blue")
        self.frame.pack()

if __name__ == "_main_":
    main()


#latest update 18/9/20 at 2.14 P.M.
#by helmy

from tkinter import*
import tkinter.messagebox
from tkinter import ttk
import random
import time
import datetime

def main ():
    root = Tk()
    #app = window(root)
    #application = Rental_Inventory(root)
    root.mainloop()

    
    
#blank windows 1
class Window1:
    def __init__ (self,master):
        self.master.title("CGPA Calculator")
        self.master.geometry("1350x750+0+0")
        self.master.config(bg="powder blue")
        self.frame = Frame(self.master, bg="powder blue")
        self.frame.pack()

#2 buttons will pop up
# buttons about us and cgpa calculator
        self.btn1 = Button(self.frame,text ="About us", width =17, command =self.new_windows)
        self.btn1.grid(row=3,column=0)

        self.btn2 = Button(self.frame,text ="CGPA Calculator", width =17, command =self.new_windows)
        self.btn2.grid(row=3,column=0)

      
    def new_window(self):
        self.newWindow = Toplevel(self.master)
        self.app = Window2(self.newWindow)

#this windows will be open if the button click
class Window2:
    def __init__ (self,master):
        self.master.title("CGPA Calculator")
        self.master.geometry("1350x750+0+0")
        self.master.config(bg="cadet blue")
        self.frame = Frame(self.master, bg="powder blue")
        self.frame.pack()


#suspect this is might be the error
if __name__ == "__main__":

    main()

