import rasterio
import numpy as np
import matplotlib.pyplot as plt


# Open satellite image
with rasterio.open("dataset/yield_satImagery/2018-08-04.tif") as src:

    # Sentinel-2 Band 4 = Red
    red = src.read(4).astype(float)

    # Sentinel-2 Band 8 = Near Infrared
    nir = src.read(8).astype(float)

    # Get NoData value
    nodata = src.nodata


# Calculate NDVI
ndvi = (nir - red) / (nir + red)


# Remove invalid values
if nodata is not None:
    ndvi[(red == nodata) | (nir == nodata)] = np.nan

ndvi[~np.isfinite(ndvi)] = np.nan


# Create NDVI map
plt.figure(figsize=(10, 7))

plt.imshow(
    ndvi,
    cmap="RdYlGn",
    vmin=0.0,
    vmax=1.0
)

plt.colorbar(label="NDVI")

plt.title("NDVI Map - 2018")

plt.xlabel("Pixel Column")
plt.ylabel("Pixel Row")

plt.tight_layout()

plt.savefig(
    "ndvi_map_2018.png",
    dpi=300
)

plt.show()

print("NDVI map created successfully!")
print("File: ndvi_map_2018.png")