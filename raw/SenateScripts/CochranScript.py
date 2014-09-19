import re, os
from BeautifulSoup import BeautifulSoup
from nltk import utilities
from urllib import urlopen



os.chdir('C:\CongressPressExpand\Cochran')


##input a bunch of stuff here

html= ['http://cochran.senate.gov/pressreleases.html',
       'http://cochran.senate.gov/2006pr.html',
       'http://cochran.senate.gov/2005pr.html']
##       'http://cochran.senate.gov/2004pr.html',
##       'http://cochran.senate.gov/2003pr.html',
##       'http://cochran.senate.gov/archivepr.html']


for j in range(len(html)):
        out = urlopen(html[j]).read()
        soup = BeautifulSoup(out)
        res  = soup.findAll('a')
        fr= []
        date = []
        for k in range(len(res)):
            if res[k].has_key('href'):
                ab = res[k]['href']
                ba = re.findall('press/pr', str(ab))
                if len(ba)>0 :
                    fr.append(ab.encode('UTF-8'))
                    ester = re.findall('\d+', ab)
                    date.append(ester[0].encode('UTF-8'))
        
            

        store =''
        for num in range(len(fr)):
            if fr[num][0:2]=='/p':
                store += 'http://cochran.senate.gov' +  fr[num] + '\n'
            elif fr[num][0:2] == 'pr':
                store += 'http://cochran.senate.gov/' +  fr[num] + '\n'
            else:
                store += fr[num] + '\n'
        fr= store.split('\n')
        fr.remove('')

        for num in range(len(fr)):
            test = urlopen(fr[num]).read()
            soup2 = BeautifulSoup(test)
            stores = ''
            mint = date[num]
            mint = re.sub('\W', '', mint)
            abd= soup2.findAll('a')
            for k in range(len(abd)):
                abd[k].extract()
            stores = utilities.clean_html(str(soup2))
            stores = re.sub('\W', ' ', stores)
            names = 'Cochran' + str(num) + mint + '.txt'
            files= open(names, 'w')
            files.write(stores)
            files.close()
        
