import re, os
from nltk import utilities
from urllib import urlopen
from BeautifulSoup import BeautifulSoup



os.chdir('C:\CongressPress\Sanders')


html=['http://sanders.senate.gov/news/index.cfm?next=10&itemNumber=1&code=*&type=*&pHeader=',
      'http://sanders.senate.gov/news/index.cfm?next=10&itemNumber=21&code=*&type=*&pHeader=',
      'http://sanders.senate.gov/news/index.cfm?next=10&itemNumber=31&code=*&type=*&pHeader=',
      'http://sanders.senate.gov/news/index.cfm?next=10&itemNumber=41&code=*&type=*&pHeader=',
      'http://sanders.senate.gov/news/index.cfm?next=10&itemNumber=51&code=*&type=*&pHeader=',
      'http://sanders.senate.gov/news/index.cfm?next=10&itemNumber=61&code=*&type=*&pHeader=',
      'http://sanders.senate.gov/news/index.cfm?next=10&itemNumber=71&code=*&type=*&pHeader=',
      'http://sanders.senate.gov/news/index.cfm?next=10&itemNumber=81&code=*&type=*&pHeader=',
      'http://sanders.senate.gov/news/index.cfm?next=10&itemNumber=91&code=*&type=*&pHeader=',
      'http://sanders.senate.gov/news/index.cfm?next=10&itemNumber=101&code=*&type=*&pHeader=',
      'http://sanders.senate.gov/news/index.cfm?next=10&itemNumber=111&code=*&type=*&pHeader=',
      'http://sanders.senate.gov/news/index.cfm?next=10&itemNumber=121&code=*&type=*&pHeader=',
      'http://sanders.senate.gov/news/index.cfm?next=10&itemNumber=131&code=*&type=*&pHeader=',
      'http://sanders.senate.gov/news/index.cfm?next=10&itemNumber=141&code=*&type=*&pHeader=',
      'http://sanders.senate.gov/news/index.cfm?next=10&itemNumber=151&code=*&type=*&pHeader=',
      'http://sanders.senate.gov/news/index.cfm?next=10&itemNumber=161&code=*&type=*&pHeader=',
      'http://sanders.senate.gov/news/index.cfm?next=10&itemNumber=171&code=*&type=*&pHeader=',
      'http://sanders.senate.gov/news/index.cfm?next=10&itemNumber=181&code=*&type=*&pHeader=',
      'http://sanders.senate.gov/news/index.cfm?next=10&itemNumber=191&code=*&type=*&pHeader=',
      'http://sanders.senate.gov/news/index.cfm?next=10&itemNumber=201&code=*&type=*&pHeader=',
      'http://sanders.senate.gov/news/index.cfm?next=10&itemNumber=211&code=*&type=*&pHeader=',
      'http://sanders.senate.gov/news/index.cfm?next=10&itemNumber=221&code=*&type=*&pHeader=',
      'http://sanders.senate.gov/news/index.cfm?next=10&itemNumber=231&code=*&type=*&pHeader=',
      'http://sanders.senate.gov/news/index.cfm?next=10&itemNumber=241&code=*&type=*&pHeader=',
      'http://sanders.senate.gov/news/index.cfm?next=10&itemNumber=251&code=*&type=*&pHeader=',
      'http://sanders.senate.gov/news/index.cfm?next=10&itemNumber=261&code=*&type=*&pHeader=',
      'http://sanders.senate.gov/news/index.cfm?next=10&itemNumber=271&code=*&type=*&pHeader=']

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
        a = 0
        ps = soup.findAll('strong')
        for m in range(len(ps)):
            a+=1
            if a<len(fr)+1:
                date.append(utilities.clean_html(str(ps[m])))

        store = ''
        for num in range(len(fr)):
            store += fr[num] + '\n'
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
                names = str(num) + 'Sanders'  + mint + '.txt'
                files = open(names, 'w')
                files.write(stores)
                files.close()


