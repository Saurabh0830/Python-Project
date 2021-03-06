#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# Support module generated by PAGE version 4.13
# In conjunction with Tcl version 8.6
#    Jun 24, 2018 01:00:14 PM


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

def CustomerChangeP_Save():
    print('CustomerChangePassword_support.CustomerChangeP_Save')
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

def variable(u):
    global d
    d = u

def CustomerChangeP_Save():
    old = w.CustomerCP_Old.get()
    new = w.CustomerCP_New.get()
    confirm = w.CustomerCP_Confirm.get()
    from firebase import firebase as fb
    fire = fb.FirebaseApplication("https://merchant-ca794.firebaseio.com/customer/login", None)
    result = fire.get("login", d)
    if old == "":
        messagebox.showerror("Change Password", "Enter the old password")
    elif new == "":
        messagebox.showerror("Change Password", "Enter the new password")
    elif confirm == "":
        messagebox.showerror("Change Password", "Enter the confirm password")
    else:
        if result["pass"] == old:
            if new == confirm:
                fire.put("login", d, {"name": result["name"], "cno": result["cno"], "pass": new, "address": result["address"]})
                messagebox.showinfo("Change Password", "Password is changed")
            else:
                messagebox.showerror("Change Password", "new and confirm password")
        else:
            messagebox.showerror("Change Password", "Invalid old password")

if __name__ == '__main__':
    import CustomerChangePassword
    CustomerChangePassword.vp_start_gui()


