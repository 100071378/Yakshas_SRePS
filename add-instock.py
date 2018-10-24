from Tkinter import *
import pymysql


root = Tk()
root.geometry('500x500')
root.title("SRePS Stock Data")

label_0 = Label(root, text="In-Stock Data",width=20,font=("bold", 20))
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


Button(root, text='Add Data',width=20,bg='brown',fg='white').place(x=180,y=380)

root.mainloop()