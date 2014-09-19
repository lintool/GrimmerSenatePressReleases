import re, os
from BeautifulSoup import BeautifulSoup
from urllib import urlopen
from nltk import utilities


os.chdir('C:\CongressPressExpand\Kohl')

html=['http://www.senate.gov/cgi-bin/nph-dpc2s?dir=~kohl/press/07/01&sort=-date&cols=0,70,30',
      'http://www.senate.gov/cgi-bin/nph-dpc2s?dir=~kohl/press/07/02&sort=-date&cols=0,70,30',
      'http://www.senate.gov/cgi-bin/nph-dpc2s?dir=~kohl/press/07/03&sort=-date&cols=0,70,30',
      'http://www.senate.gov/cgi-bin/nph-dpc2s?dir=~kohl/press/07/04&sort=-date&cols=0,70,30',
      'http://www.senate.gov/cgi-bin/nph-dpc2s?dir=~kohl/press/07/05&sort=-date&cols=0,70,30',
      'http://www.senate.gov/cgi-bin/nph-dpc2s?dir=~kohl/press/07/06&sort=-date&cols=0,70,30',
      'http://www.senate.gov/cgi-bin/nph-dpc2s?dir=~kohl/press/07/07&sort=-date&cols=0,70,30',
      'http://www.senate.gov/cgi-bin/nph-dpc2s?dir=~kohl/press/07/08&sort=-date&cols=0,70,30',
      'http://www.senate.gov/cgi-bin/nph-dpc2s?dir=~kohl/press/07/09&sort=-date&cols=0,70,30',
      'http://www.senate.gov/cgi-bin/nph-dpc2s?dir=~kohl/press/07/10&sort=-date&cols=0,70,30',
      'http://www.senate.gov/cgi-bin/nph-dpc2s?dir=~kohl/press/07/11&sort=-date&cols=0,70,30',
      'http://www.senate.gov/cgi-bin/nph-dpc2s?dir=~kohl/press/07/12&sort=-date&cols=0,70,30',
      'http://www.senate.gov/cgi-bin/nph-dpc2s?dir=~kohl/press/06/01&sort=-date&cols=0,70,30',
      'http://www.senate.gov/cgi-bin/nph-dpc2s?dir=~kohl/press/06/02&sort=-date&cols=0,70,30',
      'http://www.senate.gov/cgi-bin/nph-dpc2s?dir=~kohl/press/06/03&sort=-date&cols=0,70,30',
      'http://www.senate.gov/cgi-bin/nph-dpc2s?dir=~kohl/press/06/04&sort=-date&cols=0,70,30',
      'http://www.senate.gov/cgi-bin/nph-dpc2s?dir=~kohl/press/06/05&sort=-date&cols=0,70,30',
      'http://www.senate.gov/cgi-bin/nph-dpc2s?dir=~kohl/press/06/06&sort=-date&cols=0,70,30',
      'http://www.senate.gov/cgi-bin/nph-dpc2s?dir=~kohl/press/06/07&sort=-date&cols=0,70,30',
      'http://www.senate.gov/cgi-bin/nph-dpc2s?dir=~kohl/press/06/08&sort=-date&cols=0,70,30',
      'http://www.senate.gov/cgi-bin/nph-dpc2s?dir=~kohl/press/06/09&sort=-date&cols=0,70,30',
      'http://www.senate.gov/cgi-bin/nph-dpc2s?dir=~kohl/press/06/10&sort=-date&cols=0,70,30',
      'http://www.senate.gov/cgi-bin/nph-dpc2s?dir=~kohl/press/06/11&sort=-date&cols=0,70,30',
      'http://www.senate.gov/cgi-bin/nph-dpc2s?dir=~kohl/press/06/12&sort=-date&cols=0,70,30',
      'http://www.senate.gov/cgi-bin/nph-dpc2s?dir=~kohl/press/05/01&sort=-date&cols=0,70,30',
      'http://www.senate.gov/cgi-bin/nph-dpc2s?dir=~kohl/press/05/02&sort=-date&cols=0,70,30',
      'http://www.senate.gov/cgi-bin/nph-dpc2s?dir=~kohl/press/05/03&sort=-date&cols=0,70,30',
      'http://www.senate.gov/cgi-bin/nph-dpc2s?dir=~kohl/press/05/04&sort=-date&cols=0,70,30',
      'http://www.senate.gov/cgi-bin/nph-dpc2s?dir=~kohl/press/05/05&sort=-date&cols=0,70,30',
      'http://www.senate.gov/cgi-bin/nph-dpc2s?dir=~kohl/press/05/06&sort=-date&cols=0,70,30',
      'http://www.senate.gov/cgi-bin/nph-dpc2s?dir=~kohl/press/05/07&sort=-date&cols=0,70,30',
      'http://www.senate.gov/cgi-bin/nph-dpc2s?dir=~kohl/press/05/08&sort=-date&cols=0,70,30',
      'http://www.senate.gov/cgi-bin/nph-dpc2s?dir=~kohl/press/05/09&sort=-date&cols=0,70,30',
      'http://www.senate.gov/cgi-bin/nph-dpc2s?dir=~kohl/press/05/10&sort=-date&cols=0,70,30',
      'http://www.senate.gov/cgi-bin/nph-dpc2s?dir=~kohl/press/05/11&sort=-date&cols=0,70,30',
      'http://www.senate.gov/cgi-bin/nph-dpc2s?dir=~kohl/press/05/12&sort=-date&cols=0,70,30']
