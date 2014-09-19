import re, os
from nltk import utilities
from BeautifulSoup import BeautifulSoup
from urllib import urlopen



os.chdir('c:\CongressPress\Cantwell')

html=['http://cantwell.senate.gov/news/topics.cfm?code=aging&&type=false',
      'http://cantwell.senate.gov/news/topics.cfm?maxrows=38&startrow=1&&type=false&code=Agriculture',
      'http://cantwell.senate.gov/news/topics.cfm?code=arts&&type=false',
      'http://cantwell.senate.gov/news/topics.cfm?code=campaignelections&&type=false',
      'http://cantwell.senate.gov/news/topics.cfm?code=choice&&type=false',
      'http://cantwell.senate.gov/news/topics.cfm?code=civilrightsliberties&&type=false',
      'http://cantwell.senate.gov/news/topics.cfm?maxrows=65&startrow=1&&type=false&code=defense',
      'http://cantwell.senate.gov/news/topics.cfm?code=economy&&type=false',
      'http://cantwell.senate.gov/news/topics.cfm?maxrows=39&startrow=1&&type=false&code=education',
      'http://cantwell.senate.gov/news/topics.cfm?maxrows=94&startrow=1&&type=false&code=healthgeneral',
      'http://cantwell.senate.gov/news/topics.cfm?maxrows=78&startrow=1&&type=false&code=homelandsecurity',
      'http://cantwell.senate.gov/news/topics.cfm?code=housing&&type=false',
      'http://cantwell.senate.gov/news/topics.cfm?code=immigration&&type=false',
      'http://cantwell.senate.gov/news/topics.cfm?code=nativeamericanissues&&type=false',
      'http://cantwell.senate.gov/news/topics.cfm?maxrows=32&startrow=1&&type=false&code=judicialissues',
      'http://cantwell.senate.gov/news/topics.cfm?maxrows=121&startrow=1&&type=false&code=labor',
      'http://cantwell.senate.gov/news/topics.cfm?maxrows=83&startrow=1&&type=false&code=LawEnforcementFirstResponders',
      'http://cantwell.senate.gov/news/topics.cfm?maxrows=38&startrow=1&&type=false&code=medicaremedicaid',
      'http://cantwell.senate.gov/news/topics.cfm?maxrows=100&startrow=1&&type=false&code=misc',
      'http://cantwell.senate.gov/news/topics.cfm?code=MondayMemo&&type=false',
      'http://cantwell.senate.gov/news/topics.cfm?code=FEMA&&type=false',
      'http://cantwell.senate.gov/news/topics.cfm?code=smallbusiness&&type=false',
      'http://cantwell.senate.gov/news/topics.cfm?code=ss1&&type=false',
      'http://cantwell.senate.gov/news/topics.cfm?code=sports&&type=false',
      'http://cantwell.senate.gov/news/topics.cfm?maxrows=60&startrow=1&&type=false&code=taxbankingfinance',
      'http://cantwell.senate.gov/news/topics.cfm?maxrows=52&startrow=1&&type=false&code=technology',
      'http://cantwell.senate.gov/news/topics.cfm?code=telecom&&type=false',
      'http://cantwell.senate.gov/news/topics.cfm?maxrows=33&startrow=1&&type=false&code=trade',
      'http://cantwell.senate.gov/news/topics.cfm?maxrows=40&startrow=1&&type=false&code=transportation',
      'http://cantwell.senate.gov/news/topics.cfm?code=veterans&&type=false',
      'http://cantwell.senate.gov/news/topics.cfm?code=welfare&&type=false',
      'http://cantwell.senate.gov/news/topics.cfm?code=womensissues&&type=false']


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

        a= 0
        date=[]
        ps = soup.findAll('span')
        for m in range(len(ps)):
            if ps[m].has_key('class'):
                if ps[m]['class']=='pressappSmallText':
                    a+=1
                    if a>2:
                        date.append(utilities.clean_html(str(ps[m])))

        store = ''
        for num in range(len(fr)):
            store += 'http://cantwell.senate.gov/news/' + fr[num] + '\n'
        fr = store.split('\n')
        fr.remove('')


        for num in range(0,len(fr)):
                test = urlopen(fr[num]).read()
                soup2 = BeautifulSoup(test)
                abd= soup2.findAll('a')
                for k in range(len(abd)):
                    abd[k].extract()
                stores = utilities.clean_html(str(soup2))
                stores = re.sub('\W', ' ', stores)
                mint= date[num]
                mint= re.sub('\W', '', mint)
                names = str(num) + 'Cantwell'  + mint + '.txt'
                files = open(names, 'w')
                files.write(stores)
                files.close()
        
