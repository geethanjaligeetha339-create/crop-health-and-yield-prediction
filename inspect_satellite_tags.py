import rasterio

file = "dataset/yield_satImagery/2016-08-04.tif"

with rasterio.open(file) as src:
    print("File:", file)
    print("\nDataset tags:")
    print(src.tags())

    for i in range(1, src.count + 1):
        print(f"\nBand {i} tags:")
        print(src.tags(i))

    print("\nColor interpretation:")
    print(src.colorinterp)

    print("\nData types:")
    print(src.dtypes)
