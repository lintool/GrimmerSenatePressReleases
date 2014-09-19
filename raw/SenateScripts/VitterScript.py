import re,os
from BeautifulSoup import BeautifulSoup
from nltk import utilities
from urllib import urlopen


os.chdir('C:\CongressPress\Vitter')


html=['http://vitter.senate.gov/?module=PressRoom/PressList&Month=0&Year=0']


for j in range(0, len(html)):
        out = urlopen(html[j]).read()
        soup = BeautifulSoup(out)
        res  = soup.findAll('a')
        fr= []
        for k in range(len(res)):
            if res[k].has_key('href'):
                ab = res[k]['href']
                ab = ab.strip('..')
                ba = re.findall('&ID', str(ab))
                if len(ba)>0 :
                    fr.append(ab.encode('UTF-8'))


        store = ''
        for num in range(len(fr)):
            store += 'http://vitter.senate.gov/' + fr[num] + '\n'
        fr = store.split('\n')
        fr.remove('')

        for num in range(182,len(fr)):
                    test = urlopen(fr[num]).read()
                    soup2 = BeautifulSoup(test)
                    stow= soup2.findAll('span')
                    for m in range(len(stow)):
                        if stow[m].has_key('class'):
                            if stow[m]['class']=='PressReleaseItemDate':
                                mint = utilities.clean_html(str(stow[m]))
                    stores = ''
                    p = soup2.findAll('p')
                    for k in range(1,len(p)-1):
                        stores += utilities.clean_html(str(p[k]))
                    stores = re.sub('\W', ' ', stores)
                    mint = re.sub('\W', '', mint)
                    names = str(num)  + 'Vitter' + mint + '.txt'
                    files = open(names, 'w')
                    files.write(stores)
                    files.close()
