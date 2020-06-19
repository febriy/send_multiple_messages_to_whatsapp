# Send Multiple Personalised Messages to WhatsApp
Send multiple messages to WhatsApp using Python and Selenium

# Installation
Clone the repository `git clone <https/ssh link>`

Install required library using `pip install -r requirements.txt`

Download [chromedriver](https://chromedriver.storage.googleapis.com/index.html). Find out your Chrome [version](https://www.howtogeek.com/299243/which-version-of-chrome-do-i-have/) first. 

Then, extract chromedriver and place it at the main directory (where wa_send.py is located).

# Usage
### Prepare your csv
- Open send_list.csv and modify the column values. DO NOT CHANGE THE COLUMN HEADER NAMES!
- For the common message, you just have to input them once in the first row (see the csv).
- Save the changes in your csv file. 

### Run the code
`python wa_send.py`
- Sample texts will automatically be shown. 
- Afterwards, you will be prompted if you want to send the messages or not. Type either 'yes' or 'no'. 

