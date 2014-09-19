##cleaning Menendez's press releases

import re, os

os.chdir('C:\CongressPressExpand\Menendez')

get_files = os.listdir(os.getcwd())


quant1 = 'Senator Robert Menendez   Newsroom'
quant2 = 'SEARCH       OFFICE LOCATIONS'
quant3 = '317 Senate Hart Office Building'
quant4 = 'Washington  D C  20510'
quant5 = '202 224 4744  202 228 2197 fax'
quant6 = 'One Gateway Center'
quant7 = 'Suite 1100  Newark  New Jersey 07102'
quant8 = '973 645 3030'
quant9 = '973 645 0502 fax'
quant10 = '208 White Horse Pike  Suite 18'
quant11 = 'Barrington  New Jersey 08007'
quant12 = '856 757 5353'
quant13 = '856 546 1526 fax'
quant14 = 'Newsroom                                Press Release        of        Senator Menendez'



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
    temp = re.sub(quant12, '', temp)
    temp = re.sub(quant13, '', temp)
    temp = re.sub(quant14, '', temp)

    test = open(get_files[k], 'w')

    test.write(temp)
    test.close()


    
