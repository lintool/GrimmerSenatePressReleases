import re,os
from BeautifulSoup import BeautifulSoup
from urllib import urlopen
from nltk import utilities




os.chdir('C:\CongressPressExpand\Corker')


html=['http://corker.senate.gov/News/pressMaster.cfm?MaxRows=300&StartRow=57']

month= {}
month['01']= 'Jan'
month['02'] = 'Feb'
month['03'] = 'Mar'
month['04'] = 'Apr'
month['05'] = 'May'
month['06'] = 'Jun'
month['07'] = 'Jul'
month['08'] = 'Aug'
month['09'] = 'Sep'
month['10'] = 'Oct'
month['11'] = 'Nov'
month['12'] = 'Dec'

for j in range(0, len(html)):
        out = urlopen(html[j]).read()
        soup = BeautifulSoup(out)
        res  = soup.findAll('a')
        fr= []
        date = []
        for k in range(len(res)):
            if res[k].has_key('href'):
                ab = res[k]['href']
                ab = ab.strip('..')
                ba = re.findall('\?id', str(ab))
                if len(ba)>0 :
                    fr.append(ab.encode('UTF-8'))

        ps = soup.findAll('td')
        for m in range(len(ps)):
            if ps[m].has_key('bgcolor'):
                if m%2==1:
                    if ps[m]['bgcolor']=='ffffff' or ps[m]['bgcolor']=='efefef':
                        abc = utilities.clean_html(str(ps[m]))
                        abc = abc.split('/')
                        mons = month[abc[0]]
                        day = abc[1]
                        year = abc[-1]
                        date.append(day + mons + year)
        store = ''
        for num in range(len(fr)):
            store += 'http://corker.senate.gov/News/' + fr[num] + '\n'
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
                    mint = date[num]
                    names = mint + 'Corker' + str(num) + '.txt'
                    files = open(names, 'w')
                    files.write(stores)
                    files.close()
