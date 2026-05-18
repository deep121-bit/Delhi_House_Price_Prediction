import pandas as pd
import numpy as np
import random

np.random.seed(42)

# Delhi Locations
locations = [
    "Rohini", "Dwarka", "Saket", "Laxmi Nagar",
    "Janakpuri", "Pitampura", "Karol Bagh",
    "Vasant Kunj", "South Extension",
    "Noida", "Gurugram", "Ghaziabad"
]

furnishing_types = ["Furnished", "Semi-Furnished", "Unfurnished"]

data_size = 5000

data = []

for _ in range(data_size):

    location = random.choice(locations)

    bhk = np.random.randint(1, 6)

    bathrooms = np.random.randint(1, 5)

    area_sqft = np.random.randint(500, 4000)

    parking = np.random.randint(0, 3)

    furnishing = random.choice(furnishing_types)

    metro_distance = round(np.random.uniform(0.5, 15.0), 2)

    property_age = np.random.randint(0, 20)

    floor = np.random.randint(1, 20)

    total_floors = floor + np.random.randint(0, 20)

    # Base Price Logic
    base_price = area_sqft * 5500

    # Location Multiplier
    premium_locations = ["Vasant Kunj", "South Extension", "Gurugram"]

    if location in premium_locations:
        base_price *= 1.8

    # Furnishing Impact
    if furnishing == "Furnished":
        base_price *= 1.15

    elif furnishing == "Semi-Furnished":
        base_price *= 1.07

    # Metro Distance Impact
    base_price *= (1 - metro_distance * 0.01)

    # Property Age Impact
    base_price *= (1 - property_age * 0.005)

    # Random Noise
    final_price = base_price + np.random.randint(-500000, 500000)

    data.append([
        location,
        bhk,
        bathrooms,
        area_sqft,
        parking,
        furnishing,
        metro_distance,
        property_age,
        floor,
        total_floors,
        int(final_price)
    ])

# Create DataFrame
columns = [
    "location",
    "bhk",
    "bathrooms",
    "area_sqft",
    "parking",
    "furnishing",
    "metro_distance_km",
    "property_age",
    "floor",
    "total_floors",
    "price"
]

df = pd.DataFrame(data,columns=columns)

# Save CSV
df.to_csv("delhi_housing.csv", index=False)

print("Dataset Generated Successfully!")
print(df.head())