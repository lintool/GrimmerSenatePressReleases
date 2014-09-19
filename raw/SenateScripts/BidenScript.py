from BeautifulSoup import BeautifulSoup
import re
import os
from urllib import urlopen
from nltk import utilities
import nltk

os.chdir('C:\CongressPressExpand\Biden')

html= ['http://biden.senate.gov/newsroom/press.cfm?maxrows=1078&startrow=1&']


for j in range(len(html)):
    out = urlopen(html[j]).read()
    soup = BeautifulSoup(out)
    res  = soup.findAll('a')
    fr= []
    for k in range(len(res)):
        if res[k].has_key('href'):
            ab = res[k]['href']
            ba = re.findall('id', str(ab))
            if len(ba)>0 :
                fr.append(ab.encode('UTF-8'))
            

    store = ''
    for num in range(len(fr)):
        store += 'http://biden.senate.gov/newsroom/' + fr[num] + '\n'

    fr = store.split('\n')
    fr.remove('')
    

    for num in range(128, len(fr)):
        test = urlopen(fr[num]).read()
        soup2 = BeautifulSoup(test)
        divs = soup2.findAll('p')
        date = utilities.clean_html(str(divs[0]).split('\n')[0])
        date = re.sub('\W', '', date)
        stores = ''
        for b in range(len(divs)):
            de = utilities.clean_html(str(divs[b]))
            stores += de
        names = 'Biden' + str(num) + date + '.txt'
        files = open(names, 'w')
        files.write(stores)
        files.close()
        
