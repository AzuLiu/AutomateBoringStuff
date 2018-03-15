import bs4, requests, sys, webbrowser
res = requests.get('https://www.bing.com/search?q=kpl')
res.raise_for_status()
soup = bs4.BeautifulSoup(res.text,"html.parser")
linkElems = soup.find_all("a", target="_blank")
numOpen = min(3,len(linkElems))
for i in range(numOpen):
    print(linkElems[i].get('href'))
    webbrowser.open(linkElems[i].get('href'))
