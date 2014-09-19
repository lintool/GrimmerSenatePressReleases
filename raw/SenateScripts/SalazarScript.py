import re, os
from BeautifulSoup import BeautifulSoup
from nltk import utilities
from urllib import urlopen



os.chdir('C:\CongressPressExpand\Salazar')

html=['http://salazar.senate.gov/news/press_releases.html']

month={}
month['01'] = 'Jan'
month['02']= 'Feb'
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



for j in range(0, len(html)):
        out = urlopen(html[j]).read()
        soup = BeautifulSoup(out)
        res  = soup.findAll('a')
        fr= []
        for k in range(len(res)):
            if res[k].has_key('href'):
                ab = res[k]['href']
                ab = ab.strip('..')
                ba = re.findall('releases/\d\d\d\d\d\d', str(ab))
                if len(ba)>0 :
                    fr.append(ab.encode('UTF-8'))
        date =[]
        a = 0
        tds = soup.findAll('td')
        for m in range(len(tds)):
                if a<75:
                        if tds[m].has_key('valign'):
                                if tds[m]['valign']=='top' or tds[m]['valign']=='TOP':
                                    a+=1
                                    bt = m%2
                                    if a>3 and bt==0:
                                        emp =utilities.clean_html(str(tds[m]))
                                        if len(emp)<20:
                                                date.append(emp)
                if a>74:
                        if tds[m].has_key('valign'):
                                if tds[m]['valign']=='top' or tds[m]['valign']=='TOP':
                                    a+=1
                                    ##bt = m%3
                                    if a>3: ##and bt==0:
                                        bt = re.findall('\d\d\d\d',utilities.clean_html(str(tds[m])))
                                        if len(bt)>0:
                                                emp =utilities.clean_html(str(tds[m]))
                                                if len(emp)<20:
                                                        date.append(utilities.clean_html(str(tds[m])))


        date2 = []
        for k in range(len(date)):
            abc = date[k]
            abc = abc.split('.')
            mons = month[abc[0]]
            day = abc[1]
            years = abc[-1]
            date2.append(day + mons + years)
        store = ''
        for num in range(len(fr)):
            store += 'http://salazar.senate.gov/news/' + fr[num] + '\n'
        fr = store.split('\n')
        fr.remove('')


        for num in range(0,len(fr)):
                test = urlopen(fr[num]).read()
                soup2 = BeautifulSoup(test)
                abd= soup2.findAll('a')
                for k in range(len(abd)):
                    abd[k].extract()
                spans = soup2.findAll('span')
                for k in range(len(spans)):
                        if spans[k].has_key('style'):
                                if spans[k]['style']=='font-size:12.0pt;mso-bidi-font-size:8.0pt;font-family:Arial':
                                        spans[k].extract()                                        
                stores = utilities.clean_html(str(soup2))
                stores = re.sub(' U S    Senator Ken Salazar Member  Finance  Agriculture  Energy  Ethics and Aging Committees', '', stores)
                stores = re.sub('\W', ' ', stores)
                mint= date2[num]
                names =  mint + 'Salazar'  + str(num)  + '.txt'
                files = open(names, 'w')
                files.write(stores)
                files.close()
