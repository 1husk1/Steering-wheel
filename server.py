from flask import Flask, render_template,request
from flask_socketio import SocketIO, emit
import time
from threading import Thread
import vgamepad as vg
import os
from threading import Thread 
import time
import socket
from engineio.async_drivers import gevent

ip = socket.gethostbyname(socket.gethostname())
gamepad = vg.VX360Gamepad()
handbrake = 0
restart = 0
rts = 0
upt =0
downt = 0
lts = 0 
en = 0 
wipper = 0 
lights = 0 


def restart_btn():
	global gamepad,restart 
	while True:
		if restart == 1:
			gamepad.press_button(button = vg.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_RIGHT)
			gamepad.update()
		else:	
			gamepad.release_button(button = vg.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_RIGHT)	
			gamepad.update()
			break

def handbrake_btn():
	global gamepad,handbrake
	while True:
		if handbrake == 1:
			gamepad.press_button(button = vg.XUSB_BUTTON.XUSB_GAMEPAD_RIGHT_SHOULDER)
			gamepad.update()
		else:	
			gamepad.release_button(button = vg.XUSB_BUTTON.XUSB_GAMEPAD_RIGHT_SHOULDER)
			gamepad.update()
			break

def Up_transsmission():
	global gamepad,upt 
	while True:
		if upt == 1:
			gamepad.press_button(button = vg.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_DOWN)
			gamepad.update()
		else:
			gamepad.release_button(button = vg.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_DOWN)
			gamepad.update()
			break

def Down_transsmission():
	global gamepad,downt
	while True:
		if downt == 1:
			gamepad.press_button(button = vg.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_UP)
			gamepad.update()
		else:
			gamepad.release_button(button = vg.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_UP)
			gamepad.update()
			break

def left_turn_signal():
	global gamepad,lts 
	while True:
		if lts == 1:
			gamepad.press_button(button = vg.XUSB_BUTTON.XUSB_GAMEPAD_X)
			gamepad.update()
		else:	
			gamepad.release_button(button = vg.XUSB_BUTTON.XUSB_GAMEPAD_X)
			gamepad.update()
			break	

def right_turn_signal():
	global gamepad,rts
	while True:
		if rts == 1:
			gamepad.press_button(button = vg.XUSB_BUTTON.XUSB_GAMEPAD_Y)
			gamepad.update()
		else:
			gamepad.release_button(button = vg.XUSB_BUTTON.XUSB_GAMEPAD_Y)
			gamepad.update()

def lights_on():
	global gamepad,lights 
	while True:
		if lights == 1:
			gamepad.press_button(button = vg.XUSB_BUTTON.XUSB_GAMEPAD_A)
			gamepad.update()
		else:
			gamepad.release_button(button = vg.XUSB_BUTTON.XUSB_GAMEPAD_A)
			gamepad.update()
			break

def engine_on():
	global gamepad,en 
	while True:
		if en == 1:
			gamepad.press_button(button = vg.XUSB_BUTTON.XUSB_GAMEPAD_B)
			gamepad.update()
		else:
			gamepad.release_button(button = vg.XUSB_BUTTON.XUSB_GAMEPAD_B)
			gamepad.update()
			break

def wipper_on():
	global gamepad,wipper
	while True:
		if wipper == 1:
			gamepad.press_button(button = vg.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_LEFT)
			gamepad.update()
		else:
			gamepad.release_button(button = vg.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_LEFT)
			gamepad.update()	
			break

def true_false(arg):
	if arg == 'true':
		arg = 1
	elif arg == 'false':
		arg = 0
	elif arg == '':
		arg = 0
	elif arg == 'truee':
		arg = 1		
	return arg	

def start_thread(t):
	if not t.is_alive():
		t.start()

def angle_(ax):
	global gamepad
	gamepad.left_joystick(x_value = int(ax),y_value = 0)
	gamepad.update()



app = Flask(__name__)
app.config['SECRET_KEY'] = 'D20fndvfMK27^313787-AQl131'

socketio = SocketIO()

socketio.init_app(app)

name_space = '/abcd'

angle_last = 0


@app.route('/push')
def push_once():
	global gamepad,handbrake,rts,lts,restart,upt,downt,en,wipper,lights
	angle = request.args.get('angle')
	gas = request.args.get('gas')
	brk = request.args.get('break')
	handbrake = request.args.get('handbrake')
	restart = request.args.get('restart')
	rts = request.args.get('rts')
	lts = request.args.get('lts')
	upt = request.args.get('upt')
	downt = request.args.get('downt')
	lights = request.args.get('lights')
	en = request.args.get('en')
	wipper = request.args.get('wipper')
	max_angle = request.args.get('max_angle')
	checked = request.args.get('checked')
	sens = request.args.get('sens')
	checked = true_false(checked)
	value_gas = float(request.args.get('valuegas'))
	value_break = float(request.args.get('valuebreak'))

	if str(angle) == '':
		pass
	else:
		try:
			ang = float(angle)
			max_angle = float(max_angle)
			if ang == 0.0:
					ax = 0
			elif checked == 1:
				ang = float(angle)		
				if ang >= 1:
					ax = round(ang) * ((32000 - float(sens))/max_angle) + float(sens)
				elif ang <= -1:
					ax = round(ang) * ((32000 - float(sens))/max_angle) + (float(sens) * -1)				
			else:
				ax = round(ang) * (32000/max_angle)		
		except ValueError:
			print('Error')	

	gas = true_false(gas)
	brk = true_false(brk)
	handbrake = true_false(handbrake)
	restart = true_false(restart)
	rts = true_false(rts)
	lts = true_false(lts)
	upt = true_false(upt)
	downt = true_false(downt)
	lights = true_false(lights)
	en = true_false(en)
	wipper = true_false(wipper)	

	t_angle = Thread(target = lambda : angle_(ax),args=())
	t_angle.start()
	if gas == 1:
		print('gsa')
		gamepad.right_trigger_float(value_float=value_gas)
	if gas == 0:
		gamepad.right_trigger_float(value_float=0)	
	if brk == 1:	
		gamepad.left_trigger_float(value_float=value_break)
	if brk == 0:
		gamepad.left_trigger_float(value_float=0)	
	if handbrake == 1:
		handbrake_thread = Thread(target = handbrake_btn, args=())
		start_thread(handbrake_thread)
	elif restart == 1:
		restart_thread = Thread(target = restart_btn, args =())
		start_thread(restart_thread)
	elif rts == 1:
		rts_thread = Thread(target = right_turn_signal,args=())
		start_thread(rts_thread)
	elif lts == 1:
		lts_thread = Thread(target = left_turn_signal,args=())
		start_thread(lts_thread)
	elif upt == 1:
		upt_thread = Thread(target = Up_transsmission,args=())
		start_thread(upt_thread)
	elif downt == 1:
		downt_thread = Thread(target = Down_transsmission, args=())
		start_thread(downt_thread)
	elif lights == 1:
		lights_thread = Thread(target = lights_on,args=())
		start_thread(lights_thread)
	elif en == 1:
		en_thread = Thread(target = engine_on,args=())
		start_thread(en_thread)
	elif wipper == 1:
		wipper_thread = Thread(target = wipper_on,args=())	
		start_thread(wipper_thread)							

	gamepad.update()		
	return 'done'



@socketio.on('connect')#,name_space=name_space)
def connected_msg():
	print('client connected')

@socketio.on('disconnect')#, name_space = name_space)	
def disconnect_msg():
	print('client disconnected')


if __name__ == '__main__':
	app.run(host=ip,port=8000)
	socketio.run(app)	
	
