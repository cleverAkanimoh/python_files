>>> from tkinter import*
>>> import tkinter.messagebox as box
>>> window=Tk()
>>> window.title('button response')
''
>>> def dialog():
	var=box.askyesno('Message Box','Proceed?') if var==1:
		box.showinfo('Yes Box','Proceeding')
	else:
		box.showwarning('No Box','Terminating...')

		
>>> btn=Button(window,text='Push',command=dialog)
>>> btn.pack(padx=200,pady=50)
>>> 
