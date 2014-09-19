from nltk import utilities
from BeautifulSoup import BeautifulSoup
from urllib import urlopen
import re, os


os.chdir('C:\CongressPressExpand\Ensign')


html=['http://ensign.senate.gov/media/pressapp/releases1.cfm?maxrows=528&startrow=96&']

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
            ba = re.findall('\?id', str(ab))
            if len(ba)>0 :
                fr.append(ab.encode('UTF-8'))

    

    store = ''
    for num in range(len(fr)):
        store += 'http://ensign.senate.gov/' + fr[num] + '\n'
    fr = store.split('\n')
    fr.remove('')

    for num in range(0,len(fr)):
            test = urlopen(fr[num]).read()
            soup2 = BeautifulSoup(test)
            ps = soup2.findAll('div')
            date = soup2.findAll('span')
            for k in range(len(date)):
                if date[k].has_key('class') and date[k].has_key('alt') and  date[k].has_key('title'):
                    if date[k]['class']=='pressappReleaseBody' and date[k]['alt']=='Release Date':
                        mint = date[k]
            mint = utilities.clean_html(str(mint))
            mint = mint.split(' ')
            mons = mon_key[mint[1]]
            days = re.sub('\W', '', mint[2])
            year = mint[-1]
            stores=''
            for m in range(len(ps)):
                if ps[m].has_key('class') and ps[m].has_key('alt') and ps[m].has_key('title'):
                    if ps[m]['class']=='pressappReleaseBody' and ps[m]['title']=='Release Body':
                        stores += utilities.clean_html(str(ps[m]))
            stores = re.sub('\W', ' ', stores)
            names = days + mons + year + 'Ensign' + str(num) +  '.txt'
            files = open(names, 'w')
            files.write(stores)
            files.close()

