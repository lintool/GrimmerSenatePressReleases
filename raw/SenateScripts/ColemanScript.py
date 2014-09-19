import re, os
from nltk import utilities
from BeautifulSoup import BeautifulSoup
from urllib import urlopen




os.chdir('C:\CongressPressExpand\Coleman')

html=['http://coleman.senate.gov/index.cfm?FuseAction=PressReleases.List&Month=1&Year=2006',
      'http://coleman.senate.gov/index.cfm?FuseAction=PressReleases.List&Month=2&Year=2006',
      'http://coleman.senate.gov/index.cfm?FuseAction=PressReleases.List&Month=3&Year=2006',
      'http://coleman.senate.gov/index.cfm?FuseAction=PressReleases.List&Month=4&Year=2006',
      'http://coleman.senate.gov/index.cfm?FuseAction=PressReleases.List&Month=5&Year=2006',
      'http://coleman.senate.gov/index.cfm?FuseAction=PressReleases.List&Month=6&Year=2006',
      'http://coleman.senate.gov/index.cfm?FuseAction=PressReleases.List&Month=7&Year=2006',
      'http://coleman.senate.gov/index.cfm?FuseAction=PressReleases.List&Month=8&Year=2006',
      'http://coleman.senate.gov/index.cfm?FuseAction=PressReleases.List&Month=9&Year=2006',
      'http://coleman.senate.gov/index.cfm?FuseAction=PressReleases.List&Month=10&Year=2006',
      'http://coleman.senate.gov/index.cfm?FuseAction=PressReleases.List&Month=11&Year=2006',
      'http://coleman.senate.gov/index.cfm?FuseAction=PressReleases.List&Month=12&Year=2006',
      'http://coleman.senate.gov/index.cfm?FuseAction=PressReleases.List&Month=1&Year=2007',
      'http://coleman.senate.gov/index.cfm?FuseAction=PressReleases.List&Month=2&Year=2007',
      'http://coleman.senate.gov/index.cfm?FuseAction=PressReleases.List&Month=3&Year=2007'
      'http://coleman.senate.gov/index.cfm?FuseAction=PressReleases.List&Month=4&Year=2007',
      'http://coleman.senate.gov/index.cfm?FuseAction=PressReleases.List&Month=5&Year=2007',
      'http://coleman.senate.gov/index.cfm?FuseAction=PressReleases.List&Month=6&Year=2007',
      'http://coleman.senate.gov/index.cfm?FuseAction=PressReleases.List&Month=7&Year=2007',
      'http://coleman.senate.gov/index.cfm?FuseAction=PressReleases.List&Month=8&Year=2007',
      'http://coleman.senate.gov/index.cfm?FuseAction=PressReleases.List&Month=9&Year=2007',
      'http://coleman.senate.gov/index.cfm?FuseAction=PressReleases.List&Month=10&Year=2007',
      'http://coleman.senate.gov/index.cfm?FuseAction=PressReleases.List&Month=11&Year=2007',
      'http://coleman.senate.gov/index.cfm?FuseAction=PressReleases.List&Month=12&Year=2007',
      'http://coleman.senate.gov/index.cfm?FuseAction=PressReleases.List&Month=1&Year=2005',
      'http://coleman.senate.gov/index.cfm?FuseAction=PressReleases.List&Month=2&Year=2005',
      'http://coleman.senate.gov/index.cfm?FuseAction=PressReleases.List&Month=3&Year=2005',
      'http://coleman.senate.gov/index.cfm?FuseAction=PressReleases.List&Month=4&Year=2005',
      'http://coleman.senate.gov/index.cfm?FuseAction=PressReleases.List&Month=5&Year=2005',
      'http://coleman.senate.gov/index.cfm?FuseAction=PressReleases.List&Month=6&Year=2005',
      'http://coleman.senate.gov/index.cfm?FuseAction=PressReleases.List&Month=7&Year=2005',
      'http://coleman.senate.gov/index.cfm?FuseAction=PressReleases.List&Month=8&Year=2005',
      'http://coleman.senate.gov/index.cfm?FuseAction=PressReleases.List&Month=9&Year=2005',
      'http://coleman.senate.gov/index.cfm?FuseAction=PressReleases.List&Month=10&Year=2005',
      'http://coleman.senate.gov/index.cfm?FuseAction=PressReleases.List&Month=11&Year=2005',
      'http://coleman.senate.gov/index.cfm?FuseAction=PressReleases.List&Month=12&Year=2005']
