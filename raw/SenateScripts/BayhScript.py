

from BeautifulSoup import BeautifulSoup
import re
from re import *
import os
from urllib import *
from nltk import utilities
import nltk


##html = ['http://www.senate.gov/cgi-bin/nph-dpc2s?dir=~bayh/releases' ]

## os.chdir('C:\CongressPress\Bayh')

##for j in range(len(html)):
##    out = urlopen(html[j]).read()
##    soup = BeautifulSoup(out)
##    res  = soup.findAll('a')
##    fr= []
##    for k in range(len(res)):
##        if res[k].has_key('href'):
##            ab = res[k]['href']
##            fr.append(ab.encode('UTF-8'))
##
##    store = ''
##    for num in range(len(fr)):
##        store += 'http://bayh.senate.gov' + fr[num] + '\n'
##
##    fr = store.split('\n')
##    fr.remove('')
##    
##    for num in range(384, len(fr)):
##        test = urlopen(fr[num]).read()
##        soup2 = BeautifulSoup(test)
##        divs = soup2.findAll('div')
##        if len(divs)!=17 & len(divs)!=0:
##            date = utilities.clean_html(str(divs[0])).split('\n')[2]
##            date = re.sub('\W', '', date)
##        else:
##            date = utilities.clean_html(str(soup2.findAll('center')).split('\n')[-2].strip('\r'))
##        stores = ''
##        for b in range(len(divs)):
##            de = utilities.clean_html(str(divs[b]))
##            stores += de
##        names = str(num) + 'Bayh' + date + '.txt'
##        files = open(names, 'w')
##        files.write(stores)
##        files.close()

    
html = ['http://bayh.senate.gov/newsroom.cfm?maxrows=168&startrow=1&']
os.chdir('C:\CongressPressExpand\Bayh')
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
            store += 'http://bayh.senate.gov/' + fr[num] + '\n'
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
                names = 'Bayh' + str(num) + mint + '.txt'
                files = open(names, 'w')
                files.write(stores)
                files.close()

                
        
