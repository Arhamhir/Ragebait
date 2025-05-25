import streamlit as st
import joblib as jb

st.set_page_config(page_title="Ragebait Predictor", layout="centered")

encoders = jb.load('encoders.pkl')
scaler = jb.load('myscale.pkl')
model = jb.load('mymodel.pkl')

st.markdown("<h1 style='text-align: center; color: #FFFFFF;'>🎯 Ragebait Time Predictor</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #FAFAFA;'>See how long it'll take to tilt your friend </p>", unsafe_allow_html=True)
st.markdown("---")

with st.form("ragebait_form"):

    ragebait = st.selectbox('🎭 Ragebait Type', ['Troll Meme','Grammar mistake','Opinion bait','Gaming Rage','False Flex'])
    time = st.selectbox('🕒 Time of the Day', ['Morning','University Hours','Afternoon','Night','Midnight'])
    trigger = st.radio('🎯 Known Trigger?', ['Yes','No'])
    mood = st.slider('😤 Mood (1 = Chill, 10 = Tilted)', 1, 10, 5)
    delivery = st.selectbox('📬 Delivery Method', ['Discord','Old mention','Text','Tagged','IRL'])
    failed_triggers = st.slider('❌ Failed Attempts', 1, 10, 5)
    
    submitted = st.form_submit_button("🔥 Ragebait Now!")

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
        st.markdown(
        f"""
        <div style='background-color:#de1b28; border-radius:10px; text-align:center;'>
            <h3 style='color:##ff2634;'>⚠️ MAJOR CRASHOUT</h3>
        </div>
        """,
        unsafe_allow_html=True
    )

    else:
        st.markdown(f"<h4 style='color: #FFFFFF;'>🕒 Estimated Time: <span style='color:#22e355'>{prediction:.2f}</span> seconds</h4>", unsafe_allow_html=True)
