import sqlite3
import tkinter as tk
from tkinter import *
from tkinter import messagebox
from tkinter import ttk

import addbook
import addmember

con = sqlite3.connect('lib.db')
cur = con.cursor()


class Main:
    def __init__(self, master):
        self.master = master

        def displayBooks(self):
            books = cur.execute("SELECT * FROM books").fetchall()
            count = 0
            for book in books:
                print(book)
                self.listBooks.insert(count, str(book[0]) + "-" + book[1])
                count += 1

            def bookInfo(evt):
                value = str(self.listBooks.get(self.listBooks.curselection()))
                id = value.split('-')[0]
                book = cur.execute("SELECT * FROM books WHERE book_id=?", (id,))
                book_info = book.fetchall()
                self.listDetails.delete(0, 'end')
                self.listDetails.insert(0, "Book Name : " + book_info[0][1])
                self.listDetails.insert(1, "Author : " + book_info[0][2])
                self.listDetails.insert(2, "Page : " + book_info[0][3])
                self.listDetails.insert(3, "Language : " + book_info[0][4])
                if book_info[0][5] == 0:
                    self.listDetails.insert((4, "Status : Available"))
                else:
                    self.listDetails.insert(4, "Status : Not available")

            def doubleClick(evt):
                global given_id
                value = str(self.listBooks.get(self.listBooks.curselection()))
                given_id = value.split('-')[0]
                give_book=GiveBook()

            self.listBooks.bind('<<ListboxSelect>>', bookInfo)
            self.listBooks.bind('<Double-Button-1>', doubleClick)

        # frames
        self.mainFrame = Frame(self.master)
        self.mainFrame.pack()

        # top frames
        self.topFrame = Frame(self.mainFrame, width=1350, height=70, bg='#f8f8f8', padx=20, relief=SUNKEN,
                                borderwidth=2)
        self.topFrame.pack(side=TOP, fill=X)

        # center frame
        self.centerFrame = Frame(self.mainFrame, width=1350, height=700, bg='#e0f0f0', padx=20, relief=SUNKEN,
                                    borderwidth=2)
        self.centerFrame.pack(side=TOP)

        # center left frame
        self.centerLeftFrame = Frame(self.centerFrame, width=900, height=700, bg='#e0f0f0', borderwidth=2,
                                        relief='sunken')
        self.centerLeftFrame.pack(side=LEFT)

        # center right frame
        self.centerRightFrame = Frame(self.centerFrame, width=450, height=700, bg='#e0f0f0', borderwidth=2,
                                        relief='sunken')
        self.centerRightFrame.pack()

        # search bar
        search_bar = LabelFrame(self.centerRightFrame, width=440, height=175, text='Search Box', bg='#9bc9ff')
        search_bar.pack(fill=BOTH)
        self.lbl_search = Label(search_bar, text='search :', font='arial 12 bold', bg='#9bc9ff', fg='white')
        self.lbl_search.grid(row=0, column=0, padx=20, pady=10)
        self.ent_search = Entry(search_bar, width=30, bd=10)
        self.ent_search.grid(row=0, column=1, columnspan=3, padx=10, pady=10)
        self.btn_search = Button(search_bar, text='Search', font='arial 12', bg='#fcc324', fg='white',
                                    command=self.searchBooks)
        self.btn_search.grid(row=0, column=4, padx=10, pady=10)

        # list bar
        list_bar = LabelFrame(self.centerRightFrame, width=440, height=175, text='List Box', bg='#fcc324')
        list_bar.pack(fill=BOTH)
        lbl_list = Label(list_bar, text='Index By', font='arial 12 bold', fg='#e0f0f0', bg='#fcc324')
        lbl_list.grid(row=0, column=2)
        self.listChoice = IntVar()
        rb1 = Radiobutton(list_bar, text='All Books', var=self.listChoice, value=1, bg='#fcc324')
        rb2 = Radiobutton(list_bar, text='In Library', var=self.listChoice, value=2, bg='#fcc324')
        rb3 = Radiobutton(list_bar, text='Borrowed Books', var=self.listChoice, value=3, bg='#fcc324')
        rb1.grid(row=1, column=0)
        rb2.grid(row=1, column=1)
        rb3.grid(row=1, column=2)
        btn_list = Button(list_bar, text='List Books', bg='#9bc9ff', fg='white', font='arial 12',
                            command=self.listarBooks)
        btn_list.grid(row=1, column=3, padx=40, pady=10)

        # title and image
        self.imageBar = Frame(self.centerRightFrame, width=440, height=350)
        self.imageBar.pack(fill=BOTH)
        self.title_right = Label(self.imageBar, text='WELCOME', font='arial 16 bold')
        self.title_right.grid(row=0)
        self.imgLibrary = PhotoImage(file='icons/library.png')
        self.lblImg = Label(self.imageBar, image=self.imgLibrary)
        self.lblImg.grid(row=1)

        # add book
        self.iconBook = PhotoImage(file='icons/addBook.png')
        self.btnBook = Button(self.topFrame, text='Add Book', image=self.iconBook, compound=LEFT, font='arial 12 bold',
                                padx=10, command=self.addBook)
        self.btnBook.pack(side=LEFT)

        # add member button
        self.iconUser = PhotoImage(file='icons/new-user.png')
        self.btnUser = Button(self.topFrame, text='Add Member', image=self.iconUser, font='arial 12 bold', padx=10,
                                command=self.addMember)
        self.btnUser.configure(image=self.iconUser, compound=LEFT)
        self.btnUser.pack(side=LEFT)

        # take book
        self.iconTake = PhotoImage(file='icons/takeBook.png')
        self.btnTake = Button(self.topFrame, text='Take Book', image=self.iconTake, font='arial 12 bold', padx=10, compound=LEFT, command=self.takeBook)
        self.btnTake.pack(side=LEFT)

        # return book
        self.iconReturn = PhotoImage(file='icons/returnBook.png')
        self.btnReturn = Button(self.topFrame, text='Return Book', image=self.iconReturn, font='arial 12 bold', padx=10, compound=LEFT, command=self.returnBook)
        self.btnReturn.pack(side=LEFT)


        # tabs
        self.tabs = ttk.Notebook(self.centerLeftFrame, width=900, height=660)
        self.tabs.pack()
        self.tab1Icon = PhotoImage(file='icons/addBook.png')
        self.tab2Icon = PhotoImage(file='icons/new-user.png')
        self.tab1 = ttk.Frame(self.tabs)
        self.tab2 = ttk.Frame(self.tabs)
        self.tabs.add(self.tab1, text='LibMan', image=self.tab1Icon, compound=LEFT)

        # list books
        self.listBooks = Listbox(self.tab1, width=40, height=30, bd=5, font='times 12 bold')
        self.sb = Scrollbar(self.tab1, orient=VERTICAL)
        self.listBooks.grid(row=0, column=0, padx=(10, 0), pady=10, sticky=N)
        self.sb.config(command=self.listBooks.yview)
        self.listBooks.config(yscrollcommand=self.sb.set)
        self.sb.grid(row=0, column=0, sticky=N + S + E)

        # list details
        self.listDetails = Listbox(self.tab1, width=80, height=30, bd=5, font='times 12 bold')
        self.listDetails.grid(row=0, column=1, padx=(10, 0), pady=10, sticky=N)

        # Botão para excluir um livro
        self.btnDeleteBook = Button(self.topFrame, text='Delete Book', font='arial 12 bold', padx=10, command=self.deleteBook)
        self.btnDeleteBook.pack(side=LEFT)


        displayBooks(self)

    def addBook(self):
        addbook.AddBook()

    def addMember(self):
        member = addmember.AddMember()

    def searchBooks(self):
        value = self.ent_search.get()
        search = cur.execute("SELECT * FROM books WHERE book_name LIKE ?", ('%' + value + '%',)).fetchall()
        self.listBooks.delete(0, END)
        count = 0
        for book in search:
            self.listBooks.insert(count, str(book[0]) + "-" + book[1])
            count += 1

    def listarBooks(self):
        value = self.listChoice.get()
        if value == 1:
            all_books = cur.execute("SELECT * FROM books").fetchall()
            self.listBooks.delete(0, END)

            for book in all_books:
                self.listBooks.insert(END, str(book[0]) + "-" + book[1])
        elif value == 2:
            books_in_library = cur.execute("SELECT * FROM books WHERE book_status = ?", (0,)).fetchall()
            self.listBooks.delete(0, END)

            for book in books_in_library:
                self.listBooks.insert(END, str(book[0]) + "-" + book[1])
        else:  # value == 3 (taken books)
            taken_books = cur.execute("SELECT * FROM books WHERE book_status = ?", (1,)).fetchall()
            self.listBooks.delete(0, END)

            for book in taken_books:
                self.listBooks.insert(END, str(book[0]) + "-" + book[1])

    def deleteBook(self):
        if not self.listBooks.curselection():
            messagebox.showwarning("Warning", "Please select a book to delete.")
            return

        selected_book = str(self.listBooks.get(self.listBooks.curselection()))
        book_id = selected_book.split('-')[0]

        confirmation = messagebox.askyesno("Confirmation", f"Do you want to delete the book {selected_book} ?")

        if confirmation:
            try:
                cur.execute("DELETE FROM books WHERE book_id=?", (book_id,))
                con.commit()
                messagebox.showinfo("Success", "Book deleted successfully.")
                self.listarBooks()
            except Exception as e:
                messagebox.showerror("Error", f"Error deleting book: {str(e)}")

    def takeBook(self):
        if not self.listBooks.curselection():
            messagebox.showwarning("Warning", "Please select a book to take.")
            return

        selected_book = str(self.listBooks.get(self.listBooks.curselection()))
        book_id = selected_book.split('-')[0]

        try:
            status = cur.execute("SELECT book_status FROM books WHERE book_id=?", (book_id,)).fetchone()[0]
            if status == 1:
                messagebox.showinfo("Info", "This book is already taken.")
            else:
                cur.execute("UPDATE books SET book_status = ? WHERE book_id = ?", (1, book_id))
                con.commit()
                messagebox.showinfo("Success", "Book taken successfully.")
                self.listarBooks() 
        except Exception as e:
            messagebox.showerror("Error", f"Error taking book: {str(e)}")

    def returnBook(self):
        if not self.listBooks.curselection():
            messagebox.showwarning("Warning", "Please select a book to return.")
            return

        selected_book = str(self.listBooks.get(self.listBooks.curselection()))
        book_id = selected_book.split('-')[0]

        try:
            status = cur.execute("SELECT book_status FROM books WHERE book_id=?", (book_id,)).fetchone()[0]
            if status == 0:
                messagebox.showinfo("Info", "This book is already in the library.")
            else:
                cur.execute("UPDATE books SET book_status = ? WHERE book_id = ?", (0, book_id))
                con.commit()
                messagebox.showinfo("Success", "Book returned successfully.")
                self.listarBooks()
        except Exception as e:
            messagebox.showerror("Error", f"Error returning book: {str(e)}")


    
