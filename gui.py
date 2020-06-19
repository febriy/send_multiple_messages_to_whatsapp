from tkinter import *
from tkinter import filedialog
from wa_send import activate_wa, choose_list ,test_msg,send_to_wa, choose_to_send


root = Tk()

def get_chromedir():
    global chromedir
    chromedir =  chromedir_entry.get()
    myLabel = Label(root, text =chromedir)
    myLabel.grid(row = 3,column = 0)
    
def run_chrome():
    global driver, wait, wait5
    driver, wait, wait5 = activate_wa(chromedir)

def get_sendlistdir():
    global send_list
    sendlistdir =  sendlistdir_entry.get()
    myLabel = Label(root, text =sendlistdir)
    myLabel.grid(row = 3,column = 0)
    send_list = choose_list(sendlistdir)

def print_in_app():
    #test_msg(send_list)
    for n, row in send_list.iterrows():
        target_label = Label(root, text = send_list.loc[n,"to"])

        msg = (send_list.loc[0,"0_1"]
                +send_list.loc[n,"field_1"] 
                +send_list.loc[0,"1_2"] 
                +send_list.loc[n,"field_2"] 
                +send_list.loc[0,"2_3"]
                +send_list.loc[n,"date"] 
                +send_list.loc[0,"3_4"]
                +send_list.loc[n,"time"] 
                +send_list.loc[0,"4_end"])
        msg_label = Label(root, text = msg)
        target_label.grid(row = n+4,column = 0)
        msg_label.grid(row = n+4,column = 1)


def get_send_status():
    send_status =  send_status_entry.get()
    myLabel = Label(root, text =send_status)
    myLabel.grid(row = 3,column = 0)
    choose_to_send(send_status, send_list,driver, wait)

chromedir_label = Label(root, text="specify chromedriver directory")
chromedir_entry = Entry(root)
chromedir_entry.insert(0,"./chromedriver.exe")
chromedir_button = Button(root, text="set", command=get_chromedir)
run_chrome_button = Button(root, text="Start Chrome", command=run_chrome)

sendlistdir_label = Label(root, text="specify send_list directory")
sendlistdir_entry = Entry(root)
sendlistdir_entry.insert(0,"./send_list.csv")
sendlistdir_button = Button(root, text="set", command=get_sendlistdir)
test_msg_button = Button(root, text="Test message", command=print_in_app)


label = Label(root, text="Send messages? type 'yes' or 'no'")
send_status_entry = Entry(root)
send_status_button = Button(root, text="yes/no", command=get_send_status)

chromedir_label.grid(row = 0,column = 0)
chromedir_entry.grid(row = 0,column = 1)
chromedir_button.grid(row = 0,column = 2)

run_chrome_button.grid(row = 0,column = 3)

sendlistdir_label.grid(row = 1,column = 0)
sendlistdir_entry.grid(row = 1,column = 1)
sendlistdir_button.grid(row = 1,column = 2)
test_msg_button.grid(row = 1,column = 3)

label.grid(row = 2,column = 0)
send_status_entry.grid(row = 2,column = 1)
send_status_button.grid(row = 2,column = 2)

# run the event loop
root.mainloop()