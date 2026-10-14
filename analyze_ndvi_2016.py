import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("ndvi_2016.csv")

print("NDVI summary:")
print(df["NDVI"].describe())

plt.figure(figsize=(8, 5))
plt.hist(df["NDVI"], bins=20, edgecolor="black")
plt.title("NDVI Distribution - 2016")
plt.xlabel("NDVI")
plt.ylabel("Number of Pixels")
plt.tight_layout()
plt.savefig("ndvi_distribution_2016.png", dpi=300)
plt.show()

print("Saved: ndvi_distribution_2016.png")
