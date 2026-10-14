
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Load satellite pixel values
df = pd.read_csv("valid_tif_pixel_values_2016.csv")

# Display the first few records
print("First 10 pixel records:")
print(df.head(10))

print("\nColumns:")
print(df.columns.tolist())

# Check the available satellite bands
print("\nPixel count for each band:")
print(df["Band"].value_counts().sort_index())

# Visualize pixel values for each band
bands = sorted(df["Band"].unique())

fig, axes = plt.subplots(
    3, 4, figsize=(16, 10)
)

axes = axes.flatten()

for i, band in enumerate(bands):
    band_data = df[df["Band"] == band]

    image = band_data.pivot(
        index="Row",
        columns="Column",
        values="Pixel_Value"
    )

    axes[i].imshow(
        image,
        cmap="viridis",
        interpolation="nearest"
    )

    axes[i].set_title(f"Satellite Band {band}")
    axes[i].set_xlabel("Column")
    axes[i].set_ylabel("Row")

    plt.colorbar(
        axes[i].images[0],
        ax=axes[i],
        fraction=0.046
    )

# Hide unused subplot panels
for j in range(len(bands), len(axes)):
    axes[j].axis("off")

plt.tight_layout()
plt.savefig("satellite_bands_2016.png", dpi=300)
plt.show()

print("\nSaved: satellite_bands_2016.png")