#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# GUI module generated by PAGE version 4.13
# In conjunction with Tcl version 8.6
#    Jun 03, 2018 10:58:03 PM

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

from main.com.nnk.stocker import stocker_support

def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = Tk()
    top = Stocker_Login (root)
    stocker_support.init(root, top)
    root.mainloop()

w = None
def create_Stocker_Login(root, *args, **kwargs):
    '''Starting point when module is imported by another program.'''
    global w, w_win, rt
    rt = root
    w = Toplevel(root)
    top = Stocker_Login(w)
    stocker_support.init(w, top, *args, **kwargs)
    return (w,top)

def destroy_Stocker_Login():
    global w
    w.destroy()
    w = None


class Stocker_Login:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85' 
        _ana2color = '#d9d9d9' # X11 color: 'gray85' 
        font10 = "-family {Segoe UI Black} -size 12 -weight bold "  \
            "-slant italic -underline 0 -overstrike 0"
        font11 = "-family {Segoe UI Black} -size 13 -weight bold "  \
            "-slant italic -underline 0 -overstrike 0"
        font9 = "-family {Segoe UI Black} -size 18 -weight bold -slant"  \
            " italic -underline 0 -overstrike 0"

        top.geometry("600x321+650+268")
        top.title("Stocker_Login")
        top.configure(background="#d9d9d9")
        top.configure(highlightbackground="#d9d9d9")
        top.configure(highlightcolor="black")



        self.Frame1 = Frame(top)
        self.Frame1.place(relx=0.02, rely=0.03, relheight=0.95, relwidth=0.98)
        self.Frame1.configure(relief=GROOVE)
        self.Frame1.configure(borderwidth="10")
        self.Frame1.configure(relief=GROOVE)
        self.Frame1.configure(background="#c4632b")
        self.Frame1.configure(highlightbackground="#d9d9d9")
        self.Frame1.configure(highlightcolor="black")
        self.Frame1.configure(width=585)

        self.Label1 = Label(self.Frame1)
        self.Label1.place(relx=0.26, rely=0.1, height=46, width=292)
        self.Label1.configure(activebackground="#f9f9f9")
        self.Label1.configure(activeforeground="black")
        self.Label1.configure(background="#c4632b")
        self.Label1.configure(borderwidth="0")
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(font=font9)
        self.Label1.configure(foreground="#000000")
        self.Label1.configure(highlightbackground="#d9d9d9")
        self.Label1.configure(highlightcolor="black")
        self.Label1.configure(text='''Stocker Login''')
        self.Label1.configure(width=292)

        self.Label2 = Label(self.Frame1)
        self.Label2.place(relx=0.07, rely=0.36, height=36, width=152)
        self.Label2.configure(activebackground="#f9f9f9")
        self.Label2.configure(activeforeground="black")
        self.Label2.configure(background="#c4632b")
        self.Label2.configure(disabledforeground="#a3a3a3")
        self.Label2.configure(font=font10)
        self.Label2.configure(foreground="#000000")
        self.Label2.configure(highlightbackground="#d9d9d9")
        self.Label2.configure(highlightcolor="black")
        self.Label2.configure(text='''Username''')
        self.Label2.configure(width=152)

        self.Label2_1 = Label(self.Frame1)
        self.Label2_1.place(relx=0.07, rely=0.52, height=36, width=152)
        self.Label2_1.configure(activebackground="#f9f9f9")
        self.Label2_1.configure(activeforeground="black")
        self.Label2_1.configure(background="#c4632b")
        self.Label2_1.configure(disabledforeground="#a3a3a3")
        self.Label2_1.configure(font=font10)
        self.Label2_1.configure(foreground="#000000")
        self.Label2_1.configure(highlightbackground="#d9d9d9")
        self.Label2_1.configure(highlightcolor="black")
        self.Label2_1.configure(text='''Password''')
        self.Label2_1.configure(width=152)

        self.stockerusername = Entry(self.Frame1)
        self.stockerusername.place(relx=0.32, rely=0.36, height=34
                , relwidth=0.45)
        self.stockerusername.configure(background="white")
        self.stockerusername.configure(disabledforeground="#a3a3a3")
        self.stockerusername.configure(font="TkFixedFont")
        self.stockerusername.configure(foreground="#000000")
        self.stockerusername.configure(highlightbackground="#d9d9d9")
        self.stockerusername.configure(highlightcolor="black")
        self.stockerusername.configure(insertbackground="black")
        self.stockerusername.configure(selectbackground="#c4c4c4")
        self.stockerusername.configure(selectforeground="black")

        self.stockerpassword = Entry(self.Frame1)
        self.stockerpassword.place(relx=0.32, rely=0.52, height=34
                , relwidth=0.45)
        self.stockerpassword.configure(background="white")
        self.stockerpassword.configure(disabledforeground="#a3a3a3")
        self.stockerpassword.configure(font="TkFixedFont")
        self.stockerpassword.configure(foreground="#000000")
        self.stockerpassword.configure(highlightbackground="#d9d9d9")
        self.stockerpassword.configure(highlightcolor="black")
        self.stockerpassword.configure(insertbackground="black")
        self.stockerpassword.configure(selectbackground="#c4c4c4")
        self.stockerpassword.configure(selectforeground="black")
        self.stockerpassword.configure(show="*")

        self.Button1 = Button(self.Frame1)
        self.Button1.place(relx=0.36, rely=0.72, height=43, width=136)
        self.Button1.configure(activebackground="#d9d9d9")
        self.Button1.configure(activeforeground="#000000")
        self.Button1.configure(background="#d9d9d9")
        self.Button1.configure(borderwidth="0")
        self.Button1.configure(command=stocker_support.validateStockerLogin)
        self.Button1.configure(disabledforeground="#a3a3a3")
        self.Button1.configure(font=font11)
        self.Button1.configure(foreground="#000000")
        self.Button1.configure(highlightbackground="#d9d9d9")
        self.Button1.configure(highlightcolor="black")
        self.Button1.configure(pady="0")
        self.Button1.configure(text='''Login''')
        self.Button1.configure(width=136)






if __name__ == '__main__':
    vp_start_gui()



