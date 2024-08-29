import time
import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import zipfile
from selenium.webdriver.common.keys import Keys

token = 'NDE2Njg2NTY3OTgyMTA0NjA3.GX5HTV.zkbBn1UjFEh9TMCKtivEAHUAvdZvNol4gEZmZs'

xpath_search = '//input[@class="input__48d49"]'
xpath_cross = '//*[@aria-label="Очистить"]'
xpath_sort = '//div[text()="Сортировать"]'
xpath_memb_pozdndate = '//div[text()="В числе участников (с самой поздней даты)"]'
xpath_memb_randate = '//div[text()="В числе участников (с самой ранней даты)"]'
xpath_disc_pozdn = '//div[text()="В Discord (с самой поздней даты)"]'
xpath_disc_ran = '//div[text()="В Discord (с самой ранней даты)"]'

view_string = '//span[text()=12]'
string_100 = '(//div[text()="100"])[1]'
dalee = '//span[text()="Далее"]'

xpath_member = '(//tr[@role="row"]'

memb_name = '/descendant::span[@class="memberNameText__33162 username__4a6f7 desaturateUserColors_eb6bd2"]'
memb_date = '/descendant::div[@class="text-sm-medium__726be"]'
disco_date = '/descendant::div[@class="text-sm-medium__726be"][2]'
xpath_id = '/descendant::img'
xpath_3dots = '//div[@class="button__440c9"])[2]'
xpath_copy_id = '(//div[@class="item__183e8 labelContainer__4f869 colorDefault_e361cf"])'
xpath_signals = '//div[text()="Сигналы"]'

# (//tr[@role="row"]/descendant::span[text()="tuyenphong110@gmail.com"]/preceding::div[@class="button__440c9"])[2]

chrome_options = Options()

prefs = {'profile.default_content_setting_values.automatic_downloads': 1}
chrome_options.add_experimental_option("prefs", prefs)

chrome_options.add_argument('--disable-blink-features=AutomationControlled')
chrome_options.add_argument('--disable-features=ImprovedCookieControls')
chrome_options.add_experimental_option('useAutomationExtension', False)
chrome_options.add_experimental_option('excludeSwitches', ['enable-automation'])

webdriver_service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=webdriver_service, options=chrome_options)

wait = WebDriverWait(driver, 20)
wait2 = WebDriverWait(driver, 6)
wait_speed = WebDriverWait(driver, 2)

# Открытие файла для чтения
with open('fake_disco_login.txt', 'r') as file:
    # Чтение строк из файла и удаление символов новой строки
    logins = file.read().splitlines()


driver.get('https://discord.com/login')

time.sleep(5)

script = f"""
    const token = "{token}";
    setInterval(() => {{
        document.body.appendChild(document.createElement('iframe')).contentWindow.
        localStorage.token = `"${{token}}"`;
        }}, 50);
    setTimeout(() => {{
        location.reload();
    }}, 2500);
"""
driver.execute_script(script)

time.sleep(5)


driver.get('https://discord.com/channels/1140682688651612291/member-safety')

time.sleep(5)

input()

wait.until(ec.visibility_of_element_located(('xpath', view_string))).click()
wait.until(ec.visibility_of_element_located(('xpath', string_100))).click()


def check_id(name):

    try:
        check = wait2.until(ec.visibility_of_element_located(('xpath', f'(//tr[@role="row"]/descendant::span[text()="{name}"]/following::div[@class="button__440c9"])[2]')))
        check.click()
        return True
    except:
        # print('except')
        # driver.find_element('xpath', '//body').send_keys(Keys.END)
        # print('end')
        dalee_btn = wait.until(ec.visibility_of_element_located(('xpath', dalee)))
        # print('element')
        # driver.execute_script("arguments[0].scrollIntoView(true);", dalee_btn)
        # print('script')
        dalee_btn.click()
        # print('click')
        return False



for login in logins:

    # wait.until(ec.visibility_of_element_located(('xpath', xpath_signals))).click()

    # login = 'ducminh2019w@gmail.com'

    try:
        search = wait2.until(ec.visibility_of_element_located(('xpath', xpath_search)))
        # search.clear()
        search.send_keys(f'{login} ')

        # time.sleep(20)

        for i in range(6):
            success = check_id(login)
            if success:
                break
    
        # check_id = wait2.until(ec.visibility_of_element_located(('xpath', f'(//tr[@role="row"]/descendant::span[text()="{login}"]/following::div[@class="button__440c9"])[2]')))
    
        # check_id.click()

        # time.sleep(2)

        try:
            try:
                copy_id = wait_speed.until(ec.visibility_of_element_located(('xpath', f'{xpath_copy_id}[6]')))
            except:
                copy_id = wait_speed.until(ec.visibility_of_element_located(('xpath', f'{xpath_copy_id}[5]')))

            user_id = copy_id.get_attribute('id')

            prefix_to_remove = 'user-context-devmode-copy-id-'

            id_str = user_id[len(prefix_to_remove):]

            id_int = int(id_str)

            with open('disco_id.txt', 'a') as file:
                file.write(f'{id_int}\n')

        except:
            with open('disco_no_id.txt', 'a') as file:
                file.write(f'{login}\n')

    except:
        with open('disco_no_id.txt', 'a') as file:
            file.write(f'{login}\n')

    # driver.refresh()

    # time.sleep(30)

    try:
        wait.until(ec.visibility_of_element_located(('xpath', xpath_cross))).click()
    except:
        driver.refresh()
        wait.until(ec.visibility_of_element_located(('xpath', view_string))).click()
        wait.until(ec.visibility_of_element_located(('xpath', string_100))).click()

time.sleep(2)

input('...')










# Сбор данных

# wait.until(ec.visibility_of_element_located(('xpath', view_string))).click()
# wait.until(ec.visibility_of_element_located(('xpath', string_100))).click()
# wait.until(ec.visibility_of_element_located(('xpath', xpath_sort))).click()
# wait.until(ec.visibility_of_element_located(('xpath', xpath_memb_randate))).click()

# with open('диско.xlsx', 'w') as file:
#     file.write('Ник\tНа Сервере\tВ Дискорде\n')

# for b in range(1, 132):
#     wait.until(ec.visibility_of_element_located(('xpath', dalee))).click() 
#     time.sleep(2)


# for a in range(131, 2349):

#     for i in range(1, 101):

#         name_member = wait.until(ec.visibility_of_element_located(('xpath', f'{xpath_member})[{i}]{memb_name}')))

#         date_on_server = wait.until(ec.visibility_of_element_located(('xpath', f'{xpath_member})[{i}]{memb_date}')))

#         date_on_disco = wait.until(ec.visibility_of_element_located(('xpath', f'{xpath_member})[{i}]{disco_date}')))

#         id_element = wait.until(ec.visibility_of_element_located(('xpath', f'{xpath_member})[{i}]{xpath_id}')))

#         date_serv = date_on_server.get_attribute('aria-label')

#         date_disco = date_on_disco.get_attribute('aria-label')

#         src_value = id_element.get_attribute('src')

#         id_value = src_value.split('/')[-2]

#         nic = name_member.text
#         na_serv = date_serv
#         in_dis = date_disco

#         with open('диско.xlsx', 'a') as file:
#             file.write(f'{nic}\t{na_serv}\t{in_dis}\t{id_value}\n')

#     wait.until(ec.visibility_of_element_located(('xpath', dalee))).click() 
#     time.sleep(2)   


# time.sleep(5)
# # input(...)
# driver.quit()