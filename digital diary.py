 #Modules used 
 #These modules are inbuilt python modules.
from tkinter import*
from tkinter import messagebox
import os
import time

#These modules are user defined python modules.Each module has its own function.
import write_func
import read_func
import edit_func

def directory():
    '''This function sets the directory to the defined path.This path 
    is where all your files will be saved.'''
    path="#path"
    os.chdir(path)
directory()



class login_interface(Frame):
    '''This class contains the login section of the app.The user have 
    to enter a password to access the main application.'''
    def __init__(self,master=None):
        #initiating the frame
        Frame.__init__(self,master)
        self.master=master
        self.security()

    #function that holds the widgets of login window
    def security(self):
        self.master.title("LOGIN")
        self.pack(fill=BOTH, expand=1)
        lbl = Label(self, text="PASSWORD").grid(column=0, row=0)

        # Entry to get a input from the user
        self.pwrd = Entry(self,show="*")
        self.pwrd.focus_set()
        self.pwrd.grid(column=1, row=0)

        #login button binded to a function named login
        login = Button(self, text="login", width=20,command=self.login)
        login.grid(column=1, row=2)

    
    def login(self):
        '''this function which is binded to the "login" Button checks if the
        password given by the user.If it is correct it directs the user to main application'''

        #if the password given is correct the following get executed
        if self.pwrd.get()=="#Your_password":
            #destroys the present login window
            a.destroy()

            #initiates the main application
            b=Tk()
            b.geometry("500x500")
            app_b=journal(b)  #journal is a class mention bellow
            app_b.mainloop()  #mainloop for the program should run until we close
                              #Note  this is the mainloop of our main application

        #if the given password is wrong then an error is shown
        else:
            messagebox.showinfo("ERROR ","retry wrong password")

class journal(Frame):
    '''this class contains the frame and widgets which make up the main application.
    Main application contains three buttons Write,read,Edit respectively.'''

    #initating frame of window
    def __init__(self,master=None):
        Frame.__init__(self,master)
        self.master=master

        self.master.title("DIARY")
        self.pack(fill=BOTH, expand=1)

        #write button binded to write function.
        write_button=Button(self,text="Write",width=100,height=10,command=self.write)
        write_button.pack()

        #Read button binded to read function.
        read_button=Button(self,text="Read",width=100,height=10,command=self.read)
        read_button.pack()

        #Edit button binded to edit function.
        edit_button=Button(self,text="Edit",width=100,height=10,command=self.edit)
        edit_button.pack()

    def write(self):
        '''this function calls the function defined in the "write_func" module.This module is an user defined module.
        This module enables user to write their thoughts and save it in the respective directory.'''

    	a=Tk()
    	B=write_func.window(a)
    	B.mainloop()

    def read(self):
        '''This function calls the function defined in the "read_func" module.This module is an user defined module.
        This module enables user to read the files they have saved previously.'''

    	a=Tk()
    	B=read_func.window(a)
    	B.mainloop()    	

    def edit(self):
        '''this function calls the function defined in the "edit_func" module.This module is an user defined module.
        This module enables the user to revisit and edit the files they have saved previously.'''

    	a=Tk()
    	B=edit_func.window(a)
    	B.mainloop()

        


'''Creating the instance of the login class and running the program'''
a=Tk()
a.geometry("250x50")
app=login_interface(a)
app.mainloop()    
