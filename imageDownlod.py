import requests
import bs4
import os

# Create a new dictionary to save images.
os.makedirs('Pictures', exist_ok=True)

# Get img element from url.
url = 'http://photo.hupu.com/nba/p35162-1.html'

res = requests.get(url)
res.raise_for_status()
soup = bs4.BeautifulSoup(res.text, 'html.parser')
imgElem = soup.find_all(id='bigpicpic')
print(imgElem)
imgUrl = (imgElem[0].get('src'))
imgFile = open(os.path.join('Pictures',os.path.basename(imgUrl)), 'wb')
for chunk in requests.get('http:' + imgUrl).iter_content(1000000):
    imgFile.write(chunk)
imgFile.close()
