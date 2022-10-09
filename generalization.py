from tkinter import*
window=Tk()
window.title('GENERALIZATION')
''
label=Label(window,text='Hello world!')
label.pack(padx=400,pady=150)
import tkinter.messagebox as box
def dialog():
	var=box.askyesno('New box','proceed?')
	if var==1:
		box.showinfo('Yes Box','Proceeding...')
	else:
		box.showwarning('No Box','Canceling...')

		
btn=Button(window,text='Click',command=dialog)
btn.pack(padx=150,pady=50)
btn_end=Button(window,text='Close',command=exit)
def exit():
	var=box.askyesno('EXIT','Do you want to proceed?')
	if var==1:
		box.ABORT('Yes Box','Exiting')
	else:
		box.CANCEL('No Box','Canceling...')

		
btn.pack(padx=150,pady=50)
btn_end=Button(window,text='Close',command=exit)
btn.pack(padx=150,pady=50)
import tkinter.messagebox as box
def exit():
	var=box.askyesno('EXIT','Do you want to proceed?')
	if var==1:
		box.ABORT('Yes Box','Exiting')
	else:
		box.CANCEL('No Box','Canceling...')

		
btn_end=Button(window,text='Close',command=exit)
btn.pack(padx=150,pady=50)
btn_exit=Button(window,text='Close',command=exit)
btn=Button(window,text='Close',command=exit)
btn_end=Button(window,text='Close',command=exit)
btn_end.pack(padx=150,pady=30)
def tog():
	if window.cget('bg','fg')=='green':
		window.configure(bg='blue')
	else:
		window.configure(bg='green')

		
btn_tog=Button(window,text='Switch Background',command=tog)
btn_tog.pack(padx=150,pady=30)


def tog():
	if window.cget('bg')=='green':
		window.configure(bg='blue')
	else:
		window.configure(bg='green')


