def get_workspace(featureClass):
    catalogPath = os.path.dirname(featureClass.catalogPath)
    if arcpy.Describe(catalogPath).dataType == 'FeatureDataset':
        arcpy.env.workspace = arcpy.Describe(catalogPath).path
    else:
        arcpy.env.workspace = featureClass.path
    return arcpy.env.workspace
get_workspace(descFC)
