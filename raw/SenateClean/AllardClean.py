##this cleans the Allard files

import os, re

os.chdir('C:\CongressPressExpand\Allard')

get_files = os.listdir(os.getcwd())
quant1 = 'United States Senator'
quant2 = 'Wayne Allard'
quant3 = 'My home page contains information about the U S  Senate  Colorado  how I may be of assistance to you as well as how to contact any one of my six offices  The next time I am in your neighborhood  I hope we can meet to discuss the issues important to you and your family  My staff and I look forward to hearing from you'
quant4 = 'THURSDAY JULY 24  2008'


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
