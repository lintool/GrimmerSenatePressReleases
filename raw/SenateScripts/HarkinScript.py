import re, os
from nltk import utilities
from BeautifulSoup import BeautifulSoup
from urllib import urlopen

os.chdir('C:\CongressPress\Harkin')

html=['http://harkin.senate.gov/pr/?m=2172&s=439']


for j in range(len(html)):
    out = urlopen(html[j]).read()
    soup = BeautifulSoup(out)
    res  = soup.findAll('a')
    fr= []
    for k in range(len(res)):
        if res[k].has_key('href'):
            ab = res[k]['href']
            ba = re.findall('p.cfm\?i', str(ab))
            if len(ba)>0 :
                fr.append(ab.encode('UTF-8'))


    store = ''
    for num in range(len(fr)):
        store += 'http://harkin.senate.gov' + fr[num] + '\n'
    fr = store.split('\n')
    fr.remove('')


    for num in range(152, len(fr)):
            test = urlopen(fr[num]).read()
            soup2 = BeautifulSoup(test)
            date = soup2.findAll('h2')
            date = date[1]
            date = utilities.clean_html(str(date))
            date = re.sub('\W', '', date)
            #stores=''
            abd = soup2.findAll('a')
            for k in range(len(abd)):
                abd[k].extract()
            stores = soup2.findAll('p')
            stores = utilities.clean_html(str(stores))
            stores = re.sub('\W', ' ', stores)
            names = str(num) + 'Harkin'  + date + '.txt'
            files = open(names, 'w')
            files.write(stores)
            files.close()
