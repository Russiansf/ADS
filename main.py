# import subprocess

# subprocess.Popen("C:/Program Files/AdsPower Global/AdsPower Global.exe")

import requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from datetime import datetime
import time
import random
from stuff import *
from change_proxy import change_proxy
# from claim_gecco import start_gecco
# from AI_Arena import * #Ai_dayly, Ai_roll_your_die, check_ai_balans, open_boxes
# from Chainers import chainers_grab_nft
# from Layer3 import layer3_gm
# # from rabby_reg import rabbit_reg
# from dmail import dmail_send_mail
# from berachain import bera_faucet, bera_galxe, well3_daily
# from twiter import twit_follow, twit_like_rt
from Mezo import Mezo_dayly

start_acc = 1

# randomize = False
randomize = True
# driver: webdriver

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
        time.sleep(6)
        close_other_handles()
        time.sleep(4)
        # driver.execute_script('window.stop();')        
        return True
    except Exception as ex:
        log(f'ERROR {ex}')
        return False
        
    

def driver_close(ads_id):
    driver.quit()
    requests.get(f'{close_url}{ads_id}')
    

def close_other_handles():
    time.sleep(2)    
    curr = driver.current_window_handle
    time.sleep(2)
    for handle in driver.window_handles:
        driver.switch_to.window(handle)
        if handle != curr:
            driver.close()
    # curr = driver.current_window_handle
    # if len(curr) > 2:
        # close_other_handles()


def start_abuse(ads_id,index):
    index = index+1
    driver_init(ads_id)

    Mezo_dayly(index, ads_id, driver=driver)
    # twit_follow(index, ads_id, driver=driver)
    # twit_like_rt(driver=driver)
    # well3_daily(ads_id,index, driver=driver)
    # ai_parser(driver=driver)
    # bera_faucet(index, ads_id, driver=driver)
    driver_close(ads_id)

        # # if index <= 28:
    # layer3_gm(index, ads_id, driver=driver)
    # start_gecco(index, ads_id, driver=driver)
    # if index < 33 or index == 50:
    #     chainers_grab_nft(index, ads_id, driver=driver)
    # Ai_dayly(index, ads_id, driver=driver)
    # open_boxes(index, ads_id, driver=driver)
    # check_ai_balans(index, ads_id, driver=driver)
    # if index < 27:
    # bera_galxe(ads_id,index, driver=driver)
                

if __name__ == '__main__':    
    with open("_ids.txt", "r") as f:
        ids = [row.strip() for row in f]
        if randomize == True:
            ids = set(ids)

    log(datetime.now())

    # acc = input('Start Acc = ')
    # start_acc = int(acc)

    for index, item in enumerate(ids, start=0):
        if index+1 >= start_acc:
            log(f'========= {index+1}/{len(ids)} =========')
            log(f'start profile {item}')

            change_proxy()
            start_abuse(item, index)

            log(f'finish profile {item}')
            if (index+1) < len(ids):
                t = random.randint(1, 5)                
                timer(t)
            time.sleep(1)
    log('*************************\n''ALL PROFILES COMPLETED\n''*************************')
    # log('ALL PROFILES COMPLETED')
    # log('*************************')
    log(datetime.now())
