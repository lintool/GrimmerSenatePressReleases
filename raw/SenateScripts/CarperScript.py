import re,os
from nltk import utilities
from urllib import urlopen
from BeautifulSoup import BeautifulSoup

os.chdir('C:\CongressPressExpand\Carper')

html = ['http://carper.senate.gov/press/releases.cfm?type=date&month=12&year=2007',
        'http://carper.senate.gov/press/releases.cfm?type=date&month=11&year=2007',
        'http://carper.senate.gov/press/releases.cfm?type=date&month=10&year=2007',
        'http://carper.senate.gov/press/releases.cfm?type=date&month=09&year=2007',
        'http://carper.senate.gov/press/releases.cfm?type=date&month=08&year=2007',
        'http://carper.senate.gov/press/releases.cfm?type=date&month=07&year=2007',
        'http://carper.senate.gov/press/releases.cfm?type=date&month=06&year=2007',
        'http://carper.senate.gov/press/releases.cfm?type=date&month=05&year=2007',
        'http://carper.senate.gov/press/releases.cfm?type=date&month=04&year=2007',
        'http://carper.senate.gov/press/releases.cfm?type=date&month=03&year=2007',
        'http://carper.senate.gov/press/releases.cfm?type=date&month=02&year=2007',
        'http://carper.senate.gov/press/releases.cfm?type=date&month=01&year=2007',
        'http://carper.senate.gov/press/releases.cfm?type=date&month=12&year=2006',
        'http://carper.senate.gov/press/releases.cfm?type=date&month=11&year=2006',
        'http://carper.senate.gov/press/releases.cfm?type=date&month=10&year=2006',
        'http://carper.senate.gov/press/releases.cfm?type=date&month=09&year=2006',
        'http://carper.senate.gov/press/releases.cfm?type=date&month=08&year=2006',
        'http://carper.senate.gov/press/releases.cfm?type=date&month=07&year=2006',
        'http://carper.senate.gov/press/releases.cfm?type=date&month=06&year=2006',
        'http://carper.senate.gov/press/releases.cfm?type=date&month=05&year=2006',
        'http://carper.senate.gov/press/releases.cfm?type=date&month=04&year=2006',
        'http://carper.senate.gov/press/releases.cfm?type=date&month=03&year=2006',
        'http://carper.senate.gov/press/releases.cfm?type=date&month=02&year=2006',
        'http://carper.senate.gov/press/releases.cfm?type=date&month=01&year=2006',
        'http://carper.senate.gov/press/releases.cfm?type=date&month=12&year=2005',
        'http://carper.senate.gov/press/releases.cfm?type=date&month=11&year=2005',
        'http://carper.senate.gov/press/releases.cfm?type=date&month=10&year=2005',
        'http://carper.senate.gov/press/releases.cfm?type=date&month=09&year=2005',
        'http://carper.senate.gov/press/releases.cfm?type=date&month=08&year=2005',
        'http://carper.senate.gov/press/releases.cfm?type=date&month=07&year=2005',
        'http://carper.senate.gov/press/releases.cfm?type=date&month=06&year=2005',
        'http://carper.senate.gov/press/releases.cfm?type=date&month=05&year=2005',
        'http://carper.senate.gov/press/releases.cfm?type=date&month=04&year=2005',
        'http://carper.senate.gov/press/releases.cfm?type=date&month=03&year=2005',
        'http://carper.senate.gov/press/releases.cfm?type=date&month=02&year=2005',
        'http://carper.senate.gov/press/releases.cfm?type=date&month=01&year=2005']
