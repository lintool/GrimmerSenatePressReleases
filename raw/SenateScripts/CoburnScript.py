import re, os
from BeautifulSoup import BeautifulSoup
from nltk import utilities
from urllib import urlopen




os.chdir('C:\CongressPressExpand\Coburn')


html=['http://coburn.senate.gov/public/index.cfm?FuseAction=LatestNews.PressReleases&ContentRecordType_id=d741b7a7-7863-4223-9904-8cb9378aa03a&Issue_id=&MonthDisplay=0&YearDisplay=2007',
      'http://coburn.senate.gov/public/index.cfm?FuseAction=LatestNews.PressReleases&ContentRecordType_id=d741b7a7-7863-4223-9904-8cb9378aa03a&Issue_id=&MonthDisplay=0&YearDisplay=2006',
      'http://coburn.senate.gov/public/index.cfm?FuseAction=LatestNews.PressReleases&ContentRecordType_id=d741b7a7-7863-4223-9904-8cb9378aa03a&Issue_id=&MonthDisplay=0&YearDisplay=2005']

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


for j in range(1,len(html)):
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
            store += 'http://coburn.senate.gov/public/' + fr[num] + '\n'
        fr = store.split('\n')
        fr.remove('')

##the problem is you need to grab text that is just
        ##sitting in the middle of the page
        
        for num in range(1, len(fr)-1):
            test = urlopen(fr[num]).read()
            soup2 = BeautifulSoup(test)
            date= soup2.findAll('h4')
            date = utilities.clean_html(str(date[0]))
            date = date.split(' ')
            mons = mon_key[date[0]]
            day = re.sub('\W', '', date[1])
            year = date[-1]
            abd = soup2.findAll('a')
            for k in range(len(abd)):
                abd[k].extract()
            opt = soup2.findAll('option')
            for k in range(len(opt)):
                opt[k].extract()
            h1s = soup2.findAll('h1')
            for k in range(len(h1s)):
                h1s[k].extract()
            h3s = soup2.findAll('h3')
            for k in range(len(h3s)):
                h3s[k].extract()
            stores = utilities.clean_html(str(soup2))
            stores = re.sub('\W', ' ', stores)
            names = day + mons + year  + 'Coburn'  +  str(num) + '.txt'
            files = open(names, 'w')
            files.write(stores)
            files.close()

            
