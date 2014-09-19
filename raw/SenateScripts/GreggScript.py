import re,os
from nltk import utilities
from urllib import urlopen
from BeautifulSoup import BeautifulSoup



os.chdir('C:\CongressPressExpand\Gregg')
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

html=['http://gregg.senate.gov/public/index.cfm?FuseAction=PressRoom.PressReleases&ContentRecordType_id=ae7a6475-a01f-4da5-aa94-0a98973de620&Region_id=&Issue_id=&MonthDisplay=0&YearDisplay=2007&x=26&y=7',
      'http://gregg.senate.gov/public/index.cfm?FuseAction=PressRoom.PressReleases&ContentRecordType_id=ae7a6475-a01f-4da5-aa94-0a98973de620&Region_id=&Issue_id=&MonthDisplay=0&YearDisplay=2006&x=26&y=7',
      'http://gregg.senate.gov/public/index.cfm?FuseAction=PressRoom.PressReleases&ContentRecordType_id=ae7a6475-a01f-4da5-aa94-0a98973de620&Region_id=&Issue_id=&MonthDisplay=0&YearDisplay=2005&x=26&y=7']
##      'http://gregg.senate.gov/public/index.cfm?FuseAction=PressRoom.PressReleases&ContentRecordType_id=ae7a6475-a01f-4da5-aa94-0a98973de620&Region_id=&Issue_id=&MonthDisplay=0&YearDisplay=2004&x=26&y=7']



for j in range(1,len(html)):
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
        store += 'http://gregg.senate.gov/public/' + fr[num] + '\n'
    fr = store.split('\n')
    fr.remove('')

    for num in range(1,len(fr)-1):
            test = urlopen(fr[num]).read()
            soup2 = BeautifulSoup(test)
            ps = soup2.findAll('p')
            h1 = soup2.findAll('h1')
            date = soup2.findAll('h4')
            date = utilities.clean_html(str(date[0]))
            date = date.split(' ')
            mons = mon_key[date[0]]
            day = re.sub('\W', '', date[1])
            year = date[-1]
            stores=''
            for k in range(len(h1)):
                if h1[k].has_key('class')==False:
                    stores += utilities.clean_html(str(h1[k])) + ' '
            for m in range(len(ps)):
                stores += utilities.clean_html(str(ps[m])) + ' '
            stores = re.sub('\W', ' ', stores)
            names = day + mons + year + 'Gregg' + str(num) + '.txt'
            files = open(names, 'w')
            files.write(stores)
            files.close()
