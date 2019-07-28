import requests
import bs4
#import urllib
#import time

res = requests.get("https://www.upgrad.com/");
soup = bs4.BeautifulSoup(res.text,'html.parser')

t1 = soup.findAll('div',{'class':'HeaderPrimaryNav__navItem__listItem--wrapper'})
t2 = soup.findAll('div',{'class':'HeaderPrimaryNav__navItem__subListWrapper'})
for i in t1:
    print(i.get_text())
link = []
for i in t2:
    o = i.find_all('a')
    '''for j in o:
        link.append(j.get('href'))
        print(j.get_text())'''

#del link[1]

'''for i in link:
    res = requests.get("https://www.upgrad.com"+i)
    soup = bs4.BeautifulSoup(res.text,'html.parser')
    d = soup.findAll('div',{'class':'BannerSection__programStats__static__label'})
    d1 = soup.findAll('div',{'class':'BannerSection__programStats__static__desc'})
    for i in range(len(d)):
        print(d[i].get_text())
        print(d1[i].get_text())
        print("\n")
    d2 = soup.findAll('div',{'class':'ProgramValues__list__label mb-20'})
    d3 = soup.findAll('div',{'class':'ProgramValues__list__desc'})
    for k in range(len(d2)):
        print(d2[k].get_text())
        print(d3[k].get_text())'''

