import tkinter as tk
from tkinter import *
from tkinter import filedialog
from send_to_number import activate_wa, choose_list ,test_msg, send_whatsapp_msg, create_message
import pandas as pd
from time import sleep

root = Tk()

def get_chromedir():
    global chromedir
    chromedir =  chromedir_entry.get()
    myLabel = Label(root, text =chromedir)
    myLabel.grid(row = 3,column = 0)
    
def run_chrome():
    activate_wa(chromedir)

def get_sendlistdir():
    global send_list
    sendlistdir =  sendlistdir_entry.get()
    myLabel = Label(root, text =sendlistdir)
    myLabel.grid(row = 3,column = 0)
    send_list = choose_list(sendlistdir)

def print_in_app():
    #test_msg(send_list)
    msg = (send_list.loc[0,"0_1"]
            +send_list.loc[0,"field_1"] 
            +send_list.loc[0,"1_2"] 
            +send_list.loc[0,"field_2"] 
            +send_list.loc[0,"2_3"]
            +send_list.loc[0,"date"] 
            +send_list.loc[0,"3_4"]
            +send_list.loc[0,"time"] 
            +send_list.loc[0,"4_end"])
    msg = msg.replace ("\\n", "\n")
   
    msg_label = Label(root, text = msg)
    #target_label.grid(row = n+4,column = 0)
    msg_label.grid(row = 5,column = 1)


def get_send_status():
    send_status =  send_status_entry.get()
    myLabel = Label(root, text =send_status)
    myLabel.grid(row = 5,column = 0)
    choose_to_send(send_status, send_list)

chromedir_label = Label(root, text="specify chromedriver directory")
chromedir_entry = Entry(root)
chromedir_entry.insert(0,"./chromedriver.exe")
chromedir_button = Button(root, text="set", command=get_chromedir)
run_chrome_button = Button(root, text="Start Chrome", command=run_chrome)

sendlistdir_label = Label(root, text="specify send_list directory")
sendlistdir_entry = Entry(root)
sendlistdir_entry.insert(0,"./send_list.csv")
sendlistdir_button = Button(root, text="set", command=get_sendlistdir)

def get_template():
    template=textExample.get("1.0","end")
    print(template)

    input_spreadsheet = pd.read_csv("./send_list_1.csv", encoding ="cp1252")
    input_tuples = input_spreadsheet.to_records(index=False)
    input_list = list(input_tuples)

    for i,j in enumerate (input_list):
        mobile_no = input_spreadsheet.loc[i,"to"]
        message_text = create_message(template, *input_list[i])
        print (mobile_no, message_text)
        send_whatsapp_msg(mobile_no, message_text)


textExample=tk.Text(root, height=10)


btnRead=tk.Button(root, height=1, width=10, text="Read and send", 
                    command=get_template)


chromedir_label.grid(row = 0,column = 0)
chromedir_entry.grid(row = 0,column = 1)
chromedir_button.grid(row = 0,column = 2)

run_chrome_button.grid(row = 0,column = 3)

sendlistdir_label.grid(row = 1,column = 0)
sendlistdir_entry.grid(row = 1,column = 1)
sendlistdir_button.grid(row = 1,column = 2)

textExample.grid(row = 3,column = 1)
btnRead.grid(row = 4,column = 1)

# run the event loop
root.mainloop()