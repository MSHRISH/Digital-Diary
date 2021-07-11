#modules imported
from tkinter import*
import os
from tkinter import messagebox


class window(Frame):
	'''This class contains the widgets that allows the user to read the files stored previously'''
	def __init__(self,master=None):
		#intilisation of the frame
		Frame.__init__(self,master)
		self.master=master
		self.master.title("Diary")
		self.master.geometry("400x300")

		#Display all the files present in the directory
		Label(self.master,text="Select a file").pack(side=TOP)
		path="#path"
		self.file_names=os.listdir(path)
		self.srch_box=Entry(self.master)
		self.srch_box.pack()
		file_list=Listbox(self.master)
		file_list.pack()
		for i in range(0,len(self.file_names)):
			a=str(i+1)+") "+self.file_names[i]
			file_list.insert(END,a)

		#Read button binded to the function "read_file" which displays the content in the file.
		read_button=Button(self.master,text="Read",width=20,command=self.read_file).pack(side=BOTTOM)
	def read_file(self):
		self.file_name=self.srch_box.get()

		'''If the specified file is present it is displayed in a text
		 for the user to read.If the specified file is not present it 
		 displays an error'''
		if(self.file_name in self.file_names ):
			f=open(self.file_name,"r")
			contents=f.read()
			read_window=Tk()
			read_window.title(self.file_name)
			t=Text(read_window)
			t.pack()
			t.insert("end",contents)
			t.config(state=DISABLED)
			read_window.mainloop()
		else:
			messagebox.showinf0("Diary","File doesn't exist")
			
		

