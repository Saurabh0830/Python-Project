#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# GUI module generated by PAGE version 4.13
# In conjunction with Tcl version 8.6
#    Jun 25, 2018 04:56:29 PM

import sys
from firebase import firebase as fb

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

from main.customer import Place_Order_support

def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = Tk()
    top = Place_Order (root)
    Place_Order_support.init(root, top)
    root.mainloop()

w = None
def create_Place_Order(root, *args, **kwargs):
    '''Starting point when module is imported by another program.'''
    global w, w_win, rt
    rt = root
    w = Toplevel (root)
    top = Place_Order (w)
    Place_Order_support.init(w, top, *args, **kwargs)
    return (w, top)

def destroy_Place_Order():
    global w
    w.destroy()
    w = None


class Place_Order:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85' 
        _ana2color = '#d9d9d9' # X11 color: 'gray85' 
        font10 = "-family {Segoe UI Black} -size 16 -weight bold "  \
            "-slant italic -underline 0 -overstrike 0"
        font9 = "-family {Segoe UI Black} -size 12 -weight bold -slant"  \
            " italic -underline 0 -overstrike 0"

        top.geometry("489x647+650+150")
        top.title("Place_Order")
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
        self.Frame1.configure(width=465)

        self.Label1 = Label(self.Frame1)
        self.Label1.place(relx=0.28, rely=0.05, height=36, width=192)
        self.Label1.configure(activebackground="#f9f9f9")
        self.Label1.configure(activeforeground="black")
        self.Label1.configure(background="#c4632b")
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(font=font10)
        self.Label1.configure(foreground="#000000")
        self.Label1.configure(highlightbackground="#d9d9d9")
        self.Label1.configure(highlightcolor="black")
        self.Label1.configure(text='''Place Order''')

        self.Label2 = Label(self.Frame1)
        self.Label2.place(relx=0.02, rely=0.16, height=26, width=162)
        self.Label2.configure(activebackground="#f9f9f9")
        self.Label2.configure(activeforeground="black")
        self.Label2.configure(background="#c4632b")
        self.Label2.configure(disabledforeground="#a3a3a3")
        self.Label2.configure(font=font9)
        self.Label2.configure(foreground="#000000")
        self.Label2.configure(highlightbackground="#d9d9d9")
        self.Label2.configure(highlightcolor="black")
        self.Label2.configure(text='''Product Id :''')

        self.PlaceOrder_Id = Entry(self.Frame1)
        self.PlaceOrder_Id.place(relx=0.34, rely=0.16,height=34, relwidth=0.52)
        self.PlaceOrder_Id.configure(background="white")
        self.PlaceOrder_Id.configure(disabledforeground="#a3a3a3")
        self.PlaceOrder_Id.configure(font="TkFixedFont")
        self.PlaceOrder_Id.configure(foreground="#000000")
        self.PlaceOrder_Id.configure(highlightbackground="#d9d9d9")
        self.PlaceOrder_Id.configure(highlightcolor="black")
        self.PlaceOrder_Id.configure(insertbackground="black")
        self.PlaceOrder_Id.configure(selectbackground="#c4c4c4")
        self.PlaceOrder_Id.configure(selectforeground="black")

        self.Button1 = Button(self.Frame1)
        self.Button1.place(relx=0.41, rely=0.26, height=33, width=66)
        self.Button1.configure(activebackground="#d9d9d9")
        self.Button1.configure(activeforeground="#000000")
        self.Button1.configure(background="#d9d9d9")
        self.Button1.configure(command=self.Display)
        self.Button1.configure(disabledforeground="#a3a3a3")
        self.Button1.configure(font=font9)
        self.Button1.configure(foreground="#000000")
        self.Button1.configure(highlightbackground="#d9d9d9")
        self.Button1.configure(highlightcolor="black")
        self.Button1.configure(pady="0")
        self.Button1.configure(text='''Show''')

        self.PlaceOrder_NSP = Frame(self.Frame1)
        self.PlaceOrder_NSP.place(relx=0.04, rely=0.34, relheight=0.36
                , relwidth=0.91)
        self.PlaceOrder_NSP.configure(relief=GROOVE)
        self.PlaceOrder_NSP.configure(borderwidth="2")
        self.PlaceOrder_NSP.configure(relief=GROOVE)
        self.PlaceOrder_NSP.configure(background="#c4632b")
        self.PlaceOrder_NSP.configure(highlightbackground="#d9d9d9")
        self.PlaceOrder_NSP.configure(highlightcolor="black")
        self.PlaceOrder_NSP.configure(width=425)

        self.Lable2_1 = Label(self.PlaceOrder_NSP)
        self.Lable2_1.place(relx=0.05, rely=0.14, height=26, width=112)
        self.Lable2_1.configure(activebackground="#f9f9f9")
        self.Lable2_1.configure(activeforeground="black")
        self.Lable2_1.configure(background="#c4632b")
        self.Lable2_1.configure(disabledforeground="#a3a3a3")
        self.Lable2_1.configure(font=font9)
        self.Lable2_1.configure(foreground="#000000")
        self.Lable2_1.configure(highlightbackground="#d9d9d9")
        self.Lable2_1.configure(highlightcolor="black")
        self.Lable2_1.configure(text='''Name :''')

        self.Label2_2 = Label(self.PlaceOrder_NSP)
        self.Label2_2.place(relx=0.05, rely=0.41, height=26, width=112)
        self.Label2_2.configure(activebackground="#f9f9f9")
        self.Label2_2.configure(activeforeground="black")
        self.Label2_2.configure(background="#c4632b")
        self.Label2_2.configure(disabledforeground="#a3a3a3")
        self.Label2_2.configure(font=font9)
        self.Label2_2.configure(foreground="#000000")
        self.Label2_2.configure(highlightbackground="#d9d9d9")
        self.Label2_2.configure(highlightcolor="black")
        self.Label2_2.configure(text='''Stock :''')

        self.Label2_3 = Label(self.PlaceOrder_NSP)
        self.Label2_3.place(relx=0.02, rely=0.68, height=26, width=122)
        self.Label2_3.configure(activebackground="#f9f9f9")
        self.Label2_3.configure(activeforeground="black")
        self.Label2_3.configure(background="#c4632b")
        self.Label2_3.configure(disabledforeground="#a3a3a3")
        self.Label2_3.configure(font=font9)
        self.Label2_3.configure(foreground="#000000")
        self.Label2_3.configure(highlightbackground="#d9d9d9")
        self.Label2_3.configure(highlightcolor="black")
        self.Label2_3.configure(text='''Price :''')

        self.PlaceOrder_Name = Label(self.PlaceOrder_NSP)
        self.PlaceOrder_Name.place(relx=0.28, rely=0.14, height=26, width=112)
        self.PlaceOrder_Name.configure(activebackground="#f9f9f9")
        self.PlaceOrder_Name.configure(activeforeground="black")
        self.PlaceOrder_Name.configure(background="#c4632b")
        self.PlaceOrder_Name.configure(disabledforeground="#a3a3a3")
        self.PlaceOrder_Name.configure(font=font9)
        self.PlaceOrder_Name.configure(foreground="#000000")
        self.PlaceOrder_Name.configure(highlightbackground="#d9d9d9")
        self.PlaceOrder_Name.configure(highlightcolor="black")
        self.PlaceOrder_Name.configure(text='''..............''')

        self.PlaceOrder_Stock = Label(self.PlaceOrder_NSP)
        self.PlaceOrder_Stock.place(relx=0.28, rely=0.41, height=26, width=112)
        self.PlaceOrder_Stock.configure(activebackground="#f9f9f9")
        self.PlaceOrder_Stock.configure(activeforeground="black")
        self.PlaceOrder_Stock.configure(background="#c4632b")
        self.PlaceOrder_Stock.configure(disabledforeground="#a3a3a3")
        self.PlaceOrder_Stock.configure(font=font9)
        self.PlaceOrder_Stock.configure(foreground="#000000")
        self.PlaceOrder_Stock.configure(highlightbackground="#d9d9d9")
        self.PlaceOrder_Stock.configure(highlightcolor="black")
        self.PlaceOrder_Stock.configure(text='''..............''')

        self.PlaceOrder_Price = Label(self.PlaceOrder_NSP)
        self.PlaceOrder_Price.place(relx=0.28, rely=0.68, height=26, width=112)
        self.PlaceOrder_Price.configure(activebackground="#f9f9f9")
        self.PlaceOrder_Price.configure(activeforeground="black")
        self.PlaceOrder_Price.configure(background="#c4632b")
        self.PlaceOrder_Price.configure(disabledforeground="#a3a3a3")
        self.PlaceOrder_Price.configure(font=font9)
        self.PlaceOrder_Price.configure(foreground="#000000")
        self.PlaceOrder_Price.configure(highlightbackground="#d9d9d9")
        self.PlaceOrder_Price.configure(highlightcolor="black")
        self.PlaceOrder_Price.configure(text='''..............''')

        self.Label2_4 = Label(self.Frame1)
        self.Label2_4.place(relx=0.04, rely=0.74, height=26, width=132)
        self.Label2_4.configure(activebackground="#f9f9f9")
        self.Label2_4.configure(activeforeground="black")
        self.Label2_4.configure(background="#c4632b")
        self.Label2_4.configure(disabledforeground="#a3a3a3")
        self.Label2_4.configure(font=font9)
        self.Label2_4.configure(foreground="#000000")
        self.Label2_4.configure(highlightbackground="#d9d9d9")
        self.Label2_4.configure(highlightcolor="black")
        self.Label2_4.configure(text='''Quantity :''')


        self.PlaceOrder_Quantity = Entry(self.Frame1)
        self.PlaceOrder_Quantity.place(relx=0.32, rely=0.74, height=34
                , relwidth=0.52)
        self.PlaceOrder_Quantity.configure(background="white")
        self.PlaceOrder_Quantity.configure(disabledforeground="#a3a3a3")
        self.PlaceOrder_Quantity.configure(font="TkFixedFont")
        self.PlaceOrder_Quantity.configure(foreground="#000000")
        self.PlaceOrder_Quantity.configure(highlightbackground="#d9d9d9")
        self.PlaceOrder_Quantity.configure(highlightcolor="black")
        self.PlaceOrder_Quantity.configure(insertbackground="black")
        self.PlaceOrder_Quantity.configure(selectbackground="#c4c4c4")
        self.PlaceOrder_Quantity.configure(selectforeground="black")

        self.Button1_8 = Button(self.Frame1)
        self.Button1_8.place(relx=0.43, rely=0.87, height=33, width=66)
        self.Button1_8.configure(activebackground="#d9d9d9")
        self.Button1_8.configure(activeforeground="#000000")
        self.Button1_8.configure(background="#d9d9d9")
        self.Button1_8.configure(command=Place_Order_support.PlaceOrder_Save)
        self.Button1_8.configure(disabledforeground="#a3a3a3")
        self.Button1_8.configure(font=font9)
        self.Button1_8.configure(foreground="#000000")
        self.Button1_8.configure(highlightbackground="#d9d9d9")
        self.Button1_8.configure(highlightcolor="black")
        self.Button1_8.configure(pady="0")
        self.Button1_8.configure(text='''Save''')

        self.Button1_9 = Button(self.Frame1)
        self.Button1_9.place(relx=0.04, rely=0.03, height=33, width=66)
        self.Button1_9.configure(activebackground="#d9d9d9")
        self.Button1_9.configure(activeforeground="#000000")
        self.Button1_9.configure(background="#d9d9d9")
        self.Button1_9.configure(command=Place_Order_support.PlaceOrder_Home)
        self.Button1_9.configure(disabledforeground="#a3a3a3")
        self.Button1_9.configure(font=font9)
        self.Button1_9.configure(foreground="#000000")
        self.Button1_9.configure(highlightbackground="#d9d9d9")
        self.Button1_9.configure(highlightcolor="black")
        self.Button1_9.configure(pady="0")
        self.Button1_9.configure(text='''Home''')


    def Display(self, top=None):
        idno = self.PlaceOrder_Id.get()
        fire = fb.FirebaseApplication("https://merchant-ca794.firebaseio.com/product", None)
        result = fire.get("product", idno)
        self.PlaceOrder_Name.configure(text=result["pname"])
        self.PlaceOrder_Price.configure(text=result["price"])
        self.PlaceOrder_Stock.configure(text=result["quantity"])


if __name__ == '__main__':
    vp_start_gui()


