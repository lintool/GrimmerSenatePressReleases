import re,os
from BeautifulSoup import BeautifulSoup
from nltk import utilities
from urllib import urlopen


html = ['http://barrasso.senate.gov/public/index.cfm?FuseAction=PressOffice.PressReleases&ContentRecordType_id=e57fac22-06bd-473f-9805-b1c37e832fda&Region_id=&Issue_id=&MonthDisplay=0&YearDisplay=2007']

os.chdir('C:\CongressPressExpand\Barrasso')


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



for j in range(0, len(html)):
        out = urlopen(html[j]).read()
        soup = BeautifulSoup(out)
        res  = soup.findAll('a')
        fr= []
        date=[]
        for k in range(len(res)):
            if res[k].has_key('href'):
                ab = res[k]['href']
                ab = ab.strip('..')
                ba = re.findall('_id', str(ab))
                if len(ba)>0 :
                    fr.append(ab.encode('UTF-8'))
        det = soup.findAll('h3')
        for k in range(len(det)):
            dtt = utilities.clean_html(str(det[k]))
            dtt = dtt.split('/')
            mons = month[dtt[0]]
            day = dtt[1]
            year = '20' + dtt[2]
            almost =day + mons + year
            date.append(almost)


        
        store = ''
        for num in range(len(fr)):
            store += 'http://barrasso.senate.gov/public/' + fr[num] + '\n'
        fr = store.split('\n')
        fr.remove('')


        for num in range(0,len(fr)):
                test = urlopen(fr[num]).read()
                soup2 = BeautifulSoup(test)
                abd= soup2.findAll('a')
                for k in range(len(abd)):
                    abd[k].extract()
                opt = soup2.findAll('option')
                for k in range(len(opt)):
                    opt[k].extract()
                h3s = soup2.findAll('h3')
                for k in range(len(h3s)):
                    h3s[k].extract()
                stores = utilities.clean_html(str(soup2))
                stores = re.sub('\W', ' ', stores)
                mint= date[num]
                names = mint + 'Barrasso'  + str(num) + '.txt'
                files = open(names, 'w')
                files.write(stores)
                files.close()

        
