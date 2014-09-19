##this file scrapes the press release from Joe Biden's website (updated)


from BeautifulSoup import BeautifulSoup
import re
import os
from urllib import urlopen
from nltk import utilities
import nltk

os.chdir('C:\CongressPressExpand\Biden')

htmls= 'http://biden.senate.gov/press/press_releases/index.cfm?PageNum_rs='

html = []
numbers = range(12, 52)

for k in numbers:
    test = htmls + str(k)
    html.append(test)



os.chdir('C:\CongressPressExpand\Biden')

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
        res  = soup.findAll('a')
        fr= []
        for k in range(len(res)):
            if res[k].has_key('href'):
                ab = res[k]['href']
                ab = ab.strip('..')
                ba = re.findall('release', str(ab))
                if len(ba)>0 :
                    fr.append(ab.encode('UTF-8'))
        date = []
        ps = soup.findAll('p')
        for k in range(len(ps)):
            if ps[k].has_key('class'):
                if ps[k]['class']=='press_date':
                    temp = utilities.clean_html(str(ps[k])).split('.')
                    mons = month[temp[0]]
                    day = temp[1]
                    year= '20' + temp[2]
                    agg = day + mons + year
                    date.append(agg)
            
        for num in range(1, len(fr)):
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
            temp_date = date[num-1]
            names = temp_date + 'Biden' + str(num) + '.txt'
            files = open(names, 'w')
            files.write(store)
            files.close()
