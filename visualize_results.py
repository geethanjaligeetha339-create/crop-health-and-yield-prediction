import pandas as pd
import matplotlib.pyplot as plt


# ---------------------------------------
# 1. Load dataset
# ---------------------------------------

data = pd.read_csv("crop_health_2018.csv")

print("Dataset loaded successfully.")


# ---------------------------------------
# 2. NDVI Distribution
# ---------------------------------------

plt.figure(figsize=(8, 5))

plt.hist(data["NDVI"], bins=30)

plt.xlabel("NDVI")
plt.ylabel("Number of Records")
plt.title("NDVI Distribution")

plt.tight_layout()
plt.savefig("ndvi_distribution.png", dpi=300)

plt.show()


# ---------------------------------------
# 3. Crop Health Distribution
# ---------------------------------------

health_counts = data["Crop_Health"].value_counts()

plt.figure(figsize=(8, 5))

plt.bar(
    health_counts.index,
    health_counts.values
)

plt.xlabel("Crop Health")
plt.ylabel("Number of Records")
plt.title("Crop Health Distribution")

plt.tight_layout()
plt.savefig("crop_health_distribution.png", dpi=300)

plt.show()


# ---------------------------------------
# 4. NDVI vs Yield
# ---------------------------------------

plt.figure(figsize=(8, 5))

plt.scatter(
    data["NDVI"],
    data["YIELD"],
    alpha=0.3
)

plt.xlabel("NDVI")
plt.ylabel("Yield")
plt.title("NDVI vs Crop Yield")

plt.tight_layout()
plt.savefig("ndvi_vs_yield.png", dpi=300)

plt.show()


print("\nGraphs saved successfully!")

print("1. ndvi_distribution.png")
print("2. crop_health_distribution.png")
print("3. ndvi_vs_yield.png")