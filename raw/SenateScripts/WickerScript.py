##this is the script for scrapping Roger Wickers pages

import re, os
from BeautifulSoup import BeautifulSoup
from nltk import utilities
from urllib import urlopen

os.chdir('C:\CongressPressLN\Wicker')

html= ['http://wicker.senate.gov/public/index.cfm?FuseAction=NewsRoom.PressReleases&ContentRecordType_id=b94acc28-404a-4fc6-b143-a9e15bf92da4&Region_id=&Issue_id=&MonthDisplay=1&YearDisplay=0&x=15&y=10',
       'http://wicker.senate.gov/public/index.cfm?FuseAction=NewsRoom.PressReleases&ContentRecordType_id=b94acc28-404a-4fc6-b143-a9e15bf92da4&Region_id=&Issue_id=&MonthDisplay=2&YearDisplay=0&x=15&y=10',
       'http://wicker.senate.gov/public/index.cfm?FuseAction=NewsRoom.PressReleases&ContentRecordType_id=b94acc28-404a-4fc6-b143-a9e15bf92da4&Region_id=&Issue_id=&MonthDisplay=3&YearDisplay=0&x=15&y=10',
       'http://wicker.senate.gov/public/index.cfm?FuseAction=NewsRoom.PressReleases&ContentRecordType_id=b94acc28-404a-4fc6-b143-a9e15bf92da4&Region_id=&Issue_id=&MonthDisplay=4&YearDisplay=0&x=15&y=10']

mon_key={}
mon_key[0]='Jan'
mon_key[1]='Feb'
mon_key[2]='Mar'
mon_key[3]='Apr'


for j in range(0,len(html)):
        out = urlopen(html[j]).read()
        soup = BeautifulSoup(out)
        res  = soup.findAll('a')
        fr= []
        mons = []
        days = []
        for k in range(len(res)):
            if res[k].has_key('href'):
                ab = res[k]['href']
                ba = re.findall('id', str(ab))
                if len(ba)>0 :
                    fr.append(ab.encode('UTF-8'))
                    mons.append(mon_key[j])
        h3s = soup.findAll('h3')
        for m in range(len(h3s)):
            if h3s[m].has_key('class'):
                if h3s[m]['class']=='ContentGrid':
                    abc = utilities.clean_html(str(h3s[m]))
                    abc = re.sub('[a-z][a-z]', '', str(abc))
                    abc = re.sub('\W', '', abc)
                    days.append(abc)
            
            
        store = ''
        for num in range(len(fr)):
            store += 'http://wicker.senate.gov/public/' + fr[num] + '\n'
        fr = store.split('\n')
        fr.remove('')
        


        for num in range(len(fr)):
            test = urlopen(fr[num]).read()
            soup2 = BeautifulSoup(test)
            abd = soup2.findAll('p')
            out = ''
            for k in range(len(abd)):
                abc = utilities.clean_html(str(abd[k]))
                out += str(abc)
            names = days[num] + mons[num] + '2008' +'Wicker' + str(num) + '.txt'
            files = open(names, 'w')
            files.write(out)
            files.close()
            
                
        

        
        
        
