import re, os
from nltk import utilities
from urllib import urlopen
from BeautifulSoup import BeautifulSoup

os.chdir('C:\CongressPressExpand\Obama')


html=['http://obama.senate.gov/press/']

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

for j in range(0, len(html)):
        out = urlopen(html[j]).read()
        soup = BeautifulSoup(out)
        res  = soup.findAll('a')
        fr= []
        for k in range(len(res)):
            if res[k].has_key('href'):
                ab = res[k]['href']
                ab = ab.strip('..')
                ba = re.findall('/press/', str(ab))
                if len(ba)>0 :
                    fr.append(ab.encode('UTF-8'))


        date = []
        ps = soup.findAll('p')
        for m in range(len(ps)):
            if ps[m].has_key('class'):
                if ps[m]['class']=='date':
                    abc = utilities.clean_html(str(ps[m]))
                    abc = abc.split(' ')
                    mons = mon_key[abc[0]]
                    if len(abc[1])>0:
                            day = re.sub('\W', '', abc[1])
                          
                    if len(abc[1])==0:
                            day = re.sub('\W', '', abc[2])
                    year = abc[-1]
                    date.append(day + mons + year)
                    


        store = ''
        for num in range(len(fr)):
            store += fr[num] + '\n'
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
            names = mint + 'Obama' + str(num) + '.txt'
            files = open(names, 'w')
            files.write(stores)
            files.close()
        
