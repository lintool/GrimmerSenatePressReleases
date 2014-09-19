import os, re
from nltk import utilities
from BeautifulSoup import BeautifulSoup
from urllib import urlopen



os.chdir('C:\CongressPress\Casey')


html=['http://casey.senate.gov/articles.cfm?maxrows=270&startrow=1&']


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
        ps = soup.findAll('span')
        a=0
        date=[]
        for m in range(len(ps)):
            if ps[m].has_key('class'):
                if ps[m]['class']=='pressappSmallText':
                    a+=1
                    if a>2:
                        date.append(utilities.clean_html(str(ps[m])))
        store = ''
        for num in range(len(fr)):
            store += 'http://casey.senate.gov/' + fr[num] + '\n'
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
                    mint = re.sub('\W', '',  date[num])
                    names = str(num) + 'Casey' + mint + '.txt'
                    files = open(names, 'w')
                    files.write(stores)
                    files.close()
