##this file is the new set of scrapes for Bob Casey

import os, re
from nltk import utilities
from BeautifulSoup import BeautifulSoup
from urllib import urlopen


os.chdir('C:\CongressPressExpand\Casey')


htmls='http://casey.senate.gov/newsroom/press/index.cfm?PageNum_rs='

test  = range(8, 26)

html=[]

for k in range(len(test)):
    abc = htmls + str(test[k])
    html.append(abc)

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

    
for j in range(0,len(html)):
        out = urlopen(html[j]).read()
        soup = BeautifulSoup(out)
        res = soup.findAll('a')
        fr = []
        for k in range(len(res)):
            if res[k].has_key('href'):
                if res[k]['href']:
                    ab = res[k]['href']
                    espn = re.findall('press/release', ab)
                    if len(espn)>0:
                        fr.append(ab.encode('UTF-8'))
        date = []
        tds = soup.findAll('td')
        for k in range(len(tds)):
            if tds[k].has_key('class'):
                if tds[k]['class']=='date':
                   temps = utilities.clean_html(str(tds[k]))
                   temps = temps.split('.')
                   mons = temps[0]
                   mons = re.sub('\W', '', mons)
                   mons = month[mons]
                   day = temps[1]
                   year = temps[-1]
                   year = re.sub('\W', '', year)
                   year = '20' + year
                   date.append(day + mons + year)

        for num in range(0, len(fr)):
            test = urlopen(fr[num]).read()
            soup2= BeautifulSoup(test)
            h2s = soup2.findAll('h2')
            ps = soup2.findAll('p')
            h2s = utilities.clean_html(str(h2s[0]))
            store = ''
            store += h2s + ' '
            for k in range(len(ps)):
                if ps[k].has_key('id')==False:
                    store += utilities.clean_html(str(ps[k])) + ' '
            temp_date = date[num]
            names = temp_date + 'Casey' + str(num) + '.txt'
            files = open(names, 'w')
            files.write(store)
            files.close()
        
