# import subprocess

# subprocess.Popen("C:/Program Files/AdsPower Global/AdsPower Global.exe")

import time
import requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

open_url = 'http://local.adspower.net:50325/api/v1/browser/start?user_id='
close_url = 'http://local.adspower.net:50325/api/v1/browser/stop?user_id='


def driver_init(ads_id):
    global driver
    try:
        resp = requests.get(f'{open_url}{ads_id}').json()
        chrome_driver = resp["data"]["webdriver"]       
        options = webdriver.ChromeOptions()
        options.add_experimental_option("debuggerAddress", resp["data"]["ws"]["selenium"])
        driver = webdriver.Chrome(service=Service(chrome_driver), options=options)
        return True
    except Exception as ex:
        log(f'ERROR {ex}')
        return False
    

def driver_close(ads_id):    
    driver.quit()
    requests.get(f'{close_url}{ads_id}')
    

def log(txt):
    print(txt)
    file = open("log_gm.txt", "a")  # append mode
    file.write(f"{txt} \n")
    file.close()

# ads_id = 'j4nlwdn'
# driver_init(ads_id)
# time.sleep(2)
# print('end time')
# driver_close(ads_id)
# print('close')