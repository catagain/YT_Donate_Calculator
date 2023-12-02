from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from webdriver_manager.chrome import ChromeDriverManager

from PIL import Image

import time

TARGET = 500000

# Check which country's dollar it is.
def exchange(amount):
    if amount[0:3] == 'HK$':
        # it's HK dollar, exchange rate: 4
        excahnge_amount = float(amount[3:].replace(',', '')) * 4
    elif amount[0:4] == 'RMB¥':
        # it's RMB
        excahnge_amount = float(amount[4:].replace(',', '')) * 5
    elif amount[0:3] == 'MYR':
        excahnge_amount = float(amount[4:].replace(',', '')) * 6.72
    else :
        excahnge_amount = float(amount[1:].replace(',', ''))
    # record the SC into history
    return excahnge_amount

def getDonateInfo(ID):
    browser = webdriver.Chrome()

    # Open the chat history web
    browser.get("https://www.youtube.com/live_chat?v=" + ID)
    
    # The Set is used to avoid repeated SC
    unique_chat = set()
    
    # load history to avoid repeated SC, and check the sum of donate.
    sumOfDonate = 0
    with open("DonateHistory.txt", 'r', encoding="utf-8") as f:
        rec = f.read().split('\n')
        count = 0
        for i in rec:
            if count == 1:
                sumOfDonate += exchange(i)
            elif count == 2:
                if i != 'this is a null SC':
                    unique_chat.add(i)
            if i == '---------------':
                count = 0
            else:
                count += 1
    
    # Get last Amount
    with open("CurrentDonateAmount.txt", "r", encoding="utf-8") as f:
        file = f.read()
        if file != "":
            SC_count = float(file)
        else:
            SC_count = 0.0 
        
        if SC_count != sumOfDonate:
            print("!!! WARING !!!")
            print("The amount may be wrong.")

    
    # a loop to scrapying all SC
    while(1):
        time.sleep(10)
        # Test if the amount has been modify by manual control
        add_amount_manual = 0
        with open("AddAmountManual.txt", 'r', encoding="utf-8") as f:
            add_amount_manual = f.read()
            if add_amount_manual == "":
                add_amount_manual = '0'
        with open("AddAmountManual.txt", 'w', encoding="utf-8") as f:
            f.write('')
        
        if add_amount_manual != '0':
            with open('DonateHistory.txt', 'a', encoding="utf-8") as f:
                f.write('Manual')
                f.write('\n')
                f.write('$' + add_amount_manual)
                f.write('\n')
                f.write('---------------')
                f.write('\n')
        
        with open("CurrentDonateAmount.txt", "r", encoding="utf-8") as f:
        # Get current amount
            file = f.read()
            if file != "":
                SC_count = float(file) + float(add_amount_manual)
            else:
                SC_count = 0.0 + float(add_amount_manual)
        
        # find SC data in html
        try:
            SC = browser.find_elements(By.CLASS_NAME, 'style-scope yt-live-chat-paid-message-renderer')
        except: 
            print('The website has been closed!')
            break

        for i in SC:
            # print(count, i.text)
            data = i.text.split('\n')
            print(data[0])
            print(data[1]) # this one is the amount
            if len(data) >= 3:
                print(data[2])

                if data[2] not in unique_chat:
                    # not in Set means this is a new SC
                    unique_chat.add(data[2])

                    # Check which country's dollar it is.
                    SC_count += exchange(data[1])

                    # record the SC into history
                    with open("DonateHistory.txt", "a", encoding="utf-8") as record:
                        record.write(i.text)
                        record.write('\n')
                        record.write('---------------')
                        record.write('\n')
                print('Current Amount: ' + str(SC_count))
                with open("CurrentDonateAmount.txt", "w", encoding="utf-8") as f:
                    f.write(str(SC_count))
            else:
                if data[0] not in unique_chat:
                    # Unable to differentiate based on messages, so using account names. However, not recording in the history to prevent future identical accounts from submitting without messages.
                    SC_count += exchange(data[1])
                    unique_chat.add(data[0])

                    # record the SC into history
                    with open("DonateHistory.txt", "a", encoding="utf-8") as record:
                        record.write(i.text)
                        record.write('\n')
                        record.write('this is a null SC')
                        record.write('\n')
                        record.write('---------------')
                        record.write('\n')

                    print('Current Amount: ' + str(SC_count))
                    with open("CurrentDonateAmount.txt", "w", encoding="utf-8") as f:
                        f.write(str(SC_count))
                print("This is a null SC.")
        
        color = 'limegreen'
        width =  max(int(345 * SC_count / TARGET), 1)
        print(width)
        img = Image.new('RGBA', (width, 77), color)
        img.save('./pictures/bar.png')

print('Please input the video ID: ')
id = input()
getDonateInfo(id)