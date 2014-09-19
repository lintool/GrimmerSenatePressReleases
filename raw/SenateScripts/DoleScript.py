import re, os
from nltk import utilities
from urllib import urlopen
from BeautifulSoup import BeautifulSoup


os.chdir('C:\CongressPressExpand\Dole')


html = ['http://dole.senate.gov/public/index.cfm?FuseAction=PressReleases.List&Month=1&Year=2005',
        'http://dole.senate.gov/public/index.cfm?FuseAction=PressReleases.List&Month=2&Year=2005',
        'http://dole.senate.gov/public/index.cfm?FuseAction=PressReleases.List&Month=3&Year=2005',
        'http://dole.senate.gov/public/index.cfm?FuseAction=PressReleases.List&Month=4&Year=2005',
        'http://dole.senate.gov/public/index.cfm?FuseAction=PressReleases.List&Month=5&Year=2005',
        'http://dole.senate.gov/public/index.cfm?FuseAction=PressReleases.List&Month=6&Year=2005',
        'http://dole.senate.gov/public/index.cfm?FuseAction=PressReleases.List&Month=7&Year=2005',
        'http://dole.senate.gov/public/index.cfm?FuseAction=PressReleases.List&Month=8&Year=2005',
        'http://dole.senate.gov/public/index.cfm?FuseAction=PressReleases.List&Month=9&Year=2005',
        'http://dole.senate.gov/public/index.cfm?FuseAction=PressReleases.List&Month=10&Year=2005',
        'http://dole.senate.gov/public/index.cfm?FuseAction=PressReleases.List&Month=11&Year=2005',
        'http://dole.senate.gov/public/index.cfm?FuseAction=PressReleases.List&Month=12&Year=2005',
        'http://dole.senate.gov/public/index.cfm?FuseAction=PressReleases.List&Month=1&Year=2007',
        'http://dole.senate.gov/public/index.cfm?FuseAction=PressReleases.List&Month=2&Year=2007',
        'http://dole.senate.gov/public/index.cfm?FuseAction=PressReleases.List&Month=3&Year=2007',
        'http://dole.senate.gov/public/index.cfm?FuseAction=PressReleases.List&Month=4&Year=2007',
        'http://dole.senate.gov/public/index.cfm?FuseAction=PressReleases.List&Month=5&Year=2007',
        'http://dole.senate.gov/public/index.cfm?FuseAction=PressReleases.List&Month=6&Year=2007',
        'http://dole.senate.gov/public/index.cfm?FuseAction=PressReleases.List&Month=7&Year=2007',
        'http://dole.senate.gov/public/index.cfm?FuseAction=PressReleases.List&Month=8&Year=2007',
        'http://dole.senate.gov/public/index.cfm?FuseAction=PressReleases.List&Month=9&Year=2007',
        'http://dole.senate.gov/public/index.cfm?FuseAction=PressReleases.List&Month=10&Year=2007',
        'http://dole.senate.gov/public/index.cfm?FuseAction=PressReleases.List&Month=11&Year=2007',
        'http://dole.senate.gov/public/index.cfm?FuseAction=PressReleases.List&Month=12&Year=2007',
        'http://dole.senate.gov/public/index.cfm?FuseAction=PressReleases.List&Month=1&Year=2006',
        'http://dole.senate.gov/public/index.cfm?FuseAction=PressReleases.List&Month=2&Year=2006',
        'http://dole.senate.gov/public/index.cfm?FuseAction=PressReleases.List&Month=3&Year=2006',
        'http://dole.senate.gov/public/index.cfm?FuseAction=PressReleases.List&Month=4&Year=2006',
        'http://dole.senate.gov/public/index.cfm?FuseAction=PressReleases.List&Month=5&Year=2006',
        'http://dole.senate.gov/public/index.cfm?FuseAction=PressReleases.List&Month=6&Year=2006',
        'http://dole.senate.gov/public/index.cfm?FuseAction=PressReleases.List&Month=7&Year=2006',
        'http://dole.senate.gov/public/index.cfm?FuseAction=PressReleases.List&Month=8&Year=2006',
        'http://dole.senate.gov/public/index.cfm?FuseAction=PressReleases.List&Month=9&Year=2006',
        'http://dole.senate.gov/public/index.cfm?FuseAction=PressReleases.List&Month=10&Year=2006',
        'http://dole.senate.gov/public/index.cfm?FuseAction=PressReleases.List&Month=11&Year=2006',
        'http://dole.senate.gov/public/index.cfm?FuseAction=PressReleases.List&Month=12&Year=2006']
##        'http://dole.senate.gov/index.cfm?FuseAction=PressReleases.List&Month=1&Year=2003',
##        'http://dole.senate.gov/index.cfm?FuseAction=PressReleases.List&Month=2&Year=2003',
##        'http://dole.senate.gov/index.cfm?FuseAction=PressReleases.List&Month=3&Year=2003',
##        'http://dole.senate.gov/index.cfm?FuseAction=PressReleases.List&Month=4&Year=2003',
##        'http://dole.senate.gov/index.cfm?FuseAction=PressReleases.List&Month=5&Year=2003',
##        'http://dole.senate.gov/index.cfm?FuseAction=PressReleases.List&Month=6&Year=2003',
##        'http://dole.senate.gov/index.cfm?FuseAction=PressReleases.List&Month=7&Year=2003',
##        'http://dole.senate.gov/index.cfm?FuseAction=PressReleases.List&Month=8&Year=2003',
##        'http://dole.senate.gov/index.cfm?FuseAction=PressReleases.List&Month=9&Year=2003',
##        'http://dole.senate.gov/index.cfm?FuseAction=PressReleases.List&Month=10&Year=2003',
##          'http://dole.senate.gov/index.cfm?FuseAction=PressReleases.List&Month=1&Year=2004',
##        'http://dole.senate.gov/index.cfm?FuseAction=PressReleases.List&Month=2&Year=2004',
##        'http://dole.senate.gov/index.cfm?FuseAction=PressReleases.List&Month=3&Year=2004',
##        'http://dole.senate.gov/index.cfm?FuseAction=PressReleases.List&Month=4&Year=2004',
##        'http://dole.senate.gov/index.cfm?FuseAction=PressReleases.List&Month=5&Year=2004',
##        'http://dole.senate.gov/index.cfm?FuseAction=PressReleases.List&Month=6&Year=2004',
##        'http://dole.senate.gov/index.cfm?FuseAction=PressReleases.List&Month=7&Year=2004',
##        'http://dole.senate.gov/index.cfm?FuseAction=PressReleases.List&Month=8&Year=2004',
##        'http://dole.senate.gov/index.cfm?FuseAction=PressReleases.List&Month=9&Year=2004',
##        'http://dole.senate.gov/index.cfm?FuseAction=PressReleases.List&Month=10&Year=2004',
##        'http://dole.senate.gov/index.cfm?FuseAction=PressReleases.List&Month=11&Year=2004',
##        'http://dole.senate.gov/index.cfm?FuseAction=PressReleases.List&Month=12&Year=2004',]


for j in range(0,1):#len(html)):
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
        store += 'http://dole.senate.gov/' + fr[num] + '\n'

    fr = store.split('\n')
    fr.remove('')
    
    for num in range(2,3):#len(fr)):
            test = urlopen(fr[num]).read()
            soup2 = BeautifulSoup(test)
            ps = soup2.findAll('td')
            date = soup2.findAll('strong')
            for k in range(len(date)):
                if date[k].has_key('class'):
                    if date[k]['class']=='recorddate' :
                        out = utilities.clean_html(str(date[k]))
            stores= ''
            for m in range(len(ps)):
                if ps[m].has_key('class') and ps[m].has_key('colspan'):
                    if ps[m]['class']=='text':
                        stores += utilities.clean_html(str(ps[m]))
            stores = re.sub('\W', ' ', stores)
            out = re.sub('\W', '', out)
            names = 'Dole' + str(num) + out + '.txt'
            files = open(names, 'w')
            files.write(stores)
            files.close()  
            
