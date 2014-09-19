import re, os
from nltk import utilities
from BeautifulSoup import BeautifulSoup
from urllib import urlopen




os.chdir('C:\CongressPress\Rockefeller')





html=['http://rockefeller.senate.gov/news/2007/pressreleases2007.htm']
##      'http://rockefeller.senate.gov/news/2006/pressreleases2006.htm',
##      'http://rockefeller.senate.gov/news/2005/pressreleases2005.htm',
##      'http://rockefeller.senate.gov/news/2004/pressreleases2004.htm',
##      'http://rockefeller.senate.gov/news/2003/pressrelease2003.htm',
##      'http://rockefeller.senate.gov/news/2002/pressreleases2002.htm',
##      'http://rockefeller.senate.gov/news/2001/pressreleases01.htm'
##      'http://rockefeller.senate.gov/news/2000/pressreleases00.html']



for j in range(0, len(html)):
        out = urlopen(html[j]).read()
        soup = BeautifulSoup(out)
        res  = soup.findAll('a')
        fr= []
        for k in range(len(res)):
            if res[k].has_key('href'):
                ab = res[k]['href']
                ab = ab.strip('..')
                ba = re.findall('pr\d\d\d\d\d\d\.html', str(ab))
                if len(ba)>0 :
                    fr.append(ab.encode('UTF-8'))

        store = ''
        ranges = range(2000,2008)
        for num in range(len(fr)):
                store += 'http://rockefeller.senate.gov/news/' + str(2007) + '/' + fr[num] + '\n'
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
                stow = soup2.findAll('td')
                for m in range(len(stow)):
                    if stow[m].has_key('align'):
                        if stow[m]['align']=='LEFT':
                            fret = utilities.clean_html(str(stow[m]))
                            fret2 = fret.split('\n')
                            mint = fret2[-1]
                mint = re.sub('\W', '', mint)

                names = str(num) + 'Rockefeller'  + mint + '.txt'
                files = open(names, 'w')
                files.write(stores)
                files.close()
