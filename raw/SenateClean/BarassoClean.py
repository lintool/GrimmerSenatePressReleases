##this cleans the Barrasso file

import os, re

os.chdir('C:\CongressPressExpand\Barrasso')

get_files = os.listdir(os.getcwd())


quant1 = 'US Senator John Barrasso  R WY'
quant2 = 'Press Office'
quant3 = 'Washington'
quant4 = 'DC Office'
quant5 = '307 Dirksen Senate'
quant6 = 'Office Building'
quant7 = 'Washington  D C  20510'
quant8 = 'Phone  202 224 6441'
quant9 = 'Toll Free  866 235 9553'
quant10 = 'Fax  202 224 1724'
quant11 = 'Casper Office'
quant12 = '100 East B Street'
quant13 = 'Suite 2201'
quant14 = 'Casper  WY 82602'
quant15 = 'Main  307 261 6413  Cheyenne Office'
quant16 = '2120 Capitol Avenue'
quant17 = 'Suite 2013'
quant18 = 'Cheyenne  WY 82001'
quant19  = 'Main  307 772 2451'
quant20 = 'Press Releases Press Office'
quant21 = 'Browse by'
quant22 = 'Current record'
quant23 = 'This Home Page is maintained by the office of Senator John Barrasso  Please send comments to Pursuant to   newsletters  petitions  opinion polls and issue alerts and other electronic communications cannot be initiated by this office for the 60 day period immediately before the date of a primary or general election'
quant24 =  'D C  20510'

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
    
    test = open(get_files[k], 'w')

    test.write(temp)
    test.close()
