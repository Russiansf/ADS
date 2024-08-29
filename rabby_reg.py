# import os
# from selenium import webdriver
import time
# from dotenv import load_dotenv
# from fake_useragent import UserAgent
from selenium.webdriver.common.keys import Keys
# import pickle
# from change_proxy import change_proxy
# для явных ожиданий
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver import ActionChains
import requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from datetime import datetime
import time
import random
# from ads_init import driver_init, driver_close
from change_proxy import change_proxy

start_akk = 1
randomize = False

# driver: webdriver

open_url = 'http://local.adspower.net:50325/api/v1/browser/start?user_id='
close_url = 'http://local.adspower.net:50325/api/v1/browser/stop?user_id='

change_proxy_ip = 'https://changeip.mobileproxy.space/?proxy_key=3101c73e350650f60e5225492f6ccb91'


def driver_init(ads_id):
    global driver
    try:
        resp = requests.get(f'{open_url}{ads_id}').json()
        chrome_driver = resp["data"]["webdriver"]       
        options = webdriver.ChromeOptions()
        options.add_experimental_option("debuggerAddress", resp["data"]["ws"]["selenium"])
        driver = webdriver.Chrome(service=Service(chrome_driver), options=options)
        close_other_handles()
        return True
    except Exception as ex:
        log(f'ERROR {ex}')
        return False
    

def driver_close(ads_id):
    driver.quit()
    requests.get(f'{close_url}{ads_id}')
    

def close_other_handles():
    # time.sleep(2)    
    curr = driver.current_window_handle
    # time.sleep(2)
    for handle in driver.window_handles:
        driver.switch_to.window(handle)
        if handle != curr:
            driver.close()
    # curr = driver.current_window_handle
    # if len(curr) > 2:
    #     close_other_handles()


# def start_abuse(ads_id):
#     driver_init(ads_id)
#     # start_gecco(driver=driver)
#     # chainers_grab_nft(driver=driver)
#     # Ai_dayly(driver=driver)

#     driver_close(ads_id)
            

def log(txt):
    print(txt)
    file = open("log_gm.txt", "a")  # append mode
    file.write(f"{txt}\n")
    file.close()


def timer(sec):
    if sec >= 0:
        print(f'wait: {sec} sec.   ', end='')
        time.sleep(1)
        print('\r', end='')
        sec -= 1
        timer(sec)

# load_dotenv()

# useragent = UserAgent()

# options = webdriver.ChromeOptions()
# # options.add_argument('--no-sandbox')
# # options.add_argument('--headless')
# # options.add_argument("–disable-gpu")
# # options.add_argument("--headless=new")
# options.add_argument('--window-size=400,768')
# options.add_argument(f'user-agent={useragent.random}')
# options.add_argument('--disable-blink-features=AutomationControlled')
# options.add_argument('--disable-features=ImprovedCookieControls')
# options.add_experimental_option('useAutomationExtension', False)
# options.add_experimental_option('excludeSwitches', ['enable-automation'])
# options.page_load_strategy = 'normal' # eager normal

# options.add_extension(os.getcwd()+f'/ACMACODKJBDGMOLEEBOLMDJONILKDBCH_0_92_38_0.crx')
# options.add_argument('--enable-extensions')
# start_account = 1
# end_account = 14
# privat_keys = [os.environ[f"u{i}"] for i in range(start_account, end_account+1)]

rabbi_extension = 'chrome-extension://fddkhedhdcopkhanjnfkfbomeoddbbcn/popup.html#/no-address'

private_key_button = ('xpath','//div[text()="Import Private Key"]')
input_password = ('xpath','//input[@id="password"]')
confirm_password = ('xpath','//input[@id="confirmPassword"]')
submit_button = ('xpath','//button[@type="submit"]')
enter_privat_key = ('xpath','//input[@placeholder="Enter your Private key"]')
button_confirm = ('xpath','//button')
button_confirm2 = ('xpath','//button')
more_btn_9 = ('xpath','(//div[@class="direction pointer"])[9]')
gastoken_btn = ('xpath','(//div[@class="field-slot"])[2]')
request_btn = ('xpath','//button[@type="button"]')
pop_up = ('xpath','(//div)[65]')
Uve_req_2day = ('xpath','//div[text()="You have requested today"]')


