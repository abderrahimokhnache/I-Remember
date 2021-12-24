from tkinter import *
from config_tk import *
import sqlite3 as sql,tkinter.messagebox ,sys , re , pickle ,os 
from tkinter.scrolledtext import ScrolledText
# from win10toast import ToastNotifier
from  _entry import _entry , _text
from i_remember.new_pass import insert_new

# note = ToastNotifier()

def registered(mother , root, conn , cursor ,select):
	""" view , Delete , update the database """
	root.title("i~remember - registry")
	for widget in mother.winfo_children(): 
		widget.destroy()
	root.geometry("600x350")

	style = ttk.Style()
	style.theme_use("clam")
	style.configure("Treeview" ,font = font)
	def open_serv(event = False):			
		wind = Tk()			
		wind.title(title)			
		wind.geometry('400x300')			
		# wind.iconbitmap(icon)			
		id = tree.selection()[0][1:]					
		cursor.execute('Select * from Services where ID = ?' ,(id,))			
		MainText = _text(wind , font = font , bg = root_bg , fg = fg , relief = relief)			
		MainText.place(relx= 0.0 , rely = 0.0 , relwidth = 0.999 , relheight = 0.999)			
		for row in cursor:
				msg = 'Service ~ '+ row['Service'] +'\n\nPassword : '+row['password']
				MainText.insert(1.0 ,msg)
	def dele(event = False):
			id = tree.selection()[0][1:]
			with conn :
				cursor.execute('delete from Services where ID = ?' , (id,))
			tree.delete("#" +id)
			# note.show_toast("i-remember" , "Row %s has been deleted !" % id, icon_path = icon 
			# 	, threaded = True, duration=10)

	def update_f():
		lowlevel = Tk()
		lowlevel.geometry(geo)
		lowlevel.title(title)
		lowlevel['bg'] = root_bg
		# lowlevel.iconbitmap(icon)
		lowlevel.resizable(0,0)
		def save_update():
			id = tree.selection()[0][1:]
			try:
				with conn :
					cursor.execute('UPDATE Services SET Service = :Service where id = :id ',
						{"Service" : get_ser.get() , "id" : id })
					cursor.execute('UPDATE Services SET password = :password where id = :id ',
						{"password" : get_pass.get() , "id" : id })

			except sql.Error as e :
				msg.showerror('Error' , e)
			except sql.OperationalError as e :		
				msg.showerror('Error' , e)
			else :
				# note.show_toast("i-remember" , "Row %s has been Update !" % id , icon_path = icon 
				# 	, threaded = True, duration=10)
				lowlevel.destroy()
				registered(mother , root, conn , cursor ,select)

		service_lb = Label(lowlevel ,text = 'Service ' , fg = fg , bg = root_bg ,
			font = font)
		password_lb = Label(lowlevel ,text = 'Password ' , fg = fg , bg = root_bg ,
			font = font)
		get_ser = _entry(lowlevel ,font = font , bg = root_bg , fg = fg, relief = relief)
		get_ser.focus_set()
		get_pass = _entry(lowlevel , font = font, bg = root_bg , fg = fg, relief = relief)
		update_btn = Button(lowlevel ,text = "Update" , font = font , bg = root_bg , fg = fg ,
			relief = "solid" , command = save_update)
		service_lb.place(relx = 0.025 , rely = 0.1)
		password_lb.place(relx = 0.025 , rely = 0.3)
		get_ser.place(relx = 0.3 , rely = 0.1 )
		get_pass.place(relx = 0.3 , rely = 0.3)
		update_btn.place(relx = 0.6 , rely = 0.6 , relwidth = 0.3)
		try: 
			id = tree.selection()[0][1:]
			cursor.execute('Select * from Services where ID = ?' ,(id,))		
			for row in cursor :
				get_ser.insert(INSERT , row['Service'] )
				get_pass.insert(INSERT , row['password'])
		except IndexError  :
			lowlevel.destroy()
			msg.showerror("Error" ,"Please Select a Service to Update !")
		
		apply_ch([update_btn])

	reset_btn = Button(mother , text = "New Password" , fg = fg 
		, bg = root_bg , relief = relief , command = lambda : insert_new(mother , root, conn , cursor , select , registered) , font = font )
	back_btn = Button(mother , text = "Menu" , fg = fg 
		, bg = root_bg , relief = relief , command = lambda :select(mother , root, conn , cursor) , font = font )
	open_btn = Button(mother , text = "open" , fg = fg 
		, bg = root_bg , relief = relief , command =  open_serv , font = font )
	del_btn = Button(mother , text = "delete" , fg = fg 
		, bg = root_bg , relief = relief , command =  dele , font = font )
	update_btn = Button(mother , text = "update" , fg = fg 
		, bg = root_bg , relief = relief , command =  update_f , font = font )
	reset_btn.place(relx = 0.01 , rely = 0.01)
	back_btn.place(relx = 0.3 , rely = 0.01)
	open_btn.place(relx = 0.5 , rely = 0.01)
	del_btn.place(relx = 0.63 , rely = 0.01)
	update_btn.place(relx = 0.8 , rely = 0.01)


	tree = ttk.Treeview(mother)
	f= Scrollbar(mother)
	f.place(relx = 0.97 , rely = 0.15 , relheight = 0.85)
	tree.place(relx = 0 , rely = 0.15 , relwidth = 0.97 , relheight = 0.85)
	tree['yscrollcommand'] = f.set
	f.configure(command = tree.yview)
	tree.heading('#0' , text = 'ID')
	tree["column"] = ('#Serv' , '#Pw')
	tree.heading('#Serv' , text = 'Service' )
	tree.heading('#Pw' , text = 'Password')
	tree.column('#0', width=1)
	tree.column('#Serv', width=80)
	tree.column('#Pw', width=150)

	root.bind('<Key-d>' , dele)
	root.bind('<Key-Return>' , open_serv)
	try:
		user_data = cursor.execute("Select * from Services")
		for row in user_data:
			
			tree.insert('','end','#{}'.format(row['ID']),text=row['ID'])
			
			tree.set('#{}'.format(row['ID']),'#Serv' , row['Service'])
			
			tree.set('#{}'.format(row['ID']),'#Pw' , row['Password'])	
	except sql.OperationalError:
		# note.show_toast("i-remember" , "There is no Service To view ! "  , icon_path = icon 
		# 		, threaded = True, duration=10)
		pass

	apply_ch([back_btn , reset_btn , open_btn ,  del_btn , update_btn])
