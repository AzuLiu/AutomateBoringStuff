import bs4, requests, os
url = 'https://www.xkcd.com/1524'
os.makedirs('xkcd', exist_ok=True)

while not url.endswith('#'):
    res = requests.get(url)
    res.raise_for_status()
    soup = bs4.BeautifulSoup(res.text, 'html.parser')
    try:
        comicElem = soup.find(id="comic").find('img')
        if not comicElem:
            print('Could not find comic image.')
        else:
            comicUrl = comicElem.get('src')
            print(comicUrl)
            comicRes = requests.get('http:' + comicUrl)
            comicRes.raise_for_status()
            imageFile = open(os.path.join('xkcd', os.path.basename(comicUrl)), 'wb')
            for chunk in comicRes.iter_content(100000):
                imageFile.write(chunk)
            imageFile.close()
        prevLink = soup.find('a',accesskey='p')
        url = 'http://xkcd.com' + prevLink.get('href')
    except:
        continue

print('Done')