##        'http://carper.senate.gov/apress.cfm?type=date&month=12&year=2004',
##        'http://carper.senate.gov/apress.cfm?type=date&month=11&year=2004',
##        'http://carper.senate.gov/apress.cfm?type=date&month=10&year=2004',
##        'http://carper.senate.gov/apress.cfm?type=date&month=09&year=2004',
##        'http://carper.senate.gov/apress.cfm?type=date&month=08&year=2004',
##        'http://carper.senate.gov/apress.cfm?type=date&month=07&year=2004',
##        'http://carper.senate.gov/apress.cfm?type=date&month=06&year=2004',
##        'http://carper.senate.gov/apress.cfm?type=date&month=05&year=2004',
##        'http://carper.senate.gov/apress.cfm?type=date&month=04&year=2004',
##        'http://carper.senate.gov/apress.cfm?type=date&month=03&year=2004',
##        'http://carper.senate.gov/apress.cfm?type=date&month=02&year=2004',
##        'http://carper.senate.gov/apress.cfm?type=date&month=01&year=2004',
##        'http://carper.senate.gov/apress.cfm?type=date&month=12&year=2003',
##        'http://carper.senate.gov/apress.cfm?type=date&month=11&year=2003',
##        'http://carper.senate.gov/apress.cfm?type=date&month=10&year=2003',
##        'http://carper.senate.gov/apress.cfm?type=date&month=09&year=2003',
##        'http://carper.senate.gov/apress.cfm?type=date&month=08&year=2003',
##        'http://carper.senate.gov/apress.cfm?type=date&month=07&year=2003',
##        'http://carper.senate.gov/apress.cfm?type=date&month=06&year=2003',
##        'http://carper.senate.gov/apress.cfm?type=date&month=05&year=2003',
##        'http://carper.senate.gov/apress.cfm?type=date&month=04&year=2003',
##        'http://carper.senate.gov/apress.cfm?type=date&month=03&year=2003',
##        'http://carper.senate.gov/apress.cfm?type=date&month=02&year=2003',
##        'http://carper.senate.gov/apress.cfm?type=date&month=01&year=2003',
##        'http://carper.senate.gov/apress.cfm?type=date&month=12&year=2002',
##        'http://carper.senate.gov/apress.cfm?type=date&month=11&year=2002',
##        'http://carper.senate.gov/apress.cfm?type=date&month=10&year=2002',
##        'http://carper.senate.gov/apress.cfm?type=date&month=09&year=2002',
##        'http://carper.senate.gov/apress.cfm?type=date&month=08&year=2002',
##        'http://carper.senate.gov/apress.cfm?type=date&month=07&year=2002',
##        'http://carper.senate.gov/apress.cfm?type=date&month=06&year=2002',
##        'http://carper.senate.gov/apress.cfm?type=date&month=05&year=2002',
##        'http://carper.senate.gov/apress.cfm?type=date&month=04&year=2002',
##        'http://carper.senate.gov/apress.cfm?type=date&month=03&year=2002',
##        'http://carper.senate.gov/apress.cfm?type=date&month=02&year=2002',
##        'http://carper.senate.gov/apress.cfm?type=date&month=01&year=2002',
##        'http://carper.senate.gov/apress.cfm?type=date&month=12&year=2001',
##        'http://carper.senate.gov/apress.cfm?type=date&month=11&year=2001',
##        'http://carper.senate.gov/apress.cfm?type=date&month=10&year=2001',
##        'http://carper.senate.gov/apress.cfm?type=date&month=09&year=2001',
##        'http://carper.senate.gov/apress.cfm?type=date&month=08&year=2001',
##        'http://carper.senate.gov/apress.cfm?type=date&month=07&year=2001',
##        'http://carper.senate.gov/apress.cfm?type=date&month=06&year=2001',
##        'http://carper.senate.gov/apress.cfm?type=date&month=05&year=2001',
##        'http://carper.senate.gov/apress.cfm?type=date&month=04&year=2001',
##        'http://carper.senate.gov/apress.cfm?type=date&month=03&year=2001',
##        'http://carper.senate.gov/apress.cfm?type=date&month=02&year=2001',
##        'http://carper.senate.gov/apress.cfm?type=date&month=01&year=2001']

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
    for k in range(len(res)):
        if res[k].has_key('href'):
            ab = res[k]['href']
            ba = re.findall('id', str(ab))
            if len(ba)>0 :
                fr.append(ab.encode('UTF-8'))
    spans = soup.findAll('td')
    date = []
    for k in range(len(spans)):
            if spans[k].has_key('class'):
                if spans[k]['class']=='relcelldate':
                    damp = utilities.clean_html(str(spans[k]))
                    damp = damp.split('/')
                    mons = month[damp[0]]
                    day = damp[1]
                    year = damp[-1]
                    date.append(day + mons + year)
    


    store = ''
    for num in range(len(fr)):
        store += 'http://carper.senate.gov/' + fr[num] + '\n'
    fr = store.split('\n')
    fr.remove('')

    for num in range(1,len(fr)):
        test = urlopen(fr[num]).read()
        soup2 = BeautifulSoup(test)
        spans= soup2.findAll('p')
        stores = ''
        h1s = soup2.findAll('h1')
        stores = utilities.clean_html(str(h1s[0]))
        for k in range(len(spans)):
            stores+= utilities.clean_html(str(spans[k]))
##        bs = soup2.findAll('b')
##        bsc = utilities.clean_html(str(bs))
##        bsc = bsc.split(',')
##        date = bsc[-2] + bsc[-1]
##        date = re.sub('\W', '', date)
        names = date[num-1] + 'Carper' + str(num) +'.txt'
        files = open(names, 'w')
        files.write(stores)
        files.close()
