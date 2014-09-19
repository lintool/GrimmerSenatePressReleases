##this is a new script scrape Evan Bayh's Website (the old script wont' work on
##on the new data



from BeautifulSoup import BeautifulSoup
import re
import os
from urllib import urlopen
from nltk import utilities



htmls= 'http://bayh.senate.gov/news/press/index.cfm?PageNum_rs='

html = []
numbers = range(4, 30)

for k in numbers:
    test = htmls + str(k)
    html.append(test)
    
os.chdir('C:\CongressPressExpand\Bayh')

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
        dts = soup.findAll('dt')
        for k in range(len(dts)):
            temp = utilities.clean_html(str(dts[k]))
            temp = temp.split('.')
            mons = month[temp[0]]
            day  = temp[1]
            year = '20' + temp[2]
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
            names = temp_date + 'Bayh' + str(num) + '.txt'
            files = open(names, 'w')
            files.write(store)
            files.close()
            
