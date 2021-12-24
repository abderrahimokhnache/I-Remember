from tkinter import *

class Center_root :
	def __init__(self , master , geometry):
		self.master = master
		self.width = geometry[0]
		self.height = geometry[1]
		screen_w = self.master.winfo_screenwidth()
		screen_h = self.master.winfo_screenheight()
		x_coordinate = (screen_w/2)- (self.width/2)
		y_coordinate = (screen_h/2)- (self.height/2)
		self.master.geometry('%dx%d+%d+%d' % (self.width , self.height , x_coordinate , y_coordinate))

