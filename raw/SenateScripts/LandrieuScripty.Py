import re, os
from nltk import utilities
from urllib import urlopen
from BeautifulSoup import BeautifulSoup

os.chdir('C:\CongressPressExpand\Landrieu')


html=['http://www.senate.gov/cgi-bin/nph-dpc1s?dir=~landrieu/releases/07&head=news/prtop.htm&foot=news/prbot.htm&sort=-date&cols=0,90,10',
      'http://www.senate.gov/cgi-bin/nph-dpc1s?dir=~landrieu/releases/06&head=news/prtop.htm&foot=news/prbot.htm&sort=-date&cols=0,90,10',
      'http://www.senate.gov/cgi-bin/nph-dpc1s?dir=~landrieu/releases/05&head=news/prtop.htm&foot=news/prbot.htm&sort=-date&cols=0,90,10']
##      'http://www.senate.gov/cgi-bin/nph-dpc1s?dir=~landrieu/releases/04&head=news/prtop.htm&foot=news/prbot.htm&sort=-date&cols=0,90,10',
##      'http://www.senate.gov/cgi-bin/nph-dpc1s?dir=~landrieu/releases/03&head=news/prtop.htm&foot=news/prbot.htm&sort=-date&cols=0,90,10',
##      'http://www.senate.gov/cgi-bin/nph-dpc1s?dir=~landrieu/releases/02&head=news/prtop.htm&foot=news/prbot.htm&sort=-date&cols=0,90,10',
##      'http://www.senate.gov/cgi-bin/nph-dpc1s?dir=~landrieu/releases/01&head=news/prtop.htm&foot=news/prbot.htm&sort=-date&cols=0,90,10',
##      'http://www.senate.gov/cgi-bin/nph-dpc1s?dir=~landrieu/releases/00&head=news/prtop.htm&foot=news/prbot.htm&sort=-date&cols=0,90,10']



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
            ba = re.findall('/releases/0', str(ab))
            if len(ba)>0 :
                fr.append(ab.encode('UTF-8'))
    date=[]
    dates = soup.findAll('td')
    for m in range(1,len(dates)):
        if dates[m].has_key('width'):
            if dates[m]['width']=='10%':
                abc = utilities.clean_html(str(dates[m]))
                abc = abc.split('/')
                mons = month[abc[0]]
                day = abc[1]
                year = '20' + abc[-1]
                date.append(day + mons + year)



    store = ''
    for num in range(len(fr)):
        store += 'http://landrieu.senate.gov/' + fr[num] + '\n'
    fr = store.split('\n')
    fr.remove('')

    for num in range(0,len(fr)):
        test = urlopen(fr[num]).read()
        soup2 = BeautifulSoup(test)
        abd= soup2.findAll('a')
        mint = date[num]
        for k in range(len(abd)):
            abd[k].extract()
        stores = utilities.clean_html(str(soup2))
        stores = re.sub('\W', ' ', stores)
        names = mint + 'Landrieu' + str(num)+ '.txt'
        files = open(names, 'w')
        files.write(stores)
        files.close()
