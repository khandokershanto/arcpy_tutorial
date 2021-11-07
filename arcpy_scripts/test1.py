import arcpy


arcpy.env.overwriteOutput = 'True'
arcpy.env.workspace = r"H:\arcpy_arcgispro\data"
feature_list = arcpy.ListFeatureClasses()
print(feature_list)

points = r"H:\arcpy_arcgispro\data\ne_10m_populated_places.shp"
countries = r"H:\arcpy_arcgispro\data\ne_10m_admin_0_countries.shp"
outpath = r"H:\arcpy_arcgispro\output"

countries_interest = {'United States','Italy','France','Jordan','Kenya','Lebanon','Scotland'}

arcpy.MakeFeatureLayer_management(points,'points_layer',)

for i in countries_interest:
    print(i)
    arcpy.MakeFeatureLayer_management(countries,'countries_layer', """ "NAME_LONG" = '{}' """.format(i))
    arcpy.SelectLayerByLocation_management('points_layer', 'WITHIN', 'countries_layer')
    arcpy.FeatureClassToFeatureClass_conversion('points_layer', outpath, '{}_cities'.format(i))
