import rasterio
import numpy as np
from pathlib import Path

folder = Path("dataset/yield_satImagery")

for path in sorted(folder.glob("*.tif")):
    print("\n" + "=" * 45)
    print("FILE:", path.name)

    with rasterio.open(path) as src:
        print("Band count:", src.count)
        print("Dimensions:", src.width, "x", src.height)
        print("Descriptions:", src.descriptions)

        for i in range(1, src.count + 1):
            band = src.read(i, masked=True)
            values = band.compressed()

            if values.size:
                print(
                    f"Band {i:2}: "
                    f"min={values.min():.2f}, "
                    f"max={values.max():.2f}, "
                    f"mean={values.mean():.2f}"
                )
