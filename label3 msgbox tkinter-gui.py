import tkinter as tk
import tkinter.messagebox as msgbox
class Window(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('CRUSH APP')
        self.label_text=tk.StringVar()
        self.label_text.set('My name is:')

        self.name_text=tk.StringVar()
        
        self.label=tk.Label(self,textvar=self.name_text)
        self.label.pack(fill=tk.BOTH,expand=1,padx=100,pady=10)

        self.name_entry=tk.Entry(self,textvar=self.name_text)
        self.name_entry.pack(fill=tk.BOTH,expand=1,padx=20,pady=20)

        hello_button=tk.Button(self,text='Hello User',
                               command=self.say_hello)
        hello_button.pack(side=tk.LEFT,padx=(20,0),pady=(0,20))

        goodbye_button=tk.Button(self,text='Goodbye',
                              command=self.say_goodbye)
        goodbye_button.pack(side=tk.RIGHT,padx=(0,20),pady=(0,20))

    import tkinter.messagebox as msgbox    
    def say_hello(self):
        message='Hello there' + self.name_entry.get()
        msgbox.showinfo('Welcome',message)

    
    def say_goodbye(self):
        if msgbox.askyesno('Exit window?','Are you sure'):
            self.label_text.set('Goodbye! \n (Closing App in 5 Seconds)' + self.name_text.get())
            self.after(5000,self.destroy)
        else:
            msgbox.showinfo('Canceled','canceling...')


if __name__=='__main__':
    window=Window()
    window.mainloop()
