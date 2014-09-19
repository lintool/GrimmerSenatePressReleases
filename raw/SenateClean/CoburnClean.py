##this file clean's tom Coburn's press releases

import re, os

os.chdir('C:\CongressPressExpand\Coburn')

get_files = os.listdir(os.getcwd())



quant1 = ' United States Senator Tom Coburn'
quant6  = 'Press Room'
quant2 = 'Filter by'
quant3 = 'Browse by'
quant4 = 'Current record'
quant5 = '9 488 538 958 770 00      31 090 19 Per Citizen'


for k in range(len(get_files)):
    temp = open(get_files[k], 'r')
    temp = temp.readlines()

    temp = temp[0]

    temp = re.sub(quant1, '', temp)
    temp = re.sub(quant2,'', temp)
    temp = re.sub(quant3, '', temp)
    temp = re.sub(quant4, '', temp)
    temp = re.sub(quant5, '', temp)
    tem = re.sub(quant6, '', temp)
    test = open(get_files[k], 'w')

    test.write(temp)
    test.close()
