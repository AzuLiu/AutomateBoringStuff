from selenium import webdriver
import requests
IE =r'C:\Program Files\Internet Explorer\IEDriverServer.exe'
web = webdriver.Ie(IE)
web.get('http://mail.163.com')
try:
    web.implicitly_wait(5)
except ConnectionResetError:
    pass
emailElem = web.find_element_by_name('email')
emailElem.send_keys('your_account')
passwordElem = web.find_element_by_name('password')
passwordElem.send_keys('your_password')
passwordElem.submit()
