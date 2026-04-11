import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import r2_score, mean_squared_error


# Load dataset
df = pd.read_csv("data/processed/rainfall_clean.csv")


# Features
X = df[['JUN','JUL','AUG','SEP']]

# Target
y = df['ANNUAL']


# Train-test split
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)


# Model
model = RandomForestRegressor(
    n_estimators=300,
    random_state=42
)


# Train model
model.fit(X_train, y_train)


# Predictions
y_pred = model.predict(X_test)


# Accuracy metrics
r2 = r2_score(y_test, y_pred)
#rmse = mean_squared_error(y_test, y_pred, squared=False)


print("Rainfall Model Performance")
print("----------------------------")
print("R2 Score:", r2)
#print("RMSE:", rmse)
print("----------------------------")


# Save model
joblib.dump(model, "models/rainfall_model.pkl")

print("Rainfall model saved successfully!")