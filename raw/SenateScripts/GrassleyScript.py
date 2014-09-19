import re,os
from nltk import utilities
from urllib import urlopen
from BeautifulSoup import BeautifulSoup

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


os.chdir('C:\CongressPressExpand\Grassley')

html=['http://grassley.senate.gov/public/index.cfm?FuseAction=PressReleases.List&Month=01&Year=2006',
      'http://grassley.senate.gov/public/index.cfm?FuseAction=PressReleases.List&Month=02&Year=2006',
      'http://grassley.senate.gov/public/index.cfm?FuseAction=PressReleases.List&Month=03&Year=2006',
      'http://grassley.senate.gov/public/index.cfm?FuseAction=PressReleases.List&Month=04&Year=2006',
      'http://grassley.senate.gov/public/index.cfm?FuseAction=PressReleases.List&Month=05&Year=2006',
      'http://grassley.senate.gov/public/index.cfm?FuseAction=PressReleases.List&Month=06&Year=2006',
      'http://grassley.senate.gov/public/index.cfm?FuseAction=PressReleases.List&Month=07&Year=2006',
      'http://grassley.senate.gov/public/index.cfm?FuseAction=PressReleases.List&Month=08&Year=2006',
      'http://grassley.senate.gov/public/index.cfm?FuseAction=PressReleases.List&Month=09&Year=2006',
      'http://grassley.senate.gov/public/index.cfm?FuseAction=PressReleases.List&Month=10&Year=2006',
      'http://grassley.senate.gov/public/index.cfm?FuseAction=PressReleases.List&Month=11&Year=2006',
      'http://grassley.senate.gov/public/index.cfm?FuseAction=PressReleases.List&Month=12&Year=2006',
      'http://grassley.senate.gov/public/index.cfm?FuseAction=PressReleases.List&Month=01&Year=2005',
      'http://grassley.senate.gov/public/index.cfm?FuseAction=PressReleases.List&Month=02&Year=2005',
      'http://grassley.senate.gov/public/index.cfm?FuseAction=PressReleases.List&Month=03&Year=2005',
      'http://grassley.senate.gov/public/index.cfm?FuseAction=PressReleases.List&Month=04&Year=2005',
      'http://grassley.senate.gov/public/index.cfm?FuseAction=PressReleases.List&Month=05&Year=2005',
      'http://grassley.senate.gov/public/index.cfm?FuseAction=PressReleases.List&Month=06&Year=2005',
      'http://grassley.senate.gov/public/index.cfm?FuseAction=PressReleases.List&Month=07&Year=2005',
      'http://grassley.senate.gov/public/index.cfm?FuseAction=PressReleases.List&Month=08&Year=2005',
      'http://grassley.senate.gov/public/index.cfm?FuseAction=PressReleases.List&Month=09&Year=2005',
      'http://grassley.senate.gov/public/index.cfm?FuseAction=PressReleases.List&Month=10&Year=2005',
      'http://grassley.senate.gov/public/index.cfm?FuseAction=PressReleases.List&Month=11&Year=2005',
      'http://grassley.senate.gov/public/index.cfm?FuseAction=PressReleases.List&Month=12&Year=2005'
##      'http://grassley.senate.gov/public/index.cfm?FuseAction=PressReleases.List&Month=01&Year=2004',
##      'http://grassley.senate.gov/public/index.cfm?FuseAction=PressReleases.List&Month=02&Year=2004',
##      'http://grassley.senate.gov/public/index.cfm?FuseAction=PressReleases.List&Month=03&Year=2004',
##      'http://grassley.senate.gov/public/index.cfm?FuseAction=PressReleases.List&Month=04&Year=2004',
##      'http://grassley.senate.gov/public/index.cfm?FuseAction=PressReleases.List&Month=05&Year=2004',
##      'http://grassley.senate.gov/public/index.cfm?FuseAction=PressReleases.List&Month=06&Year=2004',
##      'http://grassley.senate.gov/public/index.cfm?FuseAction=PressReleases.List&Month=07&Year=2004',
##      'http://grassley.senate.gov/public/index.cfm?FuseAction=PressReleases.List&Month=08&Year=2004',
##      'http://grassley.senate.gov/public/index.cfm?FuseAction=PressReleases.List&Month=09&Year=2004',
##      'http://grassley.senate.gov/public/index.cfm?FuseAction=PressReleases.List&Month=10&Year=2004',
##      'http://grassley.senate.gov/public/index.cfm?FuseAction=PressReleases.List&Month=11&Year=2004',
##      'http://grassley.senate.gov/public/index.cfm?FuseAction=PressReleases.List&Month=12&Year=2004',
##      'http://grassley.senate.gov/public/index.cfm?FuseAction=PressReleases.List&Month=01&Year=2003',
##      'http://grassley.senate.gov/public/index.cfm?FuseAction=PressReleases.List&Month=02&Year=2003',
##      'http://grassley.senate.gov/public/index.cfm?FuseAction=PressReleases.List&Month=03&Year=2003',
##      'http://grassley.senate.gov/public/index.cfm?FuseAction=PressReleases.List&Month=04&Year=2003',
##      'http://grassley.senate.gov/public/index.cfm?FuseAction=PressReleases.List&Month=05&Year=2003',
##      'http://grassley.senate.gov/public/index.cfm?FuseAction=PressReleases.List&Month=06&Year=2003',
##      'http://grassley.senate.gov/public/index.cfm?FuseAction=PressReleases.List&Month=07&Year=2003',
##      'http://grassley.senate.gov/public/index.cfm?FuseAction=PressReleases.List&Month=08&Year=2003',
##      'http://grassley.senate.gov/public/index.cfm?FuseAction=PressReleases.List&Month=09&Year=2003',
##      'http://grassley.senate.gov/public/index.cfm?FuseAction=PressReleases.List&Month=10&Year=2003',
##      'http://grassley.senate.gov/public/index.cfm?FuseAction=PressReleases.List&Month=11&Year=2003',
##      'http://grassley.senate.gov/public/index.cfm?FuseAction=PressReleases.List&Month=12&Year=2003',
##      'http://grassley.senate.gov/public/index.cfm?FuseAction=PressReleases.List&Month=01&Year=2002',
##      'http://grassley.senate.gov/public/index.cfm?FuseAction=PressReleases.List&Month=02&Year=2002',
##      'http://grassley.senate.gov/public/index.cfm?FuseAction=PressReleases.List&Month=03&Year=2002',
##      'http://grassley.senate.gov/public/index.cfm?FuseAction=PressReleases.List&Month=04&Year=2002',
##      'http://grassley.senate.gov/public/index.cfm?FuseAction=PressReleases.List&Month=05&Year=2002',
##      'http://grassley.senate.gov/public/index.cfm?FuseAction=PressReleases.List&Month=06&Year=2002',
##      'http://grassley.senate.gov/public/index.cfm?FuseAction=PressReleases.List&Month=07&Year=2002',
##      'http://grassley.senate.gov/public/index.cfm?FuseAction=PressReleases.List&Month=08&Year=2002',
##      'http://grassley.senate.gov/public/index.cfm?FuseAction=PressReleases.List&Month=09&Year=2002',
##      'http://grassley.senate.gov/public/index.cfm?FuseAction=PressReleases.List&Month=10&Year=2002',
##      'http://grassley.senate.gov/public/index.cfm?FuseAction=PressReleases.List&Month=11&Year=2002',
##      'http://grassley.senate.gov/public/index.cfm?FuseAction=PressReleases.List&Month=12&Year=2002',
##      'http://grassley.senate.gov/public/index.cfm?FuseAction=PressReleases.List&Month=01&Year=2001',
##      'http://grassley.senate.gov/public/index.cfm?FuseAction=PressReleases.List&Month=02&Year=2001',
##      'http://grassley.senate.gov/public/index.cfm?FuseAction=PressReleases.List&Month=03&Year=2001',
##      'http://grassley.senate.gov/public/index.cfm?FuseAction=PressReleases.List&Month=04&Year=2001',
##      'http://grassley.senate.gov/public/index.cfm?FuseAction=PressReleases.List&Month=05&Year=2001',
##      'http://grassley.senate.gov/public/index.cfm?FuseAction=PressReleases.List&Month=06&Year=2001',
##      'http://grassley.senate.gov/public/index.cfm?FuseAction=PressReleases.List&Month=07&Year=2001',
##      'http://grassley.senate.gov/public/index.cfm?FuseAction=PressReleases.List&Month=08&Year=2001',
##      'http://grassley.senate.gov/public/index.cfm?FuseAction=PressReleases.List&Month=09&Year=2001',
##      'http://grassley.senate.gov/public/index.cfm?FuseAction=PressReleases.List&Month=10&Year=2001',
##      'http://grassley.senate.gov/public/index.cfm?FuseAction=PressReleases.List&Month=11&Year=2001',
##      'http://grassley.senate.gov/public/index.cfm?FuseAction=PressReleases.List&Month=12&Year=2001',
##      'http://grassley.senate.gov/public/index.cfm?FuseAction=PressReleases.List&Month=01&Year=2000',
##      'http://grassley.senate.gov/public/index.cfm?FuseAction=PressReleases.List&Month=02&Year=2000',
##      'http://grassley.senate.gov/public/index.cfm?FuseAction=PressReleases.List&Month=03&Year=2000',
##      'http://grassley.senate.gov/public/index.cfm?FuseAction=PressReleases.List&Month=04&Year=2000',
##      'http://grassley.senate.gov/public/index.cfm?FuseAction=PressReleases.List&Month=05&Year=2000',
##      'http://grassley.senate.gov/public/index.cfm?FuseAction=PressReleases.List&Month=06&Year=2000',
##      'http://grassley.senate.gov/public/index.cfm?FuseAction=PressReleases.List&Month=07&Year=2000',
##      'http://grassley.senate.gov/public/index.cfm?FuseAction=PressReleases.List&Month=08&Year=2000',
##      'http://grassley.senate.gov/public/index.cfm?FuseAction=PressReleases.List&Month=09&Year=2000',
##      'http://grassley.senate.gov/public/index.cfm?FuseAction=PressReleases.List&Month=10&Year=2000',
##      'http://grassley.senate.gov/public/index.cfm?FuseAction=PressReleases.List&Month=11&Year=2000',
##      'http://grassley.senate.gov/public/index.cfm?FuseAction=PressReleases.List&Month=12&Year=2000',
##      'http://grassley.senate.gov/public/index.cfm?FuseAction=PressReleases.List&Month=01&Year=1999',
##      'http://grassley.senate.gov/public/index.cfm?FuseAction=PressReleases.List&Month=02&Year=1999',
##      'http://grassley.senate.gov/public/index.cfm?FuseAction=PressReleases.List&Month=03&Year=1999',
##      'http://grassley.senate.gov/public/index.cfm?FuseAction=PressReleases.List&Month=04&Year=1999',
##      'http://grassley.senate.gov/public/index.cfm?FuseAction=PressReleases.List&Month=05&Year=1999',
##      'http://grassley.senate.gov/public/index.cfm?FuseAction=PressReleases.List&Month=06&Year=1999',
##      'http://grassley.senate.gov/public/index.cfm?FuseAction=PressReleases.List&Month=07&Year=1999',
##      'http://grassley.senate.gov/public/index.cfm?FuseAction=PressReleases.List&Month=08&Year=1999',
##      'http://grassley.senate.gov/public/index.cfm?FuseAction=PressReleases.List&Month=09&Year=1999',
##      'http://grassley.senate.gov/public/index.cfm?FuseAction=PressReleases.List&Month=10&Year=1999',
##      'http://grassley.senate.gov/public/index.cfm?FuseAction=PressReleases.List&Month=11&Year=1999',
##      'http://grassley.senate.gov/public/index.cfm?FuseAction=PressReleases.List&Month=12&Year=1999',
##      'http://grassley.senate.gov/public/index.cfm?FuseAction=PressReleases.List&Month=01&Year=1998',
##      'http://grassley.senate.gov/public/index.cfm?FuseAction=PressReleases.List&Month=02&Year=1998',
##      'http://grassley.senate.gov/public/index.cfm?FuseAction=PressReleases.List&Month=03&Year=1998',
##      'http://grassley.senate.gov/public/index.cfm?FuseAction=PressReleases.List&Month=04&Year=1998',
##      'http://grassley.senate.gov/public/index.cfm?FuseAction=PressReleases.List&Month=05&Year=1998',
##      'http://grassley.senate.gov/public/index.cfm?FuseAction=PressReleases.List&Month=06&Year=1998',
##      'http://grassley.senate.gov/public/index.cfm?FuseAction=PressReleases.List&Month=07&Year=1998',
##      'http://grassley.senate.gov/public/index.cfm?FuseAction=PressReleases.List&Month=08&Year=1998',
##      'http://grassley.senate.gov/public/index.cfm?FuseAction=PressReleases.List&Month=09&Year=1998',
##      'http://grassley.senate.gov/public/index.cfm?FuseAction=PressReleases.List&Month=10&Year=1998',
##      'http://grassley.senate.gov/public/index.cfm?FuseAction=PressReleases.List&Month=11&Year=1998',
##      'http://grassley.senate.gov/public/index.cfm?FuseAction=PressReleases.List&Month=12&Year=1998',
      'http://grassley.senate.gov/public/index.cfm?FuseAction=PressReleases.List&Month=01&Year=2007',
      'http://grassley.senate.gov/public/index.cfm?FuseAction=PressReleases.List&Month=02&Year=2007',
      'http://grassley.senate.gov/public/index.cfm?FuseAction=PressReleases.List&Month=03&Year=2007',
      'http://grassley.senate.gov/public/index.cfm?FuseAction=PressReleases.List&Month=04&Year=2007',
      'http://grassley.senate.gov/public/index.cfm?FuseAction=PressReleases.List&Month=05&Year=2007',
      'http://grassley.senate.gov/public/index.cfm?FuseAction=PressReleases.List&Month=06&Year=2007',
      'http://grassley.senate.gov/public/index.cfm?FuseAction=PressReleases.List&Month=07&Year=2007',
      'http://grassley.senate.gov/public/index.cfm?FuseAction=PressReleases.List&Month=08&Year=2007',
      'http://grassley.senate.gov/public/index.cfm?FuseAction=PressReleases.List&Month=09&Year=2007',
      'http://grassley.senate.gov/public/index.cfm?FuseAction=PressReleases.List&Month=10&Year=2007',
      'http://grassley.senate.gov/public/index.cfm?FuseAction=PressReleases.List&Month=11&Year=2007',
      'http://grassley.senate.gov/public/index.cfm?FuseAction=PressReleases.List&Month=12&Year=2007']

