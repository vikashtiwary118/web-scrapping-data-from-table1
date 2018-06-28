import urllib.request
import bs4 as bs
import pandas as pd

wp = urllib.request.urlopen("https://www.zaubacorp.com/company/AVANTI-FEEDS-LIMITED/L16001AP1993PLC095778")
pw = wp.read()
lables=[]
data=[]
soup=bs.BeautifulSoup(pw,'lxml')
table=soup.find('div',{'class':'col-lg-12 col-md-12 col-sm-12 col-xs-12'})
#print(table.text)
rows=table.find_all('tr')
for row in rows:
    lables.append(str(row.find_all('td')[0].text))
    data.append(str(row.find_all('td')[1].text))
cols={'field':lables,'Data':data}
df=pd.DataFrame(cols)
print(df)