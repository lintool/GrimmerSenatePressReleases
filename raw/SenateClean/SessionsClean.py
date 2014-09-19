import re, os


os.chdir('C:\CongressPressExpand\Sessions')

get_files = os.listdir(os.getcwd())




quant1 = 'U S  Senator Jeff Sessions  Republican   ALABAMA'
quant2 = 'Constituent Services'
quant3 = 'Legislative Resources'
quant4 = 'Press Room'
quant5 = 'Important Links'
quant6 = 'Press Release        of        Senator Sessions'



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
