import tkinter as tk
import tkinter.messagebox as msgbox
class Window(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('CRUSH APP')

        self.label=tk.Label(self,text='Select Any Button')
        self.label.pack(fill=tk.BOTH,expand=1,padx=100,pady=30)

        hello_button=tk.Button(self,text='Hello User',
                               command=self.say_hello)
        hello_button.pack(side=tk.LEFT,padx=(20,0),pady=(0,20))

        goodbye_button=tk.Button(self,text='Goodbye',
                              command=self.say_goodbye)
        goodbye_button.pack(side=tk.RIGHT,padx=(0,20),pady=(0,20))

    import tkinter.messagebox as msgbox    
    def say_hello(self):
        msgbox.showinfo('Welcome','I am happy you are here')

    
    def say_goodbye(self):
        if msgbox.askyesno('Exit window?','are you sure'):
            self.label.configure(text='Goodbye! \n (Closing App in 5 Seconds)')
            self.after(5000,self.destroy)
        else:
            msgbox.showinfo('Canceled','canceling...')


if __name__=='__main__':
    window=Window()
    window.mainloop()
