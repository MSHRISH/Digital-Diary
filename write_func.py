#moules imported
from tkinter import*
import time
import os
from tkinter import messagebox

def directory():
	'''This function sets the directory to the defined path.This path 
    is where all your files will be saved.'''
    path="#Path"
    os.chdir(path)
directory()



class window(Frame):
	'''This class contains the widgets that will allow user to write into files'''
	def __init__(self,master=None):
		#intialisation of the frame
		Frame.__init__(self,master)
		self.master=master
		self.master.title("Diary")
		title=Label(self.master,text="Title").pack()

		#Entry box to get titile of the file from the user.
		self.title_box=Entry(self.master)
		self.title_box.pack()

		scrollbar=Scrollbar(self.master).pack(side=RIGHT,fill=Y)#scrollbar
		Label(self.master,text="Content").pack()

		#Text for the user to write his thoughts
		self.content_box=Text(self.master)
		self.content_box.pack()
		
		#This button is binded to the function "save_file" wich saves the file in the specified path'''
		save_button=Button(self.master,text="Save",width=10,command=self.save_file).pack()

	def save_file(self):
		'''This function saves the content written by the user as a text file'''
		
		localtime=time.asctime(time.localtime(time.time()))
		date=localtime[8:11]
		month=localtime[4:7]
		year=localtime[20:24]
		file_name=self.title_box.get()+" "+date+month+year+".txt"
		f=open(file_name,"w+")
		f.write(self.content_box.get("1.0",END))
		messagebox.showinfo("Diary","Your file is saved successfully!! ")






