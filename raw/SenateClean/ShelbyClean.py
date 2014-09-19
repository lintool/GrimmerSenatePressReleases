import re, os


os.chdir('C:\CongressPressExpand\Shelby')

get_files = os.listdir(os.getcwd())

quant1 = 'Browse by       Month'
quant2 = 'January February March April May June July August September October November December'
quant3 = '2001 2002 2003 2004 2005 2006 2007 2008'
quant4 = 'Autauga Baldwin Barbour Bibb Blount Bullock Butler Calhoun Chambers Cherokee Chilton Choctaw Clarke Clay Cleburne Coffee Colbert Conecuh Coosa Covington Crenshaw Cullman Dale Dallas DeKalb Elmore Escambia Etowah Fayette Franklin Geneva Greene Hale Henry Houston Jackson Jefferson Lamar Lauderdale Lawrence Lee Limestone Lowndes Macon Madison Marengo Marion Marshall Mobile Monroe Montgomery Morgan Perry Pickens Pike Randolph Russell Shelby St  Clair Sumter Talladega Tallapoosa Tuscaloosa Walker Washington Wilcox Winston'
quant5 =  '110 Hart Senate Office Building'
quant6 = 'Washington  DC 20510'
quant7 = 'Tel   202  224 5744'
quant8 = 'Huntsville      1000 Glenn Hearn Boulevard  20127'
quant9 = 'Huntsville  AL 35824'
quant10 = 'Tel   256  772 0460'
quant11 = 'Birmingham      1800 5th Avenue North'
quant12 = '321 Federal Building     Birmingham  AL 35203'
quant13 = 'Tel   205  731 1384'
quant14 = 'Tuscaloosa      1118 Greensboro Avenue'
quant15 = 'Room 240     Tuscaloosa  AL 35401'
quant16 = 'Tel   205  759 5047'
quant17 = 'Montgomery      15 Lee Street'
quant18 = 'B 28 Federal Courthouse  Suite 208'
quant19 = 'Montgomery  AL 36104'
quant20 = 'Tel   334  223 7303'
quant21 = 'Mobile      113 St  Joseph Street'
quant22 = '445 U S  Federal Courthouse     Mobile  AL 36602'
quant23 = 'Tel   251  694 4164'

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
    temp = re.sub(quant19,'', temp)
    temp = re.sub(quant20, '', temp)
    temp = re.sub(quant21, '', temp)
    temp = re.sub(quant22, '', temp)
    temp = re.sub(quant23, '', temp)
    
    test = open(get_files[k], 'w')

    test.write(temp)
    test.close()
