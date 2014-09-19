##this is the lugar clean file


import re, os

quant1 = 'Richard G  Lugar  United States Senator for Indiana   Press Releases'

os.chdir('C:\CongressPressExpand\Lugar')

get_files = os.listdir(os.getcwd())


for k in range(len(get_files)):
    temp = open(get_files[k], 'r')
    temp = temp.readlines()

    temp = temp[0]

    temp = re.sub(quant1, '', temp)
    test = open(get_files[k], 'w')

    test.write(temp)
    test.close()
