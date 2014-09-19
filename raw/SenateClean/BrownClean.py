##this cleans Brown's press relases

import os, re

os.chdir('C:\CongressPressExpand\Brown')

get_files = os.listdir(os.getcwd())



quant1 = 'Senator Sherrod Brown'
quant2 = 'Senator for Ohio'
quant3 = 'Press Releases'
quant4 = 'text size'
quant5 = 'Search'
quant6 = 'The Senator'
quant7 = 'For Ohioans'
quant8 = 'Newsroom'
quant9 = 'Issues'
quant10 = 'Agenda'
quant11= 'Press Contacts'
quant12 = '202  224 3978'
quant13 = 'Newsletter Sign up Enter your e mail address below to receive Senator Browns monthly eNewsletter'
quant14 = 'Senator Browns Offices'
quant15 = 'Washington D C'
quant16 = '455 Russell Senate'
quant17 = 'Office Bldg'
quant18 = 'Washington  DC 20510'
quant19 = 'p  202  224 2315'
quant20 = 'f  202  228 6321'
quant21 = 'Cleveland'
quant22 = '1301 East Ninth St   Suite 1710'
quant23 = 'Cleveland  Ohio 44114'
quant24 = 'p  216  522 7272'
quant25 = 'f  216  522 2239'
quant26 = 'Toll Free 1 888 896 OHIO  6446'
quant27 = 'Cincinnati'
quant28 = '425 Walnut Street  Suite 2310'
quant29 = 'Cincinnati  Ohio   45202'
quant30 = 'p  513  684 1021'
quant31 = 'f  513  684 1029'
quant32 = 'Toll Free 1 888 896 OHIO  6446'
quant33 = 'Columbus        200 N High St  Room 614'
quant34 = 'Columbus  OH 43215'
quant35 = 'p  614  469 2083'
quant36 = 'f  614  469 2171'
quant37 = 'Toll Free 1 888 896 OHIO  6446'
quant38 = 'Lorain        205 West 20th St  Suite M280'
quant39 = 'Lorain  OH 44052'
quant40 = 'p  440  242 4100'
quant41 = 'f  440  242 4108'
quant42 = 'Toll Free 1 888 896 OHIO  6446'
quant43 = 'Ohio 44114'
quant44 = 'Ohio   45202'


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
    temp = re.sub(quant27, '', temp)
    temp = re.sub(quant28, '', temp)
    temp = re.sub(quant29, '', temp)
    temp = re.sub(quant30, '', temp)
    temp = re.sub(quant31, '', temp)
    temp = re.sub(quant32, '', temp)
    temp = re.sub(quant33, '', temp)
    temp = re.sub(quant34, '', temp)
    temp = re.sub(quant35, '', temp)
    temp = re.sub(quant36, '', temp)
    temp = re.sub(quant37, '', temp)
    temp = re.sub(quant38 , '', temp)
    temp = re.sub(quant39, '', temp)
    temp = re.sub(quant40, '', temp)
    temp = re.sub(quant41, '', temp)
    temp = re.sub(quant42, '', temp)
    temp = re.sub(quant43, '', temp)
    temp = re.sub(quant44, '', temp)




    test = open(get_files[k], 'w')

    test.write(temp)
    test.close()
