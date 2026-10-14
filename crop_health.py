import pandas as pd


# ---------------------------------------
# 1. Load NDVI dataset
# ---------------------------------------

data = pd.read_csv("ndvi_yield_2018.csv")

print("Dataset loaded successfully.")
print("Number of records:", len(data))


# ---------------------------------------
# 2. Create crop health categories
# ---------------------------------------

def classify_health(ndvi):

    if ndvi >= 0.80:
        return "Healthy"

    elif ndvi >= 0.70:
        return "Moderate Stress"

    else:
        return "Severe Stress"


data["Crop_Health"] = data["NDVI"].apply(classify_health)


# ---------------------------------------
# 3. Display results
# ---------------------------------------

print("\nCrop Health Classification:")
print(data[["NDVI", "Crop_Health"]].head(10))


# ---------------------------------------
# 4. Count each health category
# ---------------------------------------

print("\nHealth Category Counts:")
print(data["Crop_Health"].value_counts())


# ---------------------------------------
# 5. Save the dataset
# ---------------------------------------

data.to_csv("crop_health_2018.csv", index=False)

print("\nCrop health dataset saved successfully!")
print("File: crop_health_2018.csv")