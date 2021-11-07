#                          ~ Search Cursor ~

import arcpy


arcpy.env.overwriteOutput = 'True'
arcpy.env.workspace = r"H:\arcpy_arcgispro\data"
feature_list = arcpy.ListFeatureClasses()
print(feature_list)

points = r"H:\arcpy_arcgispro\data\ne_10m_populated_places.shp"
countries = r"H:\arcpy_arcgispro\data\ne_10m_admin_0_countries.shp"
outpath = r"H:\arcpy_arcgispro\output"

with arcpy.da.SearchCursor(countries,['FID','SOVEREIGNT']) as countries_cursor:
    for x in countries_cursor:
        print(x[0])
        arcpy.MakeFeatureLayer_management(countries,'countries_layer', """ "FID" = '{}' """.format(x[0]))
