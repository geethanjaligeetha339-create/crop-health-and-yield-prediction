import rasterio

file = "dataset/yield_satImagery/2018-08-04.tif"

with rasterio.open(file) as src:

    print("Number of bands:", src.count)

    for band_number in range(1, src.count + 1):

        band = src.read(band_number)

        print(
            "Band", band_number,
            "| Minimum:", band.min(),
            "| Maximum:", band.max(),
            "| Mean:", band.mean()
        )