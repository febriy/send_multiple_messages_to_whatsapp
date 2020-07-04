from time import sleep
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver import ActionChains
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
    input_spreadsheet = pd.read_csv(send_list_dir, encoding ="cp1252")
    input_tuples = input_spreadsheet.to_records(index=False)
    input_list = list(input_tuples)
    return input_spreadsheet, input_list

def send_whatsapp_msg(phone_no,text):
    driver.get("https://web.whatsapp.com/send?phone=65{}&source=&data=#".format(phone_no))
    try:
        driver.switch_to_alert().accept()
    except Exception as e:
        pass

    try:
        element_presence(By.XPATH,'//*[@id="main"]/footer/div[1]/div[2]/div/div[2]',30)
        #txt_box=driver.find_element(By.XPATH , '//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')
        #txt_box.send_keys(text)

        driver.find_element(By.XPATH , '//*[@id="main"]/footer/div[1]/div[2]/div/div[2]').click()

        for line in text.split('\n'):
            ActionChains(driver).send_keys(line).perform()
            ActionChains(driver).key_down(Keys.SHIFT).key_down(Keys.ENTER).key_up(Keys.SHIFT).key_up(Keys.ENTER).perform()
        ActionChains(driver).send_keys(Keys.RETURN).perform()

    except Exception as e:
        print("invalid phone no :"+str(phone_no))

def create_message(template, *arg):
    message = template.format(*arg)
    return message

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

    
    