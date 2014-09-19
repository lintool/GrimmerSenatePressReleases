import os, re
from BeautifulSoup import BeautifulSoup
from urllib import urlopen
from nltk import utilities
import nltk

os.chdir('C:\CongressPressExpand\Bond')


html= ['http://bond.senate.gov/public/index.cfm?FuseAction=PressRoom.NewsReleases&ContentRecordType_id=759d888b-7087-4636-a1dc-c6b0c67d3207&Region_id=&Issue_id=&MonthDisplay=0&YearDisplay=2007',
       'http://bond.senate.gov/public/index.cfm?FuseAction=PressRoom.NewsReleases&ContentRecordType_id=759d888b-7087-4636-a1dc-c6b0c67d3207&Region_id=&Issue_id=&MonthDisplay=0&YearDisplay=2006',
       'http://bond.senate.gov/public/index.cfm?FuseAction=PressRoom.NewsReleases&ContentRecordType_id=759d888b-7087-4636-a1dc-c6b0c67d3207&Region_id=&Issue_id=&MonthDisplay=0&YearDisplay=2005']
####       'http://bond.senate.gov/public/index.cfm?FuseAction=PressRoom.NewsReleases&ContentRecordType_id=759d888b-7087-4636-a1dc-c6b0c67d3207&Region_id=&Issue_id=&MonthDisplay=0&YearDisplay=2004',
####       'http://bond.senate.gov/public/index.cfm?FuseAction=PressRoom.NewsReleases&ContentRecordType_id=759d888b-7087-4636-a1dc-c6b0c67d3207&Region_id=&Issue_id=&MonthDisplay=0&YearDisplay=2003',
####       'http://bond.senate.gov/public/index.cfm?FuseAction=PressRoom.NewsReleases&ContentRecordType_id=759d888b-7087-4636-a1dc-c6b0c67d3207&Region_id=&Issue_id=&MonthDisplay=0&YearDisplay=2002',
####       'http://bond.senate.gov/public/index.cfm?FuseAction=PressRoom.NewsReleases&ContentRecordType_id=759d888b-7087-4636-a1dc-c6b0c67d3207&Region_id=&Issue_id=&MonthDisplay=0&YearDisplay=2001']


months = []
months.append('January')
months.append('February')
months.append('March')
months.append('April')
months.append('May')
months.append('June')
months.append('July')
months.append('August')
months.append('September')
months.append('October')
months.append('November')
months.append('December')

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
mon_key['JANUARY']='Jan'
mon_key['FEBRUARY']= 'Feb'
mon_key['MARCH']= 'Mar'
mon_key['APRIL']= 'Apr'
mon_key['MAY']= 'May'
mon_key['JUNE']= 'Jun'
mon_key['JULY']= 'Jul'
mon_key['AUGUST']= 'Aug'
mon_key['SEPTEMBER']= 'Sep'
mon_key['OCTOBER']= 'Oct'
mon_key['NOVEMBER']= 'Nov'
mon_key['DECEMBER']= 'Dec'

for j in range(2, len(html)):
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
        store += 'http://bond.senate.gov/public/' + fr[num] + '\n'
    fr = store.split('\n')
    fr.remove('')
    fr = fr[3:]

    for num in range(len(fr)):
        test = urlopen(fr[num]).read()
        soup2 = BeautifulSoup(test)
        divs = soup2.findAll('div')
        date = soup2.findAll('h4')
        date = utilities.clean_html(str(date[0]))
        date = date.split(' ')
        mons = mon_key[date[0]]
        day = re.sub('\W', '', date[1])
        year = date[-1]
        for k in range(len(divs)):
            if divs[k].has_key('id'):
                if divs[k]['id']=='contentRecord':
                    store = utilities.clean_html(str(divs[k]))
        names = day + mons + year + 'Bond' + str(num) + '.txt'
        files = open(names, 'w')
        files.write(store)
        files.close()
        
