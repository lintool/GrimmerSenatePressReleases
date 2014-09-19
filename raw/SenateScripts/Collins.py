import re, os
from nltk import utilities
from BeautifulSoup import BeautifulSoup
from urllib import urlopen

os.chdir('C:\CongressPressExpand\Collins')

html= ['http://collins.senate.gov/public/continue.cfm?FuseAction=PressRoom.PressReleases&ContentRecordType_id=ae7a6475-a01f-4da5-aa94-0a98973de620&Region_id=&Issue_id=&MonthDisplay=0&YearDisplay=2007&x=16&y=16&CFId=18597721&CFToken=41285094',
       'http://collins.senate.gov/public/continue.cfm?FuseAction=PressRoom.PressReleases&ContentRecordType_id=ae7a6475-a01f-4da5-aa94-0a98973de620&Region_id=&Issue_id=&MonthDisplay=0&YearDisplay=2006&x=16&y=16&CFId=18597721&CFToken=41285094',
       'http://collins.senate.gov/public/continue.cfm?FuseAction=PressRoom.PressReleases&ContentRecordType_id=ae7a6475-a01f-4da5-aa94-0a98973de620&Region_id=&Issue_id=&MonthDisplay=0&YearDisplay=2005&x=16&y=16&CFId=18597721&CFToken=41285094']
##       'http://collins.senate.gov/public/continue.cfm?FuseAction=PressRoom.PressReleases&ContentRecordType_id=ae7a6475-a01f-4da5-aa94-0a98973de620&Region_id=&Issue_id=&MonthDisplay=0&YearDisplay=2004&x=16&y=16&CFId=18597721&CFToken=41285094',
##       'http://collins.senate.gov/public/continue.cfm?FuseAction=PressRoom.PressReleases&ContentRecordType_id=ae7a6475-a01f-4da5-aa94-0a98973de620&Region_id=&Issue_id=&MonthDisplay=0&YearDisplay=2003&x=16&y=16&CFId=18597721&CFToken=41285094',
##       'http://collins.senate.gov/public/continue.cfm?FuseAction=PressRoom.PressReleases&ContentRecordType_id=ae7a6475-a01f-4da5-aa94-0a98973de620&Region_id=&Issue_id=&MonthDisplay=0&YearDisplay=2002&x=16&y=16&CFId=18597721&CFToken=41285094',
##       'http://collins.senate.gov/public/continue.cfm?FuseAction=PressRoom.PressReleases&ContentRecordType_id=ae7a6475-a01f-4da5-aa94-0a98973de620&Region_id=&Issue_id=&MonthDisplay=0&YearDisplay=2001&x=16&y=16&CFId=18597721&CFToken=41285094',
##       'http://collins.senate.gov/public/continue.cfm?FuseAction=PressRoom.PressReleases&ContentRecordType_id=ae7a6475-a01f-4da5-aa94-0a98973de620&Region_id=&Issue_id=&MonthDisplay=0&YearDisplay=1998&x=16&y=16&CFId=18597721&CFToken=41285094']

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

for j in range(2,len(html)):
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
    date =[]
    ps = soup.findAll('h3')
    for m in range(len(ps)):
        if ps[m].has_key('class'):
            if ps[m]['class']=='ContentGrid':
                abc = utilities.clean_html(str(ps[m]))
                abc = abc.split('/')
                mons = month[abc[0]]
                day = abc[1]
                year = '20' + abc[2]
                date.append(day + mons + year)
    


    store = ''
    for num in range(len(fr)):
        store += 'http://collins.senate.gov/public/' + fr[num] + '\n'
    fr = store.split('\n')
    fr.remove('')
    fr = fr[3:]

    for num in range(0, len(fr)):
            test = urlopen(fr[num]).read()
            soup2 = BeautifulSoup(test)
            mint = date[num]
            divs = soup2.findAll('div')
            abd= soup2.findAll('a')
            for k in range(len(abd)):
                abd[k].extract()
            act = soup2.findAll('h3')
            for k in range(len(act)):
                    act[k].extract()
            acd= soup2.findAll('h1')
            for k in range(len(acd)):
                    acd[k].extract()
            abd = soup2.findAll('option')
            for k in range(len(abd)):
                    abd[k].extract()
            stores = utilities.clean_html(str(soup2))
            stores = re.sub('\W', ' ', stores)
            names = mint + 'Collins' + str(num) + '.txt'
            files = open(names, 'w')
            files.write(stores)
            files.close()
