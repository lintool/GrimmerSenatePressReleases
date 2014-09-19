##this file cleans Collins' file

import re, os

os.chdir('C:\CongressPressExpand\Collins')

get_files = os.listdir(os.getcwd())




quant1 = 'United States Senator Susan M  Collins'
quant2 = 'Press Room'
quant3 = 'DC Office Information'
quant4 = '413 Dirksen Senate Office Building'
quant5 = 'Washington  DC 20510'
quant6 = 'Phone   202  224 2523'
quant7 = 'Fax   202  224 2693'
quant8 = 'Maine Offices'


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

    test = open(get_files[k], 'w')

    test.write(temp)
    test.close()