def run(privat_key, index):
#     driver = webdriver.Chrome(options=options)
#     driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
#     'source': '''
#         delete window.cdc_adoQpoasnfa76pfcZLmcfl_Array;
#         delete window.cdc_adoQpoasnfa76pfcZLmcfl_Promise;
#         delete window.cdc_adoQpoasnfa76pfcZLmcfl_Symbol;
#         delete window.cdc_adoQpoasnfa76pfcZLmcfl_JSON;
#         delete window.cdc_adoQpoasnfa76pfcZLmcfl_Object;
#         delete window.cdc_adoQpoasnfa76pfcZLmcfl_Proxy;
#   '''
# })
    driver.get(url=rabbi_extension)
    wait = WebDriverWait(driver, 10)
    
    try:
        # change_proxy()

        # print(f'---------------Akk {index} start---------------')     	

        # driver.get(url=rabbi_extension)

        try:
            wait.until(ec.visibility_of_element_located((private_key_button))).click()            
        except:
            driver.refresh()
            try:
                wait.until(ec.visibility_of_element_located((private_key_button))).click()
            except Exception as ex:
                driver.save_screenshot('screen.png')
                print(ex)
        
        wait.until(ec.visibility_of_element_located((input_password))).send_keys('zxcqwe5288352')

        try:
        
            wait.until(ec.visibility_of_element_located((confirm_password))).send_keys('zxcqwe5288352')
            
            wait.until(ec.visibility_of_element_located((submit_button))).click()
            
            wait.until(ec.visibility_of_element_located((enter_privat_key))).send_keys(privat_key)
            
            wait.until(ec.visibility_of_element_located((button_confirm))).click()
            
            time.sleep(1)
            driver.find_element(*button_confirm2).click()
            time.sleep(1)
            ActionChains(driver).send_keys(Keys.ESCAPE).perform() #"\ue00c"
              
            # time.sleep(2)
            # try:
                # driver.find_element(*pop_up).send_keys(Keys.ESCAPE)
            # except:
            #     driver.refresh()
            #     time.sleep(1)
            #     driver.find_element(*pop_up).send_keys(Keys.ESCAPE)
            
            # wait.until(ec.visibility_of_element_located((more_btn_9))).click()
            
            # wait.until(ec.visibility_of_element_located((gastoken_btn))).click()
            
            
            # try:
            #     wait.until(ec.visibility_of_element_located((request_btn))).click()
            #     time.sleep(1)
            #     print(f'------------------end--------------------')

            # except:
            #     wait.until(ec.visibility_of_element_located((Uve_req_2day)))
            #     print(f'-----------Already requested-------------')
        except:
            print('Уже да')

    except Exception as ex:
        print(ex)
    # finally:
    #     driver.close()
    #     driver.quit()


def rabb_reg():
    # n = (input('Введи ключ: '))
    n = 5288352
    with open("_ids.txt", "r") as f:
            ids = [row.strip() for row in f]
            if randomize == True:
                ids = set(ids)

    with open("zkeyprivat.txt", "r") as f:
        privat_keys = [row.strip() for row in f]

        log(datetime.now())

        for index, item in enumerate(ids, start=0):
            if index+1 >= start_akk:
                log(f'========= {index+1}/{len(ids)} =========')
                log(f'start profile {item}')
            for i, z_privat_key in enumerate(privat_keys):
                zkey = int(z_privat_key) + int(n)
                # zkey = z_privat_key + n
                privat_key = hex(int(zkey))            
                if z_privat_key[0] == '0':      
                    privat_key = privat_key[:2] + '0' + privat_key[2:]
                else:
                    privat_key                
                driver_init(item)                
                run(privat_key,i+1)
                driver_close(item)
            log(f'finish profile {item}')
            if (index+1) < len(ids):
                t = random.randint(3, 8)
                timer(t)
            time.sleep(1)
        log('*************************')
        log(f'ALL PROFILES COMPLETED')
        log('*************************')
        log(datetime.now())



# if __name__ == '__main__':
rabb_reg()


# 32915938875086099344605458470805908249569679795430715899112156857219499356919
# 86691154554731578071140514344631126886179420553383584306261475203298449530018
# 64457999595343585616494697752374361906683153685923713143895935327642087368256
