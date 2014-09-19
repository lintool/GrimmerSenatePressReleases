import re, os
from nltk import utilities
from BeautifulSoup import BeautifulSoup
from urllib import urlopen



os.chdir('C:\CongressPress\Stabenow')
##this is very incomplete
html=['http://stabenow.senate.gov/press/index.htm']


for j in range(0, len(html)):
        out = urlopen(html[j]).read()
        soup = BeautifulSoup(out)
        res  = soup.findAll('a')
        fr= []
        for k in range(len(res)):
            if res[k].has_key('href'):
                ab = res[k]['href']
                ab = ab.strip('..')
                ba = re.findall('\d\d\d\d/\d\d\d\d\d\d', str(ab))
                if len(ba)>0 :
                    fr.append(ab.encode('UTF-8'))
        date = []
        ps = soup.findAll('td')
        for m in range(len(ps)):
            if ps[m].has_key('class') and ps[m].has_key('height'):
                if ps[m]['class']=='main03':
                    if ps[m]['height']=='21' or ps[m]['height']=='20':
                        date.append(utilities.clean_html(str(ps[m])))


        store = ''
        for num in range(len(fr)):
            store += 'http://stabenow.senate.gov/press/' + fr[num] + '\n'
        fr = store.split('\n')
        fr.remove('')


        for num in range(0,len(fr)):
                    test = urlopen(fr[num]).read()
                    soup2 = BeautifulSoup(test)
                    abd= soup2.findAll('a')
                    for k in range(len(abd)):
                        abd[k].extract()
                    stores = utilities.clean_html(str(soup2))
                    stores = re.sub('\W', ' ', stores)
                    mint= date[num+1]
                    mint= re.sub('\W', '', mint)
                    names = str(num) + 'Stabenow'  + mint + '.txt'
                    files = open(names, 'w')
                    files.write(stores)
                    files.close() 
