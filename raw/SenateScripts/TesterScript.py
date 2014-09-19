import re,os
from nltk import utilities
from BeautifulSoup import BeautifulSoup
from urllib import urlopen


os.chdir('C:\CongressPressExpand\Tester')


html=['http://tester.senate.gov/Newsroom/press_releases.cfm?pagenum=1&nrecords=314']


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
        ps = soup.findAll('td')
        a = 0 
        for m in range(len(ps)):
            if ps[m].has_key('bgcolor'):
                if ps[m]['bgcolor']=='ffffff' or ps[m]['bgcolor']=='efefef':
                    a+=1
                    if a%2==1:
                        date.append(utilities.clean_html(str(ps[m])))


        store = ''
        for num in range(len(fr)):
            store += 'http://tester.senate.gov/' + fr[num] + '\n'
        fr = store.split('\n')
        fr.remove('')

        for num in range(0,len(fr)):
                test = urlopen(fr[num]).read()
                soup2 = BeautifulSoup(test)
                abd= soup2.findAll('a')
                for k in range(len(abd)):
                    abd[k].extract()
                span = soup2.findAll('span')
                for k in range(len(span)):
                     if span[k].has_key('class'):
                        if span[k]['class']=='dTodayInSenateDate':
                                span[k].extract()
                det = soup2.findAll('p')
                for k in range(len(det)):
                     if det[k].has_key('align'):
                        if det[k]['align']=='LEFT':
                                det[k].extract()
                stores = utilities.clean_html(str(soup2))
                stores = re.sub('\W', ' ', stores)
                mint= date[num]
                mint= re.sub('\W', '', mint)
                names =  str(num) + 'Tester' + mint + '.txt'
                files = open(names, 'w')
                files.write(stores)
                files.close()
        
