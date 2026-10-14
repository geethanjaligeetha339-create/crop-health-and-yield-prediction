import pandas as pd
import joblib
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score


# ---------------------------------------
# 1. Load the dataset
# ---------------------------------------

data = pd.read_csv("ndvi_yield_2018.csv")

print("Dataset loaded successfully.")
print("Dataset shape:", data.shape)

print("\nFirst 5 rows:")
print(data.head())


# ---------------------------------------
# 2. Select input features and target
# ---------------------------------------

X = data[["NDVI", "HUMID"]]

y = data["YIELD"]


# ---------------------------------------
# 3. Split data into training and testing
# ---------------------------------------

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

print("\nTraining records:", len(X_train))
print("Testing records:", len(X_test))


# ---------------------------------------
# 4. Create Random Forest model
# ---------------------------------------

model = RandomForestRegressor(
    n_estimators=100,
    random_state=42,
    n_jobs=-1
)


# ---------------------------------------
# 5. Train the model
# ---------------------------------------

model.fit(X_train, y_train)

print("\nModel trained successfully!")

# Save the trained model
joblib.dump(model, "yield_prediction_model.pkl")

print("Model saved successfully!")




# ---------------------------------------
# 6. Make predictions
# ---------------------------------------

y_pred = model.predict(X_test)


# ---------------------------------------
# 7. Evaluate the model
# ---------------------------------------

mae = mean_absolute_error(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)
rmse = mse ** 0.5
r2 = r2_score(y_test, y_pred)

print("\nModel Performance")
print("-------------------------")
print("MAE :", mae)
print("RMSE:", rmse)
print("R²  :", r2)


# ---------------------------------------
# 8. Show some predictions
# ---------------------------------------

results = pd.DataFrame({
    "Actual Yield": y_test.values[:10],
    "Predicted Yield": y_pred[:10]
})

print("\nSample Predictions:")
print(results)
# ---------------------------------------
# 9. Actual vs Predicted Yield
# ---------------------------------------

plt.figure(figsize=(8, 5))

plt.scatter(
    y_test,
    y_pred,
    alpha=0.4
)

plt.xlabel("Actual Yield")
plt.ylabel("Predicted Yield")
plt.title("Actual Yield vs Predicted Yield")

plt.tight_layout()

plt.savefig("actual_vs_predicted_yield.png", dpi=300)

plt.show()

print("\nActual vs Predicted graph saved successfully!")