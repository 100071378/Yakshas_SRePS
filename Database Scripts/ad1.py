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

        prodbutton= Button(self, text="Search for a Product", command=self.prodid, fg="red", bg="black")
        prodbutton.pack(side=LEFT)

        recbutton = Button(self, text="Search for a Record", command=self.recdid, fg="red", bg="black")
        recbutton.pack(side=RIGHT)

    def prodid(self):

        def prodsearch():
            db = pymysql.connect("localhost", "root", "", "pharmacy")
            cursor = db.cursor()
            sql3 = ("SELECT * from product where prodID = '%s'" % p1.get())
            cursor.execute(sql3)

            data = cursor.fetchall()
            for row in data:
                definition = row[0]

            output.insert(END, definition)

            cursor.close()
            # disconnect from server
            db.close()

        master = Tk()
        master.title("Search for Products")
        master.geometry('300x300')
        Label(master, text="Enter product ID:", fg="blue").grid(row=0)

        p1 = Entry(master)
        p1.grid(row=0, column=1)

        Button(master, text='Quit', command=master.quit, fg="red", bg="black").grid(row=3, column=0, sticky=W, pady=4)
        Button(master, text='Search', command=prodsearch, fg="red", bg="black").grid(row=3, column=1, sticky=W, pady=4)

        mainloop()

    def recdid(self):

        def recsearch():
            db = pymysql.connect("localhost", "root", "", "pharmacy")
            cursor = db.cursor()
            sql4 = ("SELECT * from  recorddescri  where recordID = '%s'" % r1.get())

            cursor.execute(sql4)

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

        master2 = Tk()
        master2.title("Search for Records")
        master2.geometry('300x300')
        Label(master2, text="Enter record ID:", fg="blue").grid(row=0)

        r1 = Entry(master2)
        r1.grid(row=0, column=1)

        Button(master2, text='Quit', command=master2.quit, fg="red", bg="black").grid(row=3, column=0, sticky=W, pady=4)
        Button(master2, text='Search', command=recsearch, fg="red", bg="black").grid(row=3, column=1, sticky=W, pady=4)

        mainloop()


root = Tk()
root.geometry("400x300")
app = Window(root)
root.mainloop()