from tkinter import *
from config_tk import *
import sqlite3 as sql ,sys , re , pickle ,os
# from win10toast import ToastNotifier
from  _entry import _entry , _text
from i_remember._select import select
from tkinter import ttk 
from tkinter import messagebox as msg 
root = Tk()
root['bg'] = root_bg
root.geometry(geo)
root.title(title)
# root.iconbitmap(icon)
root.resizable(0,0)
# note = ToastNotifier()
count = 1
counted = 30

#submitfunc		
def submit(e = None):
	"""Submit user authentication , Creates Database 
	,login in if the user exists and his auth are True else create one """
	global  count , counted
	def countdown():
		global counted , count
		if counted == 0:
			root.protocol('WM_DELETE_WINDOW', lambda : root.destroy() )        		 
			get_un["state"] = 'normal'
			get_pw["state"] = 'normal'
			submit_btn["state"] = 'normal'
			state['text'] = 'You Can Try Now !'
			state['fg'] = "lightgreen"
			del counted  
			del count
			count = 0
			counted = 30

		else:
			counted -=1
			state['text'] = "Try agine After %d !" % (counted)	
			state.after(1000,countdown  )

	if count == 3 : 
		root.protocol('WM_DELETE_WINDOW', lambda : None )        		 
		get_un["state"] = 'disable'
		get_pw["state"] = 'disable'
		submit_btn["state"] = 'disable'
		countdown()

	username , passw = get_un.get() , get_pw.get()
	get_un.delete(0 , END) 
	get_pw.delete(0 , END)
	conn = sql.connect("static/account0.db")
	conn.row_factory = sql.Row
	cursor = conn.cursor()

	try:
		cursor.execute("Select * from user")
		data = cursor.fetchall()

	except sql.OperationalError:		
		with conn :
			cursor.execute("CREATE TABLE IF NOT EXISTS user(username TEXT , password TEXT)")
			cursor.execute("INSERT INTO user Values(?,?)" , (username , passw))
		# 	note.show_toast("i-remember" , """Welcome to i-remember You are connected to the database now :)""" , icon_path = icon 
		# , threaded = True, duration=10)
			for widget in mother.winfo_children(): 
				widget.destroy()
			select(mother ,root, conn , cursor)
	else : 
		
		if username == data[0][0]  and passw == data[0][1] :
		# 	note.show_toast("i-remember" , "You are connected to the database now :)" , icon_path = icon 
		# , threaded = True, duration=10)
			select(mother, root, conn , cursor)
		else :
			 state['text'] = "invalid input !"			
			 state['fg'] ="red"
			 count +=1 

"""main widgets"""
mother = Frame(root , bg = root_bg)
mother.place(relx = 0.0 , rely = 0.0 , relwidth  = 1 , relheight = 1)

usern_lb = Label(mother,text = 'username ' , fg = fg , bg = root_bg ,
 font = font)
passw_lb = Label(mother,text = 'Password ' , fg = fg , bg = root_bg ,
 font = font)
state = Label(mother , bg = root_bg , fg = "red", font = font)
get_un = _entry(mother,font = font)
get_pw = _entry(mother,show = '*' , font = font)
submit_btn = Button(mother,text = "Submit" , font = font , bg = root_bg , fg = fg ,
 relief = "solid" , command = lambda : submit())
state.place(relx = 0.025 , rely =0.62 )
usern_lb.place(relx = 0.025 , rely = 0.1)
passw_lb.place(relx = 0.025 , rely = 0.3)
get_un.place(relx = 0.3 , rely = 0.1 )
get_pw.place(relx = 0.3 , rely = 0.3)
submit_btn.place(relx = 0.6 , rely = 0.6 , relwidth = 0.3)

#appling hover , active color changes
apply_ch([submit_btn])

# debug
try:
	with open('static/admin.~' , "rb") as admin_f:
		admin_data = admin_f.readlines()
	username , password =  str(admin_data[0]).split(',')
	get_un.insert(INSERT , username) 
	get_pw.insert(INSERT , password)
	submit_btn.invoke()
except:
	pass

root.mainloop()
