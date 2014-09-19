import os, re
from nltk import utilities
from BeautifulSoup import BeautifulSoup
from urllib import urlopen


os.chdir('C:\CongressPressExpand\BillNelson')


html=['http://billnelson.senate.gov/news/media.cfm?year=2007',
      'http://billnelson.senate.gov/news/media.cfm?year=2006',
      'http://billnelson.senate.gov/news/media.cfm?year=2005']
      #'http://billnelson.senate.gov/news/media.cfm?year=2004',
      #'http://billnelson.senate.gov/news/media.cfm?year=2003',
      #'http://billnelson.senate.gov/news/media.cfm?year=2002',
      #'http://billnelson.senate.gov/news/media.cfm?year=2001']

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
mon_key['AUGUST']= 'Aug'
mon_key['SEPTEMBER']= 'Sep'
mon_key['OCTOBER']= 'Oct'
mon_key['NOVEMBER']= 'Nov'
mon_key['DECEMBER']= 'Dec'



for j in range(0, len(html)):
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


        store = ''
        for num in range(len(fr)):
            store += 'http://billnelson.senate.gov/news/' + fr[num] + '\n'
        fr = store.split('\n')
        fr.remove('')

        for num in range(0,len(fr)):
                test = urlopen(fr[num]).read()
                soup2 = BeautifulSoup(test)
                h2s = soup2.findAll('h2')
                date = utilities.clean_html(str(h2s[0].findNext('p')))
                for k in range(len(months)):
                        att = re.findall(months[k], str(date))
                        if len(att)>0:
                                mons = mon_key[months[k]]
                                temp = date.split(' ')
                                day = re.sub('\W', '', temp[1])
                                year = temp[-1]
                                agg = day + mons + year
                abd= soup2.findAll('a')
                for k in range(len(abd)):
                    abd[k].extract()
                stores = utilities.clean_html(str(soup2))
                names = agg + 'BillNelson'  + str(num) + '.txt'
                files = open(names, 'w')
                files.write(stores)
                files.close()
