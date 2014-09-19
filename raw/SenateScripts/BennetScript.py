from BeautifulSoup import BeautifulSoup
import re
import os
from urllib import urlopen
from nltk import utilities
import nltk

os.chdir('C:\CongressPressExpand\Bennett')

html= ['http://bennett.senate.gov/press/releases.cfm?maxrows=248&startrow=48&']


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


for j in range(len(html)):
    out = urlopen(html[j]).read()
    soup = BeautifulSoup(out)
    res  = soup.findAll('a')
    fr= []
    for k in range(len(res)):
        if res[k].has_key('href'):
            ab = res[k]['href']
            ba = re.findall('id', str(ab))
            if len(ba)>0 :
                fr.append(ab.encode('UTF-8'))
            

    store = ''
    for num in range(len(fr)):
        store += 'http://bennett.senate.gov/press/' + fr[num] + '\n'

    fr = store.split('\n')
    fr.remove('')

    for num in range(0, len(fr)):
        test = urlopen(fr[num]).read()
        soup2 = BeautifulSoup(test)
        divs = soup2.findAll('p')
        start= soup2.findAll('title')
        date = utilities.clean_html(str(start[0])).split(':')[-1].strip(' ').split('/')
        mons = month[date[0]]
        day = date[1]
        year = date[2]
        agg = day + mons + year
        stores = ''
        for b in range(len(divs)):
            de = utilities.clean_html(str(divs[b]))
            stores += de
        names = agg + 'Bennett' + str(num) + '.txt'
        files = open(names, 'w')
        files.write(stores)
        files.close()
        
