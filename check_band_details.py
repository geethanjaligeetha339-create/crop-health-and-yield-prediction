import rasterio
import numpy as np

path = r"dataset\yield_satImagery\2016-08-04.tif"

with rasterio.open(path) as src:
    print("Band count:", src.count)
    print("Dimensions:", src.width, "x", src.height)
    print("CRS:", src.crs)
    print("Descriptions:", src.descriptions)
    print("Dataset tags:", src.tags())

    for i in range(1, src.count + 1):
        band = src.read(i, masked=True)
        values = band.compressed()

        print(f"\nBand {i}")
        if values.size:
            print("  Min:", float(values.min()))
            print("  Max:", float(values.max()))
            print("  Mean:", float(values.mean()))
            print("  Std:", float(values.std()))
        else:
            print("  No valid pixels")
        print("  Tags:", src.tags(i))
