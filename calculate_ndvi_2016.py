import rasterio
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

file = "dataset/yield_satImagery/2016-08-04.tif"

with rasterio.open(file) as src:
    red_ma = src.read(4, masked=True)
    nir_ma = src.read(8, masked=True)

    red = red_ma.filled(np.nan).astype(np.float32)
    nir = nir_ma.filled(np.nan).astype(np.float32)

    profile = src.profile.copy()

# Exclude NoData, invalid pixels, and zero denominators
valid = (
    ~np.ma.getmaskarray(red_ma)
    & ~np.ma.getmaskarray(nir_ma)
    & np.isfinite(red)
    & np.isfinite(nir)
    & ((nir + red) != 0)
)

ndvi = np.full(red.shape, np.nan, dtype=np.float32)
ndvi[valid] = (nir[valid] - red[valid]) / (nir[valid] + red[valid])

# Keep only physically valid NDVI values
valid &= (ndvi >= -1) & (ndvi <= 1)
ndvi[~valid] = np.nan

if not np.any(valid):
    raise ValueError("No valid NDVI pixels found. Check the band mapping and input data.")

print("NDVI calculation completed for 2016")
print("Valid pixels:", int(valid.sum()))
print("Minimum NDVI:", float(np.nanmin(ndvi)))
print("Maximum NDVI:", float(np.nanmax(ndvi)))
print("Mean NDVI:", float(np.nanmean(ndvi)))

# Save NDVI pixel values to CSV
rows, cols = np.where(valid)

df = pd.DataFrame({
    "Row": rows,
    "Column": cols,
    "NDVI": ndvi[valid]
})

df.to_csv("ndvi_2016.csv", index=False)
print("\nSaved: ndvi_2016.csv")

# Save NDVI as a georeferenced raster
profile.update(
    count=1,
    dtype="float32",
    nodata=-9999.0,
    compress="lzw"
)

with rasterio.open("ndvi_2016.tif", "w", **profile) as dst:
    dst.write(np.where(valid, ndvi, -9999.0).astype(np.float32), 1)

print("Saved: ndvi_2016.tif")

# Create NDVI visualization
plt.figure(figsize=(10, 7))

image = plt.imshow(
    np.ma.masked_invalid(ndvi),
    cmap="RdYlGn",
    vmin=-1,
    vmax=1
)

plt.colorbar(image, label="NDVI")
plt.title("Crop Vegetation Index (NDVI) - 2016")
plt.xlabel("Column")
plt.ylabel("Row")
plt.tight_layout()
plt.savefig("ndvi_map_2016.png", dpi=300)
plt.show()

print("Saved: ndvi_map_2016.png")
