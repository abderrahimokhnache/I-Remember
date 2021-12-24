from tkinter import *
from config_tk import *
# from win10toast import ToastNotifier
from i_remember.Generator import password_generator
from i_remember.new_pass import insert_new
from i_remember.reg import registered
from i_remember.about import about
from tkinter import ttk 
from tkinter import messagebox as msg 
#selectfun

def select(mother ,root, conn , cursor):
	"""Select a Part of the the Program to goto"""
	root.title(title + " - Menu ")
	for widget in mother.winfo_children(): 
		widget.destroy()
	root.geometry("400x270")
	"""main widghts"""
	def get_option(option):
		if option == 'new' :
			insert_new(mother , root, conn , cursor , select , registered)
		elif option == 'reg':
			registered(mother , root, conn , cursor , select)
		elif option== "Generator":
			password_generator(mother, root ,select, conn , cursor)
		else :
			about(mother , root, conn , cursor , select)

	NEW= Button(mother ,text = "New Password",font = font , bg= root_bg
	 , fg =fg,relief ='solid' , command = lambda : get_option('new'))
	saved= Button(mother , text = "registry",
		font = font , bg= root_bg , fg =fg,relief = 'solid'
		, command = lambda : get_option('reg'))
	passgen_btn = Button(mother , text = "Generator",
		font = font , bg= root_bg , fg =fg,relief = 'solid'
		, command = lambda : get_option('Generator'))
	about_btn = Button(mother , text = "About",
		font = font , bg= root_bg , fg =fg,relief = 'solid'
		, command = lambda : get_option('about'))

	NEW.place(relx= 0.25 , rely = 0.05 , relwidth = 0.5 , relheight = 0.2)
	saved.place(relx= 0.25 , rely = 0.28 , relwidth = 0.5 , relheight = 0.2)
	passgen_btn.place(relx= 0.25 , rely = 0.52 , relwidth = 0.5 , relheight = 0.2)
	about_btn.place(relx= 0.25 , rely = 0.75 , relwidth = 0.5 , relheight = 0.2)
	
	apply_ch([NEW, saved , about_btn , passgen_btn])
