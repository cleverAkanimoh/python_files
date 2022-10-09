Python 3.9.7 (tags/v3.9.7:1016ef3, Aug 30 2021, 20:19:38) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> #Widgets
>>> from tkinter import*
>>> window=Tk()
>>> Img=PhotoImage(file='lotto.gif')
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    Img=PhotoImage(file='lotto.gif')
  File "C:\Users\DELL\AppData\Local\Programs\Python\Python39\lib\tkinter\__init__.py", line 4064, in __init__
    Image.__init__(self, 'photo', name, cnf, master, **kw)
  File "C:\Users\DELL\AppData\Local\Programs\Python\Python39\lib\tkinter\__init__.py", line 4009, in __init__
    self.tk.call(('image', 'create', imgtype, name,) + options)
_tkinter.TclError: couldn't open "lotto.gif": no such file or directory
>>> window.title('Crush Lotto')
''
>>> label1=Label(window,relief='groove',width=2)
>>> label2=Label(window,relief='groove',width=2)
>>> label3=Label(window,relief='groove',width=2)
>>> label4=Label(window,relief='groove',width=2)
>>> label5=Label(window,relief='groove',width=2)
>>> label6=Label(window,relief='groove',width=2)
>>> getBtn=Button(window)
>>> resBtn=Button(window)
>>> #Geometry:
>>> ImgLbi.grid()
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    ImgLbi.grid()
NameError: name 'ImgLbi' is not defined
>>> label1.grid()
>>> label2.grid()
>>> label3.grid()
>>> label4.grid()
>>> label5.grid()
>>> label6.grid()
>>> getBtn.grid()
>>> resBtn.grid()
>>> #Sustain Window:
>>> window.mainloop()
