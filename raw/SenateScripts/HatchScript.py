import re, os
from nltk import utilities
from BeautifulSoup import BeautifulSoup
from urllib import urlopen


os.chdir('C:\CongressPressExpand\Hatch')


html = ['http://hatch.senate.gov/index.cfm?FuseAction=PressReleases.List&Month=0&Year=2007&CFId=18936588&CFToken=22967084',
        'http://hatch.senate.gov/index.cfm?FuseAction=PressReleases.List&Month=0&Year=2006&CFId=18936588&CFToken=22967084',
        'http://hatch.senate.gov/index.cfm?FuseAction=PressReleases.List&Month=0&Year=2005&CFId=18936588&CFToken=22967084']
##        'http://hatch.senate.gov/index.cfm?FuseAction=PressReleases.List&Month=0&Year=2004&CFId=18936588&CFToken=22967084',
##        'http://hatch.senate.gov/index.cfm?FuseAction=PressReleases.List&Month=0&Year=2003&CFId=18936588&CFToken=22967084',
##        'http://hatch.senate.gov/index.cfm?FuseAction=PressReleases.List&Month=0&Year=2002&CFId=18936588&CFToken=22967084',
##        'http://hatch.senate.gov/index.cfm?FuseAction=PressReleases.List&Month=0&Year=2001&CFId=18936588&CFToken=22967084',
##        'http://hatch.senate.gov/index.cfm?FuseAction=PressReleases.List&Month=0&Year=2000&CFId=18936588&CFToken=22967084',
##        'http://hatch.senate.gov/index.cfm?FuseAction=PressReleases.List&Month=0&Year=1999&CFId=18936588&CFToken=22967084',
##        'http://hatch.senate.gov/index.cfm?FuseAction=PressReleases.List&Month=0&Year=1998&CFId=18936588&CFToken=22967084',
##        'http://hatch.senate.gov/index.cfm?FuseAction=PressReleases.List&Month=0&Year=1997&CFId=18936588&CFToken=22967084',
##        'http://hatch.senate.gov/index.cfm?FuseAction=PressReleases.List&Month=0&Year=1996&CFId=18936588&CFToken=22967084']



for j in range(0,1):#len(html)):
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
        store += 'http://hatch.senate.gov/' + fr[num] + '\n'
    fr = store.split('\n')
    fr.remove('')

    for num in range(0,1):#len(fr)):
            test = urlopen(fr[num]).read()
            soup2 = BeautifulSoup(test)
            ps = soup2.findAll('td')
            for k in range(len(ps)):
                if ps[k].has_key('class') and ps[k].has_key('nowrap'):
                    if ps[k]['class']=='vblack10':
                        emmit = re.findall('\s\d\d\d\d', str(ps[k]))
                        if len(emmit)==1:
                            out = utilities.clean_html(str(ps[k]))
                            pass
            date = re.sub('\W', '', out)
            stores=''
            abd = soup2.findAll('a')
            for k in range(len(abd)):
                abd[k].extract()
            opt = soup2.findAll('option')
            for k in range(len(opt)):
                opt[k].extract()
            strongs = soup2.findAll('strong')
            for k in range(len(strongs)):
                strongs[k].extract()
            tds = soup2.findAll('td')
            for j in range(len(tds)):
                if tds[j].has_key('width'):
                    if tds[j]['width']=='1%':
                        tds[j].extract()
            stores = utilities.clean_html(str(soup2))
            stores = re.sub('\W', ' ', stores)
            names = 'Hatch' + str(num) + date + '.txt'
            files = open(names, 'w')
            files.write(stores)
            files.close()
    
