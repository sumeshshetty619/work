from tkinter import *
import random
import string
import ctypes
def run_on_click():
	user_input = var1.get()
	#print(user_input)
	#var.set("")
	#label = Label(root, text=user_input,bg="red",width="100").grid(row=4)
	if user_input==rand:
		import os 
		root.destroy()  & os.system('python hel.pyw')   
		

	elif user_input=="suma":
		root.destroy()
def over():
	root.destroy()


def randomStringDigits(stringLength=6):
    """Generate a random string of letters and digits """
    lettersAndDigits = string.ascii_letters + string.digits
    return ''.join(random.choice(lettersAndDigits) for i in range(stringLength))
    
def disable_event():
    pass


def countdown(count):
    # change text in label        
    label1['text'] = count

    if count > 0:
        # call countdown again after 1000ms (1s)
        root.after(1000, countdown, count-1)
    if count==0:
    	label1['text']='Times Up'
    	ctypes.windll.user32.LockWorkStation()

root = Tk() 
root.title("Captcha")
#w=Label(root, text='Enter Captcha for further using system!',width="100") 
#k=Label(root, text='CAPTCH',width="50",height="50") 

#root.config(cursor="none")
root.attributes("-fullscreen", True) 
#root.overrideredirect(True)   
root.protocol("WM_DELETE_WINDOW", disable_event)
#w.pack() 
Label(root, text='Enter Captcha for further using system esle system will shut down in 10 sec!',width="100").grid(row=0) 
label1=Label(root, text="", width=10)
label1.place(x=35, y=15)
countdown(60)
rand=randomStringDigits(5)
Label(root, text=rand).grid(row=1)
var1=StringVar() 
e1 = Entry(root,textvariable=var1) 
#e2 = Entry(root) 
e1.grid(row=2, column=0)
#k=e1.get()
#print("hello")

#e2.grid(row=1, column=1)
redbutton = Button(root, text = 'Done', fg ='Black',width="80",bg="red",command=run_on_click).grid(row=3)

#Label(root, text="press green button to continue").grid(row=5)

#redbutton = Button(root, text = 'Black', fg ='green',width="80",bg="green",command=over).grid(row=6)

#redbutton.pack( side = LEFT) 
root.mainloop() 