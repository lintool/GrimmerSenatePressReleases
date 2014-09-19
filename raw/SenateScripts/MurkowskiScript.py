import re, os
from nltk import utilities
from urllib import urlopen
from BeautifulSoup import BeautifulSoup

os.chdir('C:\CongressPressExpand\Murkowski')

html=['http://murkowski.senate.gov/pressapp/releases.cfm?type=1']
##You need to rerun this with the right name!!!

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
        date = []
        a= 0 
        ps = soup.findAll('font')
        for m in range(len(ps)):
            if ps[m].has_key('face') and ps[m].has_key('size'):
                if ps[m]['face']=='verdana,geneva,helvetica' and ps[m]['size']=='1':
                    a +=1
                    if m%2==0 and a>2:
                        date.append(utilities.clean_html(str(ps[m])))
        

        store = ''
        for num in range(len(fr)):
            store += 'http://murkowski.senate.gov/pressapp/' + fr[num] + '\n'
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
            names = str(num) + 'Murkowski'  + mint + '.txt'
            files = open(names, 'w')
            files.write(stores)
            files.close()


            
        
