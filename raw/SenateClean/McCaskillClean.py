##this file cleans Claire McCaskill's press releases


import re, os

os.chdir('C:\CongressPressExpand\McCaskill')

get_files = os.listdir(os.getcwd())


quant1 = 'Senator Claire McCaskill   Missouri                Newsroom'
quant2 = 'Get E mail Updates'
quant3 = 'Please sign up for periodic updates from Claire'
quant4 = 'Search                       Newsroom    Press Releases'



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
