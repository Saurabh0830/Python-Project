#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# Support module generated by PAGE version 4.13
# In conjunction with Tcl version 8.6
#    Jun 24, 2018 08:40:36 PM


import sys
from firebase import firebase as fb
from tkinter import messagebox
from main.customer import Customer_Home

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

def PlaceOrder_Home():
    print('Place_Order_support.PlaceOrder_Home')
    sys.stdout.flush()

def PlaceOrder_Save():
    print('Place_Order_support.PlaceOrder_Save')
    sys.stdout.flush()

def PlaceOrder_Show():
    print('Place_Order_support.PlaceOrder_Show')
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

def PlaceOrder_Home():
    destroy_window()
    Customer_Home.vp_start_gui()

def Order_Id():
    fire = fb.FirebaseApplication("https://merchant-ca794.firebaseio.com/employee/dispatcher/orderno", None)
    result = fire.get("orderno", None)
    if result == None:
        pass
        return "1"
    else:
        for x in result:
            pass
        i = int(x)
        i += 1
        return str(i)


def Registration_Id():
    fire = fb.FirebaseApplication("https://merchant-ca794.firebaseio.com/customer/order", None)
    result = fire.get("order", d)
    if result == None:
        pass
        return "101"
    else:
        for x in result:
            pass
        idno = int(x)
        idno += 1
        return str(idno)

def Id(g):
    global d
    d = g



def PlaceOrder_Save():
    pno = w.PlaceOrder_Id.get()
    quantity = w.PlaceOrder_Quantity.get()
    fire = fb.FirebaseApplication("https://merchant-ca794.firebaseio.com/product", None)
    result = fire.get("product", None)
    if pno == "":
        messagebox.showerror("Place Order", "Product number is empty")
    elif quantity == "":
        messagebox.showerror("Place Order", "Quantity is empty")
    else:
        if pno in result:
            n = result[pno]["pname"]
            q = result[pno]["quantity"]
            t = result[pno]["price"]
            s = result[pno]["pno"]
            total = float(t*int(quantity))
            r = q-int(quantity)
            id = Registration_Id()
            m = Order_Id()
            if r >= 0:
                fire1 = fb.FirebaseApplication("https://merchant-ca794.firebaseio.com/customer/order/d", None)
                fire1.put(d, id, {"name": n, "price": t, "quantity": int(quantity), "total": total, "pno": s})
                fire.put("product", pno, {"pno": s, "pname": n, "price": t, "quantity": r})
                fire2 = fb.FirebaseApplication("https://merchant-ca794.firebaseio.com/employee/dispatcher/orderno", None)
                fire2.put("orderno", m, {"name": n, "price": t, "quantity": int(quantity), "total": total, "pno": s})
                if messagebox.askyesno("Place Order", "Order is saved ,Do you want to continue") == True:
                  pass
                else:
                    destroy_window()
                    Customer_Home.vp_start_gui()
            else:
                messagebox.showinfo("Place Order", "Stock is empty")
        else:
            messagebox.showerror("Place Order", "Product number is wrong")


if __name__ == '__main__':
    import Place_Order
    Place_Order.vp_start_gui()


