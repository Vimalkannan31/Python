import tkinter as tk
from tkinter import *
from tkinter import messagebox


def store_details():
    name=input_name.get()
    rollno=input_roll.get()
    dept=input_Department.get()
    gender=user.get()
    address=input_Address.get()
    email=input_Email.get()
    mobile=input_Mobile.get()

    #incase any fields are not filled, warning message will be displayed in the window
    if not name or not rollno or not dept or not gender or not address or not email or not mobile:
        messagebox.showwarning("Missing Error", "Please fill in all fields.")
        return
    
    #all the details are stored in user_details file
    with open("user_details.txt", "a") as file:
        file.write(f"Name: {name}, Roll No: {rollno}, Department: {dept}, Gender: {gender}, Address: {address}, Email: {email},Mobile:{mobile}\n")

    input_name.delete(0, tk.END)
    input_roll.delete(0, tk.END)
    input_Department.delete(0, tk.END)
    input_Address.delete(0, tk.END)
    input_Email.delete(0, tk.END)
    input_Mobile.delete(0, tk.END)
 


root=tk.Tk()
root.geometry("500x400")
root.title("Registration Form")

#label widgets and input fields of the registration form
head_label=tk.Label(root, text="Registration Form", font=("Arial Bold",20))
head_label.grid(row=0,column=1)

label_name = tk.Label(root, text="Name:")
label_name.grid(row=1, column=0,padx=10,pady=10)

input_name=tk.Entry(root,width=50)
input_name.grid(row=1,column=1,padx=10,pady=10)

label_roll = tk.Label(root, text="Roll No:")
label_roll.grid(row=2, column=0,padx=10,pady=10)

input_roll=tk.Entry(root,width=50)
input_roll.grid(row=2,column=1,padx=10,pady=10)

label_Department = tk.Label(root, text="Department:")
label_Department.grid(row=3, column=0,padx=10,pady=10)

input_Department=tk.Entry(root,width=50)
input_Department.grid(row=3,column=1,padx=10,pady=10)


label_gender = tk.Label(root, text="Gender:")
label_gender.grid(row=4, column=0, padx=10, pady=10, sticky="e")

#Radio Buttons
user=tk.StringVar()
user.set("male")
r1=Radiobutton(root,text="male",variable=user, value="male")
r1.place(x=120,y=170)
r2=Radiobutton(root,text="female",variable=user, value="female")
r2.place(x=200,y=170)
r3=Radiobutton(root,text="others",variable=user, value="others")
r3.place(x=280,y=170)

label_Address = tk.Label(root, text="Address:")
label_Address.grid(row=5, column=0,padx=10,pady=10)

input_Address=tk.Entry(root,width=50)
input_Address.grid(row=5,column=1,padx=10,pady=10)

label_Email = tk.Label(root, text="Email ID:")
label_Email.grid(row=6, column=0,padx=10,pady=10)

input_Email=tk.Entry(root,width=50)
input_Email.grid(row=6,column=1,padx=10,pady=10)

label_Mobile = tk.Label(root, text="Mobile No:")
label_Mobile.grid(row=7, column=0,padx=10,pady=10)

input_Mobile=tk.Entry(root,width=50)
input_Mobile.grid(row=7,column=1,padx=10,pady=10)

sumit_btn=tk.Button(root, text="Submit", fg="white",bg="red",command=store_details)#fg(foreground),bg(background)
sumit_btn.grid(row=8, column=0, columnspan=2, pady=20 )

root.mainloop()