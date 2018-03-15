import requests
import bs4
import os
import time
import random


def get_html(url):
    res = requests.get(url)
    res.raise_for_status()
    return res


def get_soup(res):
    soup = bs4.BeautifulSoup(res, 'html.parser')
    return soup


def save_pictures(filename, url):
    file = open(filename, 'wb')
    res = requests.get(url)
    res.raise_for_status()
    for chunk in res.iter_content(1000000):
        file.write(chunk)
    file.close()

start = time.time()
# main = 'http://photo.hupu.com/p11937.html'
main = input('图集首页地址：')
print(os.path.dirname(main))
res = get_html(main)
soup = get_soup(res.content.decode('gbk'))
dirname = soup.find('h2').get_text()
os.makedirs(dirname, exist_ok=True)
imgurls = list()
while True:
    soup = get_soup(res.content.decode('gbk'))
    imgelem = soup.find('img', id='bigpicpic')
    if not imgelem:
        continue
    imgurls.append(imgelem.get('src'))
    nextelem = soup.find(title='键盘 → 看下一张')
    if not nextelem:
        break
    nexturlbase = nextelem.get('href')
    nexturl = os.path.dirname(main)+'/'+nexturlbase
    print(nexturl)
    res = get_html(nexturl)

print('当前图集共有图片' + str(len(imgurls)) + '张')

i = 0
for imgurl in imgurls:
    i += 1
    imgurl = 'http:' + imgurl
    print('当前正在下载%d张，进度：%d%%'% (i, i/len(imgurls)*100))
    save_pictures(os.path.join(dirname, os.path.basename(imgurl)), imgurl)
end = time.time()
print('大功告成！\n共耗时：%.2fs'% (end-start))
