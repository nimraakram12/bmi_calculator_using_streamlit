#9 Project-BMI Calculator

import streamlit as st
import numpy as np

st.set_page_config(
    page_title="Smart BMI Calculator",
    page_icon="📊",
    layout="centered",
    initial_sidebar_state="collapsed"
)


st.markdown("""
<style>
  .stApp {
    background: linear-gradient(135deg, rgba(255,255,255,0.1), rgba(255,255,255,0));
    backdrop-filter: blur(10px);
    -webkit-backdrop-filter: blur(10px);
    background-color: #6DD5FA; /* Fallback color */
}
    .title {
        color: #2f4f4f;
        text-align: center;
        font-size: 2.5em !important;
        margin-bottom: 0.5em;
    }
    .result-box {
        border-radius: 10px;
        padding: 1.5rem;
        margin: 1rem 0;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    }
    .healthy { background-color: #d4edda; color: #155724; }
    .warning { background-color: #fff3cd; color: #856404; }
    .danger { background-color: #f8d7da; color: #721c24; }
    .progress-bar {
        height: 20px;
        border-radius: 10px;
        margin: 1rem 0;
    }
            
</style>
""", unsafe_allow_html=True)


st.markdown('<h1 class="title">📈 Smart BMI Calculator</h1>', unsafe_allow_html=True)


col1, col2 = st.columns([1, 1])

with col1:
    
    unit_system = st.selectbox("Select Measurement System", 
                             ["Metric (kg & cm)", "Imperial (lbs & inches)"],
                             index=0)

with col2:
    
    gender = st.radio("Gender", ["Male", "Female"], horizontal=True)


if "Metric" in unit_system:
    weight = st.number_input("Weight (kg)", min_value=30.0, max_value=300.0, value=70.0, step=0.5)
    height = st.number_input("Height (cm)", min_value=100.0, max_value=250.0, value=170.0, step=0.5)
else:
    weight = st.number_input("Weight (lbs)", min_value=66.0, max_value=660.0, value=150.0, step=0.5)
    height = st.number_input("Height (inches)", min_value=39.0, max_value=100.0, value=65.0, step=0.5)

if st.button("Calculate BMI", use_container_width=True):
    if "Metric" in unit_system:
        bmi = weight / ((height/100) ** 2)
    else:
        bmi = (weight / (height ** 2)) * 703
    
    bmi = np.round(bmi, 1)
    
  
    if bmi < 18.5:
        category = "Underweight 🏋️"
        color_class = "warning"
    elif 18.5 <= bmi < 25:
        category = "Normal Weight ✅"
        color_class = "healthy"
    elif 25 <= bmi < 30:
        category = "Overweight ⚠️"
        color_class = "warning"
    else:
        category = "Obese 🛑"
        color_class = "danger"
    
   
    st.markdown(f"""
    <div class="result-box {color_class}">
        <h3>Your BMI: {bmi}</h3>
        <h4>{category}</h4>
    </div>
    """, unsafe_allow_html=True)
    
    
    progress_value = min(max((bmi - 15) / (40 - 15), 0), 1) 
    st.markdown(f"""
    <div class="progress-bar" style="background: linear-gradient(90deg, #4CAF50 {25}%, #FFC107 {25}% {75}%, #FF5252 {75}%);">
        <div style="width: {progress_value*100}%; height: 100%; background-color: rgba(255,255,255,0.3);"></div>
    </div>
    """, unsafe_allow_html=True)
    
    
    with st.expander("📌 Health Recommendations"):
        if bmi < 18.5:
            st.write("""
            - Consider increasing calorie intake with nutrient-dense foods
            - Incorporate strength training to build muscle mass
            - Consult a nutritionist for personalized advice
            """)
        elif 18.5 <= bmi < 25:
            st.write("""
            - Maintain current healthy habits
            - Regular exercise (150 mins/week recommended)
            - Balanced diet with variety of nutrients
            """)
        else:
            st.write("""
            - Consider gradual weight loss through diet and exercise
            - Focus on whole foods and reduce processed foods
            - Regular physical activity (300 mins/week recommended)
            - Consult healthcare professional for guidance
            """)

st.markdown("---")
st.caption("ℹ️ Note: BMI is a general indicator and doesn't account for muscle mass or body composition. Always consult with a healthcare professional for personalized advice.")