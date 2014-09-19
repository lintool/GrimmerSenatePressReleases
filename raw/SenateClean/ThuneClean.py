import re, os


os.chdir('C:\CongressPressExpand\Thune')

get_files = os.listdir(os.getcwd())


quant1 = 'Washington Office   Senator John Thune  United States Senate'
quant2 = 'Washington  DC 20510'
quant3 = 'Phone   202  224 2321'
quant4 = 'Fax   202  228 5429'
quant5 = 'TollFree  1 866 850 3855'
quant6 = 'Sioux Falls Office'
quant7 = '320 North Main Avenue  Suite B'
quant8 = 'Sioux Falls  SD 57104'
quant9 = 'Phone   605  334 9596'
quant10 = 'Rapid City Office'
quant11 = '1313 West Main Street'
quant12 = 'Rapid City  SD 57701  Phone'
quant13 = '605  348 7551'
quant14 = 'Aberdeen Office'
quant15 = '320 South 1st Street'
quant16 = 'Suite 101  Aberdeen'
quant17 = 'SD 57401  Phone'
quant18 = '605  225 8823'


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
    temp = re.sub(quant11, '', temp)
    temp = re.sub(quant12, '', temp)
    temp = re.sub(quant13, '', temp)
    temp = re.sub(quant14,'', temp)
    temp = re.sub(quant15, '', temp)
    temp = re.sub(quant16, '', temp)
    temp = re.sub(quant17, '', temp)
    temp = re.sub(quant18, '', temp)
    
    test = open(get_files[k], 'w')

    test.write(temp)
    test.close()
