#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# GUI module generated by PAGE version 4.13
# In conjunction with Tcl version 8.6
#    Jun 24, 2018 12:03:50 PM

import sys

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

from main.customer import CustomerLogin_support

def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = Tk()
    top = Customer_Login (root)
    CustomerLogin_support.init(root, top)
    root.mainloop()

w = None
def create_Customer_Login(root, *args, **kwargs):
    '''Starting point when module is imported by another program.'''
    global w, w_win, rt
    rt = root
    w = Toplevel (root)
    top = Customer_Login (w)
    CustomerLogin_support.init(w, top, *args, **kwargs)
    return (w, top)

def destroy_Customer_Login():
    global w
    w.destroy()
    w = None


class Customer_Login:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85' 
        _ana2color = '#d9d9d9' # X11 color: 'gray85' 
        font10 = "-family {Segoe UI Black} -size 15 -weight bold "  \
            "-slant italic -underline 0 -overstrike 0"
        font11 = "-family {Segoe UI Black} -size 12 -weight bold "  \
            "-slant italic -underline 0 -overstrike 0"

        top.geometry("462x381+788+150")
        top.title("Customer_Login")
        top.configure(background="#d9d9d9")



        self.Frame1 = Frame(top)
        self.Frame1.place(relx=0.02, rely=0.03, relheight=0.96, relwidth=0.96)
        self.Frame1.configure(relief=GROOVE)
        self.Frame1.configure(borderwidth="10")
        self.Frame1.configure(relief=GROOVE)
        self.Frame1.configure(background="#c4632b")
        self.Frame1.configure(width=445)

        self.Label1 = Label(self.Frame1)
        self.Label1.place(relx=0.22, rely=0.11, height=36, width=262)
        self.Label1.configure(background="#c4632b")
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(font=font10)
        self.Label1.configure(foreground="#000000")
        self.Label1.configure(text='''Login/Registration''')
        self.Label1.configure(width=262)

        self.Label2 = Label(self.Frame1)
        self.Label2.place(relx=0.04, rely=0.33, height=26, width=162)
        self.Label2.configure(background="#c4632b")
        self.Label2.configure(disabledforeground="#a3a3a3")
        self.Label2.configure(font=font11)
        self.Label2.configure(foreground="#000000")
        self.Label2.configure(text='''Username :''')
        self.Label2.configure(width=162)

        self.Label2_1 = Label(self.Frame1)
        self.Label2_1.place(relx=0.04, rely=0.49, height=26, width=162)
        self.Label2_1.configure(activebackground="#f9f9f9")
        self.Label2_1.configure(activeforeground="black")
        self.Label2_1.configure(background="#c4632b")
        self.Label2_1.configure(disabledforeground="#a3a3a3")
        self.Label2_1.configure(font=font11)
        self.Label2_1.configure(foreground="#000000")
        self.Label2_1.configure(highlightbackground="#d9d9d9")
        self.Label2_1.configure(highlightcolor="black")
        self.Label2_1.configure(text='''Password :''')

        self.CustomerLogin_Username = Entry(self.Frame1)
        self.CustomerLogin_Username.place(relx=0.38, rely=0.33, height=34
                , relwidth=0.5)
        self.CustomerLogin_Username.configure(background="white")
        self.CustomerLogin_Username.configure(disabledforeground="#a3a3a3")
        self.CustomerLogin_Username.configure(font="TkFixedFont")
        self.CustomerLogin_Username.configure(foreground="#000000")
        self.CustomerLogin_Username.configure(insertbackground="black")
        self.CustomerLogin_Username.configure(width=224)

        self.CustomerLogin_Password = Entry(self.Frame1)
        self.CustomerLogin_Password.place(relx=0.38, rely=0.49, height=34
                , relwidth=0.5)
        self.CustomerLogin_Password.configure(background="white")
        self.CustomerLogin_Password.configure(disabledforeground="#a3a3a3")
        self.CustomerLogin_Password.configure(font="TkFixedFont")
        self.CustomerLogin_Password.configure(foreground="#000000")
        self.CustomerLogin_Password.configure(highlightbackground="#d9d9d9")
        self.CustomerLogin_Password.configure(highlightcolor="black")
        self.CustomerLogin_Password.configure(insertbackground="black")
        self.CustomerLogin_Password.configure(selectbackground="#c4c4c4")
        self.CustomerLogin_Password.configure(selectforeground="black")
        self.CustomerLogin_Password.configure(show="*")

        self.Button1 = Button(self.Frame1)
        self.Button1.place(relx=0.72, rely=0.63, height=33, width=76)
        self.Button1.configure(activebackground="#d9d9d9")
        self.Button1.configure(activeforeground="#000000")
        self.Button1.configure(background="#d9d9d9")
        self.Button1.configure(command=CustomerLogin_support.Customer_Login)
        self.Button1.configure(disabledforeground="#a3a3a3")
        self.Button1.configure(font=font11)
        self.Button1.configure(foreground="#000000")
        self.Button1.configure(highlightbackground="#d9d9d9")
        self.Button1.configure(highlightcolor="black")
        self.Button1.configure(pady="0")
        self.Button1.configure(text='''Login''')
        self.Button1.configure(width=76)

        self.Button1_3 = Button(self.Frame1)
        self.Button1_3.place(relx=0.36, rely=0.82, height=33, width=136)
        self.Button1_3.configure(activebackground="#d9d9d9")
        self.Button1_3.configure(activeforeground="#000000")
        self.Button1_3.configure(background="#d9d9d9")
        self.Button1_3.configure(command=CustomerLogin_support.Customer_Registration)
        self.Button1_3.configure(disabledforeground="#a3a3a3")
        self.Button1_3.configure(font=font11)
        self.Button1_3.configure(foreground="#000000")
        self.Button1_3.configure(highlightbackground="#d9d9d9")
        self.Button1_3.configure(highlightcolor="black")
        self.Button1_3.configure(pady="0")
        self.Button1_3.configure(text='''Registration''')
        self.Button1_3.configure(width=136)






if __name__ == '__main__':
    vp_start_gui()



