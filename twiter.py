from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
from wallets import wallets
from selenium.webdriver.common.action_chains import ActionChains as AC
import time


url_follow = ['https://twitter.com/Grat3r_man',
'https://twitter.com/Ayda58550984046',
'https://twitter.com/Dilay8069240861',
'https://twitter.com/Ece850568325503',
'https://twitter.com/Meliha512434833',
'https://twitter.com/Asya64521756402',
'https://twitter.com/Bahar118079709',
'https://twitter.com/Aleyna371322494'
]

# 'https://twitter.com/ChassidyCope8',
# 'https://twitter.com/Devita_Insania',
# 'https://twitter.com/RosalynUnderdo1',
# 'https://twitter.com/ColmiSara' 1 - 4 с 1 по 40

# 'https://twitter.com/WillMayer_',
# 'https://twitter.com/seniorkoko787',
# 'https://twitter.com/Camr_n_',
# 'https://twitter.com/fleurypro1',
# 'https://twitter.com/fertrun' 5 - 9 с 1 до 25

# 'https://twitter.com/Crypt0_Karl',
# 'https://twitter.com/Kaisenkhan',
# 'https://twitter.com/Ay_sicagi',
# 'https://twitter.com/Denizha72075801',
# 'https://twitter.com/Jale15177052845' 30 - 34 c 1 по 40

# 'https://twitter.com/Dilay8069240861',
# 'https://twitter.com/Ece850568325503',
# 'https://twitter.com/Meliha512434833',
# 'https://twitter.com/Asya64521756402',
# 'https://twitter.com/Bahar118079709' 35 - 39 с 1 по 22


''' 'https://twitter.com/chrisheatherly', 'https://twitter.com/InviteToMystery' '''

url_like_rt = ['https://x.com/Wagmipad/status/1790655806750457976'
               ]

''''https://x.com/InviteToMystery/status/1756064500392907108',
                'https://x.com/Yogapetz/status/1752693511433093285', '''

xpath_follow = '//span[text()="Follow"]'
xpath_following = '(//*[text()="Following"])[1]'
xpath_like = '/html/body/div[1]/div/div/div[2]/main/div/div/div/div/div/section/div/div/div[1]/div/div/article/div/div/div[3]/div[5]/div/div/div[3]/div/div/div[1]' #'(//*[local-name()="svg"])[16]'
xpath_rt = '//*[@id="id__hnpijfqdvti"]/div[2]/button/div/div[1]/div' #'(//*[local-name()="path"])[15]'
xpath_repost = '//span[text()="Repost"]'
xpath_undo_repost = '//span[text()="Undo repost"]'
xpath_reply = '//span[text()="Reply"]'

debug_on = True


def twit_follow(index, ads_id, driver, sec=30):
    debug('start twit follow')
    wait = WebDriverWait(driver, sec)
    for urlf in url_follow:
        driver.get(urlf)
        time.sleep(3)
        try:
            try:    
                wait.until(ec.visibility_of_element_located((By.XPATH, xpath_follow))).click()
                time.sleep(2)
            except:
                wait.until(ec.visibility_of_element_located((By.XPATH, xpath_following)))
            debug('twit follow complite')
        except:
            debug('twit not login')
            file = open("exc_acc.txt", "a")  # append mode
            file.write(f"twit not login - {index} - {ads_id}\n")
            file.close()


def twit_like_rt(driver, sec=30):
    debug('start twit like rt')
    wait = WebDriverWait(driver, sec)
    for urll_rt in url_like_rt:
        driver.get(urll_rt)
        time.sleep(3)
        # rt = wait.until(ec.visibility_of_element_located((By.XPATH, xpath_rt)))
        # driver.execute_script("arguments[0].scrollIntoView(true);", rt)
        try:
            rt = wait.until(ec.visibility_of_element_located((By.XPATH, xpath_rt)))
            driver.execute_script("arguments[0].click();", rt)
            time.sleep(0.5)
            repost = wait.until(ec.visibility_of_element_located((By.XPATH, xpath_repost)))
            driver.execute_script("arguments[0].click();", repost)
            time.sleep(1)
            like = wait.until(ec.visibility_of_element_located((By.XPATH, xpath_like)))
            driver.execute_script("arguments[0].click();", like)
            print('like')
        except:
            wait.until(ec.visibility_of_element_located((By.XPATH, xpath_undo_repost)))
            # wait.until(ec.visibility_of_element_located((By.XPATH, xpath_like))).click()

    debug('twit like rt complite')


def debug(txt):
    if debug_on:
        log(txt)
        

def log(txt):
    print(txt)
    file = open("log_gm.txt", "a")  # append mode
    file.write(f"{txt} \n")
    file.close()