import re,os
from BeautifulSoup import BeautifulSoup
from nltk import utilities
from urllib import urlopen


os.chdir('C:\CongressPress\Warner')


html=['http://warner.senate.gov/public/index.cfm?FuseAction=PressRoom.PressReleases']



month ={}
month['01'] = 'January'
month['02'] = 'February'
month['03'] = 'March'
month['04'] = 'April'
month['05'] = 'May'
month['06'] = 'June'
month['07'] = 'July'
month['08'] = 'August'
month['09'] = 'September'
month['1'] = 'January'
month['2'] = 'February'
month['3'] = 'March'
month['4'] = 'April'
month['5'] = 'May'
month['6'] = 'June'
month['7'] = 'July'
month['8'] = 'August'
month['9'] = 'September'
month['10'] = 'October'
month['11'] = 'November'
month['12'] = 'December'


for j in range(0, len(html)):
        out = urlopen(html[j]).read()
        soup = BeautifulSoup(out)
        res  = soup.findAll('a')
        fr= []
        date = []
        for k in range(len(res)):
            if res[k].has_key('href'):
                ab = res[k]['href']
                ba = re.findall('PressReleases', str(ab))
                if len(ba)>0:
                        fr.append(res[k]['href'])
        awe= soup.findAll('h3')
        for k in range(len(awe)):
                ester = awe[k]
                ester = utilities.clean_html(str(ester))
                ester = re.sub('\W', '', ester)
                date.append(ester)

        store = ''
        for num in range(len(fr)):
            store += 'http://warner.senate.gov/public/' + fr[num] + '\n'
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
                add = soup2.findAll('option')
                for k in range(len(add)):
                    add[k].extract()
                stores = utilities.clean_html(str(soup2))
                stores = re.sub('\W', ' ', stores)
                mint= date[num]
                mint= re.sub('\W', '', mint)
                names = str(num) + 'Warner'  + mint + '.txt'
                files = open(names, 'w')
                files.write(stores)
                files.close()
