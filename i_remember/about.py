from tkinter import *
from config_tk import *
import sqlite3 as sql,sys , re , pickle ,os  
from tkinter import messagebox as msg 
from tkinter.scrolledtext import ScrolledText
# from win10toast import ToastNotifier
# from  _entry import _entry , _text
# note = ToastNotifier()

def about(mother , root, conn , cursor , select):
	myself = """\
i-remember 1.0.0\n
for information contact :
author :%s
email :%s
	""" % (author , email)
	msg._show("about" , myself ,"info" ,"ok")
