import arcpy
import os

#Folder containing gpx files
gpxFolder = r"C:/gpx_folder/"

#Output Folder
destinationFolder = r"Q:/dest_folder/"

#Folder containing the GPX files. ONLY HAVE GPx FILES IN THIS FOLDER! Remove the .zip file if it's here
fcs = os.listdir(gpxFolder)

for fc in fcs:
    #Rename the data path to the folder with the GPX files
    inp = os.path.join(gpxFolder, fc)
    #Rename the data path to the output folder
    output = (destinationFolder + fc + ".shp")
    arcpy.GPXtoFeatures_conversion(inp, output)
