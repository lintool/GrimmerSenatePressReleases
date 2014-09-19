import re, os


os.chdir('C:\CongressPressExpand\Stevens')

get_files = os.listdir(os.getcwd())




quant1 = 'United States Senator Ted Stevens   Newsroom'
quant2 = 'RSS Feeds'
quant3 = 'Newsroom  Press Releases'
quant4 = 'Filter by'
quant5 = 'Current record'
quant6 = 'You will need to have Real One Player installed on your computer to be able to listen or watch the clips above  Real One Player is free software that lets you play audio and video files'
quant7 = 'Click on your region of interest'
quant8 = '522 Hart Senate Office Bldg  Washington  DC 20510'
quant9 = 'Phone   202  224 3004'
quant10 = 'Fax   202  224 2354'



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
    temp = re.sub(quant8,'', temp)
    temp = re.sub(quant9, '', temp)
    temp = re.sub(quant10, '', temp)
    
    test = open(get_files[k], 'w')

    test.write(temp)
    test.close()
