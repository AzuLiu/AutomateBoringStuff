from selenium import webdriver
def Firefox():
    Firefoxpath =r'C:\Program Files\Mozilla Firefox\geckodriver.exe'
    return webdriver.Firefox(executable_path=Firefoxpath)
web = Firefox()
web.get('http://github.com/login')
web.implicitly_wait(1)
emailElem = web.find_element_by_name('login')
emailElem.send_keys('lmac0603@163.com')
passwordElem = web.find_element_by_name('password')
passwordElem.send_keys('xywxhzsjhhgh06')
passwordElem.submit()
