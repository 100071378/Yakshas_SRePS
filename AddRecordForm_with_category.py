from Tkinter import *
import datetime
import sqlite3



root = Tk()
root.geometry('500x500')
root.title("SRePS")

def add():
    record1=RecordID.get()
    product1=ProdID.get()
    quantity1=Quantity.get()
    userid1=UserID.get()
    date=getdate()
    connection=sqlite3.connect('form.db')
    with connection:
        cursor=connection.cursor()
        cursor.execute('INSERT INTO Recorddesc (RecordID,ProdID,Quantity,UserID,Date) VALUES(?,?,?,?)',(record1,product1,quantity1,userid1))
        connection.commit()




# exit function
def exit():
    tkinter.messagebox.showinfo("Exit", "Are you sure you want to exit?")
    exit()

# function for setting date
def getdate():
    date1 = input(datetime.date)
    return date1


label_0 = Label(root, text="Sales Records",width=20,font=("bold", 20))
label_0.place(x=90,y=53)


label_1 = Label(root, text="Product ID",width=20,font=("bold", 10))
label_1.place(x=80,y=130)

entry_1 = Entry(root)
entry_1.place(x=240,y=130)

label_2 = Label(root, text="Name",width=20,font=("bold", 10))
label_2.place(x=68,y=170)

entry_2 = Entry(root)
entry_2.place(x=240,y=170)

label_3 = Label(root, text="Quantity",width=20,font=("bold", 10))
label_3.place(x=68,y=210)

entry_3 = Entry(root)
entry_3.place(x=240,y=210)

label_3 = Label(root, text="Price per Item",width=20,font=("bold", 10))
label_3.place(x=68,y=240)

entry_3 = Entry(root)
entry_3.place(x=240,y=240)




label_4 = Label(root, text="Product Category",width=20,font=("bold", 10))
label_4.place(x=70,y=280)

list1 = ['Baby','Cold & Flu','Cosmetics','First Aid','Fragrances','Gift Packs', 'Giftware', 'Hair Care', 'Kids', 'Household and Domestic', 'Intimacy', 'Medical Devices', 'Medicinals', 'Oral Care', 'Pet Care', 'Pharamacist Medicines', 'Prescription', 'Skin Care', 'Toiletries', 'Vitamins', 'Weight Loss'];
c=StringVar()
droplist=OptionMenu(root,c, *list1)
droplist.config(width=15)
c.set('Select Category')
droplist.place(x=240,y=280)

label_4 = Label(root, text="Date and Time",width=20,font=("bold", 10))
label_4.place(x=85,y=330)


but1= Button(root, text='Add Record',width=20,bg='brown',fg='white',command=add).place(x=80,y=380)
but2 = Button(root,width=15,text="Exit",bg='brown',fg='white').place(x=280,y=380)


root.mainloop()























