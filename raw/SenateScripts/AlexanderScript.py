import re, os
from nltk import utilities
from BeautifulSoup import BeautifulSoup
from urllib import urlopen



os.chdir('C:\CongressPressExpand\Alexander')

html=[  'http://alexander.senate.gov/public/index.cfm?FuseAction=PressReleases.List&Region_id=&Issue_id=&MonthDisplay=0&YearDisplay=2007',
        'http://alexander.senate.gov/public/index.cfm?FuseAction=PressReleases.List&Region_id=&Issue_id=&MonthDisplay=0&YearDisplay=2006',
        'http://alexander.senate.gov/public/index.cfm?FuseAction=PressReleases.List&Region_id=&Issue_id=&MonthDisplay=0&YearDisplay=2005']
##        'http://alexander.senate.gov/public/index.cfm?FuseAction=PressReleases.List&Region_id=&Issue_id=&MonthDisplay=6&YearDisplay=2004',
##        'http://alexander.senate.gov/public/index.cfm?FuseAction=PressReleases.List&Region_id=&Issue_id=&MonthDisplay=7&YearDisplay=2004',
##        'http://alexander.senate.gov/public/index.cfm?FuseAction=PressReleases.List&Region_id=&Issue_id=&MonthDisplay=8&YearDisplay=2004',
##        'http://alexander.senate.gov/public/index.cfm?FuseAction=PressReleases.List&Region_id=&Issue_id=&MonthDisplay=9&YearDisplay=2004',
##        'http://alexander.senate.gov/public/index.cfm?FuseAction=PressReleases.List&Region_id=&Issue_id=&MonthDisplay=10&YearDisplay=2004',
##        'http://alexander.senate.gov/public/index.cfm?FuseAction=PressReleases.List&Region_id=&Issue_id=&MonthDisplay=11&YearDisplay=2004',
##        'http://alexander.senate.gov/public/index.cfm?FuseAction=PressReleases.List&Region_id=&Issue_id=&MonthDisplay=12&YearDisplay=2004']

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
                ba = re.findall('_id', str(ab))
                if len(ba)>0 :
                    fr.append(ab.encode('UTF-8'))

        store = ''
        for num in range(2, len(fr)):
            store += 'http://alexander.senate.gov/public/' + fr[num] + '\n'
        fr = store.split('\n')
        fr.remove('')

        for num in range(0,len(fr)):
                test = urlopen(fr[num]).read()
                soup2 = BeautifulSoup(test)
                abd= soup2.findAll('a')
                for k in range(len(abd)):
                    abd[k].extract()
                tds = soup2.findAll('td')
                for k in range(len(tds)):
                        if tds[k].has_key('width'):
                                if tds[k]['width']=='1%' or tds[k]['width']=='99%' or tds[k]['width']=='90%':
                                        tds[k].extract()
                        if tds[k].has_key('style'):
                                if tds[k]['style']=='font:bold 12px Verdana; color:#5A6F94; padding:6px;':
                                        tds[k].extract()
                opts = soup2.findAll('option')
                for k in range(len(opts)):
                        opts[k].extract()
                divs = soup2.findAll('div')
                for k in range(len(divs)):
                        if divs[k].has_key('style'):
                                if divs[k]['style']=="width:180px; color:#0078B9; font-family:Arial,Verdana; text-size:11px; position:absolute; bottom:20px; right:0;":
                                        divs[k].extract()
                
                stores = utilities.clean_html(str(soup2))
                stores = re.sub('\W', ' ', stores)
                ps = soup2.findAll('strong')
                for m in range(len(ps)):
                    if ps[m].has_key('class'):
                        if ps[m]['class']=='recorddate':
                            bt = utilities.clean_html(str(ps[m]))
                            mint = re.sub('\W', ' ', bt)
                #tables = soup2.findAll('table')
                #for k in range(len(tables)):
                #        if tables[k].has_key('width') and tables[k].has_key('border') and tables[k].has_key('bordercolor') and tables[k].has_key('cellspacing') and tables[k].has_key('cellpadding'):
                #
                tester = mint.split(' ')
                mons = mon_key[tester[0]]
                day = re.sub('[a-z][a-z]', '',tester[1])
                year = tester[3]
                names = day + mons + year  + 'Alexander' + str(num) + '.txt'
                files = open(names, 'w')
                files.write(stores)
                files.close()

        
