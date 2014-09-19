import os,re
from urllib import urlopen
from nltk import utilities
from BeautifulSoup import BeautifulSoup

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



os.chdir('C:\CongressPressExpand\Boxer')

html= ['http://boxer.senate.gov/news/releases/pastreleases.cfm?maxrows=499&startrow=72&']


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
        store += 'http://boxer.senate.gov/news/releases/' + fr[num] + '\n'
    fr = store.split('\n')
    fr.remove('')
    for num in range(0,len(fr)):
        test = urlopen(fr[num]).read()
        soup2 = BeautifulSoup(test)
        divs = soup2.findAll('div')
        temp = soup2.findAll('span')
        for m in range(len(temp)):
            if temp[m].has_key('class'):
                if temp[m]['class']=='pressappReleaseBody':
                    date = utilities.clean_html(str(temp[m]))
        date = date.split(',')
        year = re.sub('\W', '', date[-1])
        mons_day= date[1].split(' ')
        mons = mon_key[mons_day[1]]
        day = mons_day[-1]
        for k in range(len(divs)):
            if divs[k].has_key('class'):
                if divs[k]['class']=='pressappReleaseBody':
                    stores = utilities.clean_html(str(divs[k]))
        names = day + mons + year + 'Boxer' + str(num) + '.txt'
        files = open(names, 'w')
        files.write(stores)
        files.close()
