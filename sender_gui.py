from tkinter import *
from tkinter import filedialog
from send_to_number import activate_wa, choose_list, send_whatsapp_msg, create_message
import pandas as pd

root = Tk()
root.title("Personalised Message Sender")
#root.wm_iconbitmap('icon.ico')
myLabel = Label(root)

def get_chromedir():
    global chromedir, myLabel
    myLabel.destroy()
    chromedir = chromedir_entry.get()
    myLabel = Label(root, text =chromedir)
    myLabel.grid(row = 0,column = 4)
    
def run_chrome():
    activate_wa(chromedir)

def get_sendlistdir():
    global input_spreadsheet,input_list, myLabel
    myLabel.destroy()

    sendlistdir =  sendlistdir_entry.get()
    myLabel = Label(root, text =sendlistdir)
    myLabel.grid(row = 1,column = 4)
    input_spreadsheet, input_list = choose_list(sendlistdir)

def send_template_messages():
    template=template_box.get("1.0","end")

    for i,j in enumerate (input_list):
        mobile_no = input_spreadsheet.loc[i,"to"]
        message_text = create_message(template, *input_list[i])
        send_whatsapp_msg(mobile_no, message_text)

def show_samples():
    template=template_box.get("1.0","end")
    test_box = Text(root, width=50)
    test_box.grid(row = 4,column = 1)

    for i,j in enumerate (input_list):
        mobile_no = input_spreadsheet.loc[i,"to"]
        message_text = create_message(template, *input_list[i])
        test_box.insert(END, "Send to: {} \nMessage:\n{} \n---------------\n".format(mobile_no, message_text))

#Chromedriver directory
chromedir_label = Label(root, text="Input Chromedriver Directory")
chromedir_entry = Entry(root, width=66)
chromedir_entry.insert(0,"./chromedriver.exe")
chromedir_button = Button(root, height=1, width=10,text="Set", command=get_chromedir)
run_chrome_button = Button(root, height=1, width=10,text="Start Chrome", command=run_chrome)

#Spreadsheet directory
sendlistdir_label = Label(root, text="Input Spreadsheet Directory")
sendlistdir_entry = Entry(root, width=66)
sendlistdir_entry.insert(0,"./spreadsheet.csv")
sendlistdir_button = Button(root, height=1, width=10,text="Set", command=get_sendlistdir)

#Template box
template_box=Text(root, height=10, width=50)
read_btn=Button(root, height=1, width=10, text="Test", 
                    command=show_samples)
read_send_btn=Button(root, height=1, width=10, text="Send", 
                    command=send_template_messages)

#Placements with grid
chromedir_label.grid(row = 0,column = 0)
chromedir_entry.grid(row = 0,column = 1)
chromedir_button.grid(row = 0,column = 2)

run_chrome_button.grid(row = 0,column = 3)

sendlistdir_label.grid(row = 1,column = 0)
sendlistdir_entry.grid(row = 1,column = 1)
sendlistdir_button.grid(row = 1,column = 2)

template_box.grid(row = 3,column = 1)
read_btn.grid(row = 3,column = 0)
read_send_btn.grid(row = 3,column = 2)

#Run the event loop
root.mainloop()