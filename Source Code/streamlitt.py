import streamlit as st
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
import pickle
import os

# Set page configuration
st.set_page_config(
    page_title="Restaurant Recommender",
    page_icon="🍽️",
    layout="wide"
)

# Load data and models
@st.cache_data
def load_data():
    """Load and cache the data"""
    cleaned_data = pd.read_csv('cleaned_data.csv')
    encoded_data = pd.read_csv('encoded_data.csv')
    
    # Load label encoders
    with open('label_encoders.pkl', 'rb') as f:
        label_encoders = pickle.load(f)
    
    # Load scaler
    with open('scaler.pkl', 'rb') as f:
        scaler = pickle.load(f)
    
    # Load KMeans model
    with open('minibatch_kmeans_model.pkl', 'rb') as f:
        kmeans_model, cluster_mapping = pickle.load(f)
    
    return cleaned_data, encoded_data, label_encoders, scaler, kmeans_model, cluster_mapping

# Custom CSS
st.markdown("""
    <style>
    .restaurant-card {
        padding: 20px;
        border-radius: 10px;
        background-color: #f0f2f6;
        margin-bottom: 20px;
    }
    .metric-card {
        background-color: #ffffff;
        padding: 10px;
        border-radius: 5px;
        text-align: center;
    }
    </style>
    """, unsafe_allow_html=True)

# Load data
try:
    cleaned_data, encoded_data, label_encoders, scaler, kmeans_model, cluster_mapping = load_data()
    
    # Get unique values for filters
    cities = sorted(cleaned_data['city'].unique())
    cuisines = sorted(cleaned_data['cuisine'].unique())
    
    # Convert price ranges to numeric values
    price_mapping = {'₹ 100': 100, '₹ 200': 200, '₹ 250': 250, '₹ 300': 300}
    
except Exception as e:
    st.error(f"Error loading data: {str(e)}")
    st.stop()

# Title and description
st.title("🍽️ Restaurant Recommendation System")
st.markdown("""
    Find your next favorite restaurant based on your preferences!
    Simply select your criteria below and get personalized recommendations.
""")

# Sidebar filters
st.sidebar.header("Filter Restaurants")

# City selection
selected_city = st.sidebar.selectbox(
    "Select City",
    ["All"] + list(cities)
)

# Cuisine selection
selected_cuisine = st.sidebar.selectbox(
    "Select Cuisine",
    ["All"] + list(cuisines)
)

# Price range selection
price_range = st.sidebar.slider(
    "Price Range (₹)",
    min_value=100,
    max_value=300,
    value=(100, 300),
    step=50
)

# Rating filter
min_rating = st.sidebar.slider(
    "Minimum Rating",
    min_value=1.0,
    max_value=5.0,
    value=3.5,
    step=0.5
)

# Number of recommendations
n_recommendations = st.sidebar.number_input(
    "Number of Recommendations",
    min_value=1,
    max_value=20,
    value=5
)

def filter_restaurants(df):
    """Filter restaurants based on user preferences"""
    mask = pd.Series(True, index=df.index)
    
    if selected_city != "All":
        mask &= df['city'] == selected_city
    
    if selected_cuisine != "All":
        mask &= df['cuisine'] == selected_cuisine
    
    # Convert price strings to numeric values
    df['price_value'] = df['cost'].map(lambda x: price_mapping.get(x, 0))
    mask &= df['price_value'].between(price_range[0], price_range[1])
    
    # Handle rating filter
    df['rating_numeric'] = pd.to_numeric(df['rating'].replace('--', np.nan), errors='coerce')
    mask &= (df['rating_numeric'] >= min_rating) | df['rating_numeric'].isna()
    
    return df[mask]

def get_recommendations(restaurant_id):
    """Get restaurant recommendations using the trained model"""
    try:
        # Get restaurant features
        restaurant_features = encoded_data.iloc[restaurant_id].values.reshape(1, -1)
        restaurant_features_scaled = scaler.transform(restaurant_features)
        
        # Get cluster
        cluster = kmeans_model.predict(restaurant_features_scaled)[0]
        
        # Get recommendations from the same cluster
        similar_restaurants = cluster_mapping[cluster]
        
        # Filter out the input restaurant
        recommendations = [idx for idx in similar_restaurants if idx != restaurant_id]
        
        return cleaned_data.iloc[recommendations]
    
    except Exception as e:
        st.error(f"Error getting recommendations: {str(e)}")
        return pd.DataFrame()

def display_restaurant_card(restaurant):
    """Display a restaurant in a card format"""
    with st.container():
        col1, col2, col3 = st.columns([2, 1, 1])
        
        with col1:
            st.subheader(restaurant['name'])
            st.write(f"📍 {restaurant['address']}")
            st.write(f"🍽️ {restaurant['cuisine']}")
        
        with col2:
            st.metric("Rating", restaurant['rating'])
            st.write(f"💰 {restaurant['cost']}")
        
        with col3:
            if pd.notna(restaurant['rating_count']):
                st.write(f"👥 {restaurant['rating_count']}")
            if pd.notna(restaurant['link']):
                st.write(f"[View on Swiggy]({restaurant['link']})")

# Main content
filtered_data = filter_restaurants(cleaned_data)

if filtered_data.empty:
    st.warning("No restaurants found matching your criteria. Please adjust your filters.")
else:
    st.subheader(f"Found {len(filtered_data)} matching restaurants")
    
    # Display sample restaurants
    sample_restaurants = filtered_data.sample(min(5, len(filtered_data)))
    
    for _, restaurant in sample_restaurants.iterrows():
        display_restaurant_card(restaurant)
        
        # Get and display recommendations
        if st.button(f"Get recommendations similar to {restaurant['name']}"):
            recommendations = get_recommendations(restaurant.name)
            
            if not recommendations.empty:
                st.subheader("Similar Restaurants")
                for _, rec in recommendations.head(n_recommendations).iterrows():
                    display_restaurant_card(rec)
            else:
                st.info("No similar restaurants found.")

# Additional features
st.sidebar.markdown("---")
st.sidebar.markdown("### Search by Name")
search_query = st.sidebar.text_input("Enter restaurant name")

if search_query:
    search_results = cleaned_data[cleaned_data['name'].str.contains(search_query, case=False, na=False)]
    if not search_results.empty:
        st.subheader("Search Results")
        for _, restaurant in search_results.head(5).iterrows():
            display_restaurant_card(restaurant)
    else:
        st.sidebar.warning("No restaurants found matching your search.")

# Footer
st.markdown("---")
st.markdown("""
    <div style='text-align: center'>
        <p>Built with ❤️ by Gokul</p>
    </div>
    """, unsafe_allow_html=True)
