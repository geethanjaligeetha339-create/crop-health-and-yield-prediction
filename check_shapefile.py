import geopandas as gpd

file = "dataset/yield2018/yield2018.shp"

# Read shapefile
gdf = gpd.read_file(file)

print("Columns:")
print(gdf.columns)

print("\nFirst 5 rows:")
print(gdf.head())

print("\nNumber of records:")
print(len(gdf))

print("\nCoordinate system:")
print(gdf.crs)