from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver import ActionChains as ac
from selenium.webdriver.support.ui import WebDriverWait
import time
from login_twiter import *

url_chainers = 'https://chainers.io/game'
url_registr = 'https://chainers.io/game/login?redirectOnLogin=%2F'
xpath_claim_chainers = '//button[@class="custom-button event-btn reward-button "]'
xpath_alredy_claim = '//div[@class="timer-container en"]'
xpath_twitter_btn = '(//button[@type="button"])[3]'
# xpath_email = '//input[@id="username_or_email"]'
# xpath_password = '//input[@id="password"]'
xpath_allow = '//input[@id="allow"]'

xpath_Login = '//input[@dir="auto"]' #'(//div[@dir="ltr"])[5]'#
xpath_next_btn = '//span[text()="Next"]'
xpath_password = '//input[@type="password"]'
xpath_Log_in = '//span[text()="Log in"]'

xpath_open_me_pls = '(//button[@type="button"])[13]'
xpath_skip_flip = '(//button[@type="button"])[13]'
xpath_okay = '(//button[@type="button"])[13]'
xpath_collect_close = '//p[text()="COLLECT AND CLOSE"]'
xpath_skip_flip2 = '(//button[@type="button"])[13]'

xpath_start_game = '(//div[@class="button-text"])[1]'
xpath_start_and_get = '(//button[@type="button"])[3]'
xtath_to_the_game = '(//button[@type="button"])[10]'

'https://chainers.io/game/farm'

debug_on = True

# С 17го надо регаться в твитере.

def chainers_grab_nft(index, ads_id, driver, sec=10):
    debug('start chainers')
    global wait
    wait = WebDriverWait(driver, sec)
    driver.get(url_chainers)
    if driver.current_url == url_chainers:
    # WebDriverWait(driver, 60).until(ec.url_to_be(url_chainers)) == True:
        try:
            wait.until(ec.visibility_of_element_located((By.XPATH, xpath_claim_chainers))).click()
            debug('chainers captured')
            # input('continue')
                # driver.close()
        except:
            wait.until(ec.visibility_of_element_located((By.XPATH, xpath_alredy_claim)))
            debug('chainers allready captured')
            # input('continue')
                # driver.close()
    else:                
        # chainers_registr(ads_id, driver)
        debug('Не зареган')
        # input('continue')
        file = open("exc_acc.txt", "a")  # append mode
        file.write(f"Chainers dont reg - {index} - {ads_id}\n")
        file.close()

    
def chainers_registr(ads_id, driver):
    # if ads_id in log_twit:
    login = log_twit[ads_id]    
    if ads_id in pass_twit:
        password = pass_twit[ads_id]
    else:
        password = 'zxcqwe5288352'
    # driver.get(url_registr)    
    # print(driver.current_url)
    try:
        wait.until(ec.visibility_of_element_located((By.XPATH, xpath_twitter_btn))).click()
        wait.until(ec.visibility_of_element_located((By.XPATH, xpath_allow))).click()
        ac(driver).scroll_to_element(By.XPATH, xpath_open_me_pls).perform()
        wait.until(ec.visibility_of_element_located((By.XPATH, xpath_open_me_pls))).click()
        wait.until(ec.visibility_of_element_located((By.XPATH, xpath_skip_flip))).click()
        wait.until(ec.visibility_of_element_located((By.XPATH, xpath_okay))).click()
        wait.until(ec.visibility_of_element_located((By.XPATH, xpath_collect_close))).click()
        wait.until(ec.visibility_of_element_located((By.XPATH, xpath_claim_chainers))).click()
        debug('chainers registr and captured')        
    # print(driver.current_url)
    except:              
        wait.until(ec.visibility_of_element_located((By.XPATH, xpath_Login))).send_keys(login)
        wait.until(ec.visibility_of_element_located((By.XPATH, xpath_next_btn))).click()
        wait.until(ec.visibility_of_element_located((By.XPATH, xpath_password))).send_keys(password)
        wait.until(ec.visibility_of_element_located((By.XPATH, xpath_Log_in))).click()
        time.sleep(2)
        driver.get(url_chainers)
        wait.until(ec.visibility_of_element_located((By.XPATH, xpath_allow))).click()        
        try:
            time.sleep(7)
            wait.until(ec.visibility_of_element_located((By.XPATH, xpath_open_me_pls)))
            ac(driver).scroll_to_element(By.XPATH, xpath_open_me_pls).perform()
            wait.until(ec.visibility_of_element_located((By.XPATH, xpath_open_me_pls))).click()
            wait.until(ec.visibility_of_element_located((By.XPATH, xpath_skip_flip))).click()
            wait.until(ec.visibility_of_element_located((By.XPATH, xpath_okay))).click()
            wait.until(ec.visibility_of_element_located((By.XPATH, xpath_collect_close))).click()
            wait.until(ec.visibility_of_element_located((By.XPATH, xpath_claim_chainers))).click()
            debug('chainers registr and captured')
        # print(driver.current_url)
        except:
            input("Что-то не так")





def debug(txt):
    if debug_on:
        log(txt)
        

def log(txt):
    print(txt)
    file = open("log_gm.txt", "a")  # append mode
    file.write(f"{txt} \n")
    file.close()