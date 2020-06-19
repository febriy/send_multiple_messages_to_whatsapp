# Send Multiple Personalised Messages to WhatsApp
Send multiple messages to WhatsApp using Python and Selenium.

# Installation
Clone the repository `git clone <https/ssh link>`

Install required library using `pip install -r requirements.txt`

Download [chromedriver](https://chromedriver.storage.googleapis.com/index.html). Find out your Chrome [version](https://www.howtogeek.com/299243/which-version-of-chrome-do-i-have/) first. 

Then, extract chromedriver and place it at the main directory (where wa_send.py is located).

# Usage
### Prepare your contact list
- Make sure that you save the contacts you want to save to in your phone (and that it came up at the top when you search for it - beware of duplicate/ similar names).

### Prepare your csv
- Open send_list.csv and modify the column values. DO NOT CHANGE THE COLUMN HEADER NAMES!
- For the common message, you just have to input them once in the first row (see the csv).
- Save the changes in your csv file. 

### Run the code
`python wa_send.py`
- Sample texts will automatically be shown. 
- Afterwards, you will be prompted if you want to send the messages or not. Type either 'yes' or 'no'. 

### Use pyinstaller to create an executable 
- Install pyinstaller `pip install https://github.com/pyinstaller/pyinstaller/archive/develop.zip`
- Run this command `pyinstaller --onefile -w gui.py`
- Move the chromedriver.exe and send_list.csv to the dist folder.
- Run gui.exe
    - click "set-(chromedriver directory)"
    - click "start chrome"
    - start the whatsapp web with your phone
    - click "set-(send_list directory)"
    - click "test message" - you will see the message samples on the app
    - type "yes"
    - click "yes/no"
- You can now send the dist folder with everything inside it to someone else who might need it.

### Sending using number instead
- If you want to send to specific number instead of person name/ group: `python send_to_number.py`
- Note that currently, the code is set up to send to Singapore number. 
- If you want to change that, modify the following line: `driver.get("https://web.whatsapp.com/send?phone=65{}&source=&data=#".format(phone_no))`
    - change the number 65 to your country's code or remove the number completely. 

### References
- https://lesmartomation.com/send-whatsapp-messages-with-automated-script-using-selenium/
- https://pyinstaller.readthedocs.io/en/stable/operating-mode.html
- https://www.youtube.com/watch?v=YXPyB4XeYLA