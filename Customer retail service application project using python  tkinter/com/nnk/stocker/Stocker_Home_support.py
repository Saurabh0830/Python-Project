#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# Support module generated by PAGE version 4.13
# In conjunction with Tcl version 8.6
#    Jun 15, 2018 10:30:05 PM


import sys
from main.com.nnk.stocker import StockerHome_LogoutM
from main.com.nnk.stocker import Change_Password
from main.com.nnk.stocker import Add_Product
from main.com.nnk.stocker import ProductView
from main.com.nnk.stocker import ProductDelete
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

def StockerHome_AddProduct():
    print('Stocker_Home_support.StockerHome_AddProduct')
    sys.stdout.flush()

def StockerHome_ChangePassword():
    print('Stocker_Home_support.StockerHome_ChangePassword')
    sys.stdout.flush()

def StockerHome_Logout():
    print('Stocker_Home_support.StockerHome_Logout')
    sys.stdout.flush()

def StockerHome_ViewProduct():
    print('Stocker_Home_support.StockerHome_ViewProduct')
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

def StockerHome_ChangePassword():
    destroy_window()
    Change_Password.vp_start_gui()


def StockerHome_AddProduct():
    destroy_window()
    Add_Product.vp_start_gui()

def StockerHome_ViewProduct():
    ProductView.vp_start_gui()

def StockerHome_DeleteProduct():
    destroy_window()
    ProductDelete.vp_start_gui()


def StockerHome_Logout():
    StockerHome_LogoutM.vp_start_gui()


if __name__ == '__main__':
    import Stocker_Home
    Stocker_Home.vp_start_gui()


