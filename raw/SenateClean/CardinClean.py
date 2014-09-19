##this file cleans Cardin's file

import re, os

os.chdir('C:\CongressPressExpand\Cardin')

get_files = os.listdir(os.getcwd())



quant1 = 'Senator Benjamin L  Cardin   Maryland'
quant2 = 'Annapolis at night'
quant3 = 'Burnside Bridge at Antietam'
quant4 = 'Baltimore skyline'
quant5 = 'Great Falls on the Potomac'
quant6 = 'Flag lowering at Ft  McHenry'
quant7 = 'Beach at Ocean City'
quant8 = 'Farm near Sugarloaf Mountain'
quant9 = 'Search'
quant10 = 'Press Releases     Press Releases'
quant11 = 'Press Release        of        Senator Cardin'


for k in range(len(get_files)):
    temp = open(get_files[k], 'r')
    temp = temp.readlines()

    temp = temp[0]

    temp = re.sub(quant1, '', temp)
    temp = re.sub(quant2,'', temp)
    temp = re.sub(quant3, '', temp)
    temp = re.sub(quant4, '', temp)
    temp = re.sub(quant5, '', temp)
    temp = re.sub(quant6, '', temp)
    temp = re.sub(quant7, '', temp)
    temp = re.sub(quant8, '', temp)
    temp = re.sub(quant9, '', temp)
    temp = re.sub(quant10, '', temp)
    temp = re.sub(quant11, '', temp)

    test = open(get_files[k], 'w')

    test.write(temp)
    test.close()

    
