#http://www.mianchen.com/scraping-youtube-video-playlist/
from bs4 import BeautifulSoup
import requests
# get the html text
htmldoc = requests.get("https://www.youtube.com/feed/trending").text
print(htmldoc)
# parse the html
soup = BeautifulSoup(htmldoc, 'html.parser')
# put all links begins with '/user into a list
rawList = set(x.get('href') for x in soup('a')
           if x.get('href').startswith('/watch?'))