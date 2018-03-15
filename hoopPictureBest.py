import requests
import bs4
import os
import time
import logging

logging.basicConfig(level= logging.DEBUG, format='%(message)s')
logging.disable(logging.DEBUG)

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
os.makedirs('Best_Picture_of_Hupu', exist_ok=True)
os.chdir('Best_Picture_of_Hupu')

# 1.Get all the url of group of images.
urlList = []
for i in range(1, 11):
    main = 'http://photo.hupu.com/nba/feature?p=%d&o=2' % i
    res_main = get_html(main)
    soup_main = get_soup(res_main.content.decode('gbk'))
    urlElems = soup_main.find_all('a', class_='ku')
    for urlElem in urlElems:
        url = urlElem.get('href')
        urlList.append(url)
logging.debug('urlList='+str(urlList))

# 2.Get every picture from all the group.
for mainBranch in urlList:
    mainBranch = 'http://photo.hupu.com' + mainBranch
    res = get_html(mainBranch)
    soup = get_soup(res.content.decode('gbk'))
    dirname = soup.find('h2').get_text()
    if dirname in os.listdir(os.getcwd()):
        continue
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
        nexturl = os.path.dirname(mainBranch)+'/'+nexturlbase
        res = get_html(nexturl)

    print('当前图集共有图片' + str(len(imgurls)) + '张')

    i = 0
    for imgurl in imgurls:
        i += 1
        imgurl = 'http:' + imgurl
        print('当前正在下载%d张，进度：%d%%' % (i, i/len(imgurls)*100))
        try:
            save_pictures(os.path.join(dirname, os.path.basename(imgurl)), imgurl)
        except:
            continue
end = time.time()
print('大功告成！\n共耗时：%.2fs' % (end-start))
