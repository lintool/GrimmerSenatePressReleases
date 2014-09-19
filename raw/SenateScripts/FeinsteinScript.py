import re,os
from nltk import utilities
from BeautifulSoup import BeautifulSoup
from urllib import urlopen

##alow add in ul and li along with the paragraphs

os.chdir('C:\CongressPress\Feinstein')
html=['http://feinstein.senate.gov/public/index.cfm?FuseAction=NewsRoom.PressReleases&ContentRecordType_id=ae7a6475-a01f-4da5-aa94-0a98973de620&Region_id=&Issue_id=&MonthDisplay=0&YearDisplay=2007&x=22&y=16']
##      'http://feinstein.senate.gov/public/index.cfm?FuseAction=NewsRoom.PressReleases&ContentRecordType_id=ae7a6475-a01f-4da5-aa94-0a98973de620&Region_id=&Issue_id=&MonthDisplay=0&YearDisplay=2006&x=17&y=11']




for j in range(0,1):
    out = urlopen(html[j]).read()
    soup = BeautifulSoup(out)
    res  = soup.findAll('a')
    fr= []
    for k in range(len(res)):
        if res[k].has_key('href'):
            ab = res[k]['href']
            ba = re.findall('\_id', str(ab))
            if len(ba)>0 :
                fr.append(ab.encode('UTF-8'))

    store = ''
    for num in range(len(fr)):
        store += 'http://feinstein.senate.gov/public/' + fr[num] + '\n'
    fr = store.split('\n')
    fr.remove('')

    for num in range(2, len(fr)):
            test = urlopen(fr[num]).read()
            soup2 = BeautifulSoup(test)
            ps = soup2.findAll('p')
            ted = soup2.findAll('td')
            for k in range(len(ted)):
                if ted[k].has_key('width'):
                    if ted[k]['width']=='60%':
                        tt = ted[k]
            almost = utilities.clean_html(str(tt)).split(':')
            eta = almost[-1]
            eta = re.sub('\W', '', eta)
            date = eta
            stores=''
            opts = soup2.findAll('option')
            for k in range(len(opts)):
                opts[k].extract()
            ast = soup2.findAll('a')
            for k in range(len(ast)):
                ast[k].extract()
            h3s = soup2.findAll('h3')
            for k in range(len(h3s)):
                h3s[k].extract()
            stores = utilities.clean_html(str(soup2))
            stores = re.sub('\W', ' ', stores)
            names = str(num) + 'Feinstein' + date + '.txt'
            files = open(names, 'w')
            files.write(stores)
            files.close()
    
