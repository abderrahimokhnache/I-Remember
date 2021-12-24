from tkinter import *
from config_tk import *
import  hashlib , random 
# from win10toast import ToastNotifier
from  _entry import _entry , _text
from tkinter import ttk 
from tkinter import messagebox as msg 

def password_generator(mother , root ,select, conn , cursor):
	''' Generate a Random Password using hash lib algorithms , 
	the algorithm that being used depends on length of password '''
	for widget in mother.winfo_children() :
		widget.destroy()
	root.title("Password~Generator")
	def state_output(e):
		if e :
			get_pass['state'] = 'normal'
			get_pass.delete(0, END)
		else :
			get_pass.delete(0 , END)
			get_pass.insert(INSERT , "Output area")
			get_pass['state'] = 'disable'

	def generate():
		state['text'] =""
		size = get_size.get()
		if size.isdigit() == False :
			state['text'] = "The length must me an integer !"
			state_output(0)
		else :
			size = int(size)
			randi = str(random.randint(0, 10000)) + "azertyyuiopmlkjhgfd1333333545"
			hash = False
			if size == 32 :
				hash = hashlib.md5(bytes(randi , encoding='utf8')).hexdigest()
				state_output(1)
			elif size == 64 :
				hash = hashlib.sha256(bytes(randi , encoding='utf8')).hexdigest()
				state_output(1)
			elif size == 128 :
				hash = hashlib.sha512(bytes(randi , encoding='utf8')).hexdigest()
				state_output(1)
			elif size > 128 :
				state['text'] = "128 is the limit of password length !" 
				state_output(0)
			elif size < 10 :
				state['text'] = "Week Password !"
				state_output(0)
			else :
				hash = hashlib.sha512(bytes(randi , encoding='utf8')).hexdigest()
				hash = hash[0:size]
				state_output(1)
			if hash :
				get_pass.insert(INSERT , hash)

	back_btn = Button(mother , text = "Menu" , fg = fg 
		, bg = root_bg , relief = relief , command = lambda : select(mother, root, conn , cursor) , font = font )
	help_lb = Label(mother , text = "i~remember Generator " , fg = fg , bg = root_bg , font = font)
	get_pass = _entry(mother , font = font,bg = root_bg , fg = fg , relief = relief)
	get_size = _entry(mother , font = font,bg = root_bg , fg = fg , relief = relief)

	state = Label(mother , bg = root_bg , fg = "red", font = font)
	gener_btn = Button(mother ,text = "Generate" , font = font , bg = root_bg , fg = fg ,
		relief = "solid"  ,command = generate)
	help_lb.place(relx = 0.25 , rely = 0.1)
	get_size.place(relx = 0.1 , rely = 0.31 , relwidth = 0.8)
	get_pass.place(relx = 0.1 , rely = 0.46 , relwidth = 0.8)
	gener_btn.place(relx = 0.6 , rely = 0.61 , relwidth = 0.3)
	back_btn.place(relx = 0.1 , rely = 0.61 , relwidth = 0.4)
	state.place(relx = 0.1 , rely =0.78 )
	get_pass.insert(INSERT , "Output area ")
	get_pass['state'] = 'disable'
	if  not get_size.get():
		get_size.insert(INSERT , "length of the password ?")
	get_size.bind("<Enter>" , lambda e : get_size.delete(0 , END))
	apply_ch([gener_btn , back_btn])
