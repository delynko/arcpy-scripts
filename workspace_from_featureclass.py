import arcpy
import os

def get_workspace(featureClass):
    descFC = arcpy.Describe(featureClass)
    catalogPath = os.path.dirname(descFC.catalogPath)
    if arcpy.Describe(catalogPath).dataType == 'FeatureDataset':
        arcpy.env.workspace = arcpy.Describe(catalogPath).path
    else:
        arcpy.env.workspace = descFC.path
    return arcpy.env.workspace
