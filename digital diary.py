# modules used
from tkinter import *
from tkinter import messagebox
import os
import time


# A class that consists the widgets of login page
class journal(Frame):
    # initating frame of window.Basic tkinter stuff.
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master
        self.security()

    # function that holds the widgets of login window
    def security(self):
        self.master.title("LOGIN")
        self.pack(fill=BOTH, expand=1)
        lbl = Label(self, text="PASSWORD").grid(column=0, row=0)

        # Entry to get a input from the user
        self.pwrd = Entry(self, show="*")
        self.pwrd.grid(column=1, row=0)
        # login button binded to a function named login
        login = Button(self, text="login", width=20, command=self.login)
        login.grid(column=1, row=2)

    # function that checks whether the given password is correct
    def login(self):
        # if the password given is correct the following get executed
        if self.pwrd.get() == "PASSWORD": #pls provide your password here
            # destroys the present login window
            a.destroy()

            # initiates the main application
            b = Tk()
            b.geometry("500x500")
            app_b = journal2(b)  # journal2 is a class mention bellow
            app_b.mainloop()  # mainloop for the program should run until we close
            # Note  this is the mainloop of our main application

        # if the given password is wrong then an error is shown
        else:
            messagebox.showinfo("ERROR ", "retry wrong password")


# class which contains contents of our application
class journal2(Frame):
    # initating frame of window.Basic tkinter stuff.
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master
        self.application()

    # function that holds the widgets of the application.
    def application(self):
        self.master.title("DIARY")
        self.pack(fill=BOTH, expand=1)

        # our main window conceals only three buttons with specific function
        # i hope that these three buttons imitate the things we could do with a
        # actual diary.

        # button which opens a window in which the user can write and save his thoughts
        # this button is bonded to a function named write
        button = Button(self, text="WRITE", width=100, height=10, command=self.write)
        button.pack()

        # button opens a window which allows the user to append any information to his files.
        # button bonded with function named append
        button_ap = Button(self, text="APPEND", width=100, height=10, command=self.append)
        button_ap.pack()

        # button which allows the user to only read his previously saved files.
        # button bonded with function named read
        button2 = Button(self, text="READ", width=100, height=10, command=self.read)
        button2.pack()

    # a function that opens another window allowing the user to write in it.
    def write(self):
        # this window consists of three widgets.
        # a text widget,a scrollbar and a button

        # initiating another window which holds the following widgets
        self.w = Tk()
        self.w.title("DIARY")

        # scrollbar
        scrollbar = Scrollbar(self.w).pack(side=RIGHT, fill=Y)

        # text widget in which the user can type his thoughts
        self.content_box = Text(self.w)
        self.content_box.pack()

        # button which saves the information as text file in the preferres location
        # button bonded with function named save_file
        save_button = Button(self.w, text="SAVE", width=10, command=self.save_file)
        save_button.pack()

        # mainloop of this window
        self.w.mainloop()

    # a function whivh saves the information given in the above write window.
    def save_file(self):

        # i prefer to keep the name of my file as the date in which it was typed
        # so in this part i'm extracting the date
        localtime = time.asctime(time.localtime(time.time()))
        date = localtime[8:11]
        month = localtime[4:7]
        year = localtime[20:24]

        # name of the file
        file_name = date + month + year + ".txt"

        # opening the file to write in it
        f = open(file_name, "w+")

        # saving the information given by user in the file
        f.write(self.content_box.get("1.0", END))

        # destroys the write window
        self.w.destroy()

    # function that allows the user to read the files he had previously saved
    def read(self):
        # iniates a window which consist of a entry widget to get the name of file
        # which the user wants to read
        # this windows also consists of list of every files which the user had saved
        R = Tk()
        R.title("DIARY")
        R.geometry("500x500")
        Label(R, text="SEARCH FOR A FILE IN THE LIST").pack(side=TOP)

        # entry widget
        self.search_box = Entry(R)
        self.search_box.pack(side=TOP)

        # Path of the folder in which your files are saved
        path = "PATH"  #pls specify your path here

        #list of all files in the given path
        file_names = os.listdir(path)

        #lidtbox to display all the existing file in the provided path
        file_list = Listbox(R, height=10)
        file_list.pack()

        #loop to insert every file in the listbox
        for i in range(0, len(file_names)):
            file_list.insert(END, file_names[i])

        #button which displays file specified in the entry
        #button bonded with function named read_file
        #read_file actually diaplay the file
        read_button = Button(R, text="OPEN", command=self.read_file).pack(side=BOTTOM)

        #mainloop of this window
        R.mainloop()

    #A function whixh disaplays the file selected by the user
    def read_file(self):

        #getting the file name from above entry
        file_name = self.search_box.get()

        #Path of the folder
        path = "PATH"  #pls specify your path here

        #list of files in that folder
        file_names = os.listdir(path)

        #if the file name given in the entry is present in the folder
        #then the file is displayed
        #note the user can only read the file
        #the user could not alter the file
        if file_name in file_names:

            #opens the file in read mode
            f = open(file_name, "r")

            #the contents in the file
            contents = f.read()

            #this is another window in which the information in the file
            #is shown in a text box.
            W = Tk()
            W.title("file_name")

            #text widget
            t = Text(W)
            t.pack()

            #inserting the content into the widget
            t.insert("end", contents)

            #the state of the text is disabled so that no one can modify the information.
            #as mentioned before the user could only read the file
            t.config(state=DISABLED)

            #mainloop of this window
            W.mainloop()

        #if the filename given in the entry box is not given properly or the file isn't
        #present in the folder specified by the user then shows a error msg
        else:
            messagebox.showinfo("ERROR", "PLEASE TYPE THE FILE NAME PROPERLY")

    #this function allows the user to edit any file saved previously
    #For security reasons i have added another login system to this function.
    #I did  this so that no one could edit the files except the user.
    #It means that when the user selects append button in the main window
    #he/she must type his/her password again to gain access to edit the files.
    def append(self):
        #This is part where you would need some little bit more concentration
        # as the code gets complex.
        #This is a function which consist of a class.
        #The class is nothing but a window that holds the login system.
        #Note this login system stands as a security for editing the files.
        class Append_security(Frame):
            #initiating the login window
            #we are just reiterating the function we start at the beginning of the code
            def __init__(self, master=None):
                Frame.__init__(self, master)
                self.master = master
                self.edit_security()

            def edit_security(self):
                self.pack(fill=BOTH, expand=1)
                self.master.title("LOGIN")
                lbl = Label(self, text="PASSWORD").grid(column=0, row=0)

                #Entry wiget to type password
                self.pwrd = Entry(self, show="*")
                self.pwrd.grid(column=1, row=0)

                #Button which checks the password with a function named append_login
                login = Button(self, text="login", width=20, command=self.append_login)
                login.grid(column=1, row=2)

            #function that checks the password
            def append_login(self):
                #if the password is correct it opens a window in which useer could edit
                #any file.
                if self.pwrd.get() == "PASSWORD": #pls provide your own password here

                    #destroys the login window
                    root.destroy()

                    #initiating a window which allows to edit files
                    A = Tk()
                    boot = Append(A)      #Append is a class which is mentioned below
                    A.geometry("500x500")
                    boot.mainloop()#mainloop of the window which allows to edit files

                #if the password provided is wrong a error msg is shown
                else:
                    messagebox.showinfo("ERROR", "WRONG PASSWORD")


        #This initiates our login window
        #Note that it doesnt initiate the login window of our main application
        #It iniates the login window which is mention in the Append_security class.
        #Thus we have added a extra layer of security so that only user can edit the files.
        #
        root = Tk()
        proto = Append_security(root)
        proto.mainloop() #mainloop of the login window

