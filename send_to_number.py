from time import sleep
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
import socket
import pandas as pd

def element_presence(by,xpath,time):
    element_present = EC.presence_of_element_located((By.XPATH, xpath))
    WebDriverWait(driver, time).until(element_present)

def is_connected():
    try:
        # connect to the host -- tells us if the host is actually
        # reachable
        socket.create_connection(("www.google.com", 80))
        return True
    except :
        is_connected()

def choose_list(send_list_dir = "./send_list.csv"):
    send_list = pd.read_csv(send_list_dir)
    return send_list

def test_msg(send_list):
    print("Displaying messages to send......")

    for n, row in send_list.iterrows():
        target = send_list.loc[n,"to"]
        print("send to:", target)

        msg = (send_list.loc[0,"0_1"]
                +send_list.loc[n,"field_1"] 
                +send_list.loc[0,"1_2"] 
                +send_list.loc[n,"field_2"] 
                +send_list.loc[0,"2_3"]
                +send_list.loc[n,"date"] 
                +send_list.loc[0,"3_4"]
                +send_list.loc[n,"time"] 
                +send_list.loc[0,"4_end"])
        print("msg:", msg)

def send_whatsapp_msg(phone_no,text):
    driver.get("https://web.whatsapp.com/send?phone=65{}&source=&data=#".format(phone_no))
    try:
        driver.switch_to_alert().accept()
    except Exception as e:
        pass

    try:
        element_presence(By.XPATH,'//*[@id="main"]/footer/div[1]/div[2]/div/div[2]',30)
        txt_box=driver.find_element(By.XPATH , '//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')
        txt_box.send_keys(text)
        txt_box.send_keys("\n")

    except Exception as e:
        print("invalid phone no :"+str(phone_no))



def create_send_msg(send_list):
    for n, row in send_list.iterrows():
        mobile_no = send_list.loc[n,"to"]
        message_text = (send_list.loc[0,"0_1"]
                +send_list.loc[n,"field_1"] 
                +send_list.loc[0,"1_2"] 
                +send_list.loc[n,"field_2"] 
                +send_list.loc[0,"2_3"]
                +send_list.loc[n,"date"] 
                +send_list.loc[0,"3_4"]
                +send_list.loc[n,"time"] 
                +send_list.loc[0,"4_end"])


        try:
            send_whatsapp_msg(mobile_no,message_text)

        except Exception as e:
            sleep(10)
            is_connected()

def choose_to_send(user_answer, send_list):
    if user_answer == "yes":
        create_send_msg(send_list)
        driver.close()
    elif user_answer == "no":
        driver.close()
    else:
        print("Error: Answer must be 'yes' or 'no'")

def activate_wa(chromedriver_dir = "./chromedriver"): 
    global driver
    driver = webdriver.Chrome(chromedriver_dir)
    driver.get("https://web.whatsapp.com/")
    sleep(10)


if __name__ == "__main__":
    # driver = webdriver.Chrome(executable_path="chromedriver.exe")
    # driver.get("http://web.whatsapp.com")
    # sleep(10) #wait time to scan the code in second
    activate_wa()
    send_list = choose_list()
    test_msg(send_list)
    user_answer = input("send message? input yes or no: ").lower().strip()
    choose_to_send(user_answer, send_list)

    
    