##this clean's kennedy's press releases



import re, os

os.chdir('C:\CongressPressExpand\Kennedy')

get_files = os.listdir(os.getcwd())




quant1 = 'Skip to Content'
quant2 = 'Washington Office'
quant3 = 'Massachusetts Office'
quant4 = 'Contact Senator Kennedy'


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
