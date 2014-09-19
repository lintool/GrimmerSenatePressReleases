
##This file cleans lautenberg's press releases


import re, os



os.chdir('C:\CongressPressExpand\Lautenberg')

get_files = os.listdir(os.getcwd())





quant1 = 'Contacts   One Gateway Center'
quant2 = 'Twenty Third Floor  Newark  NJ 07102'
quant3 = 'Phone   973  639 8700  Toll Free  1 888 398 1642'
quant4 = 'Fax   973  639 8723  One Port Center Suite 505  Fifth Floor'
quant5 = '2 Riverside Drive Camden  NJ 08101 Phone   856  338 8922 Fax'
quant6 = '856  338 8936     Hart Senate Office Building    Suite 324'
quant7 = 'Washington  DC 20510    Phone   202  224 3224'
quant8 = 'TTY   202  224 2087 Fax   202  228 4054'
quant9 = 'Search                  Newsroom  Press Releases'





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
    temp = re.sub(quant7, '', temp)
    temp = re.sub(quant8, '', temp)
    temp = re.sub(quant9, '', temp)

    test = open(get_files[k], 'w')

    test.write(temp)
    test.close()





     
