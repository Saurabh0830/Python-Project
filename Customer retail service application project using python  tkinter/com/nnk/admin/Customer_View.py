#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# GUI module generated by PAGE version 4.13
# In conjunction with Tcl version 8.6
#    Jun 27, 2018 02:35:54 PM

import sys
from tkinter import messagebox
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

from main.com.nnk.admin import Customer_View_support

def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = Tk()
    top = Customer_View (root)
    Customer_View_support.init(root, top)
    root.mainloop()

w = None
def create_Customer_View(root, *args, **kwargs):
    '''Starting point when module is imported by another program.'''
    global w, w_win, rt
    rt = root
    w = Toplevel (root)
    top = Customer_View (w)
    Customer_View_support.init(w, top, *args, **kwargs)
    return (w, top)

def destroy_Customer_View():
    global w
    w.destroy()
    w = None


class Customer_View:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85' 
        _ana2color = '#d9d9d9' # X11 color: 'gray85' 
        font9 = "-family {Segoe UI Black} -size 12 -weight bold -slant"  \
            " italic -underline 0 -overstrike 0"

        top.geometry("625x764+646+137")
        top.title("Customer_View")
        top.configure(background="#d9d9d9")
        top.configure(highlightbackground="#d9d9d9")
        top.configure(highlightcolor="black")



        self.CustomerView = Frame(top)
        self.CustomerView.place(relx=0.02, rely=0.09, relheight=0.9
                , relwidth=0.97)
        self.CustomerView.configure(relief=GROOVE)
        self.CustomerView.configure(borderwidth="10")
        self.CustomerView.configure(relief=GROOVE)
        self.CustomerView.configure(background="#c4632b")
        self.CustomerView.configure(highlightbackground="#d9d9d9")
        self.CustomerView.configure(highlightcolor="black")
        self.CustomerView.configure(width=605)
        self.listofCustomer()

        self.Frame2 = Frame(top)
        self.Frame2.place(relx=0.02, rely=0.01, relheight=0.1, relwidth=0.97)
        self.Frame2.configure(relief=GROOVE)
        self.Frame2.configure(borderwidth="10")
        self.Frame2.configure(relief=GROOVE)
        self.Frame2.configure(background="#c4632b")
        self.Frame2.configure(highlightbackground="#d9d9d9")
        self.Frame2.configure(highlightcolor="black")
        self.Frame2.configure(width=605)

        self.Label1 = Label(self.Frame2)
        self.Label1.place(relx=0.05, rely=0.4, height=26, width=72)
        self.Label1.configure(activebackground="#f9f9f9")
        self.Label1.configure(activeforeground="black")
        self.Label1.configure(background="#c4632b")
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(font=font9)
        self.Label1.configure(foreground="#000000")
        self.Label1.configure(highlightbackground="#d9d9d9")
        self.Label1.configure(highlightcolor="black")
        self.Label1.configure(text='''Sr. No''')

        self.Label1_1 = Label(self.Frame2)
        self.Label1_1.place(relx=0.26, rely=0.4, height=26, width=102)
        self.Label1_1.configure(activebackground="#f9f9f9")
        self.Label1_1.configure(activeforeground="black")
        self.Label1_1.configure(background="#c4632b")
        self.Label1_1.configure(disabledforeground="#a3a3a3")
        self.Label1_1.configure(font=font9)
        self.Label1_1.configure(foreground="#000000")
        self.Label1_1.configure(highlightbackground="#d9d9d9")
        self.Label1_1.configure(highlightcolor="black")
        self.Label1_1.configure(text='''Address''')

        self.Label1_2 = Label(self.Frame2)
        self.Label1_2.place(relx=0.51, rely=0.4, height=26, width=122)
        self.Label1_2.configure(activebackground="#f9f9f9")
        self.Label1_2.configure(activeforeground="black")
        self.Label1_2.configure(background="#c4632b")
        self.Label1_2.configure(disabledforeground="#a3a3a3")
        self.Label1_2.configure(font=font9)
        self.Label1_2.configure(foreground="#000000")
        self.Label1_2.configure(highlightbackground="#d9d9d9")
        self.Label1_2.configure(highlightcolor="black")
        self.Label1_2.configure(text='''Contact No''')

        self.Label1_3 = Label(self.Frame2)
        self.Label1_3.place(relx=0.76, rely=0.4, height=26, width=102)
        self.Label1_3.configure(activebackground="#f9f9f9")
        self.Label1_3.configure(activeforeground="black")
        self.Label1_3.configure(background="#c4632b")
        self.Label1_3.configure(disabledforeground="#a3a3a3")
        self.Label1_3.configure(font=font9)
        self.Label1_3.configure(foreground="#000000")
        self.Label1_3.configure(highlightbackground="#d9d9d9")
        self.Label1_3.configure(highlightcolor="black")
        self.Label1_3.configure(text='''Name''')

    font9 = "-family {Segoe UI Black} -size 12 -weight bold -slant" \
            " italic -underline 0 -overstrike 0"

    def listofCustomer(self):
        from firebase import firebase as fb
        fire = fb.FirebaseApplication("https://merchant-ca794.firebaseio.com/customer/login", None)
        result = fire.get("login", None)
        if result == None:
            messagebox.showinfo("Details", "No login Available")
        else:
            no_of_rows = len(result.keys())
            rows = []
            # for i in range(no_of_rows):
            counter = 0
            for i in result:
                cols = []
                l = Label(self.CustomerView, w, width=12)
                l.configure(font=Customer_View.font9)
                l.grid(row=counter, column=0, sticky=NSEW)
                l.configure(borderwidth="5")
                l.configure(background="#c4632b")
                l.configure(text=i)
                dt = result[i].values()
                val = []
                for x in dt:
                    val.append(x)
                for inner in range(1, 4):
                    l1 = Label(self.CustomerView, width=13)
                    l1.configure(font=Customer_View.font9)
                    l1.grid(row=counter, column=inner, sticky=NSEW)
                    l1.configure(borderwidth="5")
                    l1.configure(background="#c4632b")
                    l1.configure(text=val[inner - 1])
                    cols.append(l1)
                counter += 1
            rows.append(l)






if __name__ == '__main__':
    vp_start_gui()



