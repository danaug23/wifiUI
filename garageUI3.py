import RPi.GPIO as GPIO
import time
import os
from Tkinter import *

timer = 0
distance = 0

root = Tk()

w, h = root.winfo_screenwidth(), root.winfo_screenheight()
root.geometry("%dx%d+0+0" % (w, h))

GPIO.setwarnings(False)
GPIO.cleanup()
GPIO.setmode(GPIO.BCM)

TRIG = 4
ECHO = 18

GPIO.setup(TRIG, GPIO.OUT)
GPIO.setup(ECHO, GPIO.IN)


def get_distance():
	global distance
	try:
		GPIO.output(TRIG, True)
		time.sleep(0.0001)
		GPIO.output(TRIG, False)
		#print("before false")
		while GPIO.input(ECHO) == False:
			#print("IN FALSE")
			start = time.time()
		#print("before true")
		while GPIO.input(ECHO) == True:
			#print("IN TRUE")
			end = time.time()

		sig_time = end-start
		#print("after while")
		#cm: 0.000058
		#inches: 0.000148
		distance = sig_time / 0.000148

		print('Distance: {} inches'.format(distance))
		return distance
	except:
		print('#######################ERROR##########################')
		return 0


def get_color():
	global timer
	timer = timer + 1
	distance = get_distance()
	if distance >= 100:
		return "green"
	elif 100 > distance > 43:
		return "yellow"
	elif distance < 43:
		return "red"

def every_second():
	global timer
	if timer < 236:
		color = get_color()
		root.configure(background=color)
		T1["text"]=round(distance,2)
		T1.pack()
		root.after(250, every_second)
	else:
		exit()
T1 = Label(root, text="Hi Dan!", bd=1, relief="solid", font=("Times 32", 100), width=8,height=2,anchor=CENTER)
#T1.place(x=200, y=300)
#T1.tag_configure("center", justify="center")
#T1.config(font=("Courier", 100))
#T1.insert("1.0", "Hi Dan!")
#T1.tag_add("center", "1.0", "end")
#T1.config(width = 10)
#T1.config(height = 1)
T1.pack(pady=300)
root.after(250, every_second)
root.mainloop()