class GiveBook(Toplevel):
    def __init__(self):
        Toplevel.__init__(self)
        self.geometry("650x750+550+200")
        self.title("Lend Book")
        self.resizable(False, False)
        global given_id
        self.book_id=int(given_id)
        query = "SELECT * FROM books"
        books = cur.execute(query).fetchall()
        book_list = []
        for book in books:
            book_list.append(str(book[0])+"-"+book[1])

        query2 = "SELECT * FROM members"
        members = cur.execute(query2).fetchall()
        member_list=[]
        for member in members:
            member_list.append(str(member[0])+"-"+member[1])



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

        self.book_name = StringVar()
        self.lbl_name = Label(self.bottomFrame, text='Book :', font='arial 15 bold', fg='white', bg='#fcc324')
        self.lbl_name.place(x=40, y=40)
        self.combo_name = ttk.Combobox(self.bottomFrame, textvariable=self.book_name)
        self.combo_name['values']=book_list
        self.combo_name.current(self.book_id-1)
        self.combo_name.place(x=180, y=45)

        self.member_name = StringVar()
        self.lbl_cpf = Label(self.bottomFrame, text='Member :', font='arial 15 bold', fg='white', bg='#fcc324')
        self.lbl_cpf.place(x=40, y=80)
        self.combo_member = ttk.Combobox(self.bottomFrame, textvariable=self.member_name)
        self.combo_member['values']=member_list
        self.combo_member.place(x=180, y=85)

        button = Button(self.bottomFrame,text='Lend Book',command=self.lendBook)
        button.place(x=220,y=120)

    def lendBook(self):
        book_name=self.book_name.get()
        member_name=self.member_name.get()

        if(book_name and member_name !=""):
            try:
                query="INSERT INTO 'borrows' (bbook.id, bmember_id) VALUES(?,?)"
                cur.execute(query,(book_name,member_name))
                con.commit()
                messagebox.showinfo("Success","Successfully added to database!", icon='info')
                cur.execute("UPDATE books SET book_status =? WHERE book_id=?", (1,self.book_id))
                con.commit()
            except:
                pass
        else:
            messagebox.showerror("Error","Fields cant be empty", icon='warning')


def main():
    root = tk.Tk()
    app = Main(root)
    root.title("LibMan")
    root.geometry("1350x750+350+200")
    root.iconbitmap('icons/closedBook.ico')
    root.mainloop()


if __name__ == '__main__':
    main()
