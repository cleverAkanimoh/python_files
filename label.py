from tkinter import*
window=Tk()
window.title('Hello Tkinter')

label=Label(window,text='Choose One')
label.pack(fill=BOTH,expand=1,padx=100,pady=30)

hello_button=Button(window,text='Say Hello')
hello_button.pack(side=LEFT,padx=(20,0),pady=(0,20))

goodbye_button=Button(window,text='Say Goodbye')
goodbye_button.pack(side=RIGHT,padx=(0,20),pady=(0,20))

hello_button.configure(text='Hello World! Welcome To Crush App',command=hello_button)

goodbye_button.configure(text='Goodbye!\n (Closing in 2 Seconds)',command=goodbye_button)

def hello_button():
    label.configure(text='Hello World! Welcome To Crush App')

def goodbye_button():
    after(2000,window.destroy)
