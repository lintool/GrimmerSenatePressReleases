##this file cleans Kerry's press releases


import re, os



os.chdir('C:\CongressPressExpand\Kerry')

get_files = os.listdir(os.getcwd())





quant1 = 'Senator John Kerry s Online Office'
quant2 = 'Newsroom'
quant3 = 'Search Site'
quant4 = 'Offices Locations'
quant5 = 'Washington D C'
quant6 = '304 Russell Bldg'
quant7 = 'Third           Floor'
quant8 = 'Washington D C  20510'
quant9 = '202  224 2742 Boston'
quant10 = 'One Bowdoin Square'
quant11 = 'Tenth Floor'
quant12 = 'Boston  MA 02114'
quant13 = '617  565 8519 Springfield  Springfield Federal'
quant14 = 'Building            1550 Main Street'
quant15 = 'Suite 304            Springfield  MA 01101'
quant16 = '413  785 4610 Fall River'
quant17 = '222 Milliken Place'
quant18 = 'Suite 312            Fall River'
quant19 = 'Ma 02721             508  677 0522'
quant20 = 'At Work In Congress   Working For MA   How Can I Help           You'
quant21 = 'About John   MA Resources'
quant22 = 'Newsroom   Contact           Sitemap'
quant23 = 'Privacy Policy   TBA'


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


    test = open(get_files[k], 'w')

    test.write(temp)
    test.close()
