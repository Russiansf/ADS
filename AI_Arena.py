from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver import ActionChains as ac
from selenium.webdriver.common.keys import Keys
import time
from datetime import datetime
from login_disco import *
import random

# Ai Arena daily drop

url_daily_drop = 'https://discord.com/channels/848599369879388170/1093212373793378335'
url_bot = 'https://discord.com/channels/848599369879388170/1018863796548276244'
url_roleYdie = 'https://discord.com/channels/848599369879388170/1154831517634265098'
url_general = 'https://discord.com/channels/848599369879388170/864551746414968838'

xpath_daily_drop_btn = '//button[@role="button"]'
xpath_received = '//span[text()="Transaction complete"]'
text_xpath = 'You have already received the max amount of rewards for this Store item '# пробел важен
xpath_already_received = f'//div//span[text()="{text_xpath}"]'

# bot
# dis_logo = 'chassidy_cope' #'rosalynunderdown'
xpath_textarea = '//div[@data-slate-node="element"]'
xpath_profile = '//div[text()="/profile"]'
xpath_menu_profile = '//div[@class="icons__374b3"]'
xpath_currencies = '(//strong[text()="Currencies"])[1]'
xpath_log = '(//div//span[text()='
xpath_bal = '/following::*[@class="embedFieldValue__53d47"]//span)[1]'
# xpath_balance = f'(//div//span[text()="{dis_logo}"]/following::*[@class="embedFieldValue__53d47"]//span)[1]'

xpath_boxes = '(//strong[text()="Boxes"])[1]'
xpath_dayly_drop_balance = '(//div//span[text()="Daily Drop"]/following::*[@class="embedFieldValue__53d47"]//span)[1]'
xpath_dice_roll_balance = '(//div//span[text()="Dice Roll"]/following::*[@class="embedFieldValue__53d47"]//span)[1]'
xpath_select_prize_box = '//span[text()="Select a prize box to open"]'
xpath_open_dice_box = '(//div[@class="labelContainer__88f1f"])[1]'

# roleYdie

xpath_roleYdie_btn = xpath_daily_drop_btn
xpath_already_received

debug_on = True


def Ai_claim_conf(driver, sec=15):
    try:
        WebDriverWait(driver, sec).until(ec.visibility_of_element_located((By.XPATH, xpath_received)))
        debug('AI daily drop claimed')
        # driver.quit()
        # если не нашел ищу что уже сделано
    except:
        WebDriverWait(driver, sec).until(ec.visibility_of_element_located((By.XPATH, xpath_already_received)))
        debug('AI daily drop allready claimed')

def Ai_dayly(index, ads_id, driver, sec=15):
    if ads_id not in Ai_except:
        debug('start AI daily claim')
        driver.get(url_daily_drop)
        global escape
        try:
            # если нашел кликнул
            daily_click = WebDriverWait(driver, 60).until(ec.visibility_of_element_located((By.XPATH, xpath_daily_drop_btn)))
            daily_click.click()
            # ищу подтверждение
            Ai_claim_conf(driver)
        except:
            try:
                escape = ac(driver).send_keys(Keys.ESCAPE).perform()
                print('Нажал ESC')
                time.sleep(2)
                escape = ac(driver).send_keys(Keys.ESCAPE).perform()
                print('Нажал ESC')
                daily_click.click()
                print('клик')
                Ai_claim_conf(driver)
            except:
                debug('#######---Не вышло---#######')
                file = open("exc_acc.txt", "a")  # append mode
                file.write(f"AI bug - {index} - {ads_id}\n")
                file.close()       
        finally:
            if datetime.today().weekday() > 4:                
                Ai_roll_your_die(ads_id, driver, sec=5)



def Ai_roll_your_die(ads_id, driver, sec=5):
    if ads_id not in Ai_except:
        debug('start roll your die')
        driver.get(url_roleYdie)    
        try:
            roleYdie = WebDriverWait(driver, 60).until(ec.visibility_of_element_located((By.XPATH, xpath_roleYdie_btn)))
            roleYdie.click()
        except:
            try:
                escape = ac(driver).send_keys(Keys.ESCAPE).perform()
                roleYdie.click()
            except:
                escape
                roleYdie.click()
                try:
                    escape
                    roleYdie.click()
                except:
                    debug('Не вышло')

        try:
            WebDriverWait(driver, sec).until(ec.visibility_of_element_located((By.XPATH, xpath_received)))
            debug('Your die claimed')
            # driver.quit()
        except:
            WebDriverWait(driver, sec).until(ec.visibility_of_element_located((By.XPATH, xpath_already_received)))
            debug('Your die allready claimed')


