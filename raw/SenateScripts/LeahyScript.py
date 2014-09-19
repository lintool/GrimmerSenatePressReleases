import re, os
from nltk import utilities
from urllib import urlopen
from BeautifulSoup import BeautifulSoup

os.chdir('C:\CongressPressExpand\Leahy')


html=['http://leahy.senate.gov/press/arch2007.html',
      'http://leahy.senate.gov/press/arch2006.html',
      'http://leahy.senate.gov/press/arch2005.html']

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



for j in range(len(html)):
        out = urlopen(html[j]).read()
        soup = BeautifulSoup(out)
        res  = soup.findAll('a')
        fr= []
        date=[]
        for k in range(len(res)):
            if res[k].has_key('href'):
                ab = res[k]['href']
                ab = ab.strip('..')
                ba = re.findall('\d\d\d\d\d\d/\d\d\d\d\d\d[a-z]\.html|\d\d\d\d\d\d/\d\d\d\d\d\d\.html', str(ab))
                if len(ba)>0 :
                    fr.append(ab.encode('UTF-8'))
                    att = ab
                    emp = re.findall('\d\d\d\d\d\d[a-z]\.html|\d\d\d\d\d\d\.html', str(att))
                    almost = re.sub('\W', '', emp[0].strip('.html'))
                    almost = almost.strip('a').strip('b').strip('c').strip('d').strip('e').strip('f')
                    mons = month[almost[0:2]]
                    day = almost[2:4]
                    year = '20' + almost[-2:]
                    date.append(day + mons + year)
                    
                    
                


        store = ''
        for num in range(len(fr)):
            store += 'http://leahy.senate.gov/press/' + fr[num] + '\n'
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
                names = mint + 'Leahy' + str(num) + '.txt'
                files = open(names, 'w')
                files.write(stores)
                files.close()
