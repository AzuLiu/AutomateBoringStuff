from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import random

def Firefox():
    Firefox =r'C:\Program Files\Mozilla Firefox\geckodriver.exe'
    return webdriver.Firefox(executable_path=Firefox)
web = Firefox()
web.get('https://gabrielecirulli.github.io/2048/')
htmlElem = web.find_element_by_tag_name('html')
for n in range(500):
    for i in range(700):
        i = random.randrange(0, 4)
        if i == 0:
            htmlElem.send_keys(Keys.UP)
        elif i == 1:
            htmlElem.send_keys(Keys.DOWN)
        elif i == 2:
            htmlElem.send_keys(Keys.LEFT)
        else:
            htmlElem.send_keys(Keys.RIGHT)
    tryagain = web.find_element_by_link_text('Try again')
    tryagain.click()
