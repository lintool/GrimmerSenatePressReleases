import re, os
from nltk import utilities
from urllib import urlopen
from BeautifulSoup import BeautifulSoup


os.chdir('C:\CongressPress\Kyl')

html=['http://kyl.senate.gov/media_center/media_main.cfm?start=1&search_field=&type=1&code=&ndays=500&theday=&submit=Search',
      'http://kyl.senate.gov/media_center/media_main.cfm?start=21&search_field=&type=1&code=&ndays=500&theday=&submit=Search',
      'http://kyl.senate.gov/media_center/media_main.cfm?start=41&search_field=&type=1&code=&ndays=500&theday=&submit=Search',
      'http://kyl.senate.gov/media_center/media_main.cfm?start=61&search_field=&type=1&code=&ndays=500&theday=&submit=Search']


for j in range(len(html)):
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
    date=[]
    a= 0 
    dates = soup.findAll('font')
    for m in range(1,len(dates)):
        if dates[m].has_key('face') and dates[m].has_key('size'):
            if dates[m]['face']=="verdana,geneva,helvetica" and dates[m]['size']=='1':
                a+= 1
                if a>3 and m%3==0:
                    date.append(utilities.clean_html(str(dates[m])))


    store = ''
    for num in range(len(fr)):
        store += 'http://kyl.senate.gov/' + fr[num] + '\n'
    fr = store.split('\n')
    fr.remove('')


    for num in range(len(fr)):
        test = urlopen(fr[num]).read()
        soup2 = BeautifulSoup(test)
        abd= soup2.findAll('a')
        mint = re.sub('\W', '', date[num])
        for k in range(len(abd)):
            abd[k].extract()
        stores = utilities.clean_html(str(soup2))
        stores = re.sub('\W', ' ', stores)
        names = 'Kyl' + str(num) + mint + '.txt'
        files = open(names, 'w')
        files.write(stores)
        files.close()
