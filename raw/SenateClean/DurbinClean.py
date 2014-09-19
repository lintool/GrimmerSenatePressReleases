##This file cleans Durbin's press releases


import re, os



os.chdir('C:\CongressPressExpand\Durbin')

get_files = os.listdir(os.getcwd())


quant1 = 'WASHINGTON  D C'
quant2 = '309 Hart Senate Bldg'
quant3 = 'Washington  DC 20510'
quant4 = '9 am to 6 pm'
quant5 = '202  224 2152   ph'
quant6 = '202  228 0400'
quant7 = 'fx   CHICAGO'
quant8 = '230 S Dearborn St'
quant9 = 'Suite 3892'
quant10 = 'Chicago  IL 60604'
quant11 = '8 30 am to 5 pm'
quant12 = '312  353 4952   ph'
quant13 = '312  353 0150   fx'
quant14 = 'SPRINGFIELD'
quant15 = '525 South 8th St'
quant16 = 'Springfield  IL 62703'
quant17 = '8 30 am to 5 pm'
quant18 = '217  492 4062   ph'
quant19 = '217  492 4382   fx'
quant20 = 'MARION'
quant21= '701 N  Court St'
quant22 = 'Marion  IL 62959'
quant23 = '8 30 am to 5 pm'
quant24 = '618  998 8812   ph'
quant25 = '618  997 0176   fx'



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


    test = open(get_files[k], 'w')

    test.write(temp)
    test.close()
