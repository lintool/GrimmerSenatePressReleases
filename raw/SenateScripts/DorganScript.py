import re,os
from nltk import utilities
from BeautifulSoup import BeautifulSoup
from urllib import urlopen

os.chdir('C:\CongressPress\Dorgan')

html=['http://dorgan.senate.gov/newsroom/releases.cfm']



for j in range(len(html)):
    out = urlopen(html[j]).read()
    soup = BeautifulSoup(out)
    res  = soup.findAll('a')
    fr= []
    for k in range(len(res)):
        if res[k].has_key('href'):
            ab = res[k]['href']
            ba = re.findall('\?id', str(ab))
            if len(ba)>0 :
                fr.append(ab.encode('UTF-8'))


    store = ''
    for num in range(len(fr)):
        store += 'http://dorgan.senate.gov/newsroom/' + fr[num] + '\n'
    fr = store.split('\n')
    fr.remove('')


    for num in range(len(fr)):
            test = urlopen(fr[num]).read()
            soup2 = BeautifulSoup(test)
            ps = soup2.findAll('h2')
            date = ps[0].findNext('p')
            date = utilities.clean_html(str(date))
            date = re.sub('\W', '', date)
            stores=''
            for m in range(len(ps)):
                stores += utilities.clean_html(str(ps[m]))
            stores = re.sub('\W', ' ', stores)
            names = str(num) + 'Dorgan'  + date + '.txt'
            files = open(names, 'w')
            files.write(stores)
            files.close()
