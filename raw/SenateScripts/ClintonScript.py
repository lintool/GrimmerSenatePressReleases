import re,os
from nltk import utilities
from BeautifulSoup import BeautifulSoup
from urllib import urlopen



os.chdir('C:\CongressPressExpand\Clinton')

html= ['http://clinton.senate.gov/news/statements/index.cfm?year=2007',
      'http://clinton.senate.gov/news/statements/index.cfm?year=2006',
       'http://clinton.senate.gov/news/statements/index.cfm?year=2005']
##       'http://clinton.senate.gov/news/statements/index.cfm?year=2004',
##       'http://clinton.senate.gov/news/statements/index.cfm?year=2003',
##       'http://clinton.senate.gov/news/statements/index.cfm?year=2002',
##       'http://clinton.senate.gov/news/statements/index.cfm?year=2001']
##
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



for j in range(3, len(html)):
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
            store += 'http://clinton.senate.gov/news/statements/' + fr[num] + '\n'
        fr = store.split('\n')
        fr.remove('')


        for num in range(0, len(fr)):
            test = urlopen(fr[num]).read()
            soup2 = BeautifulSoup(test)
            ps = soup2.findAll('p')
            date = utilities.clean_html(str(ps[0]))
            date = date.split(' ')
            mons = mon_key[date[0]]
            day = re.sub('\W', '', date[1])
            year = date[2]
            text = ''
            for k in range(len(ps)):
                text += utilities.clean_html(str(ps[k])) + ' '
            stores = re.sub('\W', ' ' , text)
            names = day + mons + year + 'Clinton'  +  str(num) + '.txt'
            files = open(names, 'w')
            files.write(stores)
            files.close()
