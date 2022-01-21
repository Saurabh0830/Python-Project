#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# Support module generated by PAGE version 4.13
# In conjunction with Tcl version 8.6
#    Jun 24, 2018 12:03:02 PM


import sys
from tkinter import messagebox
from main.customer import Customer_Home
from firebase import firebase as fb
from main.customer import Customer_Register

try:
    from Tkinter import *
except ImportError:
    from tkinter import *

try:
    import ttk
    py3 = False
except ImportError:
    import tkinter.ttk as ttk
    py3 = True

def Customer_Login():
    print('CustomerLogin_support.Customer_Login')
    sys.stdout.flush()

def Customer_Registration():
    print('CustomerLogin_support.Customer_Registration')
    sys.stdout.flush()

def init(top, gui, *args, **kwargs):
    global w, top_level, root
    w = gui
    top_level = top
    root = top

def destroy_window():
    # Function which closes the window.
    global top_level
    top_level.destroy()
    top_level = None

def Customer_Login():
    name = w.CustomerLogin_Username.get()
    from main.customer import CustomerChangePassword_support as c
    c.variable(name)
    from main.customer import Place_Order_support as o
    o.Id(name)
    from main.customer import ViewOrdered as v
    v.Hd(name)
    password = w.CustomerLogin_Password.get()
    fire = fb.FirebaseApplication("https://merchant-ca794.firebaseio.com/customer/login", None)
    s = fire.get("login", None)
    if name == "":
        messagebox.showerror("Customer_Login", "Enter the username")
    elif password == "":
        messagebox.showerror("Customer_Login", "Enter the password")
    else:
        if (name in s) and (s[name]["pass"] == password):
            destroy_window()
            Customer_Home.vp_start_gui()
        else:
            messagebox.showerror("Customer_Login", "Invalid username or password")

def Customer_Registration():
    destroy_window()
    Customer_Register.vp_start_gui()

if __name__ == '__main__':
    import CustomerLogin
    CustomerLogin.vp_start_gui()


