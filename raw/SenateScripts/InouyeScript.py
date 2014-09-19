import re,os
from nltk import utilities
from urllib import urlopen
from BeautifulSoup import BeautifulSoup

os.chdir('C:\CongressPressExpand\inouye')


html=['http://inouye.senate.gov/cgi-bin/nph-dpc1s?dir=~inouye/07pr&head=00pr/searchhead&foot=00pr/searchfoot&sort=-date&cols=0,65,35',
      'http://inouye.senate.gov/cgi-bin/nph-dpc1s?dir=~inouye/06pr&head=00pr/searchhead&foot=00pr/searchfoot&sort=-date&cols=0,65,35',
      'http://inouye.senate.gov/cgi-bin/nph-dpc1s?dir=~inouye/05pr&head=00pr/searchhead&foot=00pr/searchfoot&sort=-date&cols=0,65,35']
##      'http://inouye.senate.gov/cgi-bin/nph-dpc1s?dir=~inouye/04pr&head=00pr/searchhead&foot=00pr/searchfoot&sort=-date&cols=0,65,35',
##      'http://inouye.senate.gov/cgi-bin/nph-dpc1s?dir=~inouye/03pr&head=00pr/searchhead&foot=00pr/searchfoot&sort=-date&cols=0,65,35',
##      'http://inouye.senate.gov/cgi-bin/nph-dpc1s?dir=~inouye/02pr&head=00pr/searchhead&foot=00pr/searchfoot&sort=-date&cols=0,65,35',
##      'http://inouye.senate.gov/cgi-bin/nph-dpc1s?dir=~inouye/01pr&head=00pr/searchhead&foot=00pr/searchfoot&sort=-date&cols=0,65,35',
##      'http://inouye.senate.gov/cgi-bin/nph-dpc1s?dir=~inouye/00pr&head=00pr/searchhead&foot=00pr/searchfoot&sort=-date&cols=0,65,35',
##      'http://inouye.senate.gov/cgi-bin/nph-dpc1s?dir=~inouye/99pr&head=00pr/searchhead&foot=00pr/searchfoot&sort=-date&cols=0,65,35',
##      'http://inouye.senate.gov/cgi-bin/nph-dpc1s?dir=~inouye/98pr&head=00pr/searchhead&foot=00pr/searchfoot&sort=-date&cols=0,65,35',
##      'http://inouye.senate.gov/cgi-bin/nph-dpc1s?dir=~inouye/97pr&head=00pr/searchhead&foot=00pr/searchfoot&sort=-date&cols=0,65,35']

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
month['1']= 'Jan'
month['2'] = 'Feb'
month['3'] = 'Mar'
month['4'] = 'Apr'
month['5'] = 'May'
month['6'] = 'Jun'
month['7'] = 'Jul'
month['8'] = 'Aug'
month['9'] = 'Sep'

for j in range(0,len(html)):
    out = urlopen(html[j]).read()
    soup = BeautifulSoup(out)
    res  = soup.findAll('a')
    fr= []
    for k in range(len(res)):
        if res[k].has_key('href'):
            ab = res[k]['href']
            ba = re.findall('pr', str(ab))
            if len(ba)>0 :
                fr.append(ab.encode('UTF-8'))
    tds = soup.findAll('td')
    date=[]
    ##take away for last two years
    for m in range(len(tds)):
        if tds[m].has_key('width'):
            if tds[m]['width']=='35%':
                abc = utilities.clean_html(str(tds[m]))
                abc = abc.split('/')
                mons = month[abc[0]]
                day = abc[1]
                year = '20' + abc[-1]
                date.append(day + mons + year)


    store = ''
    for num in range(len(fr)):
        store += 'http://inouye.senate.gov/' + fr[num] + '\n'
    fr = store.split('\n')
    fr.remove('')


    



    for num in range(1,len(fr)):
            att = re.findall('html', str(fr[num]))
            if len(att)>0:
                test = urlopen(fr[num]).read()
                soup2 = BeautifulSoup(test)
                abd= soup2.findAll('a')
               # date = soup2.findAll('center')
                #date = date[1]
                #date = utilities.clean_html(str(date))
                #date = re.sub('\W', '', date)
                #mint= date
                mint = date[num]
                for k in range(len(abd)):
                    abd[k].extract()
                stores = utilities.clean_html(str(soup2))
                stores = re.sub('\W', ' ', stores)
                names = mint  + 'Inouye'  + str(num) + '.txt'
                files = open(names, 'w')
                files.write(stores)
                files.close()


    
    
