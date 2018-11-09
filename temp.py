from tkinter import *
import pymysql


class Window(Frame):

    def __init__(self, master=None):
        Frame.__init__(self, master)

        self.master = master
        self.init_window()

    def init_window(self):
        self.master.title("SEARCH")
        self.pack(fill=BOTH, expand=1)

        prodbutton= Button(self, text="Search for a Product", command=self.prodid, fg="red")
        prodbutton.pack(side=LEFT)

        recbutton = Button(self, text="Search for a Record", command=self.recdid, fg="red")
        recbutton.pack(side=RIGHT)

    def prodid(self):
        db = pymysql.connect("localhost", "root", "", "pharmacy")

        cursor = db.cursor()
        user_input = input("Enter product id of product:")
        sql3 = ("SELECT * from product where prodID = '%s'" % user_input)

        cursor.execute(sql3)

        data = cursor.fetchall()

        for row in data:
            print("Product ID = ", row[0])
            print("Category = ", row[1])
            print("Brand  = ", row[2])
            print("Name  = ", row[3])
            print("In stock number  = ", row[4])
            print("Price in RM  = ", row[5], "\n")

        cursor.close()
        # disconnect from server
        db.close()

    def recdid(self):
        db = pymysql.connect("localhost", "root", "", "pharmacy")

        cursor = db.cursor()
        user_input = input("Enter record id of sale:")
        sql3 = ("SELECT * from  recorddescri  where recordID= '%s' " % user_input)

        cursor.execute(sql3)

        data = cursor.fetchall()

        for row in data:
            print("Record ID= ", row[0])
            print("Product ID= ", row[1])
            print("Date= ", row[2])
            print("Quantity = ", row[3])
            print("Staff ID =", row[4], "\n")

        cursor.close()
        # disconnect from server
        db.close()


root = Tk()
root.geometry("400x300")
app = Window(root)
root.mainloop()









