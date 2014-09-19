import re, os
from nltk import utilities
from BeautifulSoup import BeautifulSoup
from urllib import urlopen




os.chdir('C:\CongressPress\Snowe')


html=['http://snowe.senate.gov/public/index.cfm?FuseAction=PressRoom.PressReleases&ContentRecordType_id=ae7a6475-a01f-4da5-aa94-0a98973de620&Region_id=&Issue_id=&MonthDisplay=0&YearDisplay=2007&x=25&y=15']
##      'http://snowe.senate.gov/public/index.cfm?FuseAction=PressRoom.PressReleases&ContentRecordType_id=ae7a6475-a01f-4da5-aa94-0a98973de620&Region_id=&Issue_id=&MonthDisplay=0&YearDisplay=2006&x=22&y=18',
##      'http://snowe.senate.gov/public/index.cfm?FuseAction=PressRoom.PressReleases&ContentRecordType_id=ae7a6475-a01f-4da5-aa94-0a98973de620&Region_id=&Issue_id=&MonthDisplay=0&YearDisplay=2005&x=17&y=8',
##      'http://snowe.senate.gov/public/index.cfm?FuseAction=PressRoom.PressReleases&ContentRecordType_id=ae7a6475-a01f-4da5-aa94-0a98973de620&Region_id=&Issue_id=&MonthDisplay=0&YearDisplay=2004&x=16&y=9']

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

        date = []
        ps = soup.findAll('h3')
        for m in range(len(ps)):
            if ps[m].has_key('class'):
                if ps[m]['class']=='ContentGrid':
                    date.append(utilities.clean_html(str(ps[m])))

        store = ''
        for num in range(len(fr)):
            store += 'http://snowe.senate.gov/public/' + fr[num] + '\n'
        fr = store.split('\n')
        fr.remove('')

        for num in range(0,len(fr)):
                tt = num-1
                test = urlopen(fr[num]).read()
                soup2 = BeautifulSoup(test)
                abd= soup2.findAll('a')
                for k in range(len(abd)):
                    abd[k].extract()
                act = soup2.findAll('h3')
                for k in range(len(act)):
                    act[k].extract()
                h1s = soup2.findAll('h1')
                for k in range(len(h1s)):
                    h1s[k].extract()
                opt = soup2.findAll('option')
                for k in range(len(opt)):
                    opt[k].extract()
                spans = soup2.findAll('span')
                for k in range(len(spans)):
                    spans[k].extract()
                divs = soup2.findAll('div')
                for k in range(len(divs)):
                    if divs[k].has_key('class'):
                            if divs[k]['class']=='Footer':
                                    divs[k].extract()
                stores = utilities.clean_html(str(soup2))
                stores = re.sub('\W', ' ', stores)
                mint= date[tt]
                mint= re.sub('\W', '', mint)
                names = str(num) + 'Snowe' + mint + '.txt'
                files = open(names, 'w')
                files.write(stores)
                files.close()
