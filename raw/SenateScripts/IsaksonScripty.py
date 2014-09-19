import re,os
from nltk import utilities
from urllib import urlopen
from BeautifulSoup import BeautifulSoup



os.chdir('C:\CongressPressExpand\Isakson')


html=['http://isakson.senate.gov/releases.html']

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

for j in range(0,len(html)):
    out = urlopen(html[j]).read()
    soup = BeautifulSoup(out)
    res  = soup.findAll('a')
    fr= []
    for k in range(len(res)):
        if res[k].has_key('href'):
            ab = res[k]['href']
            ba = re.findall('press/', str(ab))
            if len(ba)>0 :
                fr.append(ab.encode('UTF-8'))
    tds = soup.findAll('li')
    date=[]
    for m in range(len(tds)):
                ester = utilities.clean_html(str(tds[m]))
                ester2 = ester.split('-')
                ester3 = ester2[0]
                ester3 = ester3.split(' ')
                if len(ester3[0])==0:
                    mons = mon_key[ester3[1]]
                    day = re.sub('\W', '', ester3[2])
                    year = ester3[3]
                    date.append(day + mons + year)
                if len(ester3[3])==0:
                    mons = mon_key[ester3[0]]
                    day = re.sub('\W', '', ester3[1])
                    year = ester3[2]
                    date.append(day + mons + year)
                

    store = ''
    for num in range(len(fr)):
        store += 'http://isakson.senate.gov/' + fr[num] + '\n'
    fr = store.split('\n')
    fr.remove('')
                

    for num in range(0,1):#len(fr)):
            test = urlopen(fr[num]).read()
            soup2 = BeautifulSoup(test)
            abd= soup2.findAll('a')
            mint = re.sub('\W', '', date[num])
            for k in range(len(abd)):
                abd[k].extract()
            stores = utilities.clean_html(str(soup2))
            stores = re.sub('\W', ' ', stores)
            names = str(num) + 'Isakson'  + mint + '.txt'
            files = open(names, 'w')
            files.write(stores)
            files.close()
