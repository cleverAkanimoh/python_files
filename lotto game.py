#widget
from tkinter import*
from turtle import bgpic
window=Tk()
window.title('Crush Lotto')
''
window.configure(bg="teal")

label=Label(window)
getBtn=Button(window)
exitBtn=Button(window)

label.grid(row=0,column=3,columnspan=2,padx=100,pady=100)
getBtn.grid(row=3,column=3,columnspan=2,padx=100,pady=100)
exitBtn.grid(row=5,column=3,columnspan=2,padx=100,pady=100)

window.resizable(0,0)
''
label.configure(text='WELCOME TO CRUSH LOTTO \t Enjoy')
getBtn.configure(text='Click here to play game')
exitBtn.configure(text='Exit game')


def play_game():
	window=Toplevel()
	window.title("Play Game")
	window.configure(bg="teal")
	label=Label(window)
	label1=Label(window,relief='groove',width=4)
	label2=Label(window,relief='groove',width=4)
	label3=Label(window,relief='groove',width=4)
	label4=Label(window,relief='groove',width=4)
	label5=Label(window,relief='groove',width=4)
	label6=Label(window,relief='groove',width=4)
	getBtn=Button(window)
	resBtn=Button(window)
	togBtn=Button(window)
	
	#Geometry:
	label.grid(row=0,column=3,columnspan=3,pady=50)
	label1.grid(row=1,column=2,padx=50,pady=50)
	label2.grid(row=1,column=3,padx=50,pady=50)
	label3.grid(row=1,column=4,padx=50,pady=50)
	label4.grid(row=1,column=5,padx=50,pady=50)
	label5.grid(row=1,column=6,padx=50,pady=50)
	label6.grid(row=1,column=7,padx=50,pady=50)
	getBtn.grid(row=3,column=3,columnspan=2,padx=50,pady=50)
	resBtn.grid(row=3,column=5,columnspan=2,padx=50,pady=50)
	togBtn.grid(row=5,column=4,columnspan=2,padx=50,pady=50)

	#Static Properties:
	window.resizable(0,0)
	''
	label.configure(text="Please Enjoy the Game")
	getBtn.configure(text='Get My Lucky Numbers')
	resBtn.configure(text='Reset Values')
	togBtn.configure(text='Change Background')
	#Initial Properties:
	
	label.configure(text="Please Enjoy the Game")
	label1.configure(text='.?.')
	label2.configure(text='.?.')
	label3.configure(text='.?.')
	label4.configure(text='.?.')
	label5.configure(text='.?.')
	label6.configure(text='.?.')
	resBtn.configure(state=DISABLED)

	#Dynamic Properties:
	from random import sample
	def pick():
		nums=sample(range(1,100),6)
		label1.configure(text=nums[0])
		label2.configure(text=nums[1])
		label3.configure(text=nums[2])
		label4.configure(text=nums[3])
		label5.configure(text=nums[4])
		label6.configure(text=nums[5])
		label.configure(text="Values has been gotten")
		getBtn.configure(state=DISABLED)
		resBtn.configure(state=NORMAL)
		togBtn.configure(state=NORMAL)

	def reset():
		label1.configure(text='.?.')
		label2.configure(text='.?.')
		label3.configure(text='.?.')
		label4.configure(text='.?.')
		label5.configure(text='.?.')
		label6.configure(text='.?.')
		label.configure(text="Reseting Values...")
		getBtn.configure(state=NORMAL)
		resBtn.configure(state=DISABLED)
		togBtn.configure(state=NORMAL)

		
	def tog():
		if window.cget('bg')=='orange':
			window.configure(bg='teal')
		else:
			window.configure(bg='orange')

		label.configure(text="background color changed!")
		
	getBtn.configure(command=pick)
	resBtn.configure(command=reset)
	togBtn.configure(command=tog)

import tkinter.messagebox as msgbox
def exit():
		if msgbox.askyesno('Exiting Game','Are you sure you want to proceed?'):
			label.configure(text='please wait! \t (Game will be exited in 5 Seconds)')
			window.after(5000,window.destroy)
		else:
			msgbox.showinfo('Exit Canceled','Enjoy! \t Game Exit has been canceled...')
			label.configure(text='Continue Playing! \t Game Exit has been canceled...')

getBtn.configure(command=play_game)
exitBtn.configure(command=exit)

#Sustain window:
window.mainloop()
