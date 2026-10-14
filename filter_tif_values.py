import pandas as pd

df = pd.read_csv("tif_pixel_values_2016.csv")

valid = df.dropna(subset=["Pixel_Value"]).copy()

valid.to_csv("valid_tif_pixel_values_2016.csv", index=False)

print("Valid pixel records:", len(valid))
print("\nFirst 20 actual pixel values:")
print(valid.head(20).to_string(index=False))

print("\nSaved as valid_tif_pixel_values_2016.csv")
