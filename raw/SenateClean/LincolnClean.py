##putting together the clean file for Lincoln


import os, re

os.chdir('C:\CongressPressExpand\Lincoln')

get_files = os.listdir(os.getcwd())



quant1 = 'Constituent Services'
quant2 = 'Constituent Information'
quant3 = 'Legislative Activities'
quant4 = 'Sponsored    Co Sponsored'
quant5 = '359 Dirksen Senate Office Building  Washington D C  20510'
quant6 = 'Phone  202  224 4843 Fax  202  228 1371'
quant7 = '355 Dirksen Senate Office Building'
quant8 = 'Washington  DC 20510'
quant9 = '202  224 4843'
quant10 = 'Fax  202  228 1371'
quant11 = '912 West Fourth St'
quant12 = 'Little Rock  AR 72201'
quant13 = '501  375 2993'
quant14 = 'Fax  501  375 7064'
quant15 = 'Toll Free 1 800 352 9364' 


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
    temp = re.sub(quant15, '', temp)


    test = open(get_files[k], 'w')

    test.write(temp)
    test.close()
