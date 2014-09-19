##this file creates the text files for the expanded
##data set located in CongressPressLN

##first loading the proper libraries

import re , os

##now we want to change the directory

os.chdir('C:/CongressPressLN/')

##alright now we will put together the directories

ester = os.listdir(os.getcwd())

base = 'C:/CongressPressLN/'

##now, let's put together the folders

folders= []
for k in range(len(ester)):
    folders.append(base + ester[k])

##alright, iterating through the folders

month_key = {}
month_key['January'] = 'Jan'
month_key['February'] = 'Feb'
month_key['March'] = 'Mar'
month_key['April'] = 'Apr'
month_key['May'] = 'May'
month_key['June'] = 'Jun'
month_key['July'] = 'Jul'
month_key['August'] = 'Aug'
month_key['September'] = 'Sep'
month_key['October'] = 'Oct'
month_key['November'] = 'Nov'
month_key['December'] = 'Dec'


tots = range(2, 120)
tots.append(121)

for j in tots:
    os.chdir(folders[j])
    listdir = os.listdir(os.getcwd())
    for m in range(len(listdir)):
        espn = listdir[m].split('.')
        if espn[1]=='txt':
            temps = open(listdir[m], 'r')
            temps = temps.readlines()
            break_lines = []
            for k in range(len(temps)):
                abc = re.findall('[0-9]+\sof\s[0-9]+\sDOCUMENTS', temps[k])
                if len(abc)>0:
                   break_lines.append(k)
            stops = []
            for k in range(len(temps)):
                abc = re.findall('Copyright\s[0-9][0-9][0-9][0-9]\sHT\sMedia', temps[k])
                if len(abc)>0:
                    stops.append(k)
            ##putting the files and dates together
            for num in range(len(break_lines)):
                lines= temps[break_lines[num]:stops[num]]
                temp = lines[5].strip(' ')
                dates = temp.split(' ')
                mons = month_key[dates[0]]
                days = re.sub(',', '', dates[1])
                year = dates[2]
                date_final = days + mons + year
                stores = lines[7]
                for k in range(16, len(lines)-7):
                    stores += lines[k] + ' '
                name = date_final + ester[j] + str(num) + '.txt'
                files = file(name, 'w')
                files.write(stores)
                files.close()
                
                
