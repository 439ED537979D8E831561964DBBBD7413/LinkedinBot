import requests
import bs4
import json

url = 'https://ir.linkedin.com/in/reza-godaz-21511977'
track_url = 'https://www.linkedin.com/li/track'
headers={'Host':'www.linkedin.com','User-Agent':'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:51.0) Gecko/20100101 Firefox/51.0','Accept-Language':'en-US,en;q=0.5'}

track_page = requests.get(track_url,headers=headers)
essential_cookies = {}
for c in track_page.cookies:
    essential_cookies[ c.name ] = c.value

page = requests.get(url,headers=headers,cookies=essential_cookies)
soup = bs4.BeautifulSoup(page.content,'html.parser')
activities = soup.find('section',attrs={'id':'feed','class':'profile-section single-section','data-section':'posts'})

print( activities.contents[0].text )
for c in activities.contents[1].contents:
    print(c.text)

print('DEBUG')



'''

soup = bs4.BeautifulSoup(page.content,'html.parser')
content = soup.find('div',attrs={'class':'pv-recent-activity-detail__outlet-container'})

'''