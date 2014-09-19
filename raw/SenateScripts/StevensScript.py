import re, os
from nltk import utilities
from BeautifulSoup import BeautifulSoup
from nltk import utilities
from urllib import urlopen


os.chdir('C:\CongressPressExpand\Stevens')

html=['http://stevens.senate.gov/public/index.cfm?FuseAction=NewsRoom.PressReleases&ContentRecordType_id=ae7a6475-a01f-4da5-aa94-0a98973de620&Region_id=&Issue_id=&MonthDisplay=0&YearDisplay=2007&x=19&y=14',
      'http://stevens.senate.gov/public/index.cfm?FuseAction=NewsRoom.PressReleases&ContentRecordType_id=ae7a6475-a01f-4da5-aa94-0a98973de620&Region_id=&Issue_id=&MonthDisplay=0&YearDisplay=2006&x=18&y=17',
      'http://stevens.senate.gov/public/index.cfm?FuseAction=NewsRoom.PressReleases&ContentRecordType_id=ae7a6475-a01f-4da5-aa94-0a98973de620&Region_id=&Issue_id=&MonthDisplay=0&YearDisplay=2005&x=17&y=12']
##      'http://stevens.senate.gov/public/index.cfm?FuseAction=NewsRoom.PressReleases&ContentRecordType_id=ae7a6475-a01f-4da5-aa94-0a98973de620&Region_id=&Issue_id=&MonthDisplay=0&YearDisplay=2004&x=7&y=8',]

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

for j in range(2, len(html)):
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
            if ps[m].has_key('class') and ps[m].has_key('style'):
                if ps[m]['class']=='ContentGrid' and ps[m]['style']=='margin-right:4px;':
                    abc = utilities.clean_html(str(ps[m]))
                    abc = abc.split('/')
                    mons = month[abc[0]]
                    days = abc[1]
                    years = '20' + abc[-1]
                    date.append(days + mons + years)
                    



        store = ''
        for num in range(len(fr)):
            store += 'http://stevens.senate.gov/public/' + fr[num] + '\n'
        fr = store.split('\n')
        fr.remove('')


        for num in range(0,len(fr)-11):
                    test = urlopen(fr[num]).read()
                    soup2 = BeautifulSoup(test)
                    abd= soup2.findAll('a')
                    for k in range(len(abd)):
                        abd[k].extract()
                    divs = soup2.findAll('div')
                    for k in range(len(divs)):
                        if divs[k].has_key('style'):
                                if divs[k]['style']=='text-align:right; float:right;':
                                        divs[k].extract()
                    abc= soup2.findAll('option')
                    for k in range(len(abc)):
                        abc[k].extract()
                    abd = soup2.findAll('h3')
                    for k in range(len(abd)):
                        abd[k].extract()
                    stores = utilities.clean_html(str(soup2))
                    stores = re.sub('\W', ' ', stores)
                    mint= date[num]
                    names = mint +  'Stevens' + str(num) + '.txt'
                    files = open(names, 'w')
                    files.write(stores)
        
