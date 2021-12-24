from tkinter import *
from center_tk import Center_root 
from tkinter.scrolledtext import ScrolledText
import os , threading


class _entry(Entry) :

	def __init__(self , perent , *args , **kwargs):
		Entry.__init__(self , perent , *args , **kwargs)
		self.pop = Menu(self ,tearoff =0 )
		self.pop.add_command(label = "Cut\t\t", command = self.Cut)
		self.pop.add_command(label = "Copy\t\t", command = self.Copy)
		self.pop.add_command(label = "Paste\t\t", command = self.Paste)
		self.bind('<Button-3>' , self.pop2)

	def pop2(self, e):
		try:
			self.pop.tk_popup(e.x_root , e.y_root , 0)
		finally :
			self.pop.grab_release()
	def Copy(self):
		self.event_generate("<<Copy>>")
	def Paste(self):
		self.event_generate("<<Paste>>")
	def Cut(self):
		self.event_generate("<<Cut>>")

class _text(Text) :

	def __init__(self , perent , *args , **kwargs):
		Text.__init__(self , perent , *args , **kwargs)
		self.pop = Menu(self ,tearoff =0 )
		self.pop.add_command(label = "Cut\t\t", command = self.Cut)
		self.pop.add_command(label = "Copy\t\t", command = self.Copy)
		self.pop.add_command(label = "Paste\t\t", command = self.Paste)
		self.bind('<Button-3>' , self.pop2)

	def pop2(self, e):
		try:
			self.pop.tk_popup(e.x_root , e.y_root , 0)
		finally :
			self.pop.grab_release()
	def Copy(self):
		self.event_generate("<<Copy>>")
	def Paste(self):
		self.event_generate("<<Paste>>")
	def Cut(self):
		self.event_generate("<<Cut>>")

class scroll_text(ScrolledText) :

	def __init__(self , perent , *args , **kwargs):
		ScrolledText.__init__(self , perent , *args , **kwargs)
		self.pop = Menu(self ,tearoff =0 )
		self.pop.add_command(label = "Cut\t\t", command = self.Cut , image =None 
			, compound = 'left') 
		self.pop.add_command(label = "Copy\t\t", command = self.Copy , image =None 
			, compound = 'left') 
		self.pop.add_command(label = "Paste\t\t", command = self.Paste , image =None 
			, compound = 'left') 
		self.bind('<Button-3>' , self.pop2)

	def pop2(self, e):
		try:
			self.pop.tk_popup(e.x_root , e.y_root , 0)
		finally :
			self.pop.grab_release()
	def Copy(self):
		self.event_generate("<<Copy>>")
	def Paste(self):
		self.event_generate("<<Paste>>")
	def Cut(self):
		self.event_generate("<<Cut>>")

class Check_path :
	def __init__(self , label , Entry):
		self.label = label
		self.Entry = Entry
		self.Thread = threading.Thread(target = self.curr).start()

	def exists(self,event):
		state = os.path.exists(self.Entry.get())
		if state :
			self.label['text'] = 'The Object Dose exists' 
			self.label['foreground'] = '#00A600'
		else :
			self.label['text'] = 'The Object Dose not exists' 
			self.label['foreground'] = 'red'
		
	def curr(self):
		try:
			while True:
				if len(self.Entry.get()) > 5 :
					self.Entry.bind("<Key>" , self.exists)
				elif len(self.Entry.get()) == 0 :
					self.label['text'] = 'Please Insert Document Path !' 
					self.label['foreground'] = '#000'
		except :
			pass

if __name__ == '__main__':				
	root = Tk()
	show = Label(text = 'Please Insert Document Path !')
	show.pack()
	get_path = _entry(root , width = 40)
	exists = Check_path(label = show , Entry = get_path)
	center_ = Center_root(master = root, geometry =(300 , 50))
	get_path.pack()
	root.mainloop()