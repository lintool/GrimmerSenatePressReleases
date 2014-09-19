import re, os
from nltk import utilities
from BeautifulSoup import BeautifulSoup
from urllib import urlopen


os.chdir('C:\CongressPressExpand\Schumer')

html=['http://schumer.senate.gov/SchumerWebsite/pressroom/pr-latest_news_2007.cfm?maxrows=732&startrow=1&&year=2007',
     'http://schumer.senate.gov/SchumerWebsite/pressroom/pr-latest_news_2006.cfm?maxrows=653&startrow=1&&year=2006',
     'http://schumer.senate.gov/SchumerWebsite/pressroom/pr-latest_news_2005.cfm?maxrows=783&startrow=1&&year=2005']
##      'http://schumer.senate.gov/SchumerWebsite/pressroom/pr-latest_news.2004.html']


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


for j in range(2, len(html)):
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

        a= 0
        date=[]
        ps = soup.findAll('span')
        for m in range(len(ps)):
            if ps[m].has_key('class'):
                if ps[m]['class']=='pressappSmallText':
                    a+=1
                    if a>2:
                        abc = utilities.clean_html(str(ps[m]))
                        abc = abc.split('/')
                        mons = month[abc[0]]
                        day = abc[1]
                        year = '20' + abc[-1]
                        date.append(day + mons + year)

        store = ''
        for num in range(len(fr)):
            store += 'http://schumer.senate.gov/SchumerWebsite/pressroom/' + fr[num] + '\n'
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
                mint= date[num]
                names = mint + 'Schumer'  + str(num) + '.txt'
                files = open(names, 'w')
                files.write(stores)
                files.close()
