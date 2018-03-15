from selenium import webdriver
import requests
IE =r'C:\Program Files\Internet Explorer\IEDriverServer.exe'
web = webdriver.Ie(IE)
web.get('http://github.com/login')
web.implicitly_wait(5)
emailElem = web.find_element_by_name('login')
emailElem.send_keys('lmac0603@163.com')
passwordElem = web.find_element_by_name('password')
passwordElem.send_keys('xywxhzsjhhgh06')
passwordElem.submit()
