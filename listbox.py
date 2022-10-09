Python 3.9.7 (tags/v3.9.7:1016ef3, Aug 30 2021, 20:19:38) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> from tkinter import*
>>> import tkinter.messagebox as box
>>> window=Tk()
>>> window.title('CrushApp Listbox')
''
>>> frame=Frame(window)
>>> listbox=Listbox(frame)
>>> listbox.insert(1,'HTML5 In crushing steps')
>>> listbox.insert(2,'CSS3 In crushing steps')
>>> listbox.insert(3,'JavaScript In crushing steps')
>>> def dialog():
	box.showinfo('Selection','Your Choice:'+\
	listbox.get(listbox.curselection()))

	
>>> btn=Button(frame,text='Choose',command=dialog)
>>> btn.pack(side=RIGHT,padx=5)
>>> listbox.pack(side=LEFT)
>>> frame.pack(padx=30,pady=30)
>>> window.mainloop()
