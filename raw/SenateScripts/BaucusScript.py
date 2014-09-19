import re, os
from BeautifulSoup import BeautifulSoup
from nltk import utilities
from urllib import urlopen


os.chdir('C:\CongressPressExpand\Baucus')

html = ['http://baucus.senate.gov/newsroom/index.cfm?year=2007',
        'http://baucus.senate.gov/newsroom/index.cfm?year=2006',
        'http://baucus.senate.gov/newsroom/index.cfm?year=2005']


mon_key ={}
mon_key['January'] = 'Jan'
mon_key['February'] = 'Feb'
mon_key['March'] = 'Mar'
mon_key['April'] = 'Apr'
mon_key['May'] = 'May'
mon_key['June'] = 'Jun'
mon_key['July'] = 'Jul'
mon_key['August'] = 'Aug'
mon_key['September'] = 'Sep'
mon_key['October'] = 'Oct'
mon_key['November'] = 'Nov'
mon_key['December'] = 'Dec'


for j in range(0,len(html)):
        out = urlopen(html[j]).read()
        soup = BeautifulSoup(out)
        res  = soup.findAll('a')
        fr= []
        for k in range(len(res)):
            if res[k].has_key('href'):
                ab = res[k]['href']
                ab = ab.strip('..')
                ba = re.findall('\?id', str(ab))
                if len(ba)>0 :
                    fr.append(ab.encode('UTF-8'))
        store = ''
        for num in range(2, len(fr)):
            store += 'http://baucus.senate.gov/newsroom/' + fr[num] + '\n'
        fr = store.split('\n')
        fr.remove('')

        for num in range(len(fr)):
            test = urlopen(fr[num]).read()
            soup2 = BeautifulSoup(test)
            h2s = soup2.find('h2')
            date = h2s.findNext('p')
            date = utilities.clean_html(str(date))
            date = date.split(' ')
            mons = mon_key[date[0]]
            days = re.sub('\W', '', date[1])
            year = date[2]
            stores = utilities.clean_html(str(soup2))
            names = days + mons + year + 'Baucus' + str(num) + '.txt'
            files = open(names, 'w')
            files.write(stores)
            files.close()
            



            
