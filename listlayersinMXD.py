import arcpy
import time
import os
import csv

arcpy.env.overwriteOutput = True

# set path of mxd inside parentheses
mxd = arcpy.mapping.MapDocument(r'.mxd')
lyrs = arcpy.mapping.ListLayers(mxd)

# set path of csv file to be created
csvFile = r".csv"

lyrName = []
lyrSrce = []

for lyr in lyrs:
    if lyr.supports("DATASOURCE"):
        name = lyr.name
        srce = lyr.dataSource
        lyrName.append(name)
        lyrSrce.append(srce)

with open(str(csvFile), 'wb') as myfile:
    wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
    wr.writerow(["Layer", "Source"])
    wr.writerows(zip(lyrName, lyrSrce))
myfile.close()

del mxd
time.sleep(5)
os.system("start " + csvFile)
