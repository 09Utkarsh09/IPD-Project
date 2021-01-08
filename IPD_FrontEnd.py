from tkinter import *
import tkinter.messagebox
import IPD_BackEnd

class Student:

    def __init__(self, root):
        self.root= root
        self.root.title("Student Database")
        self.root.geometry("1350x7500")
        self.root.config(bg="cyan")

        emp_id = StringVar()
        Firstname = StringVar()
        Surname = StringVar()
        Dob = StringVar()
        Age = StringVar()
        Gender = StringVar()
        Address = StringVar()
        Mobile = StringVar()

        #FUNCTION
        def iExit():
            iExit = tkinter.messagebox.askyesno("STUDENT DATABASE" , "Confirm if you want to exit")
            if iExit > 0:
                root.destroy()
                return

        def clearData():
            self.txtemp_id.delete(0, END)
            self.txtfna.delete(0, END)
            self.txtsna.delete(0, END)
            self.txtDoB.delete(0, END)
            self.txtAge.delete(0, END)
            self.txtGender.delete(0, END)
            self.txtAddress.delete(0, END)
            self.txtMobile.delete(0, END)


        def addData():
            if(len(emp_id.get())!=0):
                IPD_BackEnd.addEmpRec(emp_id.get() , Firstname.get() , Surname.get() , Dob.get() , Age.get(), Gender.get() , Address.get() , Mobile.get() )
                Studentlist.delete(0,END)
                Studentlist.insert(emp_id.get() , Firstname.get() , Surname.get() , Dob.get() , Age.get(), Gender.get() , Address.get() , Mobile.get() )

        def DisplayData():
            Studentlist.delete(0, END)
            for row in IPD_BackEnd.viewData():
                Studentlist.insert(END,row,str(""))

        def StudentRec(event):
            global sd
            searchStudent = Studentlist.curselection()[0]
            sd = Studentlist.get(searchStudent)

            self.txtemp_id.delete(0, END)
            self.txtemp_id.insert(END , sd[1])
            self.txtfna.delete(0, END)
            self.txtfna.insert(END, sd[2])
            self.txtsna.delete(0, END)
            self.txtsna.insert(END, sd[3])
            self.txtDoB.delete(0, END)
            self.txtDoB.insert(END, sd[4])
            self.txtAge.delete(0, END)
            self.txtAge.insert(END, sd[5])
            self.txtGender.delete(0, END)
            self.txtGender.insert(END, sd[6])
            self.txtAddress.delete(0, END)
            self.txtAddress.insert(END, sd[7])
            self.txtMobile.delete(0, END)
            self.txtMobile.insert(END, sd[8])


        def DeleteData():
            if (len(emp_id.get()) != 0):
                IPD_BackEnd.deleteRec(sd[0])
                clearData()
                DisplayData()


        def searchDatabase():
            Studentlist.delete(0, END)
            for row in IPD_BackEnd.searchData(emp_id.get(), Firstname.get(), Surname.get(), Dob.get(), Age.get(), Gender.get(), Address.get(), Mobile.get()):
                Studentlist.insert(END, row, str(""))



        def update():
            if(len(emp_id.get())!=0):
                IPD_BackEnd.deleteRec(sd[0])
            if (len(emp_id.get()) != 0):
                IPD_BackEnd.addEmpRec(emp_id.get() , Firstname.get() , Surname.get() , Dob.get() , Age.get(), Gender.get() , Address.get() , Mobile.get())
                Studentlist.delete(0, END)
                Studentlist.insert(END, (emp_id.get() , Firstname.get() , Surname.get() , Dob.get() , Age.get(), Gender.get() , Address.get() , Mobile.get()))





        MainFrame = Frame(self.root , bg="cyan")
        MainFrame.grid()

        TitFrame = Frame(MainFrame, bd=2, padx=54, pady=8,  bg="Ghost White", relief=RIDGE)
        TitFrame.pack(side=TOP)

        self.lblTit= Label(TitFrame, font=('algerian',47,'bold'), text="STUDENT DATABASE SYSTEM", bg="Ghost White")
        self.lblTit.grid(sticky=W)

        ButtonFrame = Frame(MainFrame, bd=2, width=1350, height=70, padx=18, pady=10, bg="Ghost White", relief=RIDGE)
        ButtonFrame.pack(side=BOTTOM)

        DataFrame = Frame(MainFrame, bd=1, width=1300, height=400, padx=20, pady=20, relief=RIDGE, bg="cyan")
        DataFrame.pack(side=BOTTOM)

        DataFrameLEFT = LabelFrame(DataFrame, bd=1, width=1000, height=600, padx=20, relief=RIDGE, bg="Ghost White", font=('showcard gothic',20,'bold'), text="Student Info\n")
        DataFrameLEFT.pack(side=LEFT)

        DataFrameRIGHT = LabelFrame(DataFrame, bd=1, width=450, height=300, padx=31, pady=3, relief=RIDGE,  bg="Ghost White", font=('showcard gothic', 20, 'bold'), text="Student Details\n")
        DataFrameRIGHT.pack(side=RIGHT)

        # LABELS AND ENTRY WIDGET
        self.lblemp_id = Label(DataFrameLEFT, font=('algerian', 20, 'bold'), text="Student ID:", padx=2, pady=2, bg="Ghost White")
        self.lblemp_id.grid(row=0, column=0, sticky=W)
        self.txtemp_id= Entry(DataFrameLEFT, font=('algerian', 20, 'bold'),textvariable=emp_id, width=39)
        self.txtemp_id.grid(row=0, column=1)



        self.lblfna = Label(DataFrameLEFT, font=('algerian', 20, 'bold'), text="Firstname:", padx=2, pady=2,
                               bg="Ghost White")
        self.lblfna.grid(row=1, column=0, sticky=W)
        self.txtfna = Entry(DataFrameLEFT, font=('algerian', 20, 'bold'), textvariable=Firstname, width=39)
        self.txtfna.grid(row=1, column=1)



        self.lblsna = Label(DataFrameLEFT, font=('algerian', 20, 'bold'), text="Surname:", padx=2, pady=2,
                               bg="Ghost White")
        self.lblsna.grid(row=2, column=0, sticky=W)
        self.txtsna = Entry(DataFrameLEFT, font=('algerian', 20, 'bold'), textvariable=Surname, width=39)
        self.txtsna.grid(row=2, column=1)


        self.lblDoB = Label(DataFrameLEFT, font=('algerian', 20, 'bold'), text="Date Of Birth:", padx=2, pady=2,
                            bg="Ghost White")
        self.lblDoB.grid(row=3, column=0, sticky=W)
        self.txtDoB = Entry(DataFrameLEFT, font=('algerian', 20, 'bold'), textvariable=Dob, width=39)
        self.txtDoB.grid(row=3, column=1)

        self.lblAge = Label(DataFrameLEFT, font=('algerian', 20, 'bold'), text="Age:", padx=2, pady=2,
                            bg="Ghost White")
        self.lblAge.grid(row=4, column=0, sticky=W)
        self.txtAge = Entry(DataFrameLEFT, font=('algerian', 20, 'bold'), textvariable=Age, width=39)
        self.txtAge.grid(row=4, column=1)

        self.lblGender = Label(DataFrameLEFT, font=('algerian', 20, 'bold'), text="Gender:", padx=2, pady=2,
                            bg="Ghost White")
        self.lblGender.grid(row=5, column=0, sticky=W)
        self.txtGender = Entry(DataFrameLEFT, font=('algerian', 20, 'bold'), textvariable=Gender, width=39)
        self.txtGender.grid(row=5, column=1)

        self.lblAddress = Label(DataFrameLEFT, font=('algerian', 20, 'bold'), text="Address:", padx=2, pady=2,
                               bg="Ghost White")
        self.lblAddress.grid(row=6, column=0, sticky=W)
        self.txtAddress = Entry(DataFrameLEFT, font=('algerian', 20, 'bold'), textvariable=Address, width=39)
        self.txtAddress.grid(row=6, column=1)

        self.lblMobile = Label(DataFrameLEFT, font=('algerian', 20, 'bold'), text="Mobile:", padx=2, pady=2,
                                bg="Ghost White")
        self.lblMobile.grid(row=7, column=0, sticky=W)
        self.txtMobile = Entry(DataFrameLEFT, font=('algerian', 20, 'bold'), textvariable=Mobile, width=39)
        self.txtMobile.grid(row=7, column=1)

        #LIST BOX AND SCROLL BAR

        scrollbar= Scrollbar(DataFrameRIGHT)
        scrollbar.grid(row=0, column=1, sticky='ns')

        Studentlist = Listbox(DataFrameRIGHT, width=41, height= 16,font=('algerian', 12, 'bold'), yscrollcommand=scrollbar.set)
        Studentlist.bind('<<ListboxSelect>>', StudentRec)
        Studentlist.grid(row=0, column=0, padx=8)
        scrollbar.config(command= Studentlist.yview)


        #BUTTON

        self.btnAddData=Button(ButtonFrame, text="Add New", font=('algerian', 20 , 'bold'),  height=1 , width=10, bd=4, command=addData)
        self.btnAddData.grid(row=0, column=0)

        self.btnDiaplayData = Button(ButtonFrame, text="Display", font=('algerian', 20, 'bold'), height=1, width=10, bd=4, command=DisplayData)
        self.btnDiaplayData.grid(row=0, column=1)

        self.btnClearData = Button(ButtonFrame, text="Clear", font=('algerian', 20, 'bold'), height=1, width=10, bd=4, command=clearData)
        self.btnClearData.grid(row=0, column=2)

        self.btnDeleteData = Button(ButtonFrame, text="Delete", font=('algerian', 20, 'bold'), height=1, width=10, bd=4, command=DeleteData)
        self.btnDeleteData.grid(row=0, column=3)

        self.btnSearchData = Button(ButtonFrame, text="Search", font=('algerian', 20, 'bold'), height=1, width=10, bd=4, command=searchDatabase)
        self.btnSearchData.grid(row=0, column=4)

        self.btnUpdateData = Button(ButtonFrame, text="Update", font=('algerian', 20, 'bold'), height=1, width=10, bd=4, command=update)
        self.btnUpdateData.grid(row=0, column=5)

        self.btnExit = Button(ButtonFrame, text="Exit", font=('algerian', 20, 'bold'), height=1, width=10, bd=4, command= iExit)
        self.btnExit.grid(row=0, column=6)





if __name__=='__main__':
    root = Tk()
    application = Student(root)
    root.mainloop()