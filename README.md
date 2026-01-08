**🍽️ Swiggy Restaurant Recommendation System using Streamlit**
**📌 Project Overview**

This project builds a restaurant recommendation system inspired by Swiggy’s food discovery platform.
It recommends restaurants based on similarity and clustering techniques, using features such as city, cuisine, and ratings, and presents results through an interactive Streamlit web application.

The system demonstrates an end-to-end recommendation pipeline:

Data cleaning and preprocessing

Encoding categorical features

Clustering & similarity-based recommendation

Real-time recommendation using Streamlit

🎯 **Objectives**

Provide personalized restaurant recommendations

Improve customer experience through tailored suggestions

Enable data-driven insights into food preferences

Demonstrate practical implementation of recommendation systems

🧠 **Business Use Cases**

Personalized food discovery for users

Cuisine and city-based demand analysis

Market insights for restaurant owners

Recommendation engines for food delivery platforms

🗂 **Dataset Description**

Input File: swiggy.csv
Total Records: ~148,000

Columns
['id', 'name', 'city', 'rating', 'rating_count',
 'cost', 'cuisine', 'lic_no', 'link', 'address', 'menu']

**Feature Types**

Categorical: name, city, cuisine

Numerical: rating, rating_count, cost

🔍 **Project Workflow**
1️⃣ **Data Understanding & Cleaning**
Steps Performed

Checked dataset shape and structure

Identified missing values and duplicates

Removed duplicate rows

Handled missing values:

Numerical → Mean imputation

Categorical → Mode imputation

**Output**

cleaned_data.csv

Clean dataset with missing values handled

Used for recommendation display and Streamlit UI

📌 Initial dataset had missing values in rating, cost, cuisine, and address fields.

2️⃣ **Feature Encoding**
Encoding Technique

Label Encoding applied separately to:

name

city

cuisine

Each column uses its own LabelEncoder.

Files Generated

encoded_data.csv – Numerical dataset for ML models

label_encoders.pkl – Serialized encoders for Streamlit usage

Encoding Summary
Feature	Unique Categories
name	112,683
city	821
cuisine	2,131

📌 Index alignment between cleaned_data.csv and encoded_data.csv is preserved.

3️⃣ **Feature Scaling**

Applied StandardScaler

Ensures equal weight for all numerical features

Saved scaler as:

scaler.pkl

4️⃣ **Recommendation System Design**

Two complementary recommendation methods are implemented:

🔹 Method 1: MiniBatch K-Means Clustering

Algorithm: MiniBatchKMeans

Efficient for large datasets

Groups similar restaurants into clusters

**Recommendation Logic**

Identify the cluster of the selected restaurant

Retrieve other restaurants from the same cluster

Rank them based on rating

📦 **Saved Files:**

minibatch_kmeans_model.pkl

Cluster-to-restaurant index mapping

🔹 Method 2: Nearest Neighbor (Distance-Based)

Uses Euclidean distance

Processes data in batches (memory-efficient)

Finds restaurants closest in feature space

🔁 **Hybrid Recommendation Output**

Both methods are used to generate and compare recommendations for better relevance.

5️⃣ Streamlit Application
🖥️ App Features
Sidebar Filters

City

Cuisine

Price range

Minimum rating

Number of recommendations

Main Interface

Displays matching restaurants

Card-based UI with:

Name

Address

Cuisine

Rating

Cost

Swiggy link

Recommendation Trigger

“Get recommendations similar to this restaurant” button

Uses cluster-based recommendation engine

Search Functionality

Search restaurants by name

Instant results display

🎨 **UI Highlights**

Clean card-style layout

Real-time recommendations

Responsive and user-friendly

Cached data loading for performance

📊 **Results**
Data Artifacts
File	Description
cleaned_data.csv	Cleaned dataset
encoded_data.csv	Label-encoded dataset
label_encoders.pkl	Saved encoders
scaler.pkl	Feature scaler
minibatch_kmeans_model.pkl	Clustering model
System Output

Accurate similarity-based recommendations

Consistent mapping from encoded to original data

Scalable architecture for large datasets

🛠 **Technologies Used**

Language: Python

**Libraries:**

Pandas, NumPy

Scikit-learn

Streamlit

ML Techniques:

Label Encoding

Standard Scaling

MiniBatch K-Means

Distance-based similarity

🚀 **Future Enhancements**

One-Hot Encoding or Embedding-based encoding

Collaborative filtering

User preference learning

Cuisine similarity NLP embeddings

Cloud deployment (AWS / GCP)

Login-based personalized recommendations
