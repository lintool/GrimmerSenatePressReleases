import os, re

os.chdir('C:\CongressPressExpand\Bayh')

get_files = os.listdir(os.getcwd())


quant1 = 'The e-mail address  has been successfully added to our subscription list.'


for k in range(len(get_files)):
    temp = open(get_files[k], 'r')
    temp = temp.readlines()

    temp = temp[0]

    temp = re.sub(quant1, '', temp)
    
    test = open(get_files[k], 'w')

    test.write(temp)
    test.close()





