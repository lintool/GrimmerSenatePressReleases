import re, os
from BeautifulSoup import BeautifulSoup
from nltk import utilities
from urllib import urlopen


os.chdir('C:\CongressPress\Johnson')

html=['http://johnson.senate.gov/newsroom/pastreleases/2007//jan.cfm',
      'http://johnson.senate.gov/newsroom/pastreleases/2007//feb.cfm',
      'http://johnson.senate.gov/newsroom/pastreleases/2007//march.cfm',
      'http://johnson.senate.gov/newsroom/pastreleases/2007//april.cfm',
      'http://johnson.senate.gov/newsroom/pastreleases/2007//may.cfm',
      'http://johnson.senate.gov/newsroom/pastreleases/2007//june.cfm',
      'http://johnson.senate.gov/newsroom/pastreleases/2007//july.cfm',
      'http://johnson.senate.gov/newsroom/pastreleases/2007//aug.cfm',
      'http://johnson.senate.gov/newsroom/pastreleases/2007//sept.cfm',
      'http://johnson.senate.gov/newsroom/pastreleases/2007//oct.cfm',
      'http://johnson.senate.gov/newsroom/pastreleases/2007//nov.cfm',
      'http://johnson.senate.gov/newsroom/pastreleases/2007//dec.cfm']
##      'http://johnson.senate.gov/newsroom/pastreleases/2006//jan.cfm',
##      'http://johnson.senate.gov/newsroom/pastreleases/2006//feb.cfm',
##      'http://johnson.senate.gov/newsroom/pastreleases/2006//march.cfm',
##      'http://johnson.senate.gov/newsroom/pastreleases/2006//april.cfm',
##      'http://johnson.senate.gov/newsroom/pastreleases/2006//may.cfm',
##      'http://johnson.senate.gov/newsroom/pastreleases/2006//june.cfm',
##      'http://johnson.senate.gov/newsroom/pastreleases/2006//july.cfm',
##      'http://johnson.senate.gov/newsroom/pastreleases/2006//aug.cfm',
##      'http://johnson.senate.gov/newsroom/pastreleases/2006//sept.cfm',
##      'http://johnson.senate.gov/newsroom/pastreleases/2006//oct.cfm',
##      'http://johnson.senate.gov/newsroom/pastreleases/2006//nov.cfm',
##      'http://johnson.senate.gov/newsroom/pastreleases/2006//dec.cfm',
##      'http://johnson.senate.gov/newsroom/pastreleases/2005//jan.cfm',
##      'http://johnson.senate.gov/newsroom/pastreleases/2005//feb.cfm',
##      'http://johnson.senate.gov/newsroom/pastreleases/2005//march.cfm',
##      'http://johnson.senate.gov/newsroom/pastreleases/2005//april.cfm',
##      'http://johnson.senate.gov/newsroom/pastreleases/2005//may.cfm',
##      'http://johnson.senate.gov/newsroom/pastreleases/2005//june.cfm',
##      'http://johnson.senate.gov/newsroom/pastreleases/2005//july.cfm',
##      'http://johnson.senate.gov/newsroom/pastreleases/2005//aug.cfm',
##      'http://johnson.senate.gov/newsroom/pastreleases/2005//sept.cfm',
##      'http://johnson.senate.gov/newsroom/pastreleases/2005//oct.cfm',
##      'http://johnson.senate.gov/newsroom/pastreleases/2005//nov.cfm',
##      'http://johnson.senate.gov/newsroom/pastreleases/2005//dec.cfm',
##      'http://johnson.senate.gov/newsroom/pastreleases/2004//jan.cfm',
##      'http://johnson.senate.gov/newsroom/pastreleases/2004//feb.cfm',
##      'http://johnson.senate.gov/newsroom/pastreleases/2004//march.cfm',
##      'http://johnson.senate.gov/newsroom/pastreleases/2004//april.cfm',
##      'http://johnson.senate.gov/newsroom/pastreleases/2004//may.cfm',
##      'http://johnson.senate.gov/newsroom/pastreleases/2004//june.cfm',
##      'http://johnson.senate.gov/newsroom/pastreleases/2004//july.cfm',
##      'http://johnson.senate.gov/newsroom/pastreleases/2004//aug.cfm',
##      'http://johnson.senate.gov/newsroom/pastreleases/2004//sept.cfm',
##      'http://johnson.senate.gov/newsroom/pastreleases/2004//oct.cfm',
##      'http://johnson.senate.gov/newsroom/pastreleases/2004//nov.cfm',
##      'http://johnson.senate.gov/newsroom/pastreleases/2004//dec.cfm']

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
            store += 'http://johnson.senate.gov' + fr[num] + '\n'
        fr = store.split('\n')
        fr.remove('')

        for num in range(len(fr)-4):
            test = urlopen(fr[num]).read()
            soup2 = BeautifulSoup(test)
            stores = ''
            mint = date[num]
            mint = re.sub('\W', '', mint)
            abd= soup2.findAll('a')
            for k in range(len(abd)):
                abd[k].extract()
            abc = soup2.findAll('span')
            for k in range(len(abc)):
                    if abc[k].has_key('class'):
                            if abc[k]['class']=='dTodayInSenateEntry':
                                    abc[k].extract()
            tdd = soup2.findAll('td')
            for k in range(len(tdd)):
                if tdd[k].has_key('class'):
                        if tdd[k]['class']=='home_feature_discover' or tdd[k]['class']=='home_feature_title':
                                tdd[k].extract()
            p = soup2.findAll('p')
            for k in range(len(p)):
                if p[k].has_key('align'):
                        if p[k]['align']=='LEFT':
                                p[k].extract()
                            
            stores = utilities.clean_html(str(soup2))
            stores = re.sub('\W', ' ', stores)
            names = str(num)+ 'Johnson' + mint + '.txt'
            files= open(names, 'w')
            files.write(stores)
            files.close()


        
