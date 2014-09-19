##cleaning obama's press releases


import re, os


os.chdir('C:\CongressPressExpand\Obama')

get_files = os.listdir(os.getcwd())


quant1= 'Washington D C  Office 713 Hart Senate Office Building'
quant2 = 'Washington  D C  20510'
quant3 = '202  224 2854'
quant4 = '202  228 4260 fax'
quant5 = '202 228 1404 TDD'
quant6 = 'Chicago Office John C  Kluczynski Federal Office Building'
quant7 = '230 South Dearborn St   Suite 3900  39th floor'
quant8 = 'Chicago  Illinois 60604'
quant9 = '312  886 3506'
quant10 = '312  886 3514 fax'
quant11 = 'Toll free   866  445 2520'
quant12 = 'for IL residents only    Springfield Office 607 East Adams Street'
quant13 = 'Springfield  Illinois 62701'
quant14 = '217  492 5089   217  492 5099 fax'
quant15 = 'Marion Office 701 North Court Street  Marion  Illinois 62959'
quant16 = '618  997 2402   618  997 2850 fax'
quant17 = 'Moline Office 1911 52nd Avenue  Moline  Illinois  61265'
quant18 = '309 736 1217   309 736 1233 fax'


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


    test = open(get_files[k], 'w')

    test.write(temp)
    test.close()


