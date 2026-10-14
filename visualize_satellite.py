import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("valid_tif_pixel_values_2016.csv")

bands = sorted(df["Band"].unique())

fig, axes = plt.subplots(3, 4, figsize=(16, 10))
axes = axes.flatten()

for i, band in enumerate(bands):
    band_data = df[df["Band"] == band]

    image = band_data.pivot(
        index="Row",
        columns="Column",
        values="Pixel_Value"
    )

    axes[i].imshow(image, cmap="viridis")
    axes[i].set_title(f"Satellite Band {band}")
    axes[i].set_xlabel("Column")
    axes[i].set_ylabel("Row")

    plt.colorbar(axes[i].images[0], ax=axes[i])

for j in range(len(bands), len(axes)):
    axes[j].axis("off")

plt.tight_layout()
plt.savefig("satellite_bands_2016.png", dpi=300)
plt.show()

print("Satellite image saved successfully!")

