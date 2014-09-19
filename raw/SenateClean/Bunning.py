##this clean's Bunning's press releases


import os, re

os.chdir('C:\CongressPressExpand\Bunning')

get_files=os.listdir(os.getcwd())

quant1 = 'United States Senator Jim Bunning'
quant2 = 'Kentucky   News Center'
quant3 = 'Related Links'
quant4 = 'News Center News Releases'
quant5 = 'News Center  News Releases'
quant6 = 'Filter by'
quant7 = 'Browse by'
quant8 = 'Washington  DC'
quant9 = 'Current record'
quant10 = 'You will need to have Real One Player installed on your computer to be able to listen or watch the clips above  Real One Player is free software that lets you play audio and video files'


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
    temp = re.sub(quant10, '', temp)

    test = open(get_files[k], 'w')

    test.write(temp)
    test.close()
    
