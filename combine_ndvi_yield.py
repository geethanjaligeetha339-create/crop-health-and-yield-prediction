import rasterio
import geopandas as gpd
import numpy as np
import pandas as pd

# --------------------------------------------------
# 1. Open Sentinel-2 satellite image
# --------------------------------------------------

satellite_file = "dataset/yield_satImagery/2018-08-04.tif"

with rasterio.open(satellite_file) as src:

    print("Raster CRS:", src.crs)
    print("Number of bands:", src.count)
    print("Raster size:", src.width, "x", src.height)
    print("Raster bounds:", src.bounds)

    # Band 4 = Red
    red = src.read(4).astype(float)

    # Band 8 = Near Infrared
    nir = src.read(8).astype(float)

    raster_crs = src.crs
    transform = src.transform

# --------------------------------------------------
# 2. Calculate NDVI
# --------------------------------------------------

ndvi = np.full(red.shape, np.nan)

valid = (
    np.isfinite(red) &
    np.isfinite(nir) &
    ((nir + red) != 0)
)

ndvi[valid] = (
    (nir[valid] - red[valid]) /
    (nir[valid] + red[valid])
)

print("NDVI calculated successfully.")

print("NDVI minimum:", np.nanmin(ndvi))
print("NDVI maximum:", np.nanmax(ndvi))
print("NDVI mean:", np.nanmean(ndvi))

# --------------------------------------------------
# 3. Open yield shapefile
# --------------------------------------------------

yield_file = "dataset/yield2018/yield2018.shp"

gdf = gpd.read_file(yield_file)

print("\nYield records:", len(gdf))
print("Original CRS:", gdf.crs)

# Check geometry
print("\nGeometry types:")
print(gdf.geometry.geom_type.value_counts())

# --------------------------------------------------
# 4. Convert yield coordinates to satellite CRS
# --------------------------------------------------

if gdf.crs is None:
    raise ValueError(
        "Yield shapefile has no CRS. "
        "Set the correct original CRS before using to_crs()."
    )

print("Satellite CRS:", raster_crs)

gdf = gdf.to_crs(raster_crs)

print("Coordinates transformed successfully.")

# Check transformed bounds
print("\nYield bounds after CRS conversion:")
print(gdf.total_bounds)

# --------------------------------------------------
# 5. Extract NDVI at each yield location
# --------------------------------------------------

ndvi_values = []

for point in gdf.geometry:

    if point is None or point.is_empty:
        ndvi_values.append(np.nan)
        continue

    row, col = rasterio.transform.rowcol(
        transform,
        point.x,
        point.y
    )

    # Check whether point is inside image
    if (
        0 <= row < ndvi.shape[0] and
        0 <= col < ndvi.shape[1]
    ):
        value = ndvi[row, col]
    else:
        value = np.nan

    ndvi_values.append(value)

# --------------------------------------------------
# 6. Add NDVI to yield data
# --------------------------------------------------

gdf["NDVI"] = ndvi_values

print("\nNDVI extraction completed.")

print("Missing NDVI values:",
      gdf["NDVI"].isna().sum())

# --------------------------------------------------
# 7. Create ML dataset
# --------------------------------------------------

result = gdf[
    ["NUMBER", "YIELD", "HUMID", "NDVI"]
].copy()

# Remove missing NDVI
result = result.dropna(subset=["NDVI"])

# Remove invalid NDVI
result = result[
    (result["NDVI"] >= -1) &
    (result["NDVI"] <= 1)
]

# Remove missing yield values
result = result.dropna(subset=["YIELD"])

# --------------------------------------------------
# 8. Display final dataset
# --------------------------------------------------

print("\nFinal dataset:")
print(result.head())

print("\nDataset shape:")
print(result.shape)

print("\nNumber of usable records:",
      len(result))

print("\nDataset information:")
print(result.info())

# --------------------------------------------------
# 9. Save dataset
# --------------------------------------------------

output_file = "ndvi_yield_2018.csv"

result.to_csv(
    output_file,
    index=False
)

print("\nSaved successfully:")
print(output_file)