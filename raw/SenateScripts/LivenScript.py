import re,os
from nltk import utilities
from BeautifulSoup import BeautifulSoup
from urllib import urlopen


os.chdir('C:\CongressPressExpand\Levin')


html=['http://levin.senate.gov/newsroom/index.cfm?pleasesort=1&fromDate=01-01-2005&toDate=12-31-2007&issue=all&category=press&Submit=Submit']

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
    ps = soup.findAll('span')
    for m in range(len(ps)):
        if ps[m].has_key('class'):
            if ps[m]['class']=='newsdate':
                abc = utilities.clean_html(str(ps[m]))
                abc = abc.split('-')[0]
                abc= abc.split(' ')
                mons = abc[0]
                day = re.sub('\W', '', abc[1])
                year = abc[2]
                date.append(day + mons + year)
                



    store = ''
    for num in range(len(fr)):
        store += 'http://levin.senate.gov/newsroom/' + fr[num] + '\n'
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
        mints = date[num]
        names = mints + 'Levin' + str(num) + '.txt'
        files = open(names, 'w')
        files.write(stores)
        files.close()
