import requests
import bs4

def get_Program_Details(o):
    for j in o:
        print(j.get_text())
        l = j.get('href')
        if(l == "https://programs.upgrad.com/datascience-hybrid"):
            res = requests.get("https://programs.upgrad.com/datascience-hybrid")
            soup = bs4.BeautifulSoup(res.text,'html.parser')
            d =soup.findAll('font',{'color':"#dbdbdb"})
            d1 =soup.findAll('div',{'class':"page-element widget-container page-element-type-text widget-text"})

            for i in d:
                print(i.get_text())
            print("\n")
            for j in d1:
                d3 = j.findAll('font',{'color':"#5d6062"})
                for n in d3:
                    print(n.get_text())
                p = j.findAll('p',{'style':" "})
                for k in p:
                    p2 = k.findAll('font',{'color':"#ffffff"})
                    for l in p2:
                        p3 = l.findAll('b')
                        for m in p3:
                            print(m.get_text())
        else:
            res = requests.get("https://www.upgrad.com"+l)
            soup = bs4.BeautifulSoup(res.text,'html.parser')
            d = soup.findAll('div',{'class':'BannerSection__programStats__static__label'})
            d1 = soup.findAll('div',{'class':'BannerSection__programStats__static__desc'})
            for i in range(len(d)):
                 print(d1[i].get_text()+"\n"+d[i].get_text())
            print("\n")
            d2 = soup.findAll('div',{'class':'ProgramValues__list__label mb-20'})
            d3 = soup.findAll('div',{'class':'ProgramValues__list__desc'})
            for k in range(len(d2)):
                print(d2[k].get_text()+"\n"+d3[k].get_text())
            print("\n")

o = []
res = requests.get("https://www.upgrad.com/");
soup = bs4.BeautifulSoup(res.text,'html.parser')

t1 = soup.findAll('div',{'class':'HeaderPrimaryNav__navItem__listItem--wrapper'})
t2 = soup.findAll('div',{'class':'HeaderPrimaryNav__navItem__subListWrapper'})

for i in t2:
    o.append(i.find_all('a'))

for i in range(len(t1)):
    print(t1[i].get_text())
    get_Program_Details(o[i])
