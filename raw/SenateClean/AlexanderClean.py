##this file is to attempt to remove any of the ``junk" from a senators
##files

import os, re
os.chdir('C:\CongressPressExpand\Alexander')

get_files = os.listdir(os.getcwd())


quant = 'United States Senator   Lamar Alexander   Press Releases'
quant2 = 'Browse by'
quant3 = 'current Press Release'
quant4 = 'Radio Clip'
quant5 = 'Television Clip'

for k in range(len(get_files)):
    temp = open(get_files[k], 'r')
    temp = temp.readlines()

    temp = temp[0]

    temp = re.sub(quant, '', temp)
    temp = re.sub(quant2,'', temp)
    temp = re.sub(quant3, '', temp)
    temp = re.sub(quant4, '', temp)
    temp = re.sub(quant5, '', temp)

    test = open(get_files[k], 'w')

    test.write(temp)
    test.close()
