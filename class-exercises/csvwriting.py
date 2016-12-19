import csv

import math
#open csvfile
csvf = open('triangles.csv', 'w')
#create csvwriter
csvw = csv.writer(csvf, delimiter=',')

#write to file
#a, b, hypotenuse
csvw.writerow(['a','b','Hypotenuse'])

#write numbers 1-100 into the first cell
for a in range(1, 101):
    #get all possible values of b
    for b in range(a, 101):
        hypotenuse = math.sqrt((a*a)+(b*b))
        csvw.writerow([a, b, hypotenuse])
    #write a row containing a, b
#close file
csvf.close()