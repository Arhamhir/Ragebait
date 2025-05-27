import streamlit as st
import joblib as jb
import pandas as pd

df = pd.read_csv("ragebait_dataset.csv")  # replace with your real CSV path or DataFrame

encoders = jb.load('encoders.pkl')
scaler = jb.load('myscale.pkl')
model = jb.load('mymodel.pkl')

# App settings
st.set_page_config(page_title="Ragebait Predictor", layout="centered")

# Custom CSS for button
st.markdown("""
    <style>
    div.stButton > button:first-child {
        background-color: #ff4b4b;
        color:#ffffff;
        border-radius:8px;
        height:3em;
        width:100%;
        font-weight:bold;
    }
    </style>
    """, unsafe_allow_html=True)

# Header
st.markdown("<h1 style='text-align: center; color: #FFFFFF;'>🎯 Ragebait Time Predictor</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #FAFAFA;'>See how long it'll take to tilt your friend </p>", unsafe_allow_html=True)
st.markdown("---")

# Form layout
with st.form("ragebait_form"):
    col1, col2 = st.columns(2)
    with col1:
        ragebait = st.selectbox('🎭 Ragebait Type', ['Troll Meme','Grammar mistake','Opinion bait','Gaming Rage','False Flex'])
        time = st.selectbox('🕒 Time of the Day', ['Morning','University Hours','Afternoon','Night','Midnight'])
        delivery = st.selectbox('📬 Delivery Method', ['Discord','Old mention','Text','Tagged','IRL'])
    with col2:
        mood = st.slider('😤 Mood (1 = Chill, 10 = hostile)', 1, 10, 5)
        failed_triggers = st.slider('❌ Failed Attempts', 1, 10, 5)
        trigger = st.radio('🎯 Known Trigger?', ['Yes','No'])
    
    st.markdown("---")
    submitted = st.form_submit_button("Ragebait")

# Prediction
if submitted:
    ragebait_encoded = encoders['ragebait_type'].transform([ragebait])[0]
    time_encoded = encoders['time_of_day'].transform([time])[0]
    delivery_encoded = encoders['delivery_method'].transform([delivery])[0]
    trigger_encoded = encoders['known_trigger'].transform([trigger])[0]

    user_input = [[ragebait_encoded, mood, time_encoded, delivery_encoded, trigger_encoded, failed_triggers]]
    scaled_input = scaler.transform(user_input)
    prediction = model.predict(scaled_input)[0]

    st.markdown("---")
    if prediction < 0:
        st.markdown("""
        <div style='background-color:#db3737; padding: 5px; border-radius:10px; text-align:center;'>
            <h3 style='color:white; font-weight: bold;'>⚠️ MAJOR CRASHOUT</h3>
            <p style='color:white;'>Please refrain from further provocation!</p>
        </div>
        """, unsafe_allow_html=True)

    elif prediction > 150:
        st.markdown("""
        <div style='background-color:#4B4B4B; padding: 5px; border-radius:10px; text-align:center;'>
            <h3 style='color:white; font-weight: bold;'>😐 Not Worth the time</h3>
            <p style='color:white;'>They're too chill to ragebait right now. Try later!</p>
        </div>
        """, unsafe_allow_html=True)

    else:
        st.markdown(f"""
        <div style='background-color:#003B5C; padding:5px; border-radius:10px; text-align:center;'>
            <h3 style='color:white; font-weight: bold;'>⌚ Calculated Time:</h3>
            <h5 style='color:white;'>{prediction:.2f} seconds</h5>
        </div>
        """, unsafe_allow_html=True)

st.markdown("---")
st.subheader("📊 Average Time-to-Rage by Delivery Method")

# Calculate group means
avg_rage = df.groupby("delivery_method")["time_to_rage"].mean().reset_index().sort_values(by="time_to_rage")
chart_data = avg_rage.rename(columns={"delivery_method": "index"}).set_index("index")

# Interactive chart selector
# Let user pick a feature to compare with `time_to_rage`
feature = st.selectbox("📊 Choose Feature to Analyze Against `time_to_rage`", 
                       ['ragebait_type', 'time_of_day', 'delivery_method', 'known_trigger'])

# Let user choose chart type
chart_type = st.selectbox("📌 Choose Chart Type", ["Line Chart", "Bar Chart"], key="chart_select")

# Group and calculate average
chart_data = df.groupby(feature)['time_to_rage'].mean().reset_index().sort_values(by='time_to_rage')
chart_data = chart_data.rename(columns={feature: 'index'}).set_index('index')

# Show chart
if chart_type == "Line Chart":
    st.line_chart(chart_data)
else:
    st.bar_chart(chart_data)




    



