import re, os
from nltk import utilities
from BeautifulSoup import BeautifulSoup
from urllib import urlopen



os.chdir('C:\CongressPressExpand\Smith')


html=['http://gsmith.senate.gov/public/index.cfm?FuseAction=PressReleases.List&Month=1&Year=2006',
      'http://gsmith.senate.gov/public/index.cfm?FuseAction=PressReleases.List&Month=2&Year=2006',
      'http://gsmith.senate.gov/public/index.cfm?FuseAction=PressReleases.List&Month=3&Year=2006',
      'http://gsmith.senate.gov/public/index.cfm?FuseAction=PressReleases.List&Month=4&Year=2006',
      'http://gsmith.senate.gov/public/index.cfm?FuseAction=PressReleases.List&Month=5&Year=2006',
      'http://gsmith.senate.gov/public/index.cfm?FuseAction=PressReleases.List&Month=6&Year=2006',
      'http://gsmith.senate.gov/public/index.cfm?FuseAction=PressReleases.List&Month=7&Year=2006',
      'http://gsmith.senate.gov/public/index.cfm?FuseAction=PressReleases.List&Month=8&Year=2006',
      'http://gsmith.senate.gov/public/index.cfm?FuseAction=PressReleases.List&Month=9&Year=2006',
      'http://gsmith.senate.gov/public/index.cfm?FuseAction=PressReleases.List&Month=10&Year=2006',
      'http://gsmith.senate.gov/public/index.cfm?FuseAction=PressReleases.List&Month=11&Year=2006',
      'http://gsmith.senate.gov/public/index.cfm?FuseAction=PressReleases.List&Month=12&Year=2006',
      'http://gsmith.senate.gov/public/index.cfm?FuseAction=PressReleases.List&Month=1&Year=2005',
      'http://gsmith.senate.gov/public/index.cfm?FuseAction=PressReleases.List&Month=2&Year=2005',
      'http://gsmith.senate.gov/public/index.cfm?FuseAction=PressReleases.List&Month=3&Year=2005',
      'http://gsmith.senate.gov/public/index.cfm?FuseAction=PressReleases.List&Month=4&Year=2005',
      'http://gsmith.senate.gov/public/index.cfm?FuseAction=PressReleases.List&Month=5&Year=2005',
      'http://gsmith.senate.gov/public/index.cfm?FuseAction=PressReleases.List&Month=6&Year=2005',
      'http://gsmith.senate.gov/public/index.cfm?FuseAction=PressReleases.List&Month=7&Year=2005',
      'http://gsmith.senate.gov/public/index.cfm?FuseAction=PressReleases.List&Month=8&Year=2005',
      'http://gsmith.senate.gov/public/index.cfm?FuseAction=PressReleases.List&Month=9&Year=2005',
      'http://gsmith.senate.gov/public/index.cfm?FuseAction=PressReleases.List&Month=10&Year=2005',
      'http://gsmith.senate.gov/public/index.cfm?FuseAction=PressReleases.List&Month=11&Year=2005',
      'http://gsmith.senate.gov/public/index.cfm?FuseAction=PressReleases.List&Month=12&Year=2005',
##      'http://gsmith.senate.gov/public/index.cfm?FuseAction=PressReleases.List&Month=1&Year=2004',
##      'http://gsmith.senate.gov/public/index.cfm?FuseAction=PressReleases.List&Month=2&Year=2004',
##      'http://gsmith.senate.gov/public/index.cfm?FuseAction=PressReleases.List&Month=3&Year=2004',
##      'http://gsmith.senate.gov/public/index.cfm?FuseAction=PressReleases.List&Month=4&Year=2004',
##      'http://gsmith.senate.gov/public/index.cfm?FuseAction=PressReleases.List&Month=5&Year=2004',
##      'http://gsmith.senate.gov/public/index.cfm?FuseAction=PressReleases.List&Month=6&Year=2004',
##      'http://gsmith.senate.gov/public/index.cfm?FuseAction=PressReleases.List&Month=7&Year=2004',
##      'http://gsmith.senate.gov/public/index.cfm?FuseAction=PressReleases.List&Month=8&Year=2004',
##      'http://gsmith.senate.gov/public/index.cfm?FuseAction=PressReleases.List&Month=9&Year=2004',
##      'http://gsmith.senate.gov/public/index.cfm?FuseAction=PressReleases.List&Month=10&Year=2004',
##      'http://gsmith.senate.gov/public/index.cfm?FuseAction=PressReleases.List&Month=11&Year=2004',
##      'http://gsmith.senate.gov/public/index.cfm?FuseAction=PressReleases.List&Month=12&Year=2004',
      'http://gsmith.senate.gov/public/index.cfm?FuseAction=PressReleases.List&Month=1&Year=2007',
      'http://gsmith.senate.gov/public/index.cfm?FuseAction=PressReleases.List&Month=2&Year=2007',
      'http://gsmith.senate.gov/public/index.cfm?FuseAction=PressReleases.List&Month=3&Year=2007',
      'http://gsmith.senate.gov/public/index.cfm?FuseAction=PressReleases.List&Month=4&Year=2007',
      'http://gsmith.senate.gov/public/index.cfm?FuseAction=PressReleases.List&Month=5&Year=2007',
      'http://gsmith.senate.gov/public/index.cfm?FuseAction=PressReleases.List&Month=6&Year=2007',
      'http://gsmith.senate.gov/public/index.cfm?FuseAction=PressReleases.List&Month=7&Year=2007',
      'http://gsmith.senate.gov/public/index.cfm?FuseAction=PressReleases.List&Month=8&Year=2007',
      'http://gsmith.senate.gov/public/index.cfm?FuseAction=PressReleases.List&Month=9&Year=2007',
      'http://gsmith.senate.gov/public/index.cfm?FuseAction=PressReleases.List&Month=10&Year=2007',
      'http://gsmith.senate.gov/public/index.cfm?FuseAction=PressReleases.List&Month=11&Year=2007',
      'http://gsmith.senate.gov/public/index.cfm?FuseAction=PressReleases.List&Month=12&Year=2007']

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
            store += 'http://gsmith.senate.gov/public/' + fr[num] + '\n'
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
                            if tds[k]['width']=='1%':
                                    tds[k].extract()
                            if tds[k].has_key('class'):
                                    if tds[k]['width']=='90%' and tds[k]['class']=='Title':
                                            tds[k].extract()
                stores = utilities.clean_html(str(soup2))
                stores = re.sub('\W', ' ', stores)
                stow= soup2.findAll('strong')
                for m in range(len(stow)):
                    if stow[m].has_key('class'):
                        if stow[m]['class']=='recorddate':
                            mint = utilities.clean_html(str(stow[m]))
                mint = mint.split(' ')
                mons = mon_key[mint[0]]
                days = re.sub('\W', '', mint[1])
                days = re.sub('[a-z]+', '', days)
                years = mint[-1]
                names = days +  mons + years + 'Smith'  + str(num) + '.txt'
                files = open(names, 'w')
                files.write(stores)
                files.close()
        
