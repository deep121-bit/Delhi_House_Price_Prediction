import pandas as pd
import joblib

# Load Model
model = joblib.load("house_price_model.pkl")

# Sample Input Data
sample_data = pd.DataFrame([{
    "location": "Dwarka",
    "bhk": 3,
    "bathrooms": 2,
    "area_sqft": 1500,
    "parking": 1,
    "furnishing": "Semi-Furnished",
    "metro_distance_km": 2.5,
    "property_age": 5,
    "floor": 4,
    "total_floors": 10
}])

# Predict
prediction = model.predict(sample_data)

# Output
print("Predicted House Price:")
print(f"₹ {int(prediction[0]):,}")