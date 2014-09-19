from nltk import utilities
from BeautifulSoup import BeautifulSoup
from urllib import urlopen
import re, os
##import stuff

os.chdir('C:\CongressPressExpand\Chambliss')
mon_key={}
mon_key['January']= 'Jan'
mon_key['February']='Feb'
mon_key['March']='Mar'
mon_key['April']='Apr'
mon_key['May']= 'May'
mon_key['June']='Jun'
mon_key['July']='Jul'
mon_key['August']='Aug'
mon_key['September']= 'Sep'
mon_key['October']='Oct'
mon_key['November']='Nov'
mon_key['December']='Dec'

html = ['http://www.senate.gov/~chambliss/public/index.cfm?FuseAction=NewsCenter.PressReleases&ContentRecordType_id=5c81ba67-be20-4229-a615-966ecb0ccad6&Region_id=&Issue_id=&MonthDisplay=0&YearDisplay=2007&CFId=23579714&CFToken=39016683',
       'http://www.senate.gov/~chambliss/public/index.cfm?FuseAction=NewsCenter.PressReleases&ContentRecordType_id=5c81ba67-be20-4229-a615-966ecb0ccad6&Region_id=&Issue_id=&MonthDisplay=0&YearDisplay=2006&CFId=23579714&CFToken=39016683',
        'http://www.senate.gov/~chambliss/public/index.cfm?FuseAction=NewsCenter.PressReleases&ContentRecordType_id=5c81ba67-be20-4229-a615-966ecb0ccad6&Region_id=&Issue_id=&MonthDisplay=0&YearDisplay=2005&CFId=23579714&CFToken=39016683']
##        'http://www.senate.gov/~chambliss/public/index.cfm?FuseAction=NewsCenter.PressReleases&ContentRecordType_id=5c81ba67-be20-4229-a615-966ecb0ccad6&Region_id=&Issue_id=&MonthDisplay=0&YearDisplay=2004&CFId=23579714&CFToken=39016683',
##        'http://www.senate.gov/~chambliss/public/index.cfm?FuseAction=NewsCenter.PressReleases&ContentRecordType_id=5c81ba67-be20-4229-a615-966ecb0ccad6&Region_id=&Issue_id=&MonthDisplay=0&YearDisplay=2003&CFId=23579714&CFToken=39016683']


for j in range(0, len(html)):
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
        store += 'http://www.senate.gov/~chambliss/public/' + fr[num] + '\n'
    fr = store.split('\n')
    fr.remove('')


    for num in range(3, len(fr)):
        test = urlopen(fr[num]).read()
        soup2 = BeautifulSoup(test)
        date = soup2.findAll('h4')
        date = utilities.clean_html(str(date[0]))
        date = date.split(' ')
        mons = mon_key[date[0]]
        day = re.sub('\W', '', date[1])
        year = date[-1]
        divs = soup2.findAll('div')
        text = ''
        if j>=2:
            for m in range(0, len(divs)):
                text += utilities.clean_html(str(divs[m]))
        if j < 2:
            for m in range(3, len(divs)):
                text += utilities.clean_html(str(divs[m]))
        stores = re.sub('\W', ' ' , text)
        names = day + mons + year + 'Chambliss' + str(num) + '.txt'
        files = open(names, 'w')
        files.write(stores)
        files.close()
