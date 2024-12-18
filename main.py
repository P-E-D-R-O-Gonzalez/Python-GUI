###########################
##                       ##
#       FRONT - END       #
#      Pedro Gonzalez     #
##                       ##
###########################

# Imports #
import tkinter
from tkinter import PhotoImage, Toplevel, ttk
from tkinter import messagebox
from tkcalendar import DateEntry
import mysql.connector as mysql

# Variables #
yy = 2024
mm = 12
dd = 4
conn = mysql.connect(host="localhost",user="root", password="Claveprivada25",database="cse5720")
prices = {"Training":1000,"Website":500,"Detail":100,"Graphic Design":50}

# GUI defined here to avoid errors#
gui = tkinter.Tk()
gui.geometry("750x480")
gui.title("CSE5720: Final Project: POS management system")
icon_image = PhotoImage(file = "PG.png")
gui.iconphoto(False,icon_image)

# Functions #
def payment_popup():
    top = Toplevel(gui)
    top.geometry("500x500")
    top.title("Payment")
    price = tkinter.Label(top,text="Total: ", font="san-serif 15")
    price.place(x=50,y=50)
    priceDisplay = tkinter.Label(top,text=prices[services.get()],font="san-serif 15")
    priceDisplay.place(x=150,y=50)
    # calc deposit 
    due = tkinter.Label(top,text="Due Now: ",font="san-serif 15")
    due.place(x=50,y=100)
    dueNow = tkinter.Label(top,text= prices[services.get()]/4, font="san-serif 15")
    dueNow.place(x=150,y=100)
    cardPrompt = tkinter.Label(top,text="Payment recieved \n reciept been sent out to your email",font="san-serif 15")
    cardPrompt.place(x=50,y=150)  
  

def insertUser():
    # error checking
    if name_entry.get() == "" or email_entry.get().find('@') == -1 or services.get() == "" or depositTypes.get() == "" or street_entry.get() == "" or city_entry.get == "":
        messagebox.showinfo("Alert","Enter all info")
    else:
        cursor = conn.cursor()
        cursor.execute(add_user,(name_entry.get(), email_entry.get()))
        u_id = cursor.lastrowid
        cursor.execute(add_service,(services.get(), prices[services.get()],date_entry.get(),u_id))
        cursor.execute(add_address, (street_entry.get(), city_entry.get(), state_entry.get()))
        a_id = cursor.lastrowid
        cursor.execute(add_deposit, (depositTypes.get(), prices[services.get()] / 4,u_id,a_id))
        conn.commit()
        messagebox.showinfo("Alert","Succesfully Inserted")
        payment_popup()
        
        conn.close()
            
def deleteUser():
    # error checking
    if name_entry.get() == "":
        messagebox.showinfo("Alert","Enter name")
    else:
        cursor = conn.cursor()
        cursor.execute(delete_user, (name_entry.get(),))
        cursor.execute("commit")
        messagebox.showinfo("Alert","Succesfully Deleted")
        price = tkinter.Label(gui,text="Total: ", font="san-serif 15").place(x=50,y=400)
        priceDisplay = tkinter.Label(gui,text="0",font="san-serif 15").place(x=150,y=400)
        due = tkinter.Label(gui,text="Due Now: ",font="san-serif 15").place(x=50,y=440)
        dueNow = tkinter.Label(gui,text="0", font="san-serif 15").place(x=150,y=440)
        conn.close()

def updateUser():
    # error checking
    if name_entry.get() == "" or email_entry.get().find('@') == -1 or services.get() == "" or depositTypes.get() == "" or street_entry.get() == "" or city_entry.get == "":
        messagebox.showinfo("Alert","Enter all info")
    else:
        cursor = conn.cursor()
        cursor.execute(update_user,(email_entry.get(), name_entry.get()))
        conn.commit()
        messagebox.showinfo("Alert","Succesfully Updated")
        payment_popup()
        conn.close()

