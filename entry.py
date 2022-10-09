Python 3.9.7 (tags/v3.9.7:1016ef3, Aug 30 2021, 20:19:38) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> from tkinter import*
>>> import tkinter.messagebox as box
>>> window=Tk()
>>> window.title('crushapp Entry')
''
>>> frame=Frame(window)
>>> entry=Entry(frame)
>>> def dialog():
	box.showinfo('Greetings','Welcome'+entry.get())

	
>>> btn=Button(frame,text='Please Enter Name',command=dialog)
>>> btn.pack(side=RIGHT,padx=5)
>>> entry.pack(side=LEFT)
>>> frame.pack(padx=25,pady=25)
>>> window.mainloop()