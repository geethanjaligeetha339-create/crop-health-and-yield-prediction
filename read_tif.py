import rasterio
import numpy as np

file_path = "dataset/yield_satImagery/2016-08-04.tif"

with rasterio.open(file_path) as src:
    print("Bands:", src.count)
    print("Dimensions:", src.width, "x", src.height)
    print("NoData value:", src.nodata)

    for band in range(1, src.count + 1):
        data = src.read(band, masked=True)
        valid = data.compressed()

        print(f"\n--- Band {band} ---")
        print("Valid pixels:", len(valid))
        print("Missing pixels:", data.size - len(valid))

        if len(valid) > 0:
            print("First 10 valid values:", valid[:10])
            print("Minimum:", valid.min())
            print("Maximum:", valid.max())
            print("Mean:", valid.mean())
        else:
            print("No valid pixels found.")