##      'http://www.senate.gov/cgi-bin/nph-dpc2s?dir=~kohl/press/04/01&sort=-date&cols=0,70,30',
##      'http://www.senate.gov/cgi-bin/nph-dpc2s?dir=~kohl/press/04/02&sort=-date&cols=0,70,30',
##      'http://www.senate.gov/cgi-bin/nph-dpc2s?dir=~kohl/press/04/03&sort=-date&cols=0,70,30',
##      'http://www.senate.gov/cgi-bin/nph-dpc2s?dir=~kohl/press/04/04&sort=-date&cols=0,70,30',
##      'http://www.senate.gov/cgi-bin/nph-dpc2s?dir=~kohl/press/04/05&sort=-date&cols=0,70,30',
##      'http://www.senate.gov/cgi-bin/nph-dpc2s?dir=~kohl/press/04/06&sort=-date&cols=0,70,30',
##      'http://www.senate.gov/cgi-bin/nph-dpc2s?dir=~kohl/press/04/07&sort=-date&cols=0,70,30',
##      'http://www.senate.gov/cgi-bin/nph-dpc2s?dir=~kohl/press/04/08&sort=-date&cols=0,70,30',
##      'http://www.senate.gov/cgi-bin/nph-dpc2s?dir=~kohl/press/04/09&sort=-date&cols=0,70,30',
##      'http://www.senate.gov/cgi-bin/nph-dpc2s?dir=~kohl/press/04/10&sort=-date&cols=0,70,30',
##      'http://www.senate.gov/cgi-bin/nph-dpc2s?dir=~kohl/press/04/11&sort=-date&cols=0,70,30',
##      'http://www.senate.gov/cgi-bin/nph-dpc2s?dir=~kohl/press/04/12&sort=-date&cols=0,70,30',
##      'http://www.senate.gov/cgi-bin/nph-dpc2s?dir=~kohl/press/03/01&sort=-date&cols=0,70,30',
##      'http://www.senate.gov/cgi-bin/nph-dpc2s?dir=~kohl/press/03/02&sort=-date&cols=0,70,30',
##      'http://www.senate.gov/cgi-bin/nph-dpc2s?dir=~kohl/press/03/03&sort=-date&cols=0,70,30',
##      'http://www.senate.gov/cgi-bin/nph-dpc2s?dir=~kohl/press/03/04&sort=-date&cols=0,70,30',
##      'http://www.senate.gov/cgi-bin/nph-dpc2s?dir=~kohl/press/03/05&sort=-date&cols=0,70,30',
##      'http://www.senate.gov/cgi-bin/nph-dpc2s?dir=~kohl/press/03/06&sort=-date&cols=0,70,30',
##      'http://www.senate.gov/cgi-bin/nph-dpc2s?dir=~kohl/press/03/07&sort=-date&cols=0,70,30',
##      'http://www.senate.gov/cgi-bin/nph-dpc2s?dir=~kohl/press/03/08&sort=-date&cols=0,70,30',
##      'http://www.senate.gov/cgi-bin/nph-dpc2s?dir=~kohl/press/03/09&sort=-date&cols=0,70,30',
##      'http://www.senate.gov/cgi-bin/nph-dpc2s?dir=~kohl/press/03/10&sort=-date&cols=0,70,30',
##      'http://www.senate.gov/cgi-bin/nph-dpc2s?dir=~kohl/press/03/11&sort=-date&cols=0,70,30',
##      'http://www.senate.gov/cgi-bin/nph-dpc2s?dir=~kohl/press/03/12&sort=-date&cols=0,70,30',
##      'http://www.senate.gov/cgi-bin/nph-dpc2s?dir=~kohl/press/02/01&sort=-date&cols=0,70,30',
##      'http://www.senate.gov/cgi-bin/nph-dpc2s?dir=~kohl/press/02/02&sort=-date&cols=0,70,30',
##      'http://www.senate.gov/cgi-bin/nph-dpc2s?dir=~kohl/press/02/03&sort=-date&cols=0,70,30',
##      'http://www.senate.gov/cgi-bin/nph-dpc2s?dir=~kohl/press/02/04&sort=-date&cols=0,70,30',
##      'http://www.senate.gov/cgi-bin/nph-dpc2s?dir=~kohl/press/02/05&sort=-date&cols=0,70,30',
##      'http://www.senate.gov/cgi-bin/nph-dpc2s?dir=~kohl/press/02/06&sort=-date&cols=0,70,30',
##      'http://www.senate.gov/cgi-bin/nph-dpc2s?dir=~kohl/press/02/07&sort=-date&cols=0,70,30',
##      'http://www.senate.gov/cgi-bin/nph-dpc2s?dir=~kohl/press/02/08&sort=-date&cols=0,70,30',
##      'http://www.senate.gov/cgi-bin/nph-dpc2s?dir=~kohl/press/02/09&sort=-date&cols=0,70,30',
##      'http://www.senate.gov/cgi-bin/nph-dpc2s?dir=~kohl/press/02/10&sort=-date&cols=0,70,30',
##      'http://www.senate.gov/cgi-bin/nph-dpc2s?dir=~kohl/press/02/11&sort=-date&cols=0,70,30',
##      'http://www.senate.gov/cgi-bin/nph-dpc2s?dir=~kohl/press/02/12&sort=-date&cols=0,70,30']


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


