import re,os
from nltk import utilities
from urllib import urlopen
from BeautifulSoup import BeautifulSoup



os.chdir('C:\CongressPress\Craig')


html= ['http://craig.senate.gov/releases.cfm']


for j in range(len(html)):
    out = urlopen(html[j]).read()
    soup = BeautifulSoup(out)
    res  = soup.findAll('a')
    fr= []
    for k in range(len(res)):
        if res[k].has_key('href'):
            ab = res[k]['href']
            ba = re.findall('/releases/', str(ab))
            if len(ba)>0 :
                fr.append(ab.encode('UTF-8'))
    temp = soup.findAll('dd')
    date= ''
    for k in range(len(temp)):
        ab = re.findall('/releases/', str(temp[k]))
        if len(ab)>0:
            fudge = utilities.clean_html(str(temp[k]))
            fudge = fudge.split('-')
            fudge2 = re.sub('\W', '', str(fudge[-1]))
            date += fudge2 + '\n'
            
    store = ''
    for num in range(len(fr)):
        store += fr[num] + '\n'
    fr = store.split('\n')
    date = date.split('\n')
    date.remove('')
    fr.remove('')

    for num in range(len(fr)):
            test = urlopen(fr[num]).read()
            soup2 = BeautifulSoup(test)
            ps = soup2.findAll('p')
            stores=''
            for m in range(len(ps)):
                stores += utilities.clean_html(str(ps[m]))
            stores = re.sub('\W', ' ', stores)
            names = str(num) + 'Craig'  + date[num] + '.txt'
            files = open(names, 'w')
            files.write(stores)
            files.close()
    

    
