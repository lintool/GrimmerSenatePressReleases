import re,os
from nltk import utilities
from BeautifulSoup import BeautifulSoup
from urllib import urlopen


os.chdir('C:\CongressPress\Hutchison')

html  = ['http://hutchison.senate.gov/releases.html']


for j in range(len(html)):
    out = urlopen(html[j]).read()
    soup = BeautifulSoup(out)
    res  = soup.findAll('a')
    fr= []
    date = []
    for k in range(len(res)):
        if res[k].has_key('href'):
            ab = res[k]['href']
            ba = re.findall('\d\d\d\d\d\d', str(res[k]))
            if len(ba)>0 :
                fr.append(ab.encode('UTF-8'))
                date.append(ba)
    store = ''
    for num in range(len(fr)):
        store +=   'http://hutchison.senate.gov/' + fr[num] + '\n'
    fr = store.split('\n')
    fr.remove('')
    
    for num in range(len(fr)):
            test = urlopen(fr[num]).read()
            soup2 = BeautifulSoup(test)
            ps = soup2.findAll('')
            mint = re.sub('\W', '', str(date[num]))
            stores=''
            abd = soup2.findAll('a')
            for k in range(len(abd)):
                abd[k].extract()
            stores = utilities.clean_html(str(soup2))
            stores = re.sub('\W', ' ', stores)
            names = str(num) + 'Hutchison' + mint + '.txt'
            files = open(names, 'w')
            files.write(stores)
            files.close()
    
