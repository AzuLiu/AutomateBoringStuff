import requests
import os
import re

def get_html(url):
    res = requests.get(url)
    res.raise_for_status()
    return res


def save_pictures(filename, url):
    file = open(filename, 'wb')
    res = requests.get(url)
    res.raise_for_status()
    for chunk in res.iter_content(1000000):
        file.write(chunk)
    file.close()

# 1.Get image url.
main = get_html('http://www.bing.com?intIF=')
reg = re.compile(r'/az(.*?)jpg')
url_image = 'http://www.bing.com' + reg.search(main.text).group()

# 2.Save the image to the folder
os.makedirs('BingEveryday', exist_ok=True)
os.chdir('BingEveryday')
filename = os.path.basename(url_image)
save_pictures(filename, url_image)
print('Done')
