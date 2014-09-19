##extracting press releases.
##we'll only do it for the 2005-2006 congress
##actually just from 2005-2006, we can extend appropriately

from BeautifulSoup import BeautifulSoup
import re
from re import *
import os
from urllib import *
from nltk import utilities
import nltk


html = ['http://akaka.senate.gov/public/index.cfm?FuseAction=PressReleases.Home&year=2006',
        'http://akaka.senate.gov/public/index.cfm?FuseAction=PressReleases.Home&year=2005' ,
        'http://akaka.senate.gov/public/index.cfm?FuseAction=PressReleases.Home&year=2007']

os.chdir('C:/CongressPressExpand/Akaka')

for j in range(0, len(html)):
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
        store += 'http://akaka.senate.gov' + fr[num] + '\n'

    fr = store.split('\n')
    fr.remove('')

    months =[]
    months.append('January')
    months.append('February')
    months.append('March')
    months.append('April')
    months.append('May')
    months.append('June')
    months.append('July')
    months.append('August')
    months.append('September')
    months.append('October')
    months.append('November')
    months.append('December')

mon_key={}
mon_key['January']= 'Jan'
mon_key['February']='Feb'
mon_key['March']='Mar'
mon_key['April']='Apr'
mon_key['May']= 'May'
mon_key['June']='Jun'
mon_key['July']='Jul'
mon_key['August']='Aug'
mon_key['September']= 'Sep'
mon_key['October']='Oct'
mon_key['November']='Nov'
mon_key['December']='Dec'
    
    
    for num in range(0,len(fr)):
        test = urlopen(fr[num]).read()
        soup2 = BeautifulSoup(test)
        divs = soup2.findAll('div')
        for m in range(len(divs)):
            childs = divs[m].findChildren('p')
            if len(childs)>0:
                stores = ''
                for b in range(len(childs)):
                    de = utilities.clean_html(str(childs[b]))
                    stores += de
        h5s = soup2.findAll('h5')
        date = utilities.clean_html(str(h5s[0]))
        date = re.sub('\W', '', date)
        for k in range(len(months)):
            ab= re.findall(months[k], date)
            if len(ab)>0:
                mons = mon_key[ab[0]]
                temp = re.sub(months[k], '', date)
                year = temp[-4:]
                day = re.sub(year, '', temp)
        names = day + mons + year + 'akaka' + str(num) + '.txt'
        files = open(names, 'w')
        files.write(stores)
        files.close()

    


        
