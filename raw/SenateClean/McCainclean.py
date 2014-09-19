##cleaning McCain's files


import os, re

os.chdir('C:\CongressPressExpand\McCain')

get_files = os.listdir(os.getcwd())



quant1 = 'United States Senator John McCain    Press Office'
quant2 = 'Search'
quant3 = 'Related Links'
quant4 = 'Press Releases                        Filter by'
quant5 = 'United States Senate  241 Russell Senate'
quant6 = 'Ofc  Bldg  Washington  DC 20510'
quant7 = 'Main   202  224 2235  Fax   202  228 2862'


for k in range(len(get_files)):
    temp = open(get_files[k], 'r')
    temp = temp.readlines()

    temp = temp[0]

    temp = re.sub(quant1, '', temp)
    temp = re.sub(quant2,'', temp)
    temp = re.sub(quant3, '', temp)
    temp = re.sub(quant4,'', temp)
    temp = re.sub(quant5,'', temp)
    temp = re.sub(quant6, '', temp)
    temp = re.sub(quant7,'', temp)
    
    test = open(get_files[k], 'w')

    test.write(temp)
    test.close()