for j in range(35, len(html)):
        out = urlopen(html[j]).read()
        soup = BeautifulSoup(out)
        res  = soup.findAll('a')
        fr= []
        for k in range(len(res)):
            if res[k].has_key('href'):
                ab = res[k]['href']
                ab = ab.strip('..')
                ba = re.findall('/\d\d/\d\d/', str(ab))
                if len(ba)>0 :
                    fr.append(ab.encode('UTF-8'))

        
        store = ''
        for num in range(len(fr)):
            store += 'http://kohl.senate.gov/' + fr[num] + '\n'
        fr = store.split('\n')
        fr.remove('')


        
        for num in range(0,len(fr)):
                test = urlopen(fr[num]).read()
                soup2 = BeautifulSoup(test)
                abd= soup2.findAll('a')
                for k in range(len(abd)):
                    abd[k].extract()
                hope = re.findall('\<dpc\sdate\=[A-Z][a-z]+\s\d+\,\s\d\d\d\d', test)
                if len(hope)==0:
                        hope = re.findall('\<dpc\sdate\=\s[A-Z]+\s\d\d\,\s\d\d\d\d', test)
                        if len(hope)==0:
                                hope =re.findall('\<dpc\sdate\=\d\d\-\d\d\-\d\d\d\d', test)
                if len(hope)>0:
                        mint = hope[0].split('=')[-1]
                        mint = mint.split(' ')
                        mons = mon_key[mint[0]]
                        day = re.sub('\W', '', mint[1])
                        year = mint[-1]
                        stores = utilities.clean_html(str(soup2))
                        stores = re.sub('\W', ' ', stores)
                        names = day + mons + year + 'Kohl'  + str(num) + '.txt'
                        files = open(names, 'w')
                        files.write(stores)
                        files.close()                
