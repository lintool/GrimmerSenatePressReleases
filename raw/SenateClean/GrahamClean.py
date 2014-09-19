##this file cleans Graham's press releases



import re, os

os.chdir('C:\CongressPressExpand\Graham')

get_files = os.listdir(os.getcwd())


quant1 = 'United States Senator Lindsey Graham  South Carolina'
quant2 = 'Press Room'
quant3 = 'Washington Office 290 Russell Senate Office Building'
quant4 = 'Washington  DC 20510'
quant5 = '202  224 5972'
quant6 = 'Press Room Press Releases'
quant7 = 'Filter by'
quant8 = 'You will need to have Real One Player installed on your computer to be able to listen or watch the clips above  Real One Player is free software that lets you play audio and video files'
quant9 = 'Upstate Regional Office'
quant10= '101 East Washington Street'
quant11 = 'Suite 220'
quant12 = 'Greenville'
quant13 = '864  250 1417'
quant14 = 'Midlands Regional Office'
quant15 = '508 Hampton Street'
quant16 = 'Suite 202'
quant17 = 'Columbia               803  933 0112'
quant18 = 'Pee Dee Regional Office'
quant19 = 'McMillan Federal Building'
quant20 = '401 West Evans Street  Suite 226B'
quant21 = 'Florence               843  669 1505'
quant22 = 'Lowcountry Regional Office'
quant23 = '530 Johnnie Dodds Boulevard  Suite 202'
quant24 = 'Mt  Pleasant               843  849 3887'
quant25 = 'Piedmont Regional Office'
quant26 = '140 East Main Street  Suite 110'
quant27 = 'Rock Hill               803  366 2828'
quant28 = '530 Johnnie Dodds Boulevard'


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
    temp = re.sub(quant11, '', temp)
    temp = re.sub(quant12, '', temp)
    temp = re.sub(quant13, '', temp)
    temp = re.sub(quant14, '', temp)
    temp = re.sub(quant15, '', temp)
    temp = re.sub(quant16, '', temp)
    temp = re.sub(quant17, '', temp)
    temp = re.sub(quant18, '', temp)
    temp = re.sub(quant19, '', temp)
    temp = re.sub(quant20, '', temp)
    temp = re.sub(quant21, '', temp)
    temp = re.sub(quant22, '', temp)
    temp = re.sub(quant23, '', temp)
    temp = re.sub(quant24 , '', temp)
    temp = re.sub(quant25, '', temp)
    temp = re.sub(quant26, '', temp)
    temp = re.sub(quant27 , '', temp)
    temp = re.sub(quant28, '', temp)
    test = open(get_files[k], 'w')

    test.write(temp)
    test.close()
