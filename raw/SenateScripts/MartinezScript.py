import re, os
from nltk import utilities
from BeautifulSoup import BeautifulSoup
from urllib import urlopen
os.chdir('C:\CongressPressExpand\Martinez')


html=['http://martinez.senate.gov/public/index.cfm?FuseAction=NewsReleases.List&ContentRecordType_id=1d62f91e-b8b8-44a9-8175-202346eb6e9e&Region_id=&Issue_id=&CFId=32434721&CFToken=10935171&Month=0&Year=2007&x=13&y=13',
      'http://martinez.senate.gov/public/index.cfm?FuseAction=NewsReleases.List&ContentRecordType_id=1d62f91e-b8b8-44a9-8175-202346eb6e9e&Region_id=&Issue_id=&CFId=32434721&CFToken=10935171&Month=0&Year=2006&x=10&y=21',
      'http://martinez.senate.gov/public/index.cfm?FuseAction=NewsReleases.List&ContentRecordType_id=1d62f91e-b8b8-44a9-8175-202346eb6e9e&Region_id=&Issue_id=&CFId=32434721&CFToken=10935171&Month=0&Year=2005&x=7&y=15']
##      'http://martinez.senate.gov/public/index.cfm?FuseAction=PressReleases.List&ContentRecordType_id=1&Region_id=0&Issue_id=0&CFId=31199218&CFToken=75451541&Month=0&Year=2004&x=8&y=10']

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
            ba = re.findall('_id', str(ab))
            if len(ba)>0 :
                fr.append(ab.encode('UTF-8'))
    ps = soup.findAll('h3')
    date =[]
    for m in range(len(ps)):
        if ps[m].has_key('class'):
            if ps[m]['class']=='ContentGrid':
                abc = utilities.clean_html(str(ps[m]))
                abc = abc.split('/')
                mons = month[abc[0]]
                day = abc[1]
                year = '20'  + abc[-1]
                date.append(day + mons + year)

    store = ''
    for num in range(len(fr)):
        store +=  fr[num] + '\n'
    fr = store.split('\n')
    fr.remove('')

    for num in range(1,len(fr)-1):
        test = urlopen(fr[num]).read()
        soup2 = BeautifulSoup(test)
        abd= soup2.findAll('a')
        for k in range(len(abd)):
            abd[k].extract()
        opt = soup2.findAll('option')
        for k in range(len(opt)):
            opt[k].extract()
        h3s = soup2.findAll('h3')
        for k in range(len(h3s)):
            h3s[k].extract()
        stores = utilities.clean_html(str(soup2))
        stores = re.sub('\W', ' ', stores)
        mint= date[num-1]
        mint= re.sub('\W', '', mint)
        names = mint + 'Martinez' + str(num) + '.txt'
        files = open(names, 'w')
        files.write(stores)
        files.close()
