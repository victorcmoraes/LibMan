from tkinter import *
from tkinter import messagebox
import sqlite3
import __main__
con = sqlite3.connect('lib.db')
cur = con.cursor()


class AddBook(Toplevel):
    def __init__(self):
        Toplevel.__init__(self)
        self.geometry("650x750+550+200")
        self.title("Add Book")
        self.resizable(False, False)

        # Frames
        self.topFrame = Frame(self, height=150, bg='white')
        self.topFrame.pack(fill=X)

        self.bottomFrame = Frame(self, height=600, bg='#fcc324')
        self.bottomFrame.pack(fill=X)

        self.topImg = PhotoImage(file='icons/add.png')

        self.topImgLbl = Label(self.topFrame, image=self.topImg,bg='white')
        self.topImgLbl.place(x=120, y=10)
        self.heading = Label(self.topFrame, text='   Add Book', font='arial 22 bold', fg='#003f8a', bg='white')
        self.heading.place(x=290, y=60)

        def clear_text(event):
            if event.widget.get() == 'Please enter a book name' or event.widget.get() == 'Please enter author name' \
                    or event.widget.get() == 'Please enter the number of pages' or event.widget.get() == \
                    'Please enter the language of the book':
                event.widget.delete(0, END)

        self.lbl_name = Label(self.bottomFrame, text='Name :', font='arial 15 bold', fg='white', bg='#fcc324')
        self.lbl_name.place(x=40, y=40)
        self.ent_name = Entry(self.bottomFrame, width=30, bd=4)
        self.ent_name.insert(0, 'Please enter a book name')
        self.ent_name.place(x=150, y=45)

        self.ent_name.bind('<FocusIn>', clear_text)

        self.lbl_author = Label(self.bottomFrame, text='Author :', font='arial 15 bold', fg='white', bg='#fcc324')
        self.lbl_author.place(x=40, y=80)
        self.ent_author = Entry(self.bottomFrame, width=30, bd=4)
        self.ent_author.insert(0, 'Please enter author name')
        self.ent_author.place(x=150, y=85)
        self.ent_author.bind('<FocusIn>', clear_text)

        self.lbl_page = Label(self.bottomFrame, text='Page :', font='arial 15 bold', fg='white', bg='#fcc324')
        self.lbl_page.place(x=40, y=120)
        self.ent_page = Entry(self.bottomFrame, width=30, bd=4)
        self.ent_page.insert(0, 'Please enter the number of pages')
        self.ent_page.place(x=150, y=125)
        self.ent_page.bind('<FocusIn>', clear_text)

        self.lbl_language = Label(self.bottomFrame, text='Language :', font='arial 15 bold', fg='white', bg='#fcc324')
        self.lbl_language.place(x=40, y=160)
        self.ent_language = Entry(self.bottomFrame, width=30, bd=4)
        self.ent_language.insert(0, 'Please enter the language of the book')
        self.ent_language.place(x=150, y=165)
        self.ent_language.bind('<FocusIn>', clear_text)

        button=Button(self.bottomFrame,text='Add Book', command=self.addBook)
        button.place(x=270,y=200)

    def addBook(self):
        name = self.ent_name.get()
        author = self.ent_author.get()
        page = self.ent_page.get()
        language = self.ent_language.get()

        if (name and author and page and language !=""):
            try:
                query="INSERT INTO 'books' (book_name,book_author,book_page,book_language) VALUES(?,?,?,?)"
                cur.execute(query,(name,author,page,language))
                con.commit()
                messagebox.showinfo("Success", "Successfully added to the database", icon='info')
            except:
                messagebox.showerror("Error","Cant add to the database", icon='warning')
        else:
            messagebox.showerror("Error", "Files cant be empty", icon='warning')

