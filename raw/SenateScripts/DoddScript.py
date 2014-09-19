import re, os
from BeautifulSoup import BeautifulSoup
from nltk import utilities
from urllib import urlopen


os.chdir('C:\CongressPress\Dodd')


html=['http://dodd.senate.gov/index.php?q=node/3271']


for j in range(0, len(html)):
        out = urlopen(html[j]).read()
        soup = BeautifulSoup(out)
        res  = soup.findAll('a')
        fr= []
        for k in range(len(res)):
            if res[k].has_key('class'):
                if res[k]['class']=='release':
                    ab = res[k]['href']
                    fr.append(ab.encode('UTF-8'))
        #blat = re.findall('\</a\>.+\<BR\>|\</a\>.+\<br\>', out)
        blat = re.findall('[A-Z][a-z]+\s[0-9]+\,\s2007', out)
        date = []
        for m in range(0, len(blat)):
                ##tt = utilities.clean_html(str(blat[m]))
                ttt = re.sub('\W', '', blat[m])
                date.append(ttt)
                

        store = ''
        for num in range(len(fr)):
            store += 'http://dodd.senate.gov/' + fr[num] + '\n'
        fr = store.split('\n')
        fr.remove('')


        for num in range(0,265-29):
                test = urlopen(fr[num]).read()
                soup2 = BeautifulSoup(test)
                abd= soup2.findAll('a')
                for k in range(len(abd)):
                        abd[k].extract()
                abc= soup2.findAll('span')
                for k in range(len(abc)):
                        if abc[k].has_key('class'):
                                if abc[k]['class']=='projectreadmore':
                                        abc[k].extract()
                abdiv = soup2.findAll('div')
                for k in range(len(abdiv)):
                        if abdiv[k].has_key('class'):
                                if abdiv[k]['class']=='news-list' or abdiv[k]['class']=='block block-block':
                                        abdiv[k].extract()
                stores = utilities.clean_html(str(soup2))
                stores = re.sub('\W', ' ', stores)
                mint = date[num]
                mint =utilities.clean_html(str(mint))
                mint= re.sub('\W', '', mint)
                names =  str(num) + 'Dodd'+ mint + '.txt'
                files = open(names, 'w')
                files.write(stores)
                files.close()
