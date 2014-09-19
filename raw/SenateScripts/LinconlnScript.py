import re, os
from nltk import utilities
from urllib import urlopen
from BeautifulSoup import BeautifulSoup


os.chdir('C:\CongressPressExpand\Lincoln')

html = []
stow = 'http://lincoln.senate.gov/newsroom_public_statements.cfm?PageNum_releases='
for k in range(9, 41):
    str2 = stow + str(k)
    html.append(str2)


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
    ps = soup.findAll('span')
    date = []
    for m in range(len(ps)):
        if ps[m].has_key('class'):
            if ps[m]['class']=='text_bold':
                abc = utilities.clean_html(str(ps[m]))
                abc = abc.split(' ')
                mons = mon_key[abc[0]]
                day = re.sub('\W', '', abc[1])
                year = abc[-1]
                date.append(day + mons + year)
                            
    
    store = ''
    for num in range(len(fr)):
        store += 'http://lincoln.senate.gov/' + fr[num] + '\n'
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
        mint= date[num]
        names = mint  + 'Lincoln'  + str(num) + '.txt'
        files = open(names, 'w')
        files.write(stores)
        files.close()




