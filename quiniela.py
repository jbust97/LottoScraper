

from datetime import timedelta, date
from bs4 import BeautifulSoup
import urllib.request as urllib2


def daterange(start_date, end_date):
    for n in range(int ((end_date - start_date).days)):          
        yield start_date + timedelta(n)
res  = []
start_date = date(2015, 6, 1)
end_date = date(2019 ,1,31)
c = 0
total = (end_date - start_date).days
for single_date in daterange(start_date, end_date):
    c = c + 1
    url = "https://www.tuquinielateete.com/Resultados/Detalle/" +single_date.strftime("%d-%m-%Y");
    content = urllib2.urlopen(url).read()
    soup = BeautifulSoup(content,features = "html.parser")
    p = soup.find_all('div', class_= "cifra cabeza")
    for i in range(0,3):
        par = p[i].contents[0].strip()
        if par.isdigit():
            res.append(par)
    if c % 100 == 0:
        print(str(c) + " out of " + str(total)+ " days.")

with open('datosTrue.txt', 'w') as f:
    for item in res:
        f.write("%s\n" % item)
