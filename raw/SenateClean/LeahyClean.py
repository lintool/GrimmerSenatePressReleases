##patrick leahy's press releases


import os, re

os.chdir('C:\CongressPressExpand\Leahy')

get_files = os.listdir(os.getcwd())


quant1 = 'CONTACT  Office of Senator'
quant2 = 'Leahy  202 224 4242'


for k in range(len(get_files)):
    temp = open(get_files[k], 'r')
    temp = temp.readlines()

    temp = temp[0]

    temp = re.sub(quant1, '', temp)
    temp = re.sub(quant2,'', temp)

    test = open(get_files[k], 'w')

    test.write(temp)
    test.close()
