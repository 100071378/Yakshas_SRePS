from tkinter import *
import pymysql
import sys
import matplotlib.pyplot as plt


class Window(Frame):

    def __init__(self, master=None):
        Frame.__init__(self, master)

        self.master = master
        self.init_window()

    def init_window(self):
        self.master.title("SEARCH")
        self.pack(fill=BOTH, expand=1)

        graphbutton = Button(self, text="Plot a graph", command=self.gradid, fg="red", bg="black")
        graphbutton.pack(side=TOP)

        prodbutton= Button(self, text="Search for a Product", command=self.prodid, fg="red", bg="black")
        prodbutton.pack(side=RIGHT)

        recbutton = Button(self, text="Search for a Record", command=self.recdid, fg="red", bg="black")
        recbutton.pack(side=LEFT)

    def gradid(self):
        OPTIONS = [
            "Product ID",
            "Record ID",
            "User ID"
        ]

        master = Tk()
        master.title("Plot a graph!")
        master.geometry('300x300')
        variable = StringVar(master)
        variable.set(OPTIONS[0])

        w = OptionMenu(master, variable, *OPTIONS)
        w.pack()

        def ok():

            db = pymysql.connect("localhost", "root", "", "pharmacy")
            cursor = db.cursor()

            if variable.get() == "Product ID":
                sql4 = "select Date, prodID from recorddescri"
            else:
                if variable.get() == "Record ID":
                    sql4 = "select Date, recordID from recorddescri"
                else:
                    sql4 = "select Date, userID from recorddescri"

            cursor.execute(sql4)

            result = cursor.fetchall()

            date = []
            crite = []

            for record in result:
                date.append(record[1])
                crite.append(record[0])

            plt.plot(date, crite, 'ro')
            plt.title("All Sales Record!", fontsize=16, color="#FF00FF")
            plt.xlabel('%s' % variable.get(), fontsize=13, color="#0000ff")
            plt.ylabel('DATE', fontsize=13, color="#0000ff")
            plt.show()

        button = Button(master, text="Plot by selected criteria", command=ok, fg="black", bg="red")
        button.pack()
        mainloop()

    def prodid(self):

        OPTIONS = [
            "Product ID",
            "Category",
            "Name",
            "Brand"
        ]

        master = Tk()
        master.title("Search for Products")
        master.geometry('300x300')
        variable = StringVar(master)
        variable.set(OPTIONS[0])

        w = OptionMenu(master, variable, *OPTIONS)
        w.pack()

        def ok():

            def prodsearch():
                db = pymysql.connect("localhost", "root", "", "pharmacy")
                cursor = db.cursor()

                if variable.get() == "Product ID":
                    sql4 = ("SELECT * from  product where prodID = '%s'" % p1.get())
                else:
                    if variable.get() == "Category":
                        sql4 = ("SELECT * from  product where catogory = '%s'" % p1.get())
                    else:
                        if variable.get() == "Name":
                            sql4 = ("SELECT * from  product where name = '%s'" % p1.get())
                        else:
                            sql4 = ("SELECT * from  product where brand = '%s'" % p1.get())

                cursor.execute(sql4)
                data = cursor.fetchall()

                master3 = Tk()
                master3.title("Results")

                for row in data:
                    text = Text(master3, width=50, height=6, bg="black", fg="red")
                    text.pack()
                    text.insert(INSERT, "Product ID: %s \n" % (row[0]))
                    text.insert(INSERT, "Category: %s \n" % (row[1]))
                    text.insert(INSERT, "Brand: %s \n" % (row[2]))
                    text.insert(INSERT, "Name: %s \n" % (row[3]))
                    text.insert(INSERT, "In stock number: %s \n" % (row[4]))
                    text.insert(INSERT, "Price in RM: %s \n" % (row[4]))

                cursor.close()
                # disconnect from server
                db.close()

            master2 = Tk()
            master2.title("Search for Products")
            master2.geometry('300x300')
            Label(master2, text="Enter %s:" % variable.get(), fg="blue").grid(row=0)
            p1 = Entry(master2)
            p1.grid(row=0, column=1)

            Button(master2, text='Quit', command=master.quit, fg="red", bg="black").grid(row=3, column=0, sticky=W, pady=4)

            Button(master2, text='Search', command=prodsearch, fg="red", bg="black").grid(row=3, column=1, sticky=W, pady=4)

        button = Button(master, text="Search by selected criteria", command=ok, fg="black", bg="red")
        button.pack()
        mainloop()

    def recdid(self):

        OPTIONS = [
            "Record ID",
            "Product ID",
            "Date",
            "Staff ID"
        ]

        master = Tk()
        master.title("Search for Sales Record")
        master.geometry('300x300')
        variable = StringVar(master)
        variable.set(OPTIONS[0])

        w = OptionMenu(master, variable, *OPTIONS)
        w.pack()

        def ok():

            def recsearch():
                db = pymysql.connect("localhost", "root", "", "pharmacy")
                cursor = db.cursor()

                if variable.get() == "Record ID":
                    sql4 = ("SELECT * from  recorddescri where recordID = '%s'" % p1.get())
                else:
                    if variable.get() == "Product ID":
                        sql4 = ("SELECT * from  recorddescri where prodID = '%s'" % p1.get())
                    else:
                        if variable.get() == "Date":
                            sql4 = ("SELECT * from  recorddescri where Date = '%s'" % p1.get())
                        else:
                            sql4 = ("SELECT * from  recorddescri where userID = '%s'" % p1.get())

                cursor.execute(sql4)

                data = cursor.fetchall()

                master3 = Tk()
                master3.title("Results")

                for row in data:
                    text = Text(master3, width=50, height=6, bg="black", fg="red")
                    text.pack()
                    text.insert(INSERT, "Record ID: %s \n" % (row[0]))
                    text.insert(INSERT, "ProductID: %s \n" % (row[1]))
                    text.insert(INSERT, "Date: %s \n" % (row[2]))
                    text.insert(INSERT, "Quantity: %s \n" % (row[3]))
                    text.insert(INSERT, "Staff ID: %s \n" % (row[4]))

            master2 = Tk()
            master2.title("Search for Sales Records")
            master2.geometry('300x300')
            Label(master2, text="Enter %s:" % variable.get(), fg="blue").grid(row=0)
            p1 = Entry(master2)
            p1.grid(row=0, column=1)

            Button(master2, text='Quit', command=master2.quit, fg="red", bg="black").grid(row=3, column=0, sticky=W, pady=4)

            Button(master2, text='Search', command=recsearch, fg="red", bg="black").grid(row=3, column=1, sticky=W, pady=4)

        button = Button(master, text="Search by selected criteria", command=ok, fg="black", bg="red")
        button.pack()
        mainloop()


root = Tk()
root.geometry("400x300")
app = Window(root)
root.mainloop()