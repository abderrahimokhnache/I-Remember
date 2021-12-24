from tkinter import *
from config_tk import *
import sqlite3 as sql, tkinter.messagebox as msg ,sys , re , pickle ,os  
from tkinter.scrolledtext import ScrolledText
# from win10toast import ToastNotifier
from  _entry import _entry , _text
# note = ToastNotifier()

def insert_new(mother , root, conn , cursor , select , registered):
	"""Insert new password to the database """
	root.title(title + "- New Password ")
	root.geometry(geo)
	for widget in mother.winfo_children(): 
		widget.destroy()
	def save():
		Service , password = get_serv.get() , get_passw.get()
		try:
			with conn :
				cursor.execute("CREATE TABLE IF NOT EXISTS Services(ID integer primary key autoincrement , Service TEXT , password TEXT)")
				cursor.execute("INSERT INTO Services(Service , password) Values(?,?)" , (Service , password))
		except sql.Error as e:
			 msg.showerror('Error' , e)
		else :
			# note.show_toast("i-remember" , "%s Password has been saved :)" % Service , icon_path = icon 
			# 	, threaded = True, duration=10)
			registered(mother , root, conn , cursor , select)

	service_lb = Label(mother,text = 'Service ' , fg = fg , bg = root_bg ,
		font = font)
	password_lb = Label(mother,text = 'Password ' , fg = fg , bg = root_bg ,
		font = font)
	get_serv = _entry(mother,font = font ,bg = root_bg , fg = fg , relief = relief)
	get_passw = _entry(mother,show = '*' , font = font,bg = root_bg , fg = fg  , relief = relief)
	submit_btn = Button(mother,text = "Save" , font = font , bg = root_bg , fg = fg ,
		relief = "solid" , command = save)
	back_btn = Button(mother , text = "Menu" , fg = fg 
		, bg = root_bg , relief = relief , command = lambda :select(mother , root, conn , cursor )
		 , font = font )

	service_lb.place(relx = 0.025 , rely = 0.1)
	password_lb.place(relx = 0.025 , rely = 0.3)
	get_serv.place(relx = 0.3 , rely = 0.1 )
	get_passw.place(relx = 0.3 , rely = 0.3)
	submit_btn.place(relx = 0.6 , rely = 0.6 , relwidth = 0.3)
	back_btn.place(relx = 0.1 , rely = 0.6 , relwidth = 0.4)

	apply_ch([submit_btn , back_btn])