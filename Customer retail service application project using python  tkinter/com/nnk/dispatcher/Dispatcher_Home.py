#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# GUI module generated by PAGE version 4.13
# In conjunction with Tcl version 8.6
#    Jun 24, 2018 10:11:23 AM

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

from main.com.nnk.dispatcher import Dispatcher_Home_support

def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = Tk()
    top = Dispatcher_Home (root)
    Dispatcher_Home_support.init(root, top)
    root.mainloop()

w = None
def create_Dispatcher_Home(root, *args, **kwargs):
    '''Starting point when module is imported by another program.'''
    global w, w_win, rt
    rt = root
    w = Toplevel (root)
    top = Dispatcher_Home (w)
    Dispatcher_Home_support.init(w, top, *args, **kwargs)
    return (w, top)

def destroy_Dispatcher_Home():
    global w
    w.destroy()
    w = None


class Dispatcher_Home:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85' 
        _ana2color = '#d9d9d9' # X11 color: 'gray85' 
        font10 = "-family {Segoe UI Black} -size 18 -weight bold "  \
            "-slant italic -underline 0 -overstrike 0"
        font11 = "-family {Segoe UI Black} -size 12 -weight bold "  \
            "-slant italic -underline 0 -overstrike 0"

        top.geometry("404x540+650+220")
        top.title("Dispatcher_Home")
        top.configure(background="#d9d9d9")
        top.configure(highlightbackground="#d9d9d9")
        top.configure(highlightcolor="black")



        self.Frame1 = Frame(top)
        self.Frame1.place(relx=0.02, rely=0.02, relheight=0.97, relwidth=0.95)
        self.Frame1.configure(relief=GROOVE)
        self.Frame1.configure(borderwidth="10")
        self.Frame1.configure(relief=GROOVE)
        self.Frame1.configure(background="#c4632b")
        self.Frame1.configure(highlightbackground="#d9d9d9")
        self.Frame1.configure(highlightcolor="black")
        self.Frame1.configure(width=385)

        self.Label1 = Label(self.Frame1)
        self.Label1.place(relx=0.13, rely=0.06, height=46, width=282)
        self.Label1.configure(activebackground="#f9f9f9")
        self.Label1.configure(activeforeground="black")
        self.Label1.configure(background="#c4632b")
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(font=font10)
        self.Label1.configure(foreground="#000000")
        self.Label1.configure(highlightbackground="#d9d9d9")
        self.Label1.configure(highlightcolor="black")
        self.Label1.configure(text='''Dispatcher Home''')

        self.Button1_3 = Button(self.Frame1)
        self.Button1_3.place(relx=0.7, rely=0.88, height=43, width=86)
        self.Button1_3.configure(activebackground="#d9d9d9")
        self.Button1_3.configure(activeforeground="#000000")
        self.Button1_3.configure(background="#d9d9d9")
        self.Button1_3.configure(command=Dispatcher_Home_support.DispatcherHome_Logout)
        self.Button1_3.configure(disabledforeground="#a3a3a3")
        self.Button1_3.configure(font=font11)
        self.Button1_3.configure(foreground="#000000")
        self.Button1_3.configure(highlightbackground="#d9d9d9")
        self.Button1_3.configure(highlightcolor="black")
        self.Button1_3.configure(pady="0")
        self.Button1_3.configure(text='''Logout''')
        self.Button1_3.configure(width=86)

        self.Button1_1 = Button(self.Frame1)
        self.Button1_1.place(relx=0.26, rely=0.25, height=43, width=196)
        self.Button1_1.configure(activebackground="#d9d9d9")
        self.Button1_1.configure(activeforeground="#000000")
        self.Button1_1.configure(background="#d9d9d9")
        self.Button1_1.configure(command=Dispatcher_Home_support.DispatcherHome_ChangePassword)
        self.Button1_1.configure(disabledforeground="#a3a3a3")
        self.Button1_1.configure(font=font11)
        self.Button1_1.configure(foreground="#000000")
        self.Button1_1.configure(highlightbackground="#d9d9d9")
        self.Button1_1.configure(highlightcolor="black")
        self.Button1_1.configure(pady="0")
        self.Button1_1.configure(text='''Change Password''')
        self.Button1_1.configure(width=196)

        self.Button1_1 = Button(self.Frame1)
        self.Button1_1.place(relx=0.26, rely=0.4, height=43, width=196)
        self.Button1_1.configure(activebackground="#d9d9d9")
        self.Button1_1.configure(activeforeground="#000000")
        self.Button1_1.configure(background="#d9d9d9")
        self.Button1_1.configure(command=Dispatcher_Home_support.DispatcherHome_ViewOrder)
        self.Button1_1.configure(disabledforeground="#a3a3a3")
        self.Button1_1.configure(font=font11)
        self.Button1_1.configure(foreground="#000000")
        self.Button1_1.configure(highlightbackground="#d9d9d9")
        self.Button1_1.configure(highlightcolor="black")
        self.Button1_1.configure(pady="0")
        self.Button1_1.configure(text='''View Order's''')

        self.Button1_2 = Button(self.Frame1)
        self.Button1_2.place(relx=0.26, rely=0.55, height=43, width=196)
        self.Button1_2.configure(activebackground="#d9d9d9")
        self.Button1_2.configure(activeforeground="#000000")
        self.Button1_2.configure(background="#d9d9d9")
        self.Button1_2.configure(command=Dispatcher_Home_support.DispatcherHome_SendOrder)
        self.Button1_2.configure(disabledforeground="#a3a3a3")
        self.Button1_2.configure(font=font11)
        self.Button1_2.configure(foreground="#000000")
        self.Button1_2.configure(highlightbackground="#d9d9d9")
        self.Button1_2.configure(highlightcolor="black")
        self.Button1_2.configure(pady="0")
        self.Button1_2.configure(text='''Send Order''')

        self.Button1_2 = Button(self.Frame1)
        self.Button1_2.place(relx=0.26, rely=0.7, height=43, width=196)
        self.Button1_2.configure(activebackground="#d9d9d9")
        self.Button1_2.configure(activeforeground="#000000")
        self.Button1_2.configure(background="#d9d9d9")
        self.Button1_2.configure(command=Dispatcher_Home_support.DispatcherHome_ViewSendOrder)
        self.Button1_2.configure(disabledforeground="#a3a3a3")
        self.Button1_2.configure(font=font11)
        self.Button1_2.configure(foreground="#000000")
        self.Button1_2.configure(highlightbackground="#d9d9d9")
        self.Button1_2.configure(highlightcolor="black")
        self.Button1_2.configure(pady="0")
        self.Button1_2.configure(text='''View Send Order's''')






if __name__ == '__main__':
    vp_start_gui()



