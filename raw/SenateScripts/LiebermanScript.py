import re, os
from nltk import utilities
from urllib import urlopen
from BeautifulSoup import BeautifulSoup


os.chdir('C:\CongressPressExpand\Lieberman')

html=['http://lieberman.senate.gov/newsroom/releases.cfm?year=2007',
      'http://lieberman.senate.gov/newsroom/releases.cfm?year=2006',
      'http://lieberman.senate.gov/newsroom/releases.cfm?year=2005']
##      'http://lieberman.senate.gov/newsroom/releases.cfm?year=2004',
##      'http://lieberman.senate.gov/newsroom/releases.cfm?year=2003',
##      'http://lieberman.senate.gov/newsroom/releases.cfm?year=2002',
##      'http://lieberman.senate.gov/newsroom/releases.cfm?year=2001']


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
            ba = re.findall('\?id', str(ab))
            if len(ba)>0 :
                fr.append(ab.encode('UTF-8'))
    ps = soup.findAll('p')
    date= []
    for m in range(len(ps)):
        if ps[m].has_key('class'):
            if ps[m]['class']=='newsDate':
                ab = utilities.clean_html(str(ps[m]))
                if j ==0:
                    ab += ' ' + '2007'
                if j==1:
                    ab += ' ' +  '2006'
                if j==2:
                    ab +=' ' + '2005'
                if j==3:
                    ab += ' ' +'2004'
                if j==4:
                    ab+= ' ' +'2003'
                if j ==5:
                    ab+= ' ' +'2002'
                if j==6:
                    ab+= ' ' + '2001'
                test = ps[m].fetchNextSiblings('blockquote')
                for Isabella in range(len(test)):
                    abc = ab.split(' ')
                    mons = mon_key[abc[0]]
                    day  = abc[1]
                    year = abc[2]
                    date.append(day + mons + year)
                    
                    


        
    store = ''
    for num in range(len(fr)):
        store += 'http://lieberman.senate.gov/newsroom/' + fr[num] + '\n'
    fr = store.split('\n')
    fr.remove('')

    for num in range(len(fr)):
        test = urlopen(fr[num]).read()
        soup2 = BeautifulSoup(test)
        abd= soup2.findAll('a')
        for k in range(len(abd)):
            abd[k].extract()
        stores = utilities.clean_html(str(soup2))
        stores = re.sub('\W', ' ', stores)
        fret = soup.findAll('div')
        mint= date[num]
        names = mint  + 'Lieberman' + str(num) + '.txt'
        files = open(names, 'w')
        files.write(stores)
        files.close()

    