def check_ai_balans(index, ads_id, driver, sec=300):
    if ads_id not in Ai_except:
        dis_logo = log_disco[ads_id]
        x_bal = f'{xpath_log}"{dis_logo}"]{xpath_bal}'
        driver.get(url_bot)
        # global wait
        wait = WebDriverWait(driver, sec)
        text = random.choice(['/prof','/p','/pr','/pro'])
        # time.sleep(15)
        # ac(driver).send_keys(Keys.ESCAPE).perform()
        # driver.get(url_bot)
        # try:
        wait.until(ec.visibility_of_element_located((By.XPATH, xpath_textarea))).send_keys(text)
        # except:
        #     wait.until(ec.visibility_of_element_located((By.XPATH, xpath_textarea))).send_keys(text)
        try:
            wait.until(ec.visibility_of_element_located((By.XPATH, xpath_profile))).click()
        except:
            ac(driver).send_keys(Keys.ENTER).perform()
        ac(driver).send_keys(Keys.ENTER).perform()    
        wait.until(ec.visibility_of_element_located((By.XPATH, xpath_menu_profile))).click()
        wait.until(ec.visibility_of_element_located((By.XPATH, xpath_currencies))).click()
        balance = wait.until(ec.visibility_of_element_located((By.XPATH, x_bal)))
        
        text_balace = balance.text
        file = open("ai_balance.txt", "a")  # append mode
        file.write(f"{index}. {ads_id} - {text_balace}\n")
        file.close()


def box_menu(driver, sec=300):
    driver.refresh()
    wait = WebDriverWait(driver, sec)
        # добавить сет для рандомного текста
    text = random.choice(['/prof','/p','/pr','/pro'])
    time.sleep(3)
    # try:
    #     wait.until(ec.visibility_of_element_located((By.XPATH, xpath_textarea))).send_keys(text)
    # except:
    wait.until(ec.visibility_of_element_located((By.XPATH, xpath_textarea))).send_keys(text)
    
    try:
        wait.until(ec.visibility_of_element_located((By.XPATH, xpath_profile))).click()
    except:
        ac(driver).send_keys(Keys.ENTER).perform()
    ac(driver).send_keys(Keys.ENTER).perform()
    # print('enter click')
    
    wait.until(ec.visibility_of_element_located((By.XPATH, xpath_menu_profile))).click()
    wait.until(ec.visibility_of_element_located((By.XPATH, xpath_boxes))).click()

def open_boxes(index, ads_id, driver, sec=4):
    boxes = 0
    dice = 0    
    if ads_id not in Ai_except:
        dis_logo = log_disco[ads_id]
        x_logo = f'{xpath_log}"{dis_logo}"])'
        driver.get(url_bot)
        wait = WebDriverWait(driver, sec)
        box_menu(driver, sec=300)
        # print('box menu')
        try:
            balance_boxes = wait.until(ec.visibility_of_element_located((By.XPATH, xpath_dayly_drop_balance)))
            # ac(driver).scroll_to_element(xpath_dayly_drop_balance).perform()
            boxes = int(balance_boxes.text)
            # driver.execute_script("arguments[0].scrollIntoView(true);", element)
            
        except:
            boxes = 0
        # print(boxes)
        element = driver.find_element(By.XPATH, x_logo)
        if boxes != 0:
            try:
                driver.execute_script("arguments[0].scrollIntoView(true);", element)
                balance_roll_y_die = wait.until(ec.visibility_of_element_located((By.XPATH, xpath_dice_roll_balance)))
                dice = int(balance_roll_y_die.text)
                # print('sobral balans')
                wait.until(ec.visibility_of_element_located((By.XPATH, xpath_select_prize_box))).click()
                wait.until(ec.visibility_of_element_located((By.XPATH, xpath_open_dice_box))).click()
                time.sleep(3)
                box_menu(driver, sec=300)
            except:
                dice = 0
        # iter_open_box = boxes + dice
            # print(dice)        
            for i in range(0, int(boxes)):
                time.sleep(1)
                select_prize_box = wait.until(ec.visibility_of_element_located((By.XPATH, xpath_select_prize_box)))
                element = driver.find_element(By.XPATH, x_logo)
                driver.execute_script("arguments[0].scrollIntoView(true);", element)
                # element.location
                # print(element.location)
                # ac(driver).scroll_to_element(element).perform()
                # print('scroll')
                # driver.execute_script("arguments[0].scrollIntoView(true);", element)
                select_prize_box.click()
                wait.until(ec.visibility_of_element_located((By.XPATH, xpath_open_dice_box))).click()
                driver.execute_script("arguments[0].scrollIntoView(true);", element)
                t = random.uniform(0.6,2)
                time.sleep(t)

        debug(f'open {boxes} box(es)')
        if dice != 0:
            debug(f'open {dice} dice')

        # balance = wait.until(ec.visibility_of_element_located((By.XPATH, x_bal)))
        
        # text_balace = balance.text
        # file = open("ai_balance.txt", "a")  # append mode
        # file.write(f"{index}. {ads_id} - {text_balace}\n")
        # file.close()
    
    
    # //*[@class="grid_c7c4e6"]//*[text()="il_ildd"]/following-sibling::*[contains(@class="embedFieldValue__53d47")]
            
