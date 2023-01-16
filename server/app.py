from tkinter import *
import os
import psutil
from threading import Thread 
import socket


txt = open('start.txt',"w")
txt.close()
String = ""
ip = socket.gethostbyname(socket.gethostname())

def start():
	global String
	btn_start.config(text='Stop',command = end)
	dir_ = os.getcwd()
	start_activity = True
	os.startfile(r'' + dir_+ '/Server.exe')
	String += "Server started!\nip : " + ip + "\n"
	lbl.config(text=String)
	Thread_ = Thread(target=insert_in_ent,args=())
	Thread_.start()

def end():
	global String
	start_activity = False
	btn_start.config(text='Start',command=start)
	for process in (process for process in psutil.process_iter() if process.name()=="server.exe"):
		process.kill()
	String += "Server killed\n"
	lbl.config(text=String)

def change_buttons():
	dir_ = os.getcwd()
	os.startfile(r'' + dir_ + '/change_button.exe')	

def insert_in_ent():
	global stop,String
	String += "Search device\n"
	lbl.config(text=String)
	one_start = False
	one_end = False
	while True:
	 	if stop == True:
	 		break
	 	txt = open('start.txt',"r")
	 	word = txt.read()	
	 	if(word == "start" and start_activity == True):
	 		if one_start == False:
	 			print('start')
	 			String += "Device connected!\n"
	 			lbl.config(text=String)
	 			one_start = True
	 			one_end = False
	 	elif(word == 'end' and start_activity == True):
	 		if one_end == False:
	 			print('end')
	 			String += "Device disconnected!\n"
	 			lbl.config(text=String)	
	 			one_start = False
	 			one_end = True
	 	txt.close()

def clear_output():
	global String
	String = ''
	lbl.config(text=String)	 	
try:
	start_activity = True
	stop=False

	window = Tk()
	window.geometry('270x190')
	window.resizable(False,False)
	window.title('Start')


	ent = Entry(state="readonly",width=200,background="#fff")
	ent.pack(ipady=70)

	lbl = Label(text=String,background="#f0f0f0")
	lbl.place(x=0,y=5)

	btn_start = Button(text='Start',width=17,command=start)
	btn_start.place(x=2,y=159)

	btn_end = Button(text="Change buttons",width=17,command=change_buttons)
	btn_end.place(x=140,y=159)

	btn_clear_output = Button(text = "Clear",command = clear_output)
	btn_clear_output.place(x=230,y=5)
	

	window.mainloop()

except Exception as error:
        print(error)
finally:
	stop = True	 

