import urllib
import mechanize
from bs4 import BeautifulSoup

br = mechanize.Browser()
br.set_handle_robots(False)
br.addheaders = [('User-agent' , 'chrome')]


term = "cars ".replace(" ", "+")
query = 'https://www.google.com/search?num=100&site=&source=hp&q='+ term +'&oq='+term

htmltext = br.open(query).read()
#print htmltext

soup = BeautifulSoup(htmltext)

search = soup.findAll('div', attrs={'id' : 'search'})

#searchtext = str(search)[0]

#soup1 = BeautifulSoup(searchtext)
#list_items = soup1.findAll('li')

print search
#print list_items