import re, os
from nltk import utilities
from BeautifulSoup import BeautifulSoup
from urllib import urlopen

os.chdir('C:\CongressPressExpand\Durbin')



ranges = range(10, 46)
htmls = 'http://durbin.senate.gov/multimedia_releaseArchive.cfm?rTps=1&page='

html=[]

for k in ranges:
    html.append(htmls + str(k))

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
            ba = re.findall('\?releaseId', str(ab))
            if len(ba)>0 :
                fr.append(ab.encode('UTF-8'))

    date = []
    res = soup.findAll('span')
    for k in range(len(res)):
        if res[k].has_key('style'):
            if res[k]['style']=='font-size:10px':
                abc = utilities.clean_html(str(res[k]))
                abc = abc.split('/')
                mons = month[abc[0]]
                day = abc[1]
                year = '20' + abc[2]
                date.append(day + mons + year)
                

    
    store = ''
    for num in range(len(fr)):
        store += 'http://durbin.senate.gov/' + fr[num] + '\n'
    fr = store.split('\n')
    fr.remove('')


    for num in range(0,len(fr)):
            test = urlopen(fr[num]).read()
            soup2 = BeautifulSoup(test)
##            date = soup2.findAll('div')
##            if len(date)>1:
##                for k in range(len(date)):
##                    if date[k].has_key('align') and date[k].has_key('class'):
##                        if date[k]['align']=='center' and date[k]['class']=='bodytext_white':
##                            mint = date[k]
##            mint = utilities.clean_html(str(mint))
##            mint = re.sub('\W', '', mint)
            abd= soup2.findAll('a')
            for k in range(len(abd)):
                abd[k].extract()
            spans = soup2.findAll('span')
            for k in range(len(spans)):
                if spans[k].has_key('class'):
                    if spans[k]['class']=='bodytext_blue':
                        spans[k].extract()
            
            stores = utilities.clean_html(str(soup2))
            stores = re.sub('\W', ' ', stores)
            names = date[num] + 'Durbin' + str(num)  + '.txt'
            files = open(names, 'w')
            files.write(stores)
            files.close()