for j in range(1,len(html)):
    out = urlopen(html[j]).read()
    soup = BeautifulSoup(out)
    res  = soup.findAll('a')
    fr= []
    for k in range(len(res)):
        if res[k].has_key('href'):
            ab = res[k]['href']
            ba = re.findall('_id', str(ab))
            if len(ba)>0 :
                fr.append(ab.encode('UTF-8'))


    store = ''
    for num in range(len(fr)):
        store += 'http://grassley.senate.gov/public/' + fr[num] + '\n'
    fr = store.split('\n')
    fr.remove('')
    
    for num in range(0,len(fr)):
            test = urlopen(fr[num]).read()
            soup2 = BeautifulSoup(test)
            ted = soup2.findAll('td')
            a = 0
            stores =''
            for k in range(len(ted)):
                if ted[k].has_key('class'):
                    if ted[k]['class']=='text':
                        att = re.findall('\d\d\d\d', str(ted[k]))
                        if len(att)>0:
                            date = utilities.clean_html(str(ted[k]))
            for k in range(len(ted)):
                if ted[k].has_key('class') and ted[k].has_key('style'):
                    if ted[k]['class']=='Text':
                        stores += utilities.clean_html(str(ted[k]))
                if ted[k].has_key('class'):
                    if ted[k]['class']=='recordtitle':
                        stores += utilities.clean_html(str(ted[k]))
            date = date.split(' ')
            mons = mon_key[date[0]]
            day = re.findall('[0-9]+', date[1])[0]
            year = date[-1]
            stores = re.sub('\W', ' ', stores)
            names = day + mons + year +  'Grassley' + str(num) + '.txt'
            files = open(names, 'w')
            files.write(stores)
            files.close()
        


    
      
