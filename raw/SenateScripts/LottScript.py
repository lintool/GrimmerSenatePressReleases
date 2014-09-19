import re, os
from nltk import utilities
from BeautifulSoup import BeautifulSoup
from urllib import urlopen



os.chdir('C:\CongressPress\Lott')


html=['http://lott.senate.gov/public/index.cfm?FuseAction=PressOffice.PressReleases&ContentRecordType_id=b30084ac-44c4-402d-818e-86da866eb4b4&Region_id=&Issue_id=&MonthDisplay=0&YearDisplay=2007&x=12&y=13',
      'http://lott.senate.gov/public/index.cfm?FuseAction=PressOffice.PressReleases&ContentRecordType_id=b30084ac-44c4-402d-818e-86da866eb4b4&Region_id=&Issue_id=&MonthDisplay=0&YearDisplay=2006&x=12&y=13',
      'http://lott.senate.gov/public/index.cfm?FuseAction=PressOffice.PressReleases&ContentRecordType_id=b30084ac-44c4-402d-818e-86da866eb4b4&Region_id=&Issue_id=&MonthDisplay=0&YearDisplay=2005&x=12&y=13',
      'http://lott.senate.gov/public/index.cfm?FuseAction=PressOffice.PressReleases&ContentRecordType_id=b30084ac-44c4-402d-818e-86da866eb4b4&Region_id=&Issue_id=&MonthDisplay=0&YearDisplay=2004&x=12&y=13',
      'http://lott.senate.gov/public/index.cfm?FuseAction=PressOffice.PressReleases&ContentRecordType_id=b30084ac-44c4-402d-818e-86da866eb4b4&Region_id=&Issue_id=&MonthDisplay=0&YearDisplay=2003&x=12&y=13']


for j in range(0, len(html)):
    out = urlopen(html[j]).read()
    soup = BeautifulSoup(out)
    res  = soup.findAll('a')
    fr= []
    for k in range(len(res)):
        if res[k].has_key('href'):
            ab = res[k]['href']
            ab = ab.strip('..')
            ba = re.findall('_id', str(ab))
            if len(ba)>0 :
                fr.append(ab.encode('UTF-8'))
    ps= soup.findAll('h3')
    date=[]
    for m in range(len(ps)):
        if ps[m].has_key('class'):
            if ps[m]['class']=='ContentGrid':
                date.append(utilities.clean_html(str(ps[m])))


    store = ''
    for num in range(len(fr)):
        store += 'http://lott.senate.gov/public/' + fr[num] + '\n'
    fr = store.split('\n')
    fr.remove('')


    for num in range(len(fr)-2):
        test = urlopen(fr[num]).read()
        soup2 = BeautifulSoup(test)
        abd= soup2.findAll('a')
        for k in range(len(abd)):
            abd[k].extract()
        aboption = soup2.findAll('option')
        for k in range(len(aboption)):
            aboption[k].extract()
        h1s= soup2.findAll('h1')
        h3s = soup2.findAll('h3')
        for k in range(len(h1s)):
            h1s[k].extract()
        for k in range(len(h3s)):
            h3s[k].extract()
        stores = utilities.clean_html(str(soup2))
        stores = re.sub('\W', ' ', stores)
        mint= date[num]
        mint= re.sub('\W', '', mint)
        names = 'Lott' + str(num) + mint + '.txt'
        files = open(names, 'w')
        files.write(stores)
        files.close()    
