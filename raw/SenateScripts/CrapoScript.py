import re, os
from nltk import utilities
from BeautifulSoup import BeautifulSoup
from urllib import urlopen



os.chdir('C:\CongressPressExpand\Crapo')


html= ['http://crapo.senate.gov/media/newsreleases/release_all.cfm?maxrows=640&startrow=118&']


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



for j in range(len(html)):
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
        if fr[num][0]=='h':
            store += fr[num] + '\n'
        else:
            store += 'http://crapo.senate.gov/media/newsreleases/' + fr[num] + '\n'
    fr = store.split('\n')
    fr.remove('')

    for num in range(528,len(fr)):
            test = urlopen(fr[num]).read()
            soup2 = BeautifulSoup(test)
            ps = soup2.findAll('div')
            span = soup2.findAll('span')
            for k in range(len(span)):
                if span[k].has_key('title'):
                    if span[k]['title']=='Release Date':
                        date = span[k]
            date = utilities.clean_html(str(date))
            date = date.split(' ')
            mons = mon_key[re.sub('\W', '',date[1])]
            day = re.sub('\W', '', date[2])
            years = date[-1]
            stores=''
            for m in range(len(ps)):
                if ps[m].has_key('title'):
                    if ps[m]['title']=='Release Body':
                        stores += utilities.clean_html(str(ps[m]))
            stores = re.sub('\W', ' ', stores)
            names = day + mons  + years  + 'Crapo' + str(num) + '.txt'
            files = open(names, 'w')
            files.write(stores)
            files.close()