xpath_search = '//div[@data-block="true"]'
xpath_end = '(//div[@role="tab"])[2]'
xpath_masage = '//li[@class="container__7db35"]'
xpath_pgs = '(//div[@class="roundButton__9e83c pageButton_bcd673"])[3]//span'
xpath_time_box = '(//div[@class="contents_f41bb2"])[101]//time'
'//li[@class="container__7db35"][1]//div[@class="embedFieldValue__53d47"]//u//span[1]'

xpath_box = '//div[@class="embedFieldValue__53d47"]//u//span[1]'
xpath_next_btn = '//button[@rel="next"]'

xpath_change_pgs = '//div/h2[@data-text-variant="heading-sm/semibold"]'



def ai_parser(driver, sec=20):
    search_text = "'$NRN Box' opened!"
    driver.get(url_bot)
    wait = WebDriverWait(driver, sec)
    wait.until(ec.visibility_of_element_located((By.XPATH, xpath_search))).send_keys(search_text)
    ac(driver).send_keys(Keys.ENTER).perform()
    time.sleep(2)
    # wait.until(ec.visibility_of_element_located((By.XPATH, xpath_end))).click()
    # time.sleep(3)
    # time_box = driver.find_elements(By.XPATH, xpath_time_box)
    # file = open('boxes.txt', 'a')  # append mode
    # file.write(f'{time_box.text} \n')
    # file.close()
    
    # start_pg = driver.find_element(By.XPATH, xpath_change_pgs)
    # driver.execute_script("arguments[0].scrollIntoView(true);", start_pg)
    # start_pg.click()
    # ac(driver).send_keys(79).send_keys(Keys.ENTER).perform()


    # value_msg = driver.find_elements(By.XPATH, xpath_masage)
    # value_pgs = driver.find_element(By.XPATH, xpath_pgs)
    # driver.execute_script("arguments[0].scrollIntoView(true);", value_pgs)
    # for i in range(0, int(value_pgs.text)):
    for i in range(1, 90):
        time.sleep(1)
        value_msg = driver.find_elements(By.XPATH, xpath_masage)
        for msg in range(1, len(value_msg)+1):
            time.sleep(1)
            try:
                box_tupe = driver.find_element(By.XPATH, f'({xpath_masage})[{msg}]{xpath_box}')
                file = open('boxes.txt', 'a')  # append mode
                file.write(f'{box_tupe.text} \n')
                file.close()
            except:
                pass
        try:
            next_btn = driver.find_element(By.XPATH, xpath_next_btn)
        except:
            time.sleep(2)
            next_btn
        driver.execute_script("arguments[0].scrollIntoView(true);", next_btn)
        next_btn.click()


def disco_text(driver, sec):
    driver.get(url_general)
    # global wait
    wait = WebDriverWait(driver, sec)
    text = random.choice(['/prof','/p','/pr','/pro'])
    wait.until(ec.visibility_of_element_located((By.XPATH, xpath_textarea))).send_keys(text)


def debug(txt):
    if debug_on:
        log(txt)
        

def log(txt):
    print(txt)
    file = open("log_gm.txt", "a")  # append mode
    file.write(f"{txt} \n")
    file.close()


Ai_except = [
            ]