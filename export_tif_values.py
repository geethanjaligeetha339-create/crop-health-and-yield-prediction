import rasterio
import pandas as pd
import numpy as np

file_path = "dataset/yield_satImagery/2016-08-04.tif"

with rasterio.open(file_path) as src:
    data = src.read(masked=True)
    rows = []

    for band in range(src.count):
        values = data[band].filled(np.nan)

        for row in range(src.height):
            for col in range(src.width):
                rows.append({
                    "Band": band + 1,
                    "Row": row,
                    "Column": col,
                    "Pixel_Value": values[row, col]
                })

df = pd.DataFrame(rows)
df.to_csv("tif_pixel_values_2016.csv", index=False)

print("Export completed!")
print("Total pixel records:", len(df))
print("Saved as tif_pixel_values_2016.csv")
print(df.head(20))
