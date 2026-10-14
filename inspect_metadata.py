import rasterio

file = "dataset/yield_satImagery/2016-08-04.tif"

with rasterio.open(file) as src:
    print("Driver:", src.driver)
    print("Data type:", src.dtypes)
    print("Scale:", src.scales)
    print("Offset:", src.offsets)
    print("Color interpretation:", src.colorinterp)
    print("Band descriptions:", src.descriptions)
    print("Metadata namespaces:", src.tag_namespaces())

    for ns in src.tag_namespaces():
        print(f"\nMetadata for {ns}:")
        print(src.tags(ns=ns))
