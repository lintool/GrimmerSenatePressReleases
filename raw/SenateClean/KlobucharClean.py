##this file cleans Klobuchar's press releases


import re, os



os.chdir('C:\CongressPressExpand\Klobuchar')

get_files = os.listdir(os.getcwd())








quant1 = 'Senator Amy Klobuchar'
quant2 = 'News Releases'
quant3 = 'Working for the People of Minnesota'
quant4 = 'Sign Up for Our E Newsletter'
quant5 = 'Press Contact Linden ZakulaPress Secretary 202  224 2159'
quant6 = 'News Releases'

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

    test = open(get_files[k], 'w')

    test.write(temp)
    test.close()

