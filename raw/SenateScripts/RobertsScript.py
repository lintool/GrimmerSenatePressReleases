import re, os
from nltk import utilities
from BeautifulSoup import BeautifulSoup
from urllib import urlopen


os.chdir('C:\CongressPress\Roberts')


html=['http://roberts.senate.gov/public/index.cfm?FuseAction=PressRoom.PressReleases&ContentRecordType_id=ae7a6475-a01f-4da5-aa94-0a98973de620&Region_id=&Issue_id=&MonthDisplay=0&YearDisplay=2007&x=24&y=10']
##      'http://roberts.senate.gov/public/index.cfm?FuseAction=PressRoom.PressReleases&ContentRecordType_id=ae7a6475-a01f-4da5-aa94-0a98973de620&Region_id=&Issue_id=&MonthDisplay=0&YearDisplay=2006&x=15&y=10']



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

        date=[]
        ps = soup.findAll('h3')
        for m in range(len(ps)):
            if ps[m].has_key('class'):
                if ps[m]['class']=='ContentGrid':
                        date.append(utilities.clean_html(str(ps[m])))


        store = ''
        for num in range(len(fr)):
            store += 'http://Roberts.senate.gov/public/' + fr[num] + '\n'
        fr = store.split('\n')
        fr.remove('')

        for num in range(3,len(fr)):
                    tre = num-3
                    test = urlopen(fr[num]).read()
                    soup2 = BeautifulSoup(test)
                    abd= soup2.findAll('a')
                    for k in range(len(abd)):
                        abd[k].extract()
                    opt = soup2.findAll('option')
                    for m in range(len(opt)):
                        opt[m].extract()
                    h3s = soup2.findAll('h3')
                    for j in range(len(h3s)):
                        h3s[j].extract()
                    stores = utilities.clean_html(str(soup2))
                    stores = re.sub('\W', ' ', stores)
                    mint= date[tre]
                    mint= re.sub('\W', '', mint)
                    names = 'Roberts' + str(num) + mint + '.txt'
                    files = open(names, 'w')
                    files.write(stores)
                    files.close()
        
