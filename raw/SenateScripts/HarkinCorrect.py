##this file is the new scraping file for Tom Harkin

import re, os
from nltk import utilities
from BeautifulSoup import BeautifulSoup
from urllib import urlopen

os.chdir('C:\CongressPressExpand\Harkin')

html=['http://harkin.senate.gov/pr/?m=1733&s=439']
month= {}
month['01']= 'Jan'
month['02'] = 'Feb'
month['03'] = 'Mar'
month['04'] = 'Apr'
month['05'] = 'May'
month['06'] = 'Jun'
month['07'] = 'Jul'
month['08'] = 'Aug'
month['09'] = 'Sep'
month['10'] = 'Oct'
month['11'] = 'Nov'
month['12'] = 'Dec'
month['1']= 'Jan'
month['2'] = 'Feb'
month['3'] = 'Mar'
month['4'] = 'Apr'
month['5'] = 'May'
month['6'] = 'Jun'
month['7'] = 'Jul'
month['8'] = 'Aug'
month['9'] = 'Sep'

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
    date = []
    spans = soup.findAll('span')
    for k in range(len(spans)):
        if spans[k].has_key('class'):
            if spans[k]['class']=='smaller':
                abc = utilities.clean_html(str(spans[k]))
                abc = abc.split('/')
                mons = month[abc[0]]
                day = abc[1]
                year = abc[-1]
                date.append(day + mons + year)
                
    store = ''
    for num in range(len(fr)):
        store += 'http://harkin.senate.gov' + fr[num] + '\n'
    fr = store.split('\n')
    fr.remove('')

    for num in range(0, len(fr)):
            test = urlopen(fr[num]).read()
            soup2 = BeautifulSoup(test)
            mint =  date[num]
            #title = soup.findAll('title')
            #title = utilities.clean_html(str(title))
            #stores=''
            abd = soup2.findAll('a')
            for k in range(len(abd)):
                abd[k].extract()
            stores = ''
            #stores += title + ' '
            ps = soup2.findAll('p')
            ps = utilities.clean_html(str(ps))
            ps = re.sub('\W', ' ', ps)
            stores += ps 
            names = mint + 'Harkin'  + str(num) + '.txt'
            files = open(names, 'w')
            files.write(stores)
            files.close()

    
