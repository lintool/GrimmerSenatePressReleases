##cleaning Lieberman's press releases




import os, re

os.chdir('C:\CongressPressExpand\Lieberman')

get_files = os.listdir(os.getcwd())

quant1 = 'Senator Joe Lieberman  News Release'
quant2 = 'FOR IMMEDIATE RELEASE'
quant3 =  'Rob Sawicki'
quant4 = 'Phone  202 224 4041'


for k in range(len(get_files)):
    temp = open(get_files[k], 'r')
    temp = temp.readlines()

    temp = temp[0]

    temp = re.sub(quant1, '', temp)
    temp = re.sub(quant2,'', temp)
    temp = re.sub(quant3, '', temp)
    temp = re.sub(quant4,'', temp)

    
    test = open(get_files[k], 'w')

    test.write(temp)
    test.close()
