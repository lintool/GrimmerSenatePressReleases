##cleaning martinez's files


import os, re

os.chdir('C:\CongressPressExpand\Martinez')

get_files = os.listdir(os.getcwd())


quant1 = 'United States Senator Mel Martinez    News Releases'
quant2 = 'United States Senate  356 Russell Senate Office Building'
quant3 = 'Washington  DC 20510'
quant4 = 'Main   202  224 3041'
quant5 = 'Toll free   866  630 7106'
quant6 = 'Fax   202  228 5171'
quant7 = 'TTY   407  254 5548'


for k in range(len(get_files)):
    temp = open(get_files[k], 'r')
    temp = temp.readlines()

    temp = temp[0]

    temp = re.sub(quant1, '', temp)
    temp = re.sub(quant2,'', temp)
    temp = re.sub(quant3, '', temp)
    temp = re.sub(quant4,'', temp)
    temp = re.sub(quant5,'', temp)
    temp = re.sub(quant6, '', temp)
    temp = re.sub(quant7,'', temp)
    
    test = open(get_files[k], 'w')

    test.write(temp)
    test.close()
