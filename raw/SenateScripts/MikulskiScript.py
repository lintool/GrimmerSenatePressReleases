import re, os
from nltk import utilities
from urllib import urlopen
from BeautifulSoup import BeautifulSoup

os.chdir('C:\CongressPress\Mikulski')


html=['http://mikulski.senate.gov/Newsroom/releases.cfm']
##      'http://mikulski.senate.gov/cgi-bin/nph-dpc1s?dir=~mikulski/press/03/01&head=press/03/01/searchhead&foot=searchfoot&sort=-date&cols=0,65,35',
##      'http://mikulski.senate.gov/cgi-bin/nph-dpc1s?dir=~mikulski/press/03/02&head=press/03/02/searchhead&foot=searchfoot&sort=-date&cols=0,65,35',
##      'http://mikulski.senate.gov/cgi-bin/nph-dpc1s?dir=~mikulski/press/03/03&head=press/03/03/searchhead&foot=searchfoot&sort=-date&cols=0,65,35',
##      'http://mikulski.senate.gov/cgi-bin/nph-dpc1s?dir=~mikulski/press/03/04&head=press/03/04/searchhead&foot=searchfoot&sort=-date&cols=0,65,35',
##      'http://mikulski.senate.gov/cgi-bin/nph-dpc1s?dir=~mikulski/press/03/05&head=press/03/05/searchhead&foot=searchfoot&sort=-date&cols=0,65,35',
##      'http://mikulski.senate.gov/cgi-bin/nph-dpc1s?dir=~mikulski/press/03/06&head=press/03/06/searchhead&foot=searchfoot&sort=-date&cols=0,65,35',
##      'http://mikulski.senate.gov/cgi-bin/nph-dpc1s?dir=~mikulski/press/03/07&head=press/03/07/searchhead&foot=searchfoot&sort=-date&cols=0,65,35',
##      'http://mikulski.senate.gov/cgi-bin/nph-dpc1s?dir=~mikulski/press/03/08&head=press/03/08/searchhead&foot=searchfoot&sort=-date&cols=0,65,35',
##      'http://mikulski.senate.gov/cgi-bin/nph-dpc1s?dir=~mikulski/press/03/09&head=press/03/09/searchhead&foot=searchfoot&sort=-date&cols=0,65,35',
##      'http://mikulski.senate.gov/cgi-bin/nph-dpc1s?dir=~mikulski/press/03/10&head=press/03/10/searchhead&foot=searchfoot&sort=-date&cols=0,65,35',
####      'http://mikulski.senate.gov/cgi-bin/nph-dpc1s?dir=~mikulski/press/03/11&head=press/03/11/searchhead&foot=searchfoot&sort=-date&cols=0,65,35',
##      'http://mikulski.senate.gov/cgi-bin/nph-dpc1s?dir=~mikulski/press/03/12&head=press/03/12/searchhead&foot=searchfoot&sort=-date&cols=0,65,35',
##      'http://mikulski.senate.gov/cgi-bin/nph-dpc1s?dir=~mikulski/press/02/01&head=press/02/01/searchhead&foot=searchfoot&sort=-date&cols=0,65,35',
##      'http://mikulski.senate.gov/cgi-bin/nph-dpc1s?dir=~mikulski/press/02/02&head=press/02/02/searchhead&foot=searchfoot&sort=-date&cols=0,65,35',
##      'http://mikulski.senate.gov/cgi-bin/nph-dpc1s?dir=~mikulski/press/02/03&head=press/02/03/searchhead&foot=searchfoot&sort=-date&cols=0,65,35',
##      'http://mikulski.senate.gov/cgi-bin/nph-dpc1s?dir=~mikulski/press/02/04&head=press/02/04/searchhead&foot=searchfoot&sort=-date&cols=0,65,35',
##      'http://mikulski.senate.gov/cgi-bin/nph-dpc1s?dir=~mikulski/press/02/05&head=press/02/05/searchhead&foot=searchfoot&sort=-date&cols=0,65,35',
##      'http://mikulski.senate.gov/cgi-bin/nph-dpc1s?dir=~mikulski/press/02/06&head=press/02/06/searchhead&foot=searchfoot&sort=-date&cols=0,65,35',
##      'http://mikulski.senate.gov/cgi-bin/nph-dpc1s?dir=~mikulski/press/02/07&head=press/02/07/searchhead&foot=searchfoot&sort=-date&cols=0,65,35',
##      'http://mikulski.senate.gov/cgi-bin/nph-dpc1s?dir=~mikulski/press/02/08&head=press/02/08/searchhead&foot=searchfoot&sort=-date&cols=0,65,35',
##      'http://mikulski.senate.gov/cgi-bin/nph-dpc1s?dir=~mikulski/press/02/09&head=press/02/09/searchhead&foot=searchfoot&sort=-date&cols=0,65,35',
##      'http://mikulski.senate.gov/cgi-bin/nph-dpc1s?dir=~mikulski/press/02/10&head=press/02/10/searchhead&foot=searchfoot&sort=-date&cols=0,65,35',
##      'http://mikulski.senate.gov/cgi-bin/nph-dpc1s?dir=~mikulski/press/02/11&head=press/02/11/searchhead&foot=searchfoot&sort=-date&cols=0,65,35',
##      'http://mikulski.senate.gov/cgi-bin/nph-dpc1s?dir=~mikulski/press/02/12&head=press/02/12/searchhead&foot=searchfoot&sort=-date&cols=0,65,35',
##      'http://mikulski.senate.gov/cgi-bin/nph-dpc1s?dir=~mikulski/press/01/01&head=press/01/01/searchhead&foot=searchfoot&sort=-date&cols=0,65,35',
##      'http://mikulski.senate.gov/cgi-bin/nph-dpc1s?dir=~mikulski/press/01/02&head=press/01/02/searchhead&foot=searchfoot&sort=-date&cols=0,65,35',
##      'http://mikulski.senate.gov/cgi-bin/nph-dpc1s?dir=~mikulski/press/01/03&head=press/01/03/searchhead&foot=searchfoot&sort=-date&cols=0,65,35',
##      'http://mikulski.senate.gov/cgi-bin/nph-dpc1s?dir=~mikulski/press/01/04&head=press/01/04/searchhead&foot=searchfoot&sort=-date&cols=0,65,35',
##      'http://mikulski.senate.gov/cgi-bin/nph-dpc1s?dir=~mikulski/press/01/05&head=press/01/05/searchhead&foot=searchfoot&sort=-date&cols=0,65,35',
##      'http://mikulski.senate.gov/cgi-bin/nph-dpc1s?dir=~mikulski/press/01/06&head=press/01/06/searchhead&foot=searchfoot&sort=-date&cols=0,65,35',
##      'http://mikulski.senate.gov/cgi-bin/nph-dpc1s?dir=~mikulski/press/01/07&head=press/01/07/searchhead&foot=searchfoot&sort=-date&cols=0,65,35',
##      'http://mikulski.senate.gov/cgi-bin/nph-dpc1s?dir=~mikulski/press/01/08&head=press/01/08/searchhead&foot=searchfoot&sort=-date&cols=0,65,35',
##      'http://mikulski.senate.gov/cgi-bin/nph-dpc1s?dir=~mikulski/press/01/09&head=press/01/09/searchhead&foot=searchfoot&sort=-date&cols=0,65,35',
##      'http://mikulski.senate.gov/cgi-bin/nph-dpc1s?dir=~mikulski/press/01/10&head=press/01/10/searchhead&foot=searchfoot&sort=-date&cols=0,65,35',
##      'http://mikulski.senate.gov/cgi-bin/nph-dpc1s?dir=~mikulski/press/01/11&head=press/01/11/searchhead&foot=searchfoot&sort=-date&cols=0,65,35',
##      'http://mikulski.senate.gov/cgi-bin/nph-dpc1s?dir=~mikulski/press/01/12&head=press/01/12/searchhead&foot=searchfoot&sort=-date&cols=0,65,35',
##      'http://mikulski.senate.gov/cgi-bin/nph-dpc1s?dir=~mikulski/press/00/01&head=press/00/01/searchhead&foot=searchfoot&sort=-date&cols=0,65,35',
##      'http://mikulski.senate.gov/cgi-bin/nph-dpc1s?dir=~mikulski/press/00/02&head=press/00/02/searchhead&foot=searchfoot&sort=-date&cols=0,65,35',
##      'http://mikulski.senate.gov/cgi-bin/nph-dpc1s?dir=~mikulski/press/00/03&head=press/00/03/searchhead&foot=searchfoot&sort=-date&cols=0,65,35',
##      'http://mikulski.senate.gov/cgi-bin/nph-dpc1s?dir=~mikulski/press/00/04&head=press/00/04/searchhead&foot=searchfoot&sort=-date&cols=0,65,35',
##      'http://mikulski.senate.gov/cgi-bin/nph-dpc1s?dir=~mikulski/press/00/05&head=press/00/05/searchhead&foot=searchfoot&sort=-date&cols=0,65,35',
##      'http://mikulski.senate.gov/cgi-bin/nph-dpc1s?dir=~mikulski/press/00/06&head=press/00/06/searchhead&foot=searchfoot&sort=-date&cols=0,65,35',
##      'http://mikulski.senate.gov/cgi-bin/nph-dpc1s?dir=~mikulski/press/00/07&head=press/00/07/searchhead&foot=searchfoot&sort=-date&cols=0,65,35',
##      'http://mikulski.senate.gov/cgi-bin/nph-dpc1s?dir=~mikulski/press/00/08&head=press/00/08/searchhead&foot=searchfoot&sort=-date&cols=0,65,35',
##      'http://mikulski.senate.gov/cgi-bin/nph-dpc1s?dir=~mikulski/press/00/09&head=press/00/09/searchhead&foot=searchfoot&sort=-date&cols=0,65,35',
##      'http://mikulski.senate.gov/cgi-bin/nph-dpc1s?dir=~mikulski/press/00/10&head=press/00/10/searchhead&foot=searchfoot&sort=-date&cols=0,65,35',
##      'http://mikulski.senate.gov/cgi-bin/nph-dpc1s?dir=~mikulski/press/00/11&head=press/00/11/searchhead&foot=searchfoot&sort=-date&cols=0,65,35',
##      'http://mikulski.senate.gov/cgi-bin/nph-dpc1s?dir=~mikulski/press/00/12&head=press/00/12/searchhead&foot=searchfoot&sort=-date&cols=0,65,35',
##      'http://mikulski.senate.gov/cgi-bin/nph-dpc1s?dir=~mikulski/press/99/01&head=press/99/01/searchhead&foot=searchfoot&sort=-date&cols=0,65,35',
##      'http://mikulski.senate.gov/cgi-bin/nph-dpc1s?dir=~mikulski/press/99/02&head=press/99/02/searchhead&foot=searchfoot&sort=-date&cols=0,65,35',
##      'http://mikulski.senate.gov/cgi-bin/nph-dpc1s?dir=~mikulski/press/99/03&head=press/99/03/searchhead&foot=searchfoot&sort=-date&cols=0,65,35',
##      'http://mikulski.senate.gov/cgi-bin/nph-dpc1s?dir=~mikulski/press/99/04&head=press/99/04/searchhead&foot=searchfoot&sort=-date&cols=0,65,35',
##      'http://mikulski.senate.gov/cgi-bin/nph-dpc1s?dir=~mikulski/press/99/05&head=press/99/05/searchhead&foot=searchfoot&sort=-date&cols=0,65,35',
##      'http://mikulski.senate.gov/cgi-bin/nph-dpc1s?dir=~mikulski/press/99/06&head=press/99/06/searchhead&foot=searchfoot&sort=-date&cols=0,65,35',
##      'http://mikulski.senate.gov/cgi-bin/nph-dpc1s?dir=~mikulski/press/99/07&head=press/99/07/searchhead&foot=searchfoot&sort=-date&cols=0,65,35',
##      'http://mikulski.senate.gov/cgi-bin/nph-dpc1s?dir=~mikulski/press/99/08&head=press/99/08/searchhead&foot=searchfoot&sort=-date&cols=0,65,35',
##      'http://mikulski.senate.gov/cgi-bin/nph-dpc1s?dir=~mikulski/press/99/09&head=press/99/09/searchhead&foot=searchfoot&sort=-date&cols=0,65,35',
##      'http://mikulski.senate.gov/cgi-bin/nph-dpc1s?dir=~mikulski/press/99/10&head=press/99/10/searchhead&foot=searchfoot&sort=-date&cols=0,65,35',
##      'http://mikulski.senate.gov/cgi-bin/nph-dpc1s?dir=~mikulski/press/99/11&head=press/99/11/searchhead&foot=searchfoot&sort=-date&cols=0,65,35',
##      'http://mikulski.senate.gov/cgi-bin/nph-dpc1s?dir=~mikulski/press/99/12&head=press/99/12/searchhead&foot=searchfoot&sort=-date&cols=0,65,35']




