import rasterio
import numpy as np

file = "dataset/yield_satImagery/2016-08-04.tif"

with rasterio.open(file) as src:
    print("Satellite file:", file)
    print("Number of bands:", src.count)
    print("Image dimensions:", src.width, "x", src.height)
    print("CRS:", src.crs)
    print("NoData value:", src.nodata)

    print("\nBand descriptions:", src.descriptions)
    print("\nSatellite metadata:")
    print(src.tags())

    for i in range(1, src.count + 1):
        band = src.read(i, masked=True)
        values = band.compressed()

        if values.size > 0:
            print(
                f"Band {i}: "
                f"Min={values.min():.4f}, "
                f"Max={values.max():.4f}, "
                f"Mean={values.mean():.4f}"
            )
        else:
            print(f"Band {i}: No valid pixels")
