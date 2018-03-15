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
os.makedirs('Most_Frequently_Downloaded_eBooks', exist_ok=True)
os.chdir('Most_Frequently_Downloaded_eBooks')
fileType = {}
dirname = ''
pdfurls = []
# 1.Get all the url of Books.
urlList = []
for i in range(1, 77, 25):
    main = 'http://www.gutenberg.org/ebooks/search/?start_index=%d&sort_order=downloads' % i
    res_main = get_html(main)
    soup_main = get_soup(res_main.text)
    for urlElem in soup_main.find_all(class_='link'):
        urlList.append(urlElem.get('href'))

# 2.Find the urls of books.
for mainBranch in urlList[2:]:
    mainBranch = 'http://www.gutenberg.org' + mainBranch
    logging.debug(mainBranch)
    res = get_html(mainBranch)
    print(res.text)
    soup = get_soup(res.text)
    dirname = soup.find('h1').get_text()
    if dirname in os.listdir(os.getcwd()):
        continue
    try:
        os.makedirs(dirname, exist_ok=True)
    except NotADirectoryError:
        pass
    pdfelem = soup.findall(title='Download')
    print(pdfelem[0])
    if not pdfelem:
        continue
    pdfurls.append(pdfelem[0].get('href'))

# 3.Download the books.
# i = 0
# for pdfurl in pdfurls:
#     i += 1
#     pdfurl = 'http:' + pdfurl
#     print('当前正在下载第%d本，进度：%d%%' % (i, i/len(pdfurls)*100))
#     try:
#         save_pictures(os.path.join(dirname, dirname+'.pdf'), pdfurl)
#     except:
#         continue
# end = time.time()
# print('大功告成！\n共耗时：%.2fs' % (end-start))
