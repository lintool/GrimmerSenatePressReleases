import re,os
from nltk import utilities
from BeautifulSoup import BeautifulSoup
from urllib import urlopen


os.chdir('C:\CongressPressExpand\McCain')


html=['http://mccain.senate.gov/public/index.cfm?FuseAction=PressOffice.PressReleases&ContentRecordType_id=75e7e4a0-6088-44b6-8061-089d80513dc4&Region_id=&Issue_id=&MonthDisplay=0&YearDisplay=2007',
      'http://mccain.senate.gov/public/index.cfm?FuseAction=PressOffice.PressReleases&ContentRecordType_id=75e7e4a0-6088-44b6-8061-089d80513dc4&Region_id=&Issue_id=&MonthDisplay=0&YearDisplay=2006',
      'http://mccain.senate.gov/public/index.cfm?FuseAction=PressOffice.PressReleases&ContentRecordType_id=75e7e4a0-6088-44b6-8061-089d80513dc4&Region_id=&Issue_id=&MonthDisplay=0&YearDisplay=2005']
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

for j in range(1, len(html)):
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
    date = []
    ps = soup.findAll('h3')
    for k in range(len(ps)):
        if ps[k].has_key('class'):
            if ps[k]['class']=='ContentGrid':
                abc = utilities.clean_html(str(ps[k]))
                abc = abc.split('/')
                mons = month[abc[0]]
                day = abc[1]
                years = '20' + abc[-1]
                date.append(day + mons + years)

    store = ''
    for num in range(len(fr)):
        store += 'http://mccain.senate.gov/public/' + fr[num] + '\n'
    fr = store.split('\n')
    fr.remove('')

    for num in range(1,len(fr)-1):
        test = urlopen(fr[num]).read()
        soup2 = BeautifulSoup(test)
        abd= soup2.findAll('a')
        for k in range(len(abd)):
            abd[k].extract()
        opt = soup2.findAll('option')
        for k in range(len(opt)):
            opt[k].extract()
        h3s = soup2.findAll('h3')
        for k in range(len(h3s)):
            h3s[k].extract()
        stores = utilities.clean_html(str(soup2))
        stores = re.sub('\W', ' ', stores)
        mint= date[num-1]
        names = mint  + 'McCain'  + str(num) + '.txt'
        files = open(names, 'w')
        files.write(stores)
        files.close()
