import re, os
from nltk import utilities
from BeautifulSoup import BeautifulSoup
from urllib import urlopen


os.chdir('C:\CongressPressExpand\Reed')


html=[]
stre = 'http://reed.senate.gov/newsroom/PressReleases.cfm?s='
for m in range(100, 475, 25):
    strew = stre + str(m)
    html.append(strew)

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
        a = 0
        for k in range(len(res)):
            if res[k].has_key('href'):
                ab = res[k]['href']
                ab = ab.strip('..')
                ba = re.findall('\?id', str(ab))
                if len(ba)>0 :
                    a +=1
                    if a%2 ==1:
                        fr.append(ab.encode('UTF-8'))


        store = ''
        for num in range(len(fr)):
            store += 'http://reed.senate.gov/newsroom/' + fr[num] + '\n'
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
            mint = soup2.findAll('strong')
            mint = utilities.clean_html(str(mint[0]))
            mint=  mint.split(' ')
            mons = mon_key[mint[0]]
            day = re.sub('\W', '', mint[1])
            year = mint[-1]
            names = day + mons + year + 'Reed' + str(num) + '.txt'
            files = open(names, 'w')
            files.write(stores)
            files.close()
        
