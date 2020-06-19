from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import sys
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import datetime
import time
import pandas as pd

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

def send_to_wa(send_list,driver, wait):
    for n, row in send_list.iterrows():
        target = send_list.loc[n,"to"]
        print("send to:", target)

        x_arg = '//span[contains(@title,' +'"' +target+ '"' +')]' #.decode('utf-8') 
        print (x_arg)
        group_title = wait.until(EC.presence_of_element_located((
            By.XPATH, x_arg)))
        group_title.click()

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

        # message = driver.find_element_by_class_name('_2FVVk')
        message = driver.find_element_by_xpath('/html/body/div[1]/div/div/div[4]/div/footer/div[1]/div[2]/div')
        message.send_keys(msg)
        time.sleep(1)

        #sendbutton = driver.find_element_by_class_name('._1U1xa')
        sendbutton =driver.find_element_by_xpath('/html/body/div[1]/div/div/div[4]/div/footer/div[1]/div[3]/button')
        sendbutton.click()
        time.sleep(1)


def choose_to_send(user_answer, send_list):
    if user_answer == "yes":
        send_to_wa(send_list,driver, wait)
        driver.close()
    elif user_answer == "no":
        driver.close()
    else:
        print("Error: Answer must be 'yes' or 'no'")
        


#print(targets)
def activate_wa(chromedriver_dir = "./chromedriver"): 
    global driver, wait, wait5
    driver = webdriver.Chrome(chromedriver_dir)
    driver.get("https://web.whatsapp.com/")
    wait = WebDriverWait(driver, 600)
    wait5 = WebDriverWait(driver, 5)


def choose_list(send_list_dir = "./send_list.csv"):
    send_list = pd.read_csv(send_list_dir)
    return send_list
    

if __name__ == "__main__":
    activate_wa()
    send_list = choose_list('send_list_2.csv')
    test_msg(send_list)
    user_answer = input("send message? input yes or no: ").lower().strip()
    choose_to_send(user_answer, send_list)
    
    


