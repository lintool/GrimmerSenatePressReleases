import re, os
from nltk import utilities
from BeautifulSoup import BeautifulSoup
from urllib import urlopen

os.chdir('C:\CongressPressExpand\Kennedy')


html=[]
temp ='http://kennedy.senate.gov/newsroom/press_releases.cfm?PageNum_rs='
for m in range(18, 131):
    comp = temp + str(m)
    html.append(comp)

    


##need to make the html's yourself
month= {}
month['01']= 'Jan'
month['02'] = 'Feb'
month['03'] = 'Mar'
month['04'] = 'Apr'
month['05'] = 'May'
month['06'] = 'Jun'
month['07'] = 'Jul'
month['08'] = 'Aug'
month['09'] = 'Sep'
month['10'] = 'Oct'
month['11'] = 'Nov'
month['12'] = 'Dec'
month['1']= 'Jan'
month['2'] = 'Feb'
month['3'] = 'Mar'
month['4'] = 'Apr'
month['5'] = 'May'
month['6'] = 'Jun'
month['7'] = 'Jul'
month['8'] = 'Aug'
month['9'] = 'Sep'


for j in range(0,len(html)):
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
    date=[]
    dates = soup.findAll('dt')
    for m in range(len(dates)):
        abc = utilities.clean_html(str(dates[m]))
        abc = abc.split('/')
        mons = month[abc[0]]
        day = abc[1]
        year = '20' + abc[2]
        date.append(day + mons + year)

    store = ''
    for num in range(len(fr)):
        store += 'http://kennedy.senate.gov/newsroom/' + fr[num] + '\n'
    fr = store.split('\n')
    fr.remove('')



    for num in range(0,len(fr)):
        test = urlopen(fr[num]).read()
        soup2 = BeautifulSoup(test)
        abd= soup2.findAll('a')
        mint = date[num]
        #for k in range(len(abd)):
        #    abd[k].extract()
        #acd = soup2.findAll('option')
        #for k in range(len(acd)):
        #    acd[k].extract()
        #spans = soup2.findAll('span')
        #for k in range(len(spans)):
        #    spans[k].extract()
        #stores = utilities.clean_html(str(soup2))
        #stores = re.sub('\W', ' ', stores)
        ps = soup2.findAll('p')
        ps = utilities.clean_html(str(ps))
        stores = re.sub('\W',' ', ps)
        names = mint + 'Kennedy' + str(num) + '.txt'
        files = open(names, 'w')
        files.write(stores)
        files.close()
