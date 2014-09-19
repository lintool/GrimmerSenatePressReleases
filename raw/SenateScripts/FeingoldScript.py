import re, os
from nltk import utilities
from urllib import urlopen
from BeautifulSoup import BeautifulSoup


os.chdir('C:\CongressPressExpand\Feingold')


html=['http://www.senate.gov/cgi-bin/nph-dpc2s?dir=%7Efeingold/releases']

for j in range(len(html)):
    out = urlopen(html[j]).read()
    soup = BeautifulSoup(out)
    res  = soup.findAll('a')
    fr= []
    for k in range(len(res)):
        if res[k].has_key('href'):
            ab = res[k]['href']
            ba = re.findall('/~feingold/releases', str(ab))
            if len(ba)>0 :
                fr.append(ab.encode('UTF-8'))

    store = ''
    for num in range(len(fr)):
        store += 'http://feingold.senate.gov/' + fr[num] + '\n'
    fr = store.split('\n')
    fr.remove('')

    for num in range(535, len(fr)):
            test = urlopen(fr[num]).read()
            fret = re.findall('\<dpc\s.+', str(test))
            fret2 = fret[0].split('=')
            fret3 = fret2[-1]
            date = re.sub('\W', '', fret3)
            soup2 = BeautifulSoup(test)
            ps = soup2.findAll('p')
            stores=''
            for m in range(0, len(ps)):
                stores += utilities.clean_html(str(ps[m])) + ' '
            stores = re.sub('\W', ' ', stores)
            names = str(num) + 'Feingold'+ date + '.txt'
            files = open(names, 'w')
            files.write(stores)
            files.close()