for j in range(0, len(html)):
    if j==0:
        out = urlopen(html[j]).read()
        out = out[13000:]
        soup = BeautifulSoup(out)
        res  = soup.findAll('a')
        fr= []
        for k in range(len(res)):
            if res[k].has_key('href'):
                ab = res[k]['href']
                ab = ab.strip('..')
                ba = re.findall('\?id', str(ab))
                if len(ba)>0 :
                    fr.append(ab.encode('UTF-8'))
        date = []

        ps = soup.findAll('font')
        for m in range(len(ps)):
            if ps[m].has_key('face') and ps[m].has_key('size'):
                if ps[m]['face']=='verdana,geneva,helvetica' and ps[m]['size']=='1':
                    if m%2==1:
                        date.append(utilities.clean_html(str(ps[m])))
        
        store = ''
        for num in range(len(fr)):
            store += 'http://mikulski.senate.gov/' + fr[num] + '\n'
        fr = store.split('\n')
        fr.remove('')

        for num in range(0,len(fr)):
            test = urlopen(fr[num]).read()
            soup2 = BeautifulSoup(test)
            abd= soup2.findAll('a')
            for k in range(len(abd)):
                abd[k].extract()
            stores = utilities.clean_html(str(soup2))
            stores = re.sub('\W', ' ', stores)
            mint= date[num]
            mint= re.sub('\W', '', mint)
            names = 'Mikulski' + str(num) + mint + '.txt'
            files = open(names, 'w')
            files.write(stores)
            files.close()
    if j>0:
        out = urlopen(html[j]).read()
        soup = BeautifulSoup(out)
        res  = soup.findAll('a')
        fr= []
        for k in range(len(res)):
            if res[k].has_key('href'):
                ab = res[k]['href']
                ab = ab.strip('~mikulski')
                ba = re.findall('/press/', str(ab))
                if len(ba)>0 :
                    fr.append(ab.encode('UTF-8'))
        date = []
        ps = soup.findAll('td')
        for m in range(len(ps)):
            if ps[m].has_key('width'):
                if ps[m]['width']=='35%':
                    date.append(utilities.clean_html(str(ps[m])))

        store = ''
        for num in range(len(fr)):
            store += 'http://mikulski.senate.gov/' + fr[num] + '\n'
        fr = store.split('\n')
        fr.remove('')
        
        for num in range(0,len(fr)):
            test = urlopen(fr[num]).read()
            soup2 = BeautifulSoup(test)
            abd= soup2.findAll('a')
            for k in range(len(abd)):
                abd[k].extract()
            stores = utilities.clean_html(str(soup2))
            stores = re.sub('\W', ' ', stores)
            mint= date[num]
            mint= re.sub('\W', '', mint)
            names = 'Mikulski' + str(num) + mint + '.txt'
            files = open(names, 'w')
            files.write(stores)
            files.close()
        
