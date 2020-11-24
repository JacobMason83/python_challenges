import requests
import bs4
from bs4 import BeautifulSoup
import pprint
# from bs4.element import CData
import inflection
from inflection import titleize

# r = requests.get('http://www.dailysmarty.com/topics/python.')


# soup = BeautifulSoup(r.content, "html.parser")
#this i a beautiful soup that scrapes the requests for a tags 
# def atag_scaper(soup):
#     for link in soup.find_all('h1'):
#         return soup.get_text()
# print(atag_scaper(soup))
# pprint.pprint(links)


# def get_links(): 
#   links = soup.find_all('a')
#   link2 = []
#   for link in links:  
#     print(link.get("href"))
#     link2 = link.get("href")
#   return ''.join(link2)
# print(get_links())


# def get_the_posts():
#     titles = []
#     link2 = get_links()
#     for link in links
#     if "/posts" in link2:
#       titles.append(link) 
#       return posts
        
#     # return titles
# print(get_the_posts())
  
   

# soup = soup.find_all('/posts')
# print(soup)
# titles = soup.find_all('/posts')
# print(titles)  
# #jordans solution 
def title_generator(links):
    titles = []

    def post_formatter(url):
        if 'posts' in url:
            url = url.split('/')[-1]
            url = url.replace('-', ' ')
            url = titleize(url)
            titles.append(url)

# <!--- UPDATED CODE -->
    for link in links:
        if link.get('href') == None:
            continue
        else:
            post_formatter(link.get("href"))
# <!--- UPDATED CODE -->

    return titles


r = requests.get('http://www.dailysmarty.com/topics/python')
soup = BeautifulSoup(r.text, 'html.parser')
links = soup.find_all('a')
titles = title_generator(links)

for title in titles:
    print(title)
  
