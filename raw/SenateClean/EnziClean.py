##this cleans Enzi's press releaess


import re, os



os.chdir('C:\CongressPressExpand\Enzi')

get_files = os.listdir(os.getcwd())


quant1= 'United States Senator Mike Enzi   News Room'
quant2 = 'Filter by'

for k in range(len(get_files)):
    temp = open(get_files[k], 'r')
    temp = temp.readlines()

    temp = temp[0]

    temp = re.sub(quant1, '', temp)
    temp = re.sub(quant2,'', temp)

    test = open(get_files[k], 'w')

    test.write(temp)
    test.close()
