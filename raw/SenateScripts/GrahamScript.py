##trick is to use the h3 letter from the other page
import re, os
from nltk import utilities
from BeautifulSoup import BeautifulSoup
from urllib import urlopen

os.chdir('C:\CongressPressExpand\Graham')

html=['http://lgraham.senate.gov/public/index.cfm?FuseAction=PressRoom.PressReleases&ContentRecordType_id=ae7a6475-a01f-4da5-aa94-0a98973de620&Region_id=&Issue_id=&MonthDisplay=0&YearDisplay=2007&x=8&y=5',
      'http://lgraham.senate.gov/public/index.cfm?FuseAction=PressRoom.PressReleases&ContentRecordType_id=ae7a6475-a01f-4da5-aa94-0a98973de620&Region_id=&Issue_id=&MonthDisplay=0&YearDisplay=2006&x=22&y=16',
      'http://lgraham.senate.gov/public/index.cfm?FuseAction=PressRoom.PressReleases&ContentRecordType_id=ae7a6475-a01f-4da5-aa94-0a98973de620&Region_id=&Issue_id=&MonthDisplay=0&YearDisplay=2005&x=18&y=14']
##      'http://lgraham.senate.gov/public/index.cfm?FuseAction=PressRoom.PressReleases&ContentRecordType_id=ae7a6475-a01f-4da5-aa94-0a98973de620&Region_id=&Issue_id=&MonthDisplay=0&YearDisplay=2004&x=25&y=9',
##      'http://lgraham.senate.gov/public/index.cfm?FuseAction=PressRoom.PressReleases&ContentRecordType_id=ae7a6475-a01f-4da5-aa94-0a98973de620&Region_id=&Issue_id=&MonthDisplay=0&YearDisplay=2003&x=16&y=11']

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
        hs= soup.findAll('h3')
        for k in range(len(res)):
            if res[k].has_key('href'):
                ab = res[k]['href']
                ba = re.findall('id', str(ab))
                if len(ba)>0 :
                    fr.append(ab.encode('UTF-8'))                  
        for m in range(len(hs)):
            if hs[m].has_key('class') and hs[m].has_key('style'):
                if hs[m]['class']== 'ContentGrid':
                    date = utilities.clean_html(str(hs))
    

        store = ''
        for num in range(len(fr)):
            store += 'http://lgraham.senate.gov/public/' + fr[num] + '\n'
        fr = store.split('\n')
        date = date.strip('[').strip(']')
        date = date.split(',')
        fr.remove('')

    ##so we can process the pages as we move along
        for num in range(1, len(fr)):
                test = urlopen(fr[num]).read()
                soup2 = BeautifulSoup(test)
                ps = soup2.findAll('a')
                for m in range(len(ps)):
                    out = ps[m].extract()
                opt = soup2.findAll('option')
                for k in range(len(opt)):
                        opt[k].extract()
                h3s = soup2.findAll('h3')
                for k in range(len(h3s)):
                        h3s[k].extract()
                stores =utilities.clean_html(str(soup2))
                stores = re.sub('\W', ' ', stores)
                date2 = date[num-1].split('/')
                mons = month[re.sub('\W', '', date2[0])]
                day = date2[1]
                year = '20' + date2[2]
                names = day + mons + year + 'Graham' + str(num) + '.txt'
                files = open(names, 'w')
                files.write(stores)
                files.close()
