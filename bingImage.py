#! python3
from selenium import webdriver
import requests
import os
import re

def save_pictures(filename, url):
    file = open(filename, 'wb')
    res = requests.get(url)
    res.raise_for_status()
    for chunk in res.iter_content(1000000):
        file.write(chunk)
    file.close()

def Firefox():
    Firefoxpath =r'C:\Program Files\Mozilla Firefox\geckodriver.exe'
    return webdriver.Firefox(executable_path=Firefoxpath)

# 1.Get image url
web = Firefox()
web.get('http://www.bing.com?intIF=')
# web.implicitly_wait(5)
html = web.page_source
web.close()
reg = re.compile(r'/az(.*?)jpg')
main = 'http://www.bing.com'
url_image = main + reg.search(html).group()

# 2.Save the image to the folder
os.makedirs('BingEveryday',exist_ok=True)
os.chdir('BingEveryday')
filename = os.path.basename(url_image)
save_pictures(filename, url_image)
print('Done')