def selectUser():
    # error checking
    if name_entry.get() == "":
        messagebox.showinfo("Alert","Enter name")
    else:
        cursor = conn.cursor()
        cursor.execute(get_user,(name_entry.get(),))
        conn.commit()
        messagebox.showinfo("Alert","Succesfully Selected")
        info = tkinter.Label(gui,text = "To be implemented based on backend", font="san-serif 15")
        info.place(x=400,y=25)
        
        conn.close()

# Queries #
add_user = """
INSERT INTO User (name, email) VALUES (%s, %s)
"""
add_service = """
INSERT INTO Service (name, price, s_date, u_id)
VALUES (%s, %s, %s, %s)
"""
add_address = """
INSERT INTO Address (street, city, state)
VALUES (%s, %s, %s)
"""
add_deposit = """
INSERT INTO Deposit (method, amount, u_id, a_id)
VALUES (%s, %s, %s, %s)
"""
delete_user = """
DELETE FROM User WHERE name = %s;
"""
update_user = """
UPDATE User SET email = %s WHERE name = %s;
"""
get_user = """
SELECT * FROM User WHERE name = %s;
"""

# GUI layout and design #

name = tkinter.Label(gui,text="Name: ", font=("sans-serif 15"))
name.place(x=50, y=30)
name_entry = tkinter.Entry(gui,font=("sans-serif 15"))
name_entry.place(x=150,y=30)

email = tkinter.Label(gui,text="Email: ", font=("sans-serif 15"))
email.place(x=50, y=80)
email_entry = tkinter.Entry(gui,font=("sans-serif 15"))
email_entry.place(x=150,y=80)

service = tkinter.Label(gui,text="Service: ", font=("sans-serif 15"))
service.place(x=50, y=120)
services = ttk.Combobox(state="readonly" , values=["Training","Website","Detail","Graphic Design"])
services.place(x=150,y=120)

# calendar #
date = tkinter.Label(gui, text="Date: ", font="san-serif 15")
date.place(x=50,y=150)
date_entry = DateEntry(gui,selectmode='day',year=yy,month=mm, day=dd)
date_entry.grid(row=5,column=4,padx=150,pady=150)

deposit = tkinter.Label(gui,text="Deposit: ", font=("sans-serif 15"))
deposit.place(x=50, y=180)
depositTypes = ttk.Combobox(state="readonly" , values=["Credit / Debit","Digital Wallet"])
depositTypes.place(x=150,y=180)

street = tkinter.Label(gui,text="Street: ", font=("sans-serif 15"))
street.place(x=50, y=220)
street_entry = tkinter.Entry(gui,font=("sans-serif 15"))
street_entry.place(x=150,y=220)

city = tkinter.Label(gui,text="City: ", font=("sans-serif 15"))
city.place(x=50, y=260)
city_entry = tkinter.Entry(gui,font=("sans-serif 15"))
city_entry.place(x=150,y=260)

state = tkinter.Label(gui,text="State: ", font=("sans-serif 15"))
state.place(x=50, y=300)
state_entry = ttk.Combobox(state="readonly" , values=["AK", "AL", "AR", "AZ", "CA", "CO", "CT","DC", "DE", "FL", "GA", "HI", "IA",
    "ID", "IL", "IN", "KS", "KY", "LA", "MA", "MD", "ME", "MI", "MN", "MO",
    "MS", "MT", "NC", "ND", "NE", "NH", "NJ", "NM", "NV", "NY", "OH", "OK",
    "OR", "PA", "RI", "SC", "SD", "TN", "TX", "UT", "VA", "VT", "WA", "WI",
    "WV", "WY"])
# https://en.wikipedia.org/wiki/List_of_states_and_territories_of_the_United_States#Federal_district.
state_entry.place(x=150,y=300)

# Buttons #
# submit button #

submit = tkinter.Button(gui, text="submit", command=insertUser)
submit.place(x=350,y=350)

# delete button #

delete = tkinter.Button(gui, text="delete", command=deleteUser)
delete.place(x=352,y=380)

# update button #

update = tkinter.Button(gui, text="update", command=updateUser)
update.place(x=300,y=380)

# select button #

select = tkinter.Button(gui, text="select", command=selectUser)
select.place(x=400,y=380)

gui.mainloop()