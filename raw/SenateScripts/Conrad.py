from nltk import utilities
from BeautifulSoup import BeautifulSoup
from urllib import urlopen
import re, os




os.chdir('C:\CongressPressExpand\Conrad')


html= ['http://conrad.senate.gov/pressroom/01_06_releases.cfm',
       'http://conrad.senate.gov/pressroom/02_06_releases.cfm',
       'http://conrad.senate.gov/pressroom/03_06_releases.cfm',
       'http://conrad.senate.gov/pressroom/04_06_releases.cfm',
       'http://conrad.senate.gov/pressroom/05_06_releases.cfm',
       'http://conrad.senate.gov/pressroom/06_06_releases.cfm',
       'http://conrad.senate.gov/pressroom/07_06_releases.cfm',
       'http://conrad.senate.gov/pressroom/08_06_releases.cfm',
       'http://conrad.senate.gov/pressroom/09_06_releases.cfm',
       'http://conrad.senate.gov/pressroom/10_06_releases.cfm',
       'http://conrad.senate.gov/pressroom/11_06_releases.cfm',
       'http://conrad.senate.gov/pressroom/12_06_releases.cfm',
       'http://conrad.senate.gov/pressroom/01_07_releases.cfm',
       'http://conrad.senate.gov/pressroom/02_07_releases.cfm',
       'http://conrad.senate.gov/pressroom/03_07_releases.cfm',
       'http://conrad.senate.gov/pressroom/04_07_releases.cfm',
       'http://conrad.senate.gov/pressroom/05_07_releases.cfm',
       'http://conrad.senate.gov/pressroom/06_07_releases.cfm',
       'http://conrad.senate.gov/pressroom/07_07_releases.cfm',
       'http://conrad.senate.gov/pressroom/08_07_releases.cfm',
       'http://conrad.senate.gov/pressroom/09_07_releases.cfm',
       'http://conrad.senate.gov/pressroom/10_07_releases.cfm',
       'http://conrad.senate.gov/pressroom/11_07_releases.cfm',
       'http://conrad.senate.gov/pressroom/12_07_releases.cfm',
       'http://conrad.senate.gov/pressroom/01_05_releases.cfm',
       'http://conrad.senate.gov/pressroom/02_05_releases.cfm',
       'http://conrad.senate.gov/pressroom/03_05_releases.cfm',
       'http://conrad.senate.gov/pressroom/04_05_releases.cfm',
       'http://conrad.senate.gov/pressroom/05_05_releases.cfm',
       'http://conrad.senate.gov/pressroom/06_05_releases.cfm',
       'http://conrad.senate.gov/pressroom/07_05_releases.cfm',
       'http://conrad.senate.gov/pressroom/08_05_releases.cfm',
       'http://conrad.senate.gov/pressroom/09_05_releases.cfm',
       'http://conrad.senate.gov/pressroom/10_05_releases.cfm',
       'http://conrad.senate.gov/pressroom/11_05_releases.cfm',
       'http://conrad.senate.gov/pressroom/12_05_releases.cfm']
##       'http://conrad.senate.gov/pressroom/01_04_releases.cfm',
##       'http://conrad.senate.gov/pressroom/02_04_releases.cfm',
##       'http://conrad.senate.gov/pressroom/03_04_releases.cfm',
##       'http://conrad.senate.gov/pressroom/04_04_releases.cfm',
##       'http://conrad.senate.gov/pressroom/05_04_releases.cfm',
##       'http://conrad.senate.gov/pressroom/06_04_releases.cfm',
##       'http://conrad.senate.gov/pressroom/07_04_releases.cfm',
##       'http://conrad.senate.gov/pressroom/08_04_releases.cfm',
##       'http://conrad.senate.gov/pressroom/09_04_releases.cfm',
##       'http://conrad.senate.gov/pressroom/10_04_releases.cfm',
##       'http://conrad.senate.gov/pressroom/11_04_releases.cfm',
##       'http://conrad.senate.gov/pressroom/12_04_releases.cfm',
##       'http://conrad.senate.gov/pressroom/01_03_releases.cfm',
##       'http://conrad.senate.gov/pressroom/02_03_releases.cfm',
##       'http://conrad.senate.gov/pressroom/03_03_releases.cfm',
##       'http://conrad.senate.gov/pressroom/04_03_releases.cfm',
##       'http://conrad.senate.gov/pressroom/05_03_releases.cfm',
##       'http://conrad.senate.gov/pressroom/06_03_releases.cfm',
##       'http://conrad.senate.gov/pressroom/07_03_releases.cfm',
##       'http://conrad.senate.gov/pressroom/08_03_releases.cfm',
##       'http://conrad.senate.gov/pressroom/09_03_releases.cfm',
##       'http://conrad.senate.gov/pressroom/10_03_releases.cfm',
##       'http://conrad.senate.gov/pressroom/11_03_releases.cfm',
##       'http://conrad.senate.gov/pressroom/12_03_releases.cfm']


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
        store += 'http://conrad.senate.gov/pressroom/' + fr[num] + '\n'
    fr = store.split('\n')
    fr.remove('')

    for num in range(len(fr)):
            test = urlopen(fr[num]).read()
            soup2 = BeautifulSoup(test)
            ps = soup2.findAll('p')
            date = ps[2]
            date = utilities.clean_html(str(date))
            date = date.split(' ')
            mons = mon_key[date[0]]
            day = re.sub('\W', '', date[1])
            year = date[-1]
            stores=''
            h2s = soup2.findAll('h2')
            h3s = soup2.findAll('h3')
            stores += utilities.clean_html(str(h2s[1])).strip(' ').strip('\n') + ' '
            stores += utilities.clean_html(str(h3s[0])).strip(' ').strip('\n').strip('\r') + ' '
            for m in range(len(ps)):
                if ps[m].has_key('style')==False :
                    stores += utilities.clean_html(str(ps[m])) + ' '
            stores = re.sub('\W', ' ', stores)
            names = day + mons + year + 'Conrad'  + str(num) + '.txt'
            files = open(names, 'w')
            files.write(stores)
            files.close()
            
