import rasterio
import numpy as np

path = r"dataset\yield_satImagery\2016-08-04.tif"

with rasterio.open(path) as src:
    print("File:", path)
    print("Band count:", src.count)
    print("Dimensions:", src.width, "x", src.height)
    print("CRS:", src.crs)
    print("Descriptions:", src.descriptions)
    print("Dataset tags:", src.tags())

    for band_number in range(1, src.count + 1):
        band = src.read(band_number, masked=True)
        values = band.compressed()

        print(f"\nBand {band_number}")
        if values.size:
            print("  Min:", float(values.min()))
            print("  Max:", float(values.max()))
            print("  Mean:", float(values.mean()))
            print("  Standard deviation:", float(values.std()))
        else:
            print("  No valid pixels")
        print("  Tags:", src.tags(band_number))