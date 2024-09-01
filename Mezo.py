from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver import ActionChains as ac
from selenium.webdriver.common.keys import Keys
import time
import random
from stuff import *


url_mezo_lootbox = 'https://discord.com/channels/1220035427952627863/1275113835753373840'


xpath_claim = '//button[@role="button"]'

xpath_given = '//span[text()="You have been given "]'

text_xpath = 'You can use this button again ' # пробел важен
xpath_already_claim = f'//div//span[text()="{text_xpath}"]'
xpath_remaining_time = '//span[@class="timestamp_f8f345"]'

debug_on = True

with open("mezo_ignor_id.txt", "r") as f:
	mezo_except = [row.strip() for row in f]


def Mezo_claim_conf(driver, sec=5):
    try:
        WebDriverWait(driver, sec).until(ec.visibility_of_element_located((By.XPATH, xpath_given)))
        debug('Mezo deily loot claimed')        
        # если не нашел ищу что уже сделано
    except:
        WebDriverWait(driver, sec).until(ec.visibility_of_element_located((By.XPATH, xpath_already_claim)))
        remaining_time = WebDriverWait(driver, sec).until(ec.visibility_of_element_located((By.XPATH, xpath_remaining_time)))
        rem_time = remaining_time.text
        debug(f'I can use the Mezo claim again {rem_time}')


def Mezo_dayly(index, ads_id, driver, sec=15):
    if ads_id not in mezo_except:
        debug('start mezo claim')
        driver.get(url_mezo_lootbox)
        global escape
        try:
            # если нашел кликнул
            daily_click = WebDriverWait(driver, 60).until(ec.visibility_of_element_located((By.XPATH, xpath_claim)))
            daily_click.click()
            # ищу подтверждение
            Mezo_claim_conf(driver)
        except:
            try:
                escape = ac(driver).send_keys(Keys.ESCAPE).perform()
                print('Нажал ESC')
                # time.sleep(2)
                # escape = ac(driver).send_keys(Keys.ESCAPE).perform()
                # print('Нажал ESC')
                daily_click.click()
                print('клик')
                Mezo_claim_conf(driver)
            except:
                debug('#######---Не вышло---#######')
                file = open("exc_acc.txt", "a")  # append mode
                file.write(f"Mezo bug - {index} - {ads_id}\n")
                file.close()
        t = random.randint(45, 600)
        timer(t)


def debug(txt):
    if debug_on:
        log(txt)
        

def log(txt):
    print(txt)
    file = open("log_gm.txt", "a")  # append mode
    file.write(f"{txt} \n")
    file.close()