##      'http://coleman.senate.gov/index.cfm?FuseAction=PressReleases.List&Month=1&Year=2004',
##      'http://coleman.senate.gov/index.cfm?FuseAction=PressReleases.List&Month=2&Year=2004',
##      'http://coleman.senate.gov/index.cfm?FuseAction=PressReleases.List&Month=3&Year=2004',
##      'http://coleman.senate.gov/index.cfm?FuseAction=PressReleases.List&Month=4&Year=2004',
##      'http://coleman.senate.gov/index.cfm?FuseAction=PressReleases.List&Month=5&Year=2004',
##      'http://coleman.senate.gov/index.cfm?FuseAction=PressReleases.List&Month=6&Year=2004',
##      'http://coleman.senate.gov/index.cfm?FuseAction=PressReleases.List&Month=7&Year=2004',
##      'http://coleman.senate.gov/index.cfm?FuseAction=PressReleases.List&Month=8&Year=2004',
##      'http://coleman.senate.gov/index.cfm?FuseAction=PressReleases.List&Month=9&Year=2004',
##      'http://coleman.senate.gov/index.cfm?FuseAction=PressReleases.List&Month=10&Year=2004',
##      'http://coleman.senate.gov/index.cfm?FuseAction=PressReleases.List&Month=11&Year=2004',
##      'http://coleman.senate.gov/index.cfm?FuseAction=PressReleases.List&Month=12&Year=2004',
##      'http://coleman.senate.gov/index.cfm?FuseAction=PressReleases.List&Month=1&Year=2003',
##      'http://coleman.senate.gov/index.cfm?FuseAction=PressReleases.List&Month=2&Year=2003',
##      'http://coleman.senate.gov/index.cfm?FuseAction=PressReleases.List&Month=3&Year=2003',
##      'http://coleman.senate.gov/index.cfm?FuseAction=PressReleases.List&Month=4&Year=2003',
##      'http://coleman.senate.gov/index.cfm?FuseAction=PressReleases.List&Month=5&Year=2003',
##      'http://coleman.senate.gov/index.cfm?FuseAction=PressReleases.List&Month=6&Year=2003',
##      'http://coleman.senate.gov/index.cfm?FuseAction=PressReleases.List&Month=7&Year=2003',
##      'http://coleman.senate.gov/index.cfm?FuseAction=PressReleases.List&Month=8&Year=2003',
##      'http://coleman.senate.gov/index.cfm?FuseAction=PressReleases.List&Month=9&Year=2003',
##      'http://coleman.senate.gov/index.cfm?FuseAction=PressReleases.List&Month=10&Year=2003',
##      'http://coleman.senate.gov/index.cfm?FuseAction=PressReleases.List&Month=11&Year=2003',
##      'http://coleman.senate.gov/index.cfm?FuseAction=PressReleases.List&Month=12&Year=2003']



for j in range(0,5):#len(html)):
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
        store += 'http://coleman.senate.gov/' + fr[num] + '\n'
    fr = store.split('\n')
    fr.remove('')


    for num in range(20, len(fr)):
        test = urlopen(fr[num]).read()
        soup2 = BeautifulSoup(test)
        divs = soup2.findAll('td')
        stores =''
        date =''
        for k in range(len(divs)):
            if divs[k].has_key('class') and divs[k].has_key('style'):
                if divs[k]['class']=='Text':
                    stores += utilities.clean_html(str(divs[k]))
                    aqw = divs[k].findChildren('strong')
                    for m in range(len(aqw)):
                        ester = re.findall('\d\d\d\d', str(aqw[m]))
                        if len(ester)>0:
                            date = utilities.clean_html(str(aqw[m]))
        date = re.sub('\W', '', date)
        abd= soup2.findAll('a')
        for k in range(len(abd)):
            abd[k].extract()
        tds = soup2.findAll('td')
        for k in range(len(tds)):
            if tds[k].has_key('class') and tds[k].has_key('width'):
                if tds[k]['class']=='Text' and tds[k]['width']=='99%':
                    tds[k].extract()
        stores = utilities.clean_html(str(soup2))
        stores = re.sub('\W', ' ', stores)
        names = str(num) + 'Coleman' + date + '.txt'
        files = open(names, 'w')
        files.write(stores)
        files.close()
        
    
