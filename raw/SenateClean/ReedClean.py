##cleaning obama's press releases


import re, os


os.chdir('C:\CongressPressExpand\Reed')

get_files = os.listdir(os.getcwd())



quant1 = 'Senator Jack Reed              Skip to'
quant2 = 'United States Senator Jack Reed  Rhode Island'
quant3 = 'Adjust your text size'
quant4 = 'Page_Title Menu'

for k in range(len(get_files)):
    temp = open(get_files[k], 'r')
    temp = temp.readlines()

    temp = temp[0]

    temp = re.sub(quant1, '', temp)
    temp = re.sub(quant2,'', temp)
    temp = re.sub(quant3, '', temp)
    temp = re.sub(quant4, '', temp)

    test = open(get_files[k], 'w')

    test.write(temp)
    test.close()



