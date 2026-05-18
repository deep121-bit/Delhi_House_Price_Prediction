import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, r2_score

import joblib

# Load Dataset
df = pd.read_csv("delhi_housing.csv")

# Features and Target
X = df.drop("price", axis=1)
y = df["price"]

# Categorical Columns
categorical_cols = ["location", "furnishing"]

# Preprocessing
preprocessor = ColumnTransformer([
    ("cat", OneHotEncoder(handle_unknown="ignore"), categorical_cols)
], remainder="passthrough")

# Model
model = RandomForestRegressor(
    n_estimators=100,
    random_state=42
)

# Pipeline
pipeline = Pipeline([
    ("preprocessor", preprocessor),
    ("model", model)
])

# Train-Test Split
X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.2,
    random_state=42
)

# Train Model
pipeline.fit(X_train, y_train)

# Predictions
y_pred = pipeline.predict(X_test)

# Evaluation
mae = mean_absolute_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print("Model Training Completed!")

print(f"MAE: {mae:.2f}")
print(f"R2 Score: {r2:.2f}")

# Save Model
joblib.dump(pipeline, "house_price_model.pkl")

print("Model Saved Successfully!")