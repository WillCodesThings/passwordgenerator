import re
import random
import tkinter as tk
from tkinter import *
from tkinter import messagebox
from cryptography.fernet import Fernet

#creatng a window 
app = tk.Tk()
height = 500
width = 600
app.configure(background='#CAADDD')

while True:
	#making buttons able to change check value
	enc1 = IntVar()
	rnus1 = IntVar()
	slch1 = IntVar()


	#Creating inital password
	passw = random.randint(0, 1000000000)


	#changing password
	#encrypting message
	def Encrypt():
		file = open('encrpytionkeys.txt', 'rb')
		key = file.read()
		file.close()
		#encoding message
		message = str(passw)
		encodedmsg = message.encode()
		#encrypt
		f = Fernet(key)
		encrypted = f.encrypt(encodedmsg)
		def epwd():
			msgs = messagebox.showinfo('Password', encrypted)
		epasswo = tk.Button(app, text = 'Show Encrypted password', command = epwd, bg = '#44E770')
		epasswo.pack()
	#random username
	def usrdef():
		usrs = [ 'Howling', 'Jumping', 'Swimming', 'Happy', 'Sad', 'Singing', 'Silly', 'Fun', 'Charming', 'Cruel', 'Perfect']
		usre = [ 'Wolf', 'Frog', 'Fish', 'Giraffe', 'Eagle', 'Bird', 'Dolphin', 'Beaver', 'Fox', 'Snake', 'Axolotl']
		rndurs = random.choice(usrs)
		rndure = random.choice(usre)
		usr = rndurs + rndure
		def usrp():
			msgs = messagebox.showinfo('Username', usr)
		usrn = tk.Button(app, text = 'Show Username', command = usrp, bg = '#44E770')
		usrn.pack()
	def spechar():
		lis = ['*','&','%','$','#','!']
		li = re.findall('.', str(passw))
		
		print(li)
		l = li + lis
		random.shuffle(l)
		rnd = ''.join(l)
		def uchb():
			msgs = messagebox.showinfo('Password', rnd)
		rpc = tk.Button(app, text = 'Special character password', command = uchb, bg = '#44E770')
		rpc.pack()

	#buttons
	ENCRPPASS = tk.Checkbutton(app, text = 'encrypt password', variable = enc1, onvalue = 1, offvalue = 0, height= 5, width = 20, command = Encrypt, bg = '#995EDA')
	RANDUSR = tk.Checkbutton(app, text = 'random username', variable = rnus1, onvalue = 1, offvalue = 0, height= 5, width = 20, command = usrdef, bg = '#9E9E9E')
	SPCHARAC = tk.Checkbutton(app, text = 'special characters', variable = slch1, onvalue = 1, offvalue = 0, height= 5, width = 20, command = spechar, bg = '#2DC2B9')

	#Creating inital password
	passw = random.randint(0, 1000000000)



	def pwd():
		msg = messagebox.showinfo('Password', passw)

	passwo = tk.Button(app, text = 'Show password', command = pwd, bg = '#3FF06F')
  #reloads passwords
	
	#packing widgets/continuing main loop
	ENCRPPASS.pack()
	RANDUSR.pack()
	SPCHARAC.pack()
	passwo.pack()
	app.mainloop()
