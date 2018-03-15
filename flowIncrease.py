import time
import random
import requests
from selenium import webdriver

def Firefox():
    Firefoxpath =r'C:\Program Files\Mozilla Firefox\geckodriver.exe'
    return webdriver.Firefox(executable_path=Firefoxpath)

def selenium_flow(url, num=100):
    browser = Firefox()
    browser.get(url)
    for i in range(num):
        browser.refresh()


def requests_flow(url, num=100 , headers={}):
    for i in range(num):
        requests.get(url, headers=headers)

headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:56.0) Gecko/20100101 Firefox/56.0'}
