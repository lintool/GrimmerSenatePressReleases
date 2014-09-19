##include stuff here
import os, re
from BeautifulSoup import BeautifulSoup
from urllib import urlopen
from nltk import utilities


os.chdir('C:\CongressPressExpand\Burr')

html=['http://burr.senate.gov/public/index.cfm?FuseAction=PressReleases.List&Month=12&Year=2007',
     'http://burr.senate.gov/public/index.cfm?FuseAction=PressReleases.List&Month=11&Year=2007',
     'http://burr.senate.gov/public/index.cfm?FuseAction=PressReleases.List&Month=10&Year=2007',
     'http://burr.senate.gov/public/index.cfm?FuseAction=PressReleases.List&Month=09&Year=2007',
     'http://burr.senate.gov/public/index.cfm?FuseAction=PressReleases.List&Month=08&Year=2007',
     'http://burr.senate.gov/public/index.cfm?FuseAction=PressReleases.List&Month=07&Year=2007',
     'http://burr.senate.gov/public/index.cfm?FuseAction=PressReleases.List&Month=06&Year=2007',
     'http://burr.senate.gov/public/index.cfm?FuseAction=PressReleases.List&Month=05&Year=2007',
     'http://burr.senate.gov/public/index.cfm?FuseAction=PressReleases.List&Month=04&Year=2007',
     'http://burr.senate.gov/public/index.cfm?FuseAction=PressReleases.List&Month=03&Year=2007',
     'http://burr.senate.gov/public/index.cfm?FuseAction=PressReleases.List&Month=02&Year=2007',
     'http://burr.senate.gov/public/index.cfm?FuseAction=PressReleases.List&Month=01&Year=2007',
     'http://burr.senate.gov/public/index.cfm?FuseAction=PressReleases.List&Month=12&Year=2006',
     'http://burr.senate.gov/public/index.cfm?FuseAction=PressReleases.List&Month=11&Year=2006',
     'http://burr.senate.gov/public/index.cfm?FuseAction=PressReleases.List&Month=10&Year=2006',
     'http://burr.senate.gov/public/index.cfm?FuseAction=PressReleases.List&Month=09&Year=2006',
     'http://burr.senate.gov/public/index.cfm?FuseAction=PressReleases.List&Month=08&Year=2006',
     'http://burr.senate.gov/public/index.cfm?FuseAction=PressReleases.List&Month=07&Year=2006',
     'http://burr.senate.gov/public/index.cfm?FuseAction=PressReleases.List&Month=06&Year=2006',
     'http://burr.senate.gov/public/index.cfm?FuseAction=PressReleases.List&Month=05&Year=2006',
     'http://burr.senate.gov/public/index.cfm?FuseAction=PressReleases.List&Month=04&Year=2006',
     'http://burr.senate.gov/public/index.cfm?FuseAction=PressReleases.List&Month=03&Year=2006',
     'http://burr.senate.gov/public/index.cfm?FuseAction=PressReleases.List&Month=02&Year=2006',
     'http://burr.senate.gov/public/index.cfm?FuseAction=PressReleases.List&Month=01&Year=2006',
     'http://burr.senate.gov/public/index.cfm?FuseAction=PressReleases.List&Month=12&Year=2005',
     'http://burr.senate.gov/public/index.cfm?FuseAction=PressReleases.List&Month=11&Year=2005',
     'http://burr.senate.gov/public/index.cfm?FuseAction=PressReleases.List&Month=10&Year=2005',
     'http://burr.senate.gov/public/index.cfm?FuseAction=PressReleases.List&Month=09&Year=2005',
     'http://burr.senate.gov/public/index.cfm?FuseAction=PressReleases.List&Month=08&Year=2005',
     'http://burr.senate.gov/public/index.cfm?FuseAction=PressReleases.List&Month=07&Year=2005',
     'http://burr.senate.gov/public/index.cfm?FuseAction=PressReleases.List&Month=06&Year=2005',
     'http://burr.senate.gov/public/index.cfm?FuseAction=PressReleases.List&Month=05&Year=2005',
     'http://burr.senate.gov/public/index.cfm?FuseAction=PressReleases.List&Month=04&Year=2005',
     'http://burr.senate.gov/public/index.cfm?FuseAction=PressReleases.List&Month=03&Year=2005',
     'http://burr.senate.gov/public/index.cfm?FuseAction=PressReleases.List&Month=02&Year=2005',
     'http://burr.senate.gov/public/index.cfm?FuseAction=PressReleases.List&Month=01&Year=2005',]



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
        store += 'http://burr.senate.gov/' + fr[num] + '\n'
    fr = store.split('\n')
    fr.remove('')

    for num in range(2, len(fr)):
        test = urlopen(fr[num]).read()
        soup2 = BeautifulSoup(test)
        tempd = soup2.findAll('strong')
        for k in range(len(tempd)):
            if tempd[k].has_key('class'):
                if tempd[k]['class']=='recorddate':
                    date = utilities.clean_html(str(tempd[k]))
        date = date.split(' ')
        mons = mon_key[date[0]]
        day = re.sub('\W', '', date[1])
        year = date[-1]
        tds = soup2.findAll('td')
        its =[]
        for m in range(len(tds)):
            if tds[m].has_key('class'):
                its.append(m)
        for k in its:
            if tds[(k-1)].has_key('align') and tds[k]['class']=='vblack11':
                if tds[(k-1)]['align']=='center' and tds[(k-1)]['class']=='Text':
                    stores = utilities.clean_html(str(tds[k]))
        names = day + mons + year  +  'Burr'  +  str(num) + '.txt'
        files = open(names, 'w')
        files.write(stores)
        files.close()
                
            
        
    
        


    
