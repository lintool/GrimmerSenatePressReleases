import re, os
from nltk import utilities
from urllib import urlopen
from BeautifulSoup import BeautifulSoup



os.chdir('C:\CongressPressExpand\Wyden')


html=['http://wyden.senate.gov/newsroom/releases.cfm?maxrows=477&startrow=77&']



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

        
        store = ''
        for num in range(len(fr)):
            store += 'http://wyden.senate.gov' + fr[num] + '\n'
        fr = store.split('\n')
        fr.remove('')

        for num in range(0,len(fr)):
                test = urlopen(fr[num]).read()
                soup2 = BeautifulSoup(test)
                abd= soup2.findAll('a')
                for k in range(len(abd)):
                    abd[k].extract()
                act = soup2.findAll('h3')
                for k in range(len(act)):
                    act[k].extract()
                span = soup2.findAll('span')
                for j in range(len(span)):
                        if span[j].has_key('class') and span[j].has_key('alt') and span[j].has_key('title'):
                                if span[j]['class']=='pressappReleaseBody' and span[j]['alt']=='Release Date' and span[j]['title']=='Release Date' :
                                        date = utilities.clean_html(str(span[j]))
                stores = utilities.clean_html(str(soup2))
                stores = re.sub('\W', ' ', stores)
                mint = date
                date= date.split(" ")
                mons = date[1]
                day = re.sub('\W', '', date[2])
                year = date[-1]
                names = day + mons + year  + 'Wyden'  + str(num) + '.txt'
                files = open(names, 'w')
                files.write(stores)
                files.close()
        
