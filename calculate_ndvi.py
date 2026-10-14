import rasterio
import numpy as np
import matplotlib.pyplot as plt

# Satellite image
file = "dataset/yield_satImagery/2018-08-04.tif"

# Open satellite image
with rasterio.open(file) as src:

    # Read Band 4 = Red
    red = src.read(4).astype(float)

    # Read Band 8 = Near Infrared
    nir = src.read(8).astype(float)

    # Get NoData value
    nodata = src.nodata

    print("NoData value:", nodata)

# Create mask for invalid pixels
invalid = red < -1e20

# Calculate NDVI
ndvi = np.full(red.shape, np.nan)

valid = ~invalid & ((nir + red) != 0)

ndvi[valid] = (nir[valid] - red[valid]) / (nir[valid] + red[valid])

# Print NDVI information
print("Minimum NDVI:", np.nanmin(ndvi))
print("Maximum NDVI:", np.nanmax(ndvi))
print("Mean NDVI:", np.nanmean(ndvi))

# Display NDVI
plt.figure(figsize=(8, 6))

plt.imshow(ndvi, cmap="RdYlGn", vmin=-1, vmax=1)

plt.colorbar(label="NDVI")

plt.title("Crop Health - NDVI 2018")

plt.xlabel("Pixel")
plt.ylabel("Pixel")

plt.show()