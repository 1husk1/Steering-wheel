from tkinter import *
from tkinter import messagebox as ms
import ast


window = Tk()
window.geometry('200x300')
window.resizable(False,False)
window.title('Change Buttons')
dict_ = {}
destroy_object = []
count = 0
def read_txt():
	global dict_
	txt = open('buttons.txt')
	count = 0
	for i in txt:
		string = i
	dict_ = dict((a.strip(),str(b.strip()))
		for a,b in (element.split(':')
			for element in string.split(',')))
	txt.close()

def collect(list_s,list_b,name,btn):
	global dict_,handbrake_btn
	selection_index = list_s.curselection()
	select = list_b[int(selection_index[0])]
	dict_[name] = select
	strings = []
	for key,item in dict_.items():
		strings.append("{} : {}".format(key.capitalize(), item))
	result = ", ".join(strings)
	txt = open('buttons.txt','w')
	txt.write(result)
	txt.close()
	btn['text'] = select

	


def list_box(name_button,btn):
	topl = Toplevel()
	list_buttons = ['A','B','Y','X','dpad Up','dpad Down', 'dpad Left', 'dpad Right','R1','L1']
	list_box1 = Listbox(topl,selectmode=SINGLE)
	list_box1.insert(0,*list_buttons)
	list_box1.pack()
	button = Button(topl,text='Save',command = lambda : collect(list_box1,list_buttons,name_button,btn)).pack()

read_txt()	
handbrake_lbl = Label(text='Handbrake').place(x=15,y=20)
handbrake_btn = Button(text=dict_.get('Handbrake'),command=lambda :list_box('handbrake',handbrake_btn))
handbrake_btn.place(x=100,y=20)
up_t = Label(text='Up').place(x=15,y=50)
upt_btn = Button(text=dict_.get('Upt'),command=lambda :list_box('upt',upt_btn))
upt_btn.place(x=100,y=50)
down_t = Label(text='Down').place(x=15,y=80)
downt_btn = Button(text=dict_.get('Downt'),command=lambda :list_box('donwt',downt_btn))
downt_btn.place(x=100,y=80)
wipper = Label(text='Wippers').place(x=15,y=110)
wipper_btn = Button(text=dict_.get('Wipper'),command=lambda :list_box('Wipper',wipper_btn))
wipper_btn.place(x=100,y=110)
startEnging = Label(text='Start engine').place(x=15,y=140)
Start_engine_btn = Button(text=dict_.get('Start_engine'),command=lambda :list_box('Start_Engine',Start_engine_btn))
Start_engine_btn.place(x=100,y=140)
lights = Label(text='lights').place(x=15,y=170)
lights_btn = Button(text=dict_.get('Lights'),command=lambda :list_box('Lights',lights_btn))
lights_btn.place(x=100,y=170)
restart = Label(text='Restart').place(x=15,y=200)
restart_btn = Button(text=dict_.get('Restart'),command=lambda :list_box('Restart',restart_btn))
restart_btn.place(x=100,y=200)
rts = Label(text='R turn signal').place(x=15,y=230)
rts_btn = Button(text=dict_.get('Rts'),command=lambda :list_box('rts',rts_btn))
rts_btn.place(x=100,y=230)
lts = Label(text='L turn signal').place(x=15,y=260)
lts_btn = Button(text=dict_.get('Lts'),command = lambda : list_box('lts',lts_btn))
lts_btn.place(x=100,y=260)



window.mainloop()