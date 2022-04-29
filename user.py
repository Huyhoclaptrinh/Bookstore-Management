import tkinter as tk
from tkinter import ttk, messagebox
import mysql.connector
import os
import sqlite3
from tkinter import *

                                             # USER WINDOW
def user_win():
    user = Tk()
    user.geometry("300x300")
    user.title("User")
    bt_user_signin = Button(user, text="Sign in", width=20, command=user_login_win).pack(side=LEFT)
    bt_user_signup = Button(user, text="Sign up", width=20, command=user_register_win).pack(side=RIGHT)


def login_sucess():
    global screen3
    screen3 = Tk()
    screen3.title("Success")
    screen3.geometry("150x100")
    Label(screen3, text="Login Sucess").pack()
    Button(screen3, text="OK", command=user_menu_win).pack()


def password_not_recognised():
    global screen4
    screen4 = Tk()
    screen4.title("Success")
    screen4.geometry("150x100")
    Label(screen4, text="Password Error").pack()
    Button(screen4, text="OK").pack()


def user_not_found():
    global screen5
    screen5 = Tk()
    screen5.title("Success")
    screen5.geometry("150x100")
    Label(screen5, text="User Not Found").pack()
    Button(screen5, text="OK").pack()


def user_register():
    print("working")

    
    username_info = username.get()
    password_info = password.get()
    email_info = mail.get()
    address_info = address.get()
    
    
    file = open(username_info, "w")
    file.write(username_info + "\n")
    file.write(password_info + "\n")
    file.write(email_info +"\n")
    file.write(address_info + "\n")
    file.close()

    Label(screen1, text="Registration Sucess", fg="green", font=("calibri", 11)).pack()


def user_login_verify():
    username1 = username_verify.get()
    password1 = password_verify.get()

    list_of_files = os.listdir()
    if username1 in list_of_files:
        file1 = open(username1, "r")
        verify = file1.read().splitlines()
        if password1 in verify:
            login_sucess()
        else:
            password_not_recognised()

    else:
        user_not_found()

                                               # REGISTER WINDOW
def user_register_win():
    global screen1
    screen1 = Tk()
    screen1.title("Register")
    screen1.geometry("800x500")

    global username
    global password
    global mail
    global address
    global username_entry
    global password_entry
    global mail_entry
    global address_entry
    username = StringVar()
    password = StringVar()
    mail = StringVar()
    address = StringVar()

    Label(screen1, text="Please enter details below").pack()
    Label(screen1, text="").pack()

    Label(screen1, text="Username * ").pack()
    username_entry = Entry(screen1, textvariable=username)
    username_entry.pack()

    Label(screen1, text="Password * ").pack()
    password_entry = Entry(screen1, textvariable=password, show='*')
    password_entry.pack()

    Label(screen1, text="email").pack()
    mail_entry = Entry(screen1, textvariable=mail)
    mail_entry.pack()

    Label(screen1, text="address").pack()
    address_entry = Entry(screen1, textvariable=address)
    address_entry.pack()

    Button(screen1, text="Register", width=10, height=1, command=user_register).pack()

                                           # USER LOGIN WINDOW

def user_login_win():
    global screen2
    screen2 = Tk()
    screen2.title("Login")
    screen2.geometry("300x250")
    Label(screen2, text="Please enter details below to login").pack()
    Label(screen2, text="").pack()

    global username_verify
    global password_verify

    username_verify = StringVar()
    password_verify = StringVar()

    global username_entry1
    global password_entry1

    Label(screen2, text="Username * ").pack()
    username_entry1 = Entry(screen2, textvariable=username_verify)
    username_entry1.pack()
    Label(screen2, text="").pack()
    Label(screen2, text="Password * ").pack()
    password_entry1 = Entry(screen2, textvariable=password_verify, show='*')
    password_entry1.pack()
    Label(screen2, text="").pack()
    Button(screen2, text="Login", width=10, height=1, command=user_login_verify).pack()

                                            # USER MENU WINDOW
def user_menu_win():
    user_menu = Tk()
    user_menu.geometry("300x300")
    user_menu.title("Menu")

    bt_user_detail = Button(user_menu, text="User", width=10, height=3, command=user_detail_win).place(x=20, y=0)
    bt_display_book = Button(user_menu, text="Display book", width=10, height=3, command=display_book_win).place(x=20,
                                                                                                                 y=50)
    bt_search = Button(user_menu, text="Search", width=10, height=3, command=search_win).place(x=20, y=100)


                                               # USER DETAIL WINDOW

def user_detail_win():
    user_detail = Tk()
    user_detail.title("User Detail")
    user_detail.geometry("300x300")
    
    name_user = Label(user_detail, text="Name: ").pack()
    name_user_entry = Entry(user_detail, textvariable = username).pack()
    
    email_user = Label(user_detail, text="Email: ").pack()
    email_user_entry = Entry(user_detail, textvariable=mail).pack()
    
    address_user = Label(user_detail, text="Address: ").pack()
    address_user_entry = Entry(user_detail, textvariable = address).pack()

                                            # USER DISPLAY BOOK WINDOW

def display_book_win():
    display_book = Tk()
    display_book.title("Display Book")
    display_book.geometry("300x300")

    def show():
        mysqldb = mysql.connector.connect(host="Localhost", user="root", password="12345678910",database="bookstore")
        mycursor = mysqldb.cursor()
        mycursor.execute("SELECT id,book_name,author_name,genre,price FROM books")
        records = mycursor.fetchall()
        print(records)
        for i, (id1,book_name1,author_name1, genre1,price1) in enumerate(records,start=1):
              listBox.insert("", "end", values=(id1,book_name1,author_name1, genre1,price1))
              mysqldb.close()
    
    cols = ('id', 'book_name', 'author_name','genre','price')
    listBox = ttk.Treeview(display_book, columns=cols, show='headings' )
    
    for col in cols:
       listBox.heading(col, text=col)
       listBox.grid(row=1, column=0, columnspan=2)
       listBox.place(x=10, y=200)
    
    show()                                        
    
                                              # SEARCH WINDOW

def search_win():
    search = Tk()
    search.title("Search")
    search.geometry("300x300")

    def show():
        mysqldb = mysql.connector.connect(host="Localhost", user="root", password="12345678910", database="bookstore")
        mycursor = mysqldb.cursor()
        id_get = id_entry.get()
        mycursor.execute("SELECT id,book_name,author_name,genre,price FROM books where id = '" + id_get + "'")
        records = mycursor.fetchall()
        print(records)
        for i, (id1,book_name1,author_name1, genre1,price1) in enumerate(records,start=1):
           listBox.insert("", "end", values=(id1,book_name1,author_name1, genre1,price1))
           mysqldb.close()
    
 
    
    Label(search, text="Student ID").place(x=10, y=10)
    Button(search, text="Search", command=show ,height = 1, width = 13).place(x=140, y=40)
    #Label(root, text="Course").place(x=10, y=80)
    #Label(root, text="Fee").place(x=10, y=120)
    
    id_entry = Entry(search)
    id_entry.place(x=140, y=10)
    
    
    cols = ('id', 'book_name', 'author_name','genre','price')
    listBox = ttk.Treeview(search, columns=cols, show='headings' )
    
    for col in cols:
       listBox.heading(col, text=col)
       listBox.grid(row=1, column=0, columnspan=2)
       listBox.place(x=10, y=200)