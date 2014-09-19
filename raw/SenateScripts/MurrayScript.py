import re, os
from nltk import utilities
from BeautifulSoup import BeautifulSoup
from urllib import urlopen


os.chdir('C:\CongressPressExpand\Murray')

html=[]

stre = 'http://murray.senate.gov/news/continued.cfm?StartRow='

mon_key={}
mon_key['January']= 'Jan'
mon_key['February']='Feb'
mon_key['March']='Mar'
mon_key['April']='Apr'
mon_key['May']= 'May'
mon_key['June']='Jun'
mon_key['July']='Jul'
mon_key['August']='Aug'
mon_key['September']= 'Sep'
mon_key['October']='Oct'
mon_key['November']='Nov'
mon_key['December']='Dec'


for m in range(233, 1420, 15):
    strew = stre + str(m)
    html.append(strew)


for j in range(20, len(html)):
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


        store =''
        for num in range(len(fr)):
            store += 'http://murray.senate.gov/' + fr[num] + '\n'
        fr = store.split('\n')
        fr.remove('')


        for num in range(0, len(fr)):
            test = urlopen(fr[num]).read()
            soup2 = BeautifulSoup(test)
            abd= soup2.findAll('a')
            for k in range(len(abd)):
                abd[k].extract()
            opt = soup2.findAll('option')
            for k in range(len(opt)):
                opt[k].extract()
            stores = utilities.clean_html(str(soup2))
            stores = re.sub('\W', ' ', stores)
            tds = soup2.findAll('div')
            for m in range(len(tds)):
                if tds[m].has_key('align'):
                    if tds[m]['align']=='right':
                        mint = utilities.clean_html(str(tds[m]))
            mint = mint.split(' ')
            mons = mon_key[mint[1]]
            day =  re.sub('\W', '', mint[2])
            years = mint[-1]
            names = day + mons + years + 'Murray' + str(num) + '.txt'
            files = open(names, 'w')
            files.write(stores)
            files.close()