#this class conceals the widgets which allows the user to edit the files
class Append(Frame):
    #initialisation
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master
        self.edit()
    #function which consists the widgets
    #This window consists of a entry box and list box
    #the listbox displays every file that could be edited by the user
    #This is almost similar to the one we did in read function
    def edit(self):
        self.master.title("DIARY")
        self.pack(fill=BOTH, expand=1)
        Label(self, text="SEARCH").pack()

        #entry box
        self.file_entry = Entry(self)
        self.file_entry.pack()

        #Path of the folder
        path = "PATH"  #pls specify your path here

        #list of all files in the specified path
        file_names = os.listdir(path)

        #listbox
        file_list = Listbox(self, height=10)
        file_list.pack()

        #displaying every files in the specified path
        for i in range(0, len(file_names)):
            file_list.insert(END, file_names[i])

        #A button which opens the file specified in the entry box for editing
        #bonded with a function named main_edit
        edit_button = Button(self, text="EDIT", command=self.main_edit).pack()

    #function opens the file speified in the entry box
    def main_edit(self):
        #path
        path = "PATH"   #pls specify your path here
        #list of the files in the path
        file_names = os.listdir(path)

        #file name specified in the entry box
        file_name = self.file_entry.get()

        #if the file name specified is present the following is executed
        if self.file_entry.get() in file_names:
            #opens the file in read mode
            f = open(file_name, "r")

            #contents in the file
            contents = f.read()

            #New window which allows us to edit the content
            #the new window consists of teaxt box and a button
            S = Tk()
            S.title("DIARY")
            #Text box
            t = Text(S)
            t.pack()
            #inserting the contents in the textbox
            t.insert("end", contents)

            #Function that saves the  edited file
            #this function is bonded with button mention below
            def save_edit():

                #opens the file specified in the entry box in write
                F = open(self.file_entry.get(), "w+")
                #saves the edit file by getting the information from text box
                F.write(t.get("1.0", END))
                #destroys this window after saving the file
                S.destroy()
             #the button mention above
            Button(S, text="SAVE", command=save_edit).pack()

            #mainloop of this window
            S.mainloop()
        #if the file name specified in the entry box is not proper error is shown
        else:
            messagebox.showinfo("ERROR", "PLEASE TYPE THE FILE NAME PROPERLY")

#function to change the directory
def directory():
    path = "PATH"   #pls specify your path here
    os.chdir(path)

#fn call
directory()

#final part of the code but this is where we call our very first class
#initiates the fisrt login window
a = Tk()
a.geometry("250x50")
app = journal(a)
app.mainloop()#mainloop of the login window
