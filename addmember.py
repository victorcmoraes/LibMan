from tkinter import *
from tkinter import messagebox
import sqlite3
con = sqlite3.connect('lib.db')
cur = con.cursor()


class AddMember(Toplevel):
    def __init__(self):
        Toplevel.__init__(self)
        self.geometry("650x750+550+200")
        self.title("Add Member")
        self.resizable(False, False)

        # Frames
        self.topFrame = Frame(self, height=150, bg='white')
        self.topFrame.pack(fill=X)

        self.bottomFrame = Frame(self, height=600, bg='#fcc324')
        self.bottomFrame.pack(fill=X)

        self.topImg = PhotoImage(file='icons/add-contact.png')

        self.topImgLbl = Label(self.topFrame, image=self.topImg,bg='white')
        self.topImgLbl.place(x=120, y=10)
        self.heading = Label(self.topFrame, text='   Add Member', font='arial 22 bold', fg='#003f8a', bg='white')
        self.heading.place(x=290, y=60)

        def clear_text(event):
            if event.widget.get() == 'Please enter member name' or event.widget.get() == 'Please enter CPF':
                event.widget.delete(0, END)

        self.lbl_name = Label(self.bottomFrame, text='Name :', font='arial 15 bold', fg='white', bg='#fcc324')
        self.lbl_name.place(x=40, y=40)
        self.ent_name = Entry(self.bottomFrame, width=30, bd=4)
        self.ent_name.insert(0, 'Please enter member name')
        self.ent_name.place(x=150, y=45)

        self.ent_name.bind('<FocusIn>', clear_text)

        self.lbl_cpf = Label(self.bottomFrame, text='CPF :', font='arial 15 bold', fg='white', bg='#fcc324')
        self.lbl_cpf.place(x=40, y=80)
        self.ent_cpf = Entry(self.bottomFrame, width=30, bd=4)
        self.ent_cpf.insert(0, 'Please enter CPF')
        self.ent_cpf.place(x=150, y=85)
        self.ent_cpf.bind('<FocusIn>', clear_text)

        button = Button(self.bottomFrame,text='Add Member', command=self.addMember)
        button.place(x=270,y=200)

    def addMember(self):
        name = self.ent_name.get()
        cpf = self.ent_cpf.get()

        if name and cpf != "":
            try:
                query = "INSERT INTO 'members' (members_name,members_cpf) VALUES(?,?)"
                cur.execute(query, (name, cpf))
                con.commit()
                messagebox.showinfo("Success", "Successfully added to the database", icon='info')

            except:
                messagebox.showerror("Error","Cant add to the database", icon='warning')
        else:
            messagebox.showerror("Error", "Files cant be empty", icon='warning')
