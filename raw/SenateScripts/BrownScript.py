import re,os
from nltk import utilities
from BeautifulSoup import BeautifulSoup
from urllib import urlopen



os.chdir('C:\CongressPressExpand\Brown')


html=['http://brown.senate.gov/newsroom/press_releases/index.cfm?PageNum_rs=13',
      'http://brown.senate.gov/newsroom/press_releases/index.cfm?PageNum_rs=14',
      'http://brown.senate.gov/newsroom/press_releases/index.cfm?PageNum_rs=15',
      'http://brown.senate.gov/newsroom/press_releases/index.cfm?PageNum_rs=16',
      'http://brown.senate.gov/newsroom/press_releases/index.cfm?PageNum_rs=17',
      'http://brown.senate.gov/newsroom/press_releases/index.cfm?PageNum_rs=18',
      'http://brown.senate.gov/newsroom/press_releases/index.cfm?PageNum_rs=19',
      'http://brown.senate.gov/newsroom/press_releases/index.cfm?PageNum_rs=20',
      'http://brown.senate.gov/newsroom/press_releases/index.cfm?PageNum_rs=21',
      'http://brown.senate.gov/newsroom/press_releases/index.cfm?PageNum_rs=22',
      'http://brown.senate.gov/newsroom/press_releases/index.cfm?PageNum_rs=23',
      'http://brown.senate.gov/newsroom/press_releases/index.cfm?PageNum_rs=24',
      'http://brown.senate.gov/newsroom/press_releases/index.cfm?PageNum_rs=25']
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


for j in range(0, len(html)):
        out = urlopen(html[j]).read()
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
        ps = soup.findAll('td')
        for m in range(len(ps)):
            if ps[m].has_key('class'):
                if ps[m]['class']=='date':
                        #sting = ps[m]
                        #string = string.replace('\', '_')
                        abc = utilities.clean_html(str(ps[m]))
                        temp = abc.split('/')
                        clean = re.sub('\W', '', temp[0])
                        mons =  month[clean]
                        clean_year = re.sub('\W', '', temp[-1]) 
                        day = temp[1]
                        year = '20' + clean_year
                        date.append(day + mons + year)
        store = ''
        for num in range(len(fr)):
            store += fr[num] + '\n'
        fr = store.split('\n')
        fr.remove('')

        for num in range(0,len(fr)):
                    test = urlopen(fr[num]).read()
                    soup2 = BeautifulSoup(test)
                    abd= soup2.findAll('a')
                    for k in range(len(abd)):
                        abd[k].extract()
                    abc = soup2.findAll('h3')
                    for k in range(len(abc)):
                        abc[k].extract()
                    abm = soup2.findAll('td')
                    for k in range(len(abm)):
                        if abm[k].has_key('class') and abm[k].has_key('valign'):
                                if abm[k]['class']=='date':
                                        abm[k].extract()
                    stores = utilities.clean_html(str(soup2))
                    stores = re.sub('\W', ' ', stores)
                    mint= date[num]
                    names = mint + 'Brown'  +  str(num) + '.txt'
                    files = open(names, 'w')
                    files.write(stores)
                    files.close()
        
