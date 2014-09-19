import re, os
from BeautifulSoup import BeautifulSoup
from nltk import utilities
from urllib import urlopen


os.chdir('C:\CongressPressExpand\Allard')


html=['http://allard.senate.gov/public/index.cfm?FuseAction=PressReleases.List&Month=1&Year=2007',
      'http://allard.senate.gov/public/index.cfm?FuseAction=PressReleases.List&Month=2&Year=2007',
      'http://allard.senate.gov/public/index.cfm?FuseAction=PressReleases.List&Month=3&Year=2007',
      'http://allard.senate.gov/public/index.cfm?FuseAction=PressReleases.List&Month=4&Year=2007',
      'http://allard.senate.gov/public/index.cfm?FuseAction=PressReleases.List&Month=5&Year=2007',
      'http://allard.senate.gov/public/index.cfm?FuseAction=PressReleases.List&Month=6&Year=2007',
      'http://allard.senate.gov/public/index.cfm?FuseAction=PressReleases.List&Month=7&Year=2007',
      'http://allard.senate.gov/public/index.cfm?FuseAction=PressReleases.List&Month=8&Year=2007',
      'http://allard.senate.gov/public/index.cfm?FuseAction=PressReleases.List&Month=9&Year=2007',
      'http://allard.senate.gov/public/index.cfm?FuseAction=PressReleases.List&Month=10&Year=2007',
      'http://allard.senate.gov/public/index.cfm?FuseAction=PressReleases.List&Month=11&Year=2007',
      'http://allard.senate.gov/public/index.cfm?FuseAction=PressReleases.List&Month=12&Year=2007',
      'http://allard.senate.gov/public/index.cfm?FuseAction=PressReleases.List&Month=1&Year=2006',
      'http://allard.senate.gov/public/index.cfm?FuseAction=PressReleases.List&Month=2&Year=2006',
      'http://allard.senate.gov/public/index.cfm?FuseAction=PressReleases.List&Month=3&Year=2006',
      'http://allard.senate.gov/public/index.cfm?FuseAction=PressReleases.List&Month=4&Year=2006',
      'http://allard.senate.gov/public/index.cfm?FuseAction=PressReleases.List&Month=5&Year=2006',
      'http://allard.senate.gov/public/index.cfm?FuseAction=PressReleases.List&Month=6&Year=2006',
      'http://allard.senate.gov/public/index.cfm?FuseAction=PressReleases.List&Month=7&Year=2006',
      'http://allard.senate.gov/public/index.cfm?FuseAction=PressReleases.List&Month=8&Year=2006',
      'http://allard.senate.gov/public/index.cfm?FuseAction=PressReleases.List&Month=9&Year=2006',
      'http://allard.senate.gov/public/index.cfm?FuseAction=PressReleases.List&Month=10&Year=2006',
      'http://allard.senate.gov/public/index.cfm?FuseAction=PressReleases.List&Month=11&Year=2006',
      'http://allard.senate.gov/public/index.cfm?FuseAction=PressReleases.List&Month=12&Year=2006',
      'http://allard.senate.gov/public/index.cfm?FuseAction=PressReleases.List&Month=1&Year=2005',
      'http://allard.senate.gov/public/index.cfm?FuseAction=PressReleases.List&Month=2&Year=2005',
      'http://allard.senate.gov/public/index.cfm?FuseAction=PressReleases.List&Month=3&Year=2005',
      'http://allard.senate.gov/public/index.cfm?FuseAction=PressReleases.List&Month=4&Year=2005',
      'http://allard.senate.gov/public/index.cfm?FuseAction=PressReleases.List&Month=5&Year=2005',
      'http://allard.senate.gov/public/index.cfm?FuseAction=PressReleases.List&Month=6&Year=2005',
      'http://allard.senate.gov/public/index.cfm?FuseAction=PressReleases.List&Month=7&Year=2005',
      'http://allard.senate.gov/public/index.cfm?FuseAction=PressReleases.List&Month=8&Year=2005',
      'http://allard.senate.gov/public/index.cfm?FuseAction=PressReleases.List&Month=9&Year=2005',
      'http://allard.senate.gov/public/index.cfm?FuseAction=PressReleases.List&Month=10&Year=2005',
      'http://allard.senate.gov/public/index.cfm?FuseAction=PressReleases.List&Month=11&Year=2005',
      'http://allard.senate.gov/public/index.cfm?FuseAction=PressReleases.List&Month=12&Year=2005']


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



for j in range(0, len(html)):
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
        for num in range(len(fr)):
            store += 'http://allard.senate.gov/public/' + fr[num] + '\n'
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
                                if tds[k]['width']=='1%' or tds[k]['width']=='99%':
                                        tds[k].extract()   
                stores = utilities.clean_html(str(soup2))
                stores = re.sub('\W', ' ', stores)
                test = soup2.findAll('strong')
                for m in range(len(test)):
                    if test[m].has_key('class'):
                        if test[m]['class']=='recorddate':
                            date = utilities.clean_html(str(test[m]))
                date = date.split(' ')
                mons = mon_key[date[0]]
                days = re.findall('[0-9]+', date[1])[0]
                year = date[2]
               # mint = re.sub('\W', '', date)
                names = days + mons + year + 'Allard' + str(num) + '.txt'
                files = open(names, 'w')
                files.write(stores)
                files.close()
                
    
