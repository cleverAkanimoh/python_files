Python 3.9.7 (tags/v3.9.7:1016ef3, Aug 30 2021, 20:19:38) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> from tkinter import*
>>> window=Tk()
>>> window.title('another button sample')
''
>>> btn_end=Button(window,text='close',command=exit)
>>> def tog():
	if window.cget('bg')== 'red':
		window.configure(bg='blue')
	else:
		window.configure(bg='red')

		
>>> btn_tog=Button(window,text='switch',command=tog)
>>> btn_end.pack(padx=200,pady=25)
>>> btn_tog.pack(padx=200,pady=25)
>>> window.mainloop()
