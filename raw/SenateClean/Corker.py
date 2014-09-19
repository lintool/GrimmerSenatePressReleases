##cleans corke's press releases

import re, os

os.chdir('C:\CongressPressExpand\Corker')

get_files = os.listdir(os.getcwd())




quant1 = 'Senator Bob Corker   Press Release Detail'
quant2 = 'Press Release Detail     Press Releases'


for k in range(len(get_files)):
    temp = open(get_files[k], 'r')
    temp = temp.readlines()

    temp = temp[0]

    temp = re.sub(quant1, '', temp)
    temp = re.sub(quant2,'', temp)

    test = open(get_files[k], 'w')

    test.write(temp)
    test.close()
