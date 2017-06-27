#http://www.mianchen.com/scraping-youtube-video-playlist/
from bs4 import BeautifulSoup
import requests
# get the html text
htmldoc = requests.get("https://www.youtube.com/feed/trending").text
# parse the html
soup = BeautifulSoup(htmldoc, 'html.parser')
# put all links begins with '/user into a list
userSet = set(x.get('href') for x in soup('a')
           if x.get('href').startswith('/user'))
		   
		   
#convert set to list #maybe not needed, set working now
#userList = list(userSet)

#Generate valid url based on rawList
for user in set(userSet):
	print("https://www.youtube.com" + user + "/videos")
#after validation assign list to variable
userLinkList = set("https://www.youtube.com" + user + "/videos" for user in userSet)

#loop through the list
for vidURL in set(userLinkList):
	subHTML = requests.get(vidURL).text
	subSoup = BeautifulSoup(subHTML, 'html.parser')
	#get the subscriber tag
	spans = subSoup.find("span",attrs={"class": "yt-subscription-button-subscriber-count-branded-horizontal subscribed yt-uix-tooltip"})
	#spit out the subscriber count
	print(spans.contents)

#	userLinkList = "https://www.youtube.com" + "/user/hyperkingames" + "/videos"


#testing subscriber retrieval 
subHTML = requests.get("https://www.youtube.com/user/hyperkingames/videos").text
subSoup = BeautifulSoup(subHTML, 'html.parser')

#get the subscriber tag
spans = subSoup.find("span",attrs={"class": "yt-subscription-button-subscriber-count-branded-horizontal subscribed yt-uix-tooltip"})
#spit out the subscriber count
spans.contents

#get views for videos
viewsList = subSoup.find_all("div",attrs={"class": "yt-lockup-meta"})
vidURL = subSoup.find_all("div",attrs={"class": "yt-lockup-content"})

#validate counts match
len(viewsList)
len(vidURL)
#
subscribersCount = set(user.get('title') for userLink in subSoup
           if x.get('href').startswith('/user'))
		   
print(subscribersCount)
#
#cleanedUserSubscriber = set(user.get('title') for userLink in userLinkList
#           if userLink.get('href').startswith('/user'))
#
#cleanedUserLinkList = set(user.get('href') for userLink in userLinkList
#           if userLink.get('href').startswith('/user'))
#           
#print(cleanedUserLinkList)
#
#
##loop through user List and generate new link list
#for user in set("userList")
#	userLinkList = "https://www.youtube.com" + userList([user]) + "/videos"
#
##
#userLinkList = "https://www.youtube.com" + "/user/hyperkingames" + "/videos"
#htmldocUserPage = requests.get(userLinkList).text
#
#
#
#for user in set("userList")