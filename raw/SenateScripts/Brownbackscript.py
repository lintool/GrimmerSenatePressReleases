import re,os
from BeautifulSoup import BeautifulSoup
from nltk import utilities
from urllib import urlopen


os.chdir('C:\CongressPressExpand\Brownback')

html= ['http://brownback.senate.gov/pressapp/view_by_year.cfm?year=2007',
       'http://brownback.senate.gov/pressapp/view_by_year.cfm?year=2006',
       'http://brownback.senate.gov/pressapp/view_by_year.cfm?year=2005']
##       'http://brownback.senate.gov/pressapp/view_by_year.cfm?year=2004',
##       'http://brownback.senate.gov/pressapp/view_by_year.cfm?year=2003',
##       'http://brownback.senate.gov/pressapp/view_by_year.cfm?year=2002',
##       'http://brownback.senate.gov/pressapp/view_by_year.cfm?year=2001',
##       'http://brownback.senate.gov/pressapp/view_by_year.cfm?year=2000',
##       'http://brownback.senate.gov/pressapp/view_by_year.cfm?year=1999']


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


for j in range(0,len(html)):
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
        store += 'http://brownback.senate.gov/pressapp/' + fr[num] + '\n'
    fr = store.split('\n')
    fr.remove('')


    for num in range(len(fr)):
        test = urlopen(fr[num]).read()
        soup2 = BeautifulSoup(test)
        divs = soup2.findAll('p')
        date = utilities.clean_html(str(divs[0]))
        date = re.sub(' ', '', date)
        date = date.split(',')
        mon_day = date[1]
        for k in range(len(months)):
            abc = re.findall(months[k], mon_day)
            if len(abc)>0:
                mons = mon_key[months[k]]
                day = re.sub(months[k], '', mon_day)
        
        year = re.sub('\W', '', date[-1])
        
        stores = ''
        for b in range(len(divs)):
            de = utilities.clean_html(str(divs[b]))
            stores += de + ' '
        names = day + mons + year + 'Brownback' + str(num)+ '.txt'
        files = open(names, 'w')
        files.write(stores)
        files.close()
