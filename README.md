# Swiggy-s-Restaurant-Recommendation-System-using-Streamlit

Overview:
The objective is to build a recommendation system based on restaurant data
provided in a CSV file. The system should recommend restaurants to users based
on input features such as city, rating, cost, and cuisine preferences. The
application will utilize clustering or similarity measures to generate
recommendations and display results in an easy-to-use Streamlit interface. This
project will provide
1. Personalized Recommendations: Help users discover restaurants based
on their preferences.
2. Improved Customer Experience: Provide tailored suggestions to
enhance decision-making.
3. Market Insights: Understand customer preferences and behaviors for
targeted marketing.
4. Operational Efficiency: Enable businesses to optimize their offerings
based on popular preferences.
Skills:
1. Data Pre-processing
2. One-Hot Encoding
3. Clustering (K-Means, Cosine Similarity)
4. Streamlit Application Development
5. Python
Domain: Recommendation Systems and Data Analytics
Approach:
1. The dataset is provided as a CSV file with the following columns: ['id',
'name', 'city', 'rating', 'rating_count', 'cost', 'cuisine', 'lic_no', 'link', 'address',
'menu']
2. Categorical: name, city, cuisine
3. Numerical: rating, rating_count, cost
Data Understanding and Cleaning
1. Duplicate Removal: Identified and drop duplicate rows.
2. Handling Missing Values: Imputed rows with missing values.
3. Save the cleaned data to a new CSV file (cleaned_data.csv).
Data Pre-processing
1. Encoding: Applied One-Hot Encoding to categorical features (name, city,
cuisine).
2. Saved the encoder as a Pickle file (encoder.pkl).
3. Ensured all features are numerical after encoding.
4. Created a pre-processed dataset (encoded_data.csv).
5. Ensured the indices of cleaned_data.csv and encoded_data.csv match.
Recommendation Methodology
 Clustering or Similarity Measures:
 Used K-Means Clustering and Cosine Similarity to identify similar
restaurants based on input features.
 Used the encoded dataset for computations.
Result Mapping:
 Mapped the recommendation results (indices) back to the nonencoded dataset (cleaned_data.csv).
Streamlit Application
 An interactive application with the following components:
 User Input: Accept user preferences (e.g., city, cuisine,
rating,price,etc).
 Recommendation Engine: Process the input, query the encoded
data, and generate recommendations.
 Output: Displayed recommended restaurants using
cleaned_data.csv.
Results:
Data Pre-processing
 Cleaned Dataset (cleaned_data.csv):
 Categorical and numerical features with missing values and
duplicates removed.
 Encoded Dataset (encoded_data.csv):
 Pre-processed numerical dataset with categorical features
One-Hot Encoded.
 Encoder File (encoder.pkl):
 Serialized One-Hot Encoder for Streamlit use.
Recommendation System
 Clustering or Similarity-based recommendation engine.
 Mapping results from encoded_data.csv to cleaned_data.csv for
interpretation.
Streamlit Application
 User-friendly interface for input and output.
 Clear display of recommendations from the cleaned dataset.

