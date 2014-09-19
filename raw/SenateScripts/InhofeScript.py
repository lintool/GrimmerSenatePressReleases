import re, os
from nltk import utilities
from BeautifulSoup import BeautifulSoup
from urllib import urlopen



os.chdir('C:\CongressPressExpand\Inhofe')

html=['http://inhofe.senate.gov/public/index.cfm?FuseAction=PressRoom.PressReleases&ContentRecordType_id=ae7a6475-a01f-4da5-aa94-0a98973de620&Region_id=&Issue_id=&MonthDisplay=0&YearDisplay=2007&x=17&y=15',
      'http://inhofe.senate.gov/public/index.cfm?FuseAction=PressRoom.PressReleases&ContentRecordType_id=ae7a6475-a01f-4da5-aa94-0a98973de620&Region_id=&Issue_id=&MonthDisplay=0&YearDisplay=2006&x=17&y=15',
      'http://inhofe.senate.gov/public/index.cfm?FuseAction=PressRoom.PressReleases&ContentRecordType_id=ae7a6475-a01f-4da5-aa94-0a98973de620&Region_id=&Issue_id=&MonthDisplay=0&YearDisplay=2005&x=17&y=15']
#      'http://inhofe.senate.gov/public/index.cfm?FuseAction=PressRoom.PressReleases&ContentRecordType_id=ae7a6475-a01f-4da5-aa94-0a98973de620&Region_id=&Issue_id=&MonthDisplay=0&YearDisplay=2004&x=17&y=15']

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

for j in range(0,len(html)):
    out = urlopen(html[j]).read()
    soup = BeautifulSoup(out)
    res  = soup.findAll('a')
    fr= []
    for k in range(len(res)):
        if res[k].has_key('href'):
            ab = res[k]['href']
            ba = re.findall('_id', str(ab))
            if len(ba)>0 :
                fr.append(ab.encode('UTF-8'))

    store = ''
    for num in range(len(fr)):
        store += 'http://inhofe.senate.gov/public/' + fr[num] + '\n'
    fr = store.split('\n')
    fr.remove('')


    
    for num in range(3,len(fr)-2):
            if num=='temp':
                pass
            else:
                test = urlopen(fr[num]).read()
                soup2 = BeautifulSoup(test)
                date = soup2.findAll('h4')
                date = utilities.clean_html(str(date[0]))
                date = date.split(' ')
                mons = mon_key[date[0]]
                day = re.sub('\W', '',date[1])
                year = date[-1]
                for k in range(len(date)):
                    date = utilities.clean_html(str(date))
                ps = soup2.findAll('a')
                stores = ''
                for k in range(len(ps)):
                    ps[k].extract()
                pss = soup2.findAll('option')
                for k in range(len(pss)):
                    pss[k].extract()
                pst = soup2.findAll('span')
                for k in range(len(pst)):
                    pst[k].extract()
                h3s = soup2.findAll('h3')
                for k in range(len(h3s)):
                    h3s[k].extract()
                h1s = soup2.findAll('h1')
                for k in range(len(h1s)):
                    h1s[k].extract()
                divs = soup2.findAll('div')
                for k in range(len(divs)):
                    if divs[k].has_key('class') and divs[k].has_key('style'):
                        if divs[k]['class']== 'ptext11':
                            divs[k].extract()
                stores = utilities.clean_html(str(soup2))
                names = day + mons + year +'Inhofe'  + str(num) + '.txt'
                files = open(names, 'w')
                files.write(stores)
                files.close()
