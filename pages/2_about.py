import streamlit as st

st.markdown("<h1 style='text-align: center;'>📖 About This Project</h1>", unsafe_allow_html=True)
st.markdown("---")

st.markdown("""
<div style='max-width: 800px; margin: 0 auto;'>
            
<h2 style='text-align: center;'>Ragebait Time Predictor</h2>

<p>Ever wondered how long it takes to push someone's buttons? This playful app predicts how quickly your friend might lose their cool based on how you tease them.</p>

<h3>🔧 How It Works</h3>
<p>We created a machine learning model from a part of real dataset and the rest simulated on it, about our daily interactions with each other. The model considers:</p>
<ul>
    <li>Type of ragebait (memes, grammar mistakes, etc.)</li>
    <li>Your target's current mood</li>
    <li>Time of day and delivery method</li>
    <li>Past attempts and known triggers</li>
</ul>

<h3>🛠️ Technical Implementation</h3>
<p>Here's how we built the prediction engine:</p>

<div style='background: #003B5C; margin-bottom:20px; padding: 15px; border-radius: 10px;'>
<strong>1. Data Preparation:</strong>
<ul>
    <li>Encoded categorical features (like bait type, mood) using LabelEncoder</li>
    <li>Standardized numerical features with StandardScaler</li>
    <li>Split data into 80% training and 20% testing sets</li>
</ul>

<strong>2. Model Selection:</strong>
<ul>
    <li>Evaluated multiple algorithms using LazyPredict</li>
    <li>Selected LinearRegression for its balance of performance and simplicity</li>
    <li>Achieved R² score of 0.90 on test data</li>
</ul>

<strong>3. Deployment:</strong>
<ul>
    <li>Serialized the model, scaler, and encoders using Joblib</li>
    <li>Built interactive interface with Streamlit</li>
    <li>Deployed on Github</li>
</ul>
</div>

<h3>💻 Tech Stack</h3>
<div style='display: flex; flex-wrap: wrap; gap: 10px;'>
    <span style='background: #FF5733; color: white; padding: 5px 10px; border-radius: 20px;'>Python</span>
    <span style='background: #3498DB; color: white; padding: 5px 10px; border-radius: 20px;'>scikit-learn</span>
    <span style='background: #FFC300; color: black; padding: 5px 10px; border-radius: 20px;'>Streamlit</span>
    <span style='background: #2ECC71; color: white; padding: 5px 10px; border-radius: 20px;'>Joblib</span>
    <span style='background: #9B59B6; color: white; padding: 5px 10px; border-radius: 20px;'>Pandas</span>
</div>

<div style='margin-top: 30px; padding: 15px; background: #003B5C; border-radius: 10px;'>
⚠️ <strong>Important Note:</strong> This simulation is satire. If you’re using it to actually tease someone in real life — maybe <b>you</b> need a timeout.
</div>

<p style='text-align: center; margin-top: 30px;'>Built by <b>Syed Ashtar Ali Zaidi</b> and <b>Muhammad Arham Tahir</b></p>
</div>
""", unsafe_allow_html=True)
