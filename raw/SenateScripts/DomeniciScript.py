import re,os
from nltk import utilities
from BeautifulSoup import BeautifulSoup
from urllib import urlopen



os.chdir('C:\CongressPress\Domenici')


html = ['http://domenici.senate.gov/news/index.cfm?all=1&start=1',
        'http://domenici.senate.gov/news/index.cfm?all=1&start=21',
        'http://domenici.senate.gov/news/index.cfm?all=1&start=41',
        'http://domenici.senate.gov/news/index.cfm?all=1&start=61',
        'http://domenici.senate.gov/news/index.cfm?all=1&start=81',
        'http://domenici.senate.gov/news/index.cfm?all=1&start=101',
        'http://domenici.senate.gov/news/index.cfm?all=1&start=121',
        'http://domenici.senate.gov/news/index.cfm?all=1&start=141']




for j in range(2,len(html)):
    out = urlopen(html[j]).read()
    soup = BeautifulSoup(out)
    res  = soup.findAll('a')
    fr= []
    for k in range(len(res)):
        if res[k].has_key('href'):
            ab = res[k]['href']
            ba = re.findall('id', str(ab))
            if len(ba)>0 :
                fr.append(ab.encode('UTF-8'))

    store = ''
    for num in range(len(fr)):
        store += 'http://domenici.senate.gov/news/' + fr[num] + '\n'
    fr = store.split('\n')
    fr.remove('')

    for num in range(len(fr)):
            test = urlopen(fr[num]).read()
            soup2 = BeautifulSoup(test)
            ps = soup2.findAll('p')
            a = 0 
            for k in range(len(ps)):
                if ps[k].has_key('class'):
                    a += 1
                    if a==2:
                        date = utilities.clean_html(str(ps[k]))
            date = utilities.clean_html(str(date))
            date = re.sub('\W', '', date)
            stores=''
            for m in range(len(ps)):
                stores += utilities.clean_html(str(ps[m]))
            stores = re.sub('\W', ' ', stores)
            names = str(num) +  'Domenici' + date + '.txt'
            files = open(names, 'w')
            files.write(stores)
            files.close()




