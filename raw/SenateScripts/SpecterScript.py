import re, os
from nltk import utilities
from BeautifulSoup import BeautifulSoup
from urllib import urlopen

os.chdir('C:\CongressPressExpand\Specter')


html=['http://specter.senate.gov/public/index.cfm?FuseAction=NewsRoom.NewsReleases&ContentRecordType_id=b94acc28-404a-4fc6-b143-a9e15bf92da4&Region_id=&Issue_id=&MonthDisplay=0&YearDisplay=2007&x=22&y=7',
      'http://specter.senate.gov/public/index.cfm?FuseAction=NewsRoom.NewsReleases&ContentRecordType_id=b94acc28-404a-4fc6-b143-a9e15bf92da4&Region_id=&Issue_id=&MonthDisplay=0&YearDisplay=2006&x=15&y=9',
      'http://specter.senate.gov/public/index.cfm?FuseAction=NewsRoom.NewsReleases&ContentRecordType_id=b94acc28-404a-4fc6-b143-a9e15bf92da4&Region_id=&Issue_id=&MonthDisplay=0&YearDisplay=2005&x=29&y=13']
##      'http://specter.senate.gov/public/index.cfm?FuseAction=NewsRoom.NewsReleases&ContentRecordType_id=b94acc28-404a-4fc6-b143-a9e15bf92da4&Region_id=&Issue_id=&MonthDisplay=0&YearDisplay=2004&x=15&y=8',
##      'http://specter.senate.gov/public/index.cfm?FuseAction=NewsRoom.NewsReleases&ContentRecordType_id=b94acc28-404a-4fc6-b143-a9e15bf92da4&Region_id=&Issue_id=&MonthDisplay=0&YearDisplay=2003&x=2&y=18',
##      'http://specter.senate.gov/public/index.cfm?FuseAction=NewsRoom.NewsReleases&ContentRecordType_id=b94acc28-404a-4fc6-b143-a9e15bf92da4&Region_id=&Issue_id=&MonthDisplay=0&YearDisplay=2002&x=6&y=13',
##      'http://specter.senate.gov/public/index.cfm?FuseAction=NewsRoom.NewsReleases&ContentRecordType_id=b94acc28-404a-4fc6-b143-a9e15bf92da4&Region_id=&Issue_id=&MonthDisplay=0&YearDisplay=2001&x=12&y=13']

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

for j in range(0, len(html)):
        out = urlopen(html[j]).read()
        soup = BeautifulSoup(out)
        res  = soup.findAll('a')
        fr= []
        for k in range(len(res)):
            if res[k].has_key('href'):
                ab = res[k]['href']
                ab = ab.strip('..')
                ba = re.findall('_id', str(ab))
                if len(ba)>0 :
                    fr.append(ab.encode('UTF-8'))
        date =[]
        ps = soup.findAll('h3')
        for m in range(len(ps)):
            if ps[m].has_key('class'):
                if ps[m]['class']=='ContentGrid':
                    abc = utilities.clean_html(str(ps[m]))
                    abc = abc.split('/')
                    mons = month[abc[0]]
                    days = abc[1]
                    years = '20' + abc[-1]
                    date.append(days + mons + years)


        store = ''
        for num in range(len(fr)):
            store += 'http://specter.senate.gov/public/' + fr[num] + '\n'
        fr = store.split('\n')
        fr.remove('')

        for num in range(3,len(fr)):
                    test = urlopen(fr[num]).read()
                    soup2 = BeautifulSoup(test)
                    abd= soup2.findAll('a')
                    for k in range(len(abd)):
                        abd[k].extract()
                    abc = soup2.findAll('option')
                    for k in range(len(abc)):
                        abc[k].extract()
                    apt = soup2.findAll('td')
                    for k in range(len(apt)):
                        if apt[k].has_key('class'):
                                if apt[k]['class']=='EventsText' or apt[k]['class']=='CopyText' or apt[k]['class']=='NewsAlert':
                                        apt[k].extract()
                    h3s = soup2.findAll('h3')
                    for k in range(len(h3s)):
                        h3s[k].extract()
                    script = soup2.findAll('script')
                    for k in range(len(script)):
                        script[k].extract()
                    h1s = soup2.findAll('h1')
                    for m in range(len(h1s)):
                        h1s[m].extract()
                    h5s = soup2.findAll('h5')
                    for k in range(len(h5s)):
                        h5s[k].extract()
                    h6s = soup2.findAll('h6')
                    for m in range(len(h6s)):
                        h6s[m].extract()
                    stores = utilities.clean_html(str(soup2))
                    stores = re.sub('\W', ' ', stores)
                    mint= date[num-3]
                    mint= re.sub('\W', '', mint)
                    names = mint  + 'Specter'  +  str(num) + '.txt'
                    files = open(names, 'w')
                    files.write(stores)
                    files.close() 
        
                    
