import json

#load the configuration file
with open('static/config.json') as json_file :
	load = json.load(json_file)

style = [obj for obj in load['style'] ]
about = [obj for obj in load['about'] ]
root_config = [obj for obj in load['root-config'] ]
author , email = about[0]['author'] ,about[0]['email']
style_on_event = [obj for obj in load['style-on-event'] ]

abg , afg , enter_color , leave_color = (style_on_event[0]['activebackground'] ,
	style_on_event[0]['activeforeground'] , style_on_event[0]['Enter'], style_on_event[0]['Leave']  )


bg , fg , font  , relief  , images = (style[0]['bg'] ,style[0]['fg'] ,
 tuple(style[0]['font']) , style[0]["relief"] ,  style[0]["images"])

title , geo , icon , root_bg , Extra =( root_config[0]['title'] ,root_config[0]['geometry'] 
	,root_config[0]['icon'] ,root_config[0]['bg-root'] ,root_config[0]['Extra-data'])  

def color_ch(element):
	
	element.bind('<Enter>' , lambda e : element.config(bg = enter_color))
	element.bind('<Leave>' , lambda e : element.config(bg = leave_color))
	element.config(activebackground = abg)
	element.config(activeforeground = afg)

def apply_ch(objs):
	for element in objs :
		color_ch(element)
