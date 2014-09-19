import re, os
from nltk import utilities
from urllib import urlopen
from BeautifulSoup import BeautifulSoup


os.chdir('C:\CongressPress\Reid')


html=['http://reid.senate.gov/newsroom/index.cfm?maxrows=493&startrow=1&&type=false&code=HomeNevada']



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


        a= 0
        date=[]
        ps = soup.findAll('span')
        for m in range(len(ps)):
            if ps[m].has_key('class'):
                if ps[m]['class']=='pressappSmallText':
                    a+=1
                    if a>2:
                        date.append(utilities.clean_html(str(ps[m])))



        store = ''
        for num in range(len(fr)):
            store += 'http://reid.senate.gov/newsroom/' + fr[num] + '\n'
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
                mint= date[num]
                mint= re.sub('\W', '', mint)
                names = 'Reid' + str(num) + mint + '.txt'
                files = open(names, 'w')
                files.write(stores)
                files.close()
        
