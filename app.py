# app.py
import streamlit as st
import pandas as pd
import joblib
import plotly.express as px
import plotly.graph_objects as go

# Page Config
st.set_page_config(
    page_title="Delhi House Price Prediction",
    page_icon="🏠",
    layout="wide"
)

# Load Model
model = joblib.load("house_price_model.pkl")

# Custom CSS
st.markdown("""
<style>
.main {
    background-color: #0E1117;
}

.stApp {
    background: linear-gradient(to right, #141E30, #243B55);
    color: white;
}

h1, h2, h3, h4 {
    color: white;
}

[data-testid="stSidebar"] {
    background: linear-gradient(to bottom, #000428, #004e92);
}

.stButton>button {
    width: 100%;
    background: linear-gradient(to right, #ff512f, #dd2476);
    color: white;
    border-radius: 12px;
    height: 3em;
    font-size: 18px;
    font-weight: bold;
    border: none;
}

.stButton>button:hover {
    background: linear-gradient(to right, #36d1dc, #5b86e5);
    color: white;
}

.metric-card {
    background: rgba(255,255,255,0.1);
    padding: 20px;
    border-radius: 15px;
    text-align: center;
    box-shadow: 0 4px 20px rgba(0,0,0,0.3);
}
</style>
""", unsafe_allow_html=True)

# Header
st.markdown("""
<h1 style='text-align: center; font-size: 55px;'>🏠 Delhi House Price Prediction Dashboard</h1>
<p style='text-align: center; font-size: 20px;'>AI Powered Real Estate Price Prediction System</p>
<hr>
""", unsafe_allow_html=True)

# Sidebar
st.sidebar.title("📌 Property Details")

location = st.sidebar.selectbox(
    "Select Location",
    [
        "Rohini", "Dwarka", "Saket", "Laxmi Nagar",
        "Janakpuri", "Pitampura", "Karol Bagh",
        "Vasant Kunj", "South Extension",
        "Noida", "Gurugram", "Ghaziabad"
    ]
)

bhk = st.sidebar.slider("BHK", 1, 5, 2)

bathrooms = st.sidebar.slider("Bathrooms", 1, 5, 2)

area_sqft = st.sidebar.number_input(
    "Area (sqft)",
    min_value=500,
    max_value=5000,
    value=1200
)

parking = st.sidebar.slider("Parking", 0, 3, 1)

furnishing = st.sidebar.selectbox(
    "Furnishing",
    ["Furnished", "Semi-Furnished", "Unfurnished"]
)

metro_distance_km = st.sidebar.slider(
    "Metro Distance (km)",
    0.5, 15.0, 2.0
)

property_age = st.sidebar.slider(
    "Property Age",
    0, 30, 5
)

floor = st.sidebar.slider("Floor", 1, 30, 3)

total_floors = st.sidebar.slider(
    "Total Floors",
    floor, 40, 10
)

# Main Layout
col1, col2 = st.columns([2, 1])

with col1:
    st.subheader("📊 Property Overview")

    overview_data = pd.DataFrame({
        "Feature": [
            "Area Sqft",
            "BHK",
            "Bathrooms",
            "Parking",
            "Property Age"
        ],
        "Value": [
            area_sqft,
            bhk,
            bathrooms,
            parking,
            property_age
        ]
    })

    fig = px.bar(
        overview_data,
        x="Feature",
        y="Value",
        text="Value",
        title="Property Features"
    )

    st.plotly_chart(fig, use_container_width=True)

with col2:
    st.subheader("📍 Selected Details")

    st.markdown(f"""
    <div class="metric-card">
        <h3>📍 Location</h3>
        <h2>{location}</h2>
    </div>
    <br>
    <div class="metric-card">
        <h3>🛋 Furnishing</h3>
        <h2>{furnishing}</h2>
    </div>
    """, unsafe_allow_html=True)

# Prediction
st.markdown("---")

if st.button("🚀 Predict House Price"):

    input_data = pd.DataFrame([{
        "location": location,
        "bhk": bhk,
        "bathrooms": bathrooms,
        "area_sqft": area_sqft,
        "parking": parking,
        "furnishing": furnishing,
        "metro_distance_km": metro_distance_km,
        "property_age": property_age,
        "floor": floor,
        "total_floors": total_floors
    }])

    prediction = model.predict(input_data)

    predicted_price = int(prediction[0])

    st.success(f"🏠 Estimated House Price: ₹ {predicted_price:,}")

    # Gauge Chart
    gauge_fig = go.Figure(go.Indicator(
        mode = "gauge+number",
        value = predicted_price,
        title = {'text': "Predicted Price"},
        gauge = {
            'axis': {'range': [None, 50000000]},
        }
    ))

    st.plotly_chart(gauge_fig, use_container_width=True)

# Footer
st.markdown("---")
st.markdown(
    "<h4 style='text-align:center;'>Built with ❤️ using Streamlit & Machine Learning</h4>",
    unsafe_allow_html=True
)
