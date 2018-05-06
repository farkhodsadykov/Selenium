from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
driver = webdriver.Chrome(executable_path=r'/Users/sadykovfarhad/PycharmProjects/selenium/chromedriver')


driver.get('https://wiki.evolvecyber.com/index.php?title=Special:UserLogin&returnto=Main+Page')
driver.find_element_by_xpath("//input[@class='loginText mw-ui-input']").send_keys('username')

driver.find_element_by_xpath("//input[@class='loginPassword mw-ui-input']").send_keys('password')
driver.find_element_by_xpath("//button[@class='mw-htmlform-submit mw-ui-button mw-ui-primary mw-ui-progressive']").click()
driver.get("https://wiki.evolvecyber.com/index.php/Special:UserRights")

file = open(r'list_of_users', 'r')

for i in file:
    driver.get("https://wiki.evolvecyber.com/index.php/Special:UserRights")
    driver.find_element_by_xpath("//input[@name='user']").send_keys(i)
    time.sleep(1)
    checkboxclick = driver.find_element_by_xpath("//input[@name='wpGroup-April_Class']")
    time.sleep(1)
    if (checkboxclick.is_selected()):
        print(i + "is April CLass")
    else:
        checkboxclick.click()
    checkboxclick = driver.find_element_by_xpath("//input[@name='wpGroup-SysAdmin']")
    time.sleep(1)
    if (checkboxclick.is_selected()):
        print(i + "is Sysadmin")
    else:
        checkboxclick.click()
    checkboxclick = driver.find_element_by_xpath("//input[@name='wpGroup-DevOps']")
    time.sleep(1)
    if (checkboxclick.is_selected()):
        print(i + "is DevOps")
    else:
        checkboxclick.click()
    driver.find_element_by_xpath("//input[@name='saveusergroups']").click()
file.close()
