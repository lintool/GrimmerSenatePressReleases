import re, os
from BeautifulSoup import BeautifulSoup
from nltk import utilities
from urllib import urlopen


os.chdir('C:\CongressPressExpand\Cornyn')


html = ['http://cornyn.senate.gov/public/index.cfm?FuseAction=ForPress.NewsReleases&ContentRecordType_id=b94acc28-404a-4fc6-b143-a9e15bf92da4&Region_id=&Issue_id=&MonthDisplay=0&YearDisplay=2007&x=16&y=18',
        'http://cornyn.senate.gov/public/index.cfm?FuseAction=ForPress.NewsReleases&ContentRecordType_id=b94acc28-404a-4fc6-b143-a9e15bf92da4&Region_id=&Issue_id=&MonthDisplay=0&YearDisplay=2006&x=16&y=18',
        'http://cornyn.senate.gov/public/index.cfm?FuseAction=ForPress.NewsReleases&ContentRecordType_id=b94acc28-404a-4fc6-b143-a9e15bf92da4&Region_id=&Issue_id=&MonthDisplay=0&YearDisplay=2005&x=16&y=18']
##        'http://cornyn.senate.gov/public/index.cfm?FuseAction=ForPress.NewsReleases&ContentRecordType_id=b94acc28-404a-4fc6-b143-a9e15bf92da4&Region_id=&Issue_id=&MonthDisplay=0&YearDisplay=2004&x=16&y=18',
##        'http://cornyn.senate.gov/public/index.cfm?FuseAction=ForPress.NewsReleases&ContentRecordType_id=b94acc28-404a-4fc6-b143-a9e15bf92da4&Region_id=&Issue_id=&MonthDisplay=0&YearDisplay=2003&x=16&y=18']
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
            store += 'http://cornyn.senate.gov/public/' + fr[num] + '\n'
        fr = store.split('\n')
        fr.remove('')




        for num in range(2,len(fr)):
                test = urlopen(fr[num]).read()
                soup2 = BeautifulSoup(test)
                date = soup2.findAll('center')
                date = utilities.clean_html(str(date))
                date = date.split(' ')
                mons = mon_key[date[1]]
                day = re.sub('\W', '', date[2])
                year = re.sub('\W', '', date[3])
                abd= soup2.findAll('a')
                for k in range(len(abd)):
                        abd[k].extract()
                abc = soup2.findAll('h3')
                for k in range(len(abc)):
                        abc[k].extract()
                abm = soup2.findAll('option')
                for k in range(len(abm)):
                        abm[k].extract()
                stores = utilities.clean_html(str(soup2))
                stores = re.sub('\W', ' ', stores)
                names = day + mons + year  + 'Cornyn' + str(num) + '.txt'
                files = open(names, 'w')
                files.write(stores)
                files.close()
            
