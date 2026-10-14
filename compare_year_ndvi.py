import rasterio
import numpy as np
from pathlib import Path

folder = Path("dataset/yield_satImagery")

for path in sorted(folder.glob("*.tif")):
    with rasterio.open(path) as src:
        red = src.read(4, masked=True)
        nir = src.read(8, masked=True)

        red_data = red.filled(np.nan).astype(np.float64)
        nir_data = nir.filled(np.nan).astype(np.float64)

        valid = (
            ~np.ma.getmaskarray(red)
            & ~np.ma.getmaskarray(nir)
            & np.isfinite(red_data)
            & np.isfinite(nir_data)
            & ((nir_data + red_data) != 0)
        )

        ndvi = np.full(red_data.shape, np.nan)
        ndvi[valid] = (
            (nir_data[valid] - red_data[valid])
            / (nir_data[valid] + red_data[valid])
        )

        valid &= (ndvi >= -1) & (ndvi <= 1)

        print(f"\n{path.name}")
        print("Valid pixels:", int(valid.sum()))

        if valid.any():
            print("Minimum NDVI:", float(np.nanmin(ndvi[valid])))
            print("Maximum NDVI:", float(np.nanmax(ndvi[valid])))
            print("Mean NDVI:", float(np.nanmean(ndvi[valid])))
