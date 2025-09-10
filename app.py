import streamlit as st
from PIL import Image
import os

st.set_page_config(
    page_title="♻️ Sustainable Energy Builder", 
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for professional look
st.markdown("""
<style>
    .main-header {
        background: linear-gradient(90deg, #4CAF50, #2196F3);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-size: 3rem;
        font-weight: bold;
        text-align: center;
        margin-bottom: 20px;
    }
    
    .welcome-card {
        background: linear-gradient(145deg, #ffffff, #f0f2f6);
        padding: 30px;
        border-radius: 20px;
        box-shadow: 20px 20px 60px #d9d9d9, -20px -20px 60px #ffffff;
        border: 1px solid #e1e5e9;
        margin: 20px 0;
    }
    
    .energy-option {
        background: linear-gradient(45deg, #667eea, #764ba2);
        color: white;
        padding: 20px;
        border-radius: 15px;
        margin: 15px 0;
        text-align: center;
        transition: transform 0.3s ease;
    }
    
    .energy-option:hover {
        transform: translateY(-5px);
    }
    
    .stats-box {
        background: linear-gradient(90deg, #00b894, #00a085);
        color: white;
        padding: 15px;
        border-radius: 10px;
        margin: 10px 0;
        text-align: center;
    }
</style>
""", unsafe_allow_html=True)

# Initialize session state for progress tracking
if "total_score" not in st.session_state:
    st.session_state.total_score = 0
if "systems_completed" not in st.session_state:
    st.session_state.systems_completed = []

# Main header
st.markdown('<h1 class="main-header">♻️ Sustainable Energy Builder Game</h1>', unsafe_allow_html=True)

# Welcome section
col1, col2 = st.columns([2, 1])

with col1:
    st.markdown('<div class="welcome-card">', unsafe_allow_html=True)
    st.markdown("""
    ## Welcome Engineers! 🌍
    
    This interactive platform helps you **learn and build renewable energy systems** step by step.
    Designed specifically for **ECE Engineers** with detailed component analysis and circuit understanding.
    
    ### 🎯 What You'll Learn:
    - **Component identification** and assembly sequences
    - **Electrical characteristics** of each energy system
    - **Performance optimization** techniques
    - **Real-world engineering applications**
    
    ### 🎮 How to Play:
    1. Choose an energy system from the sidebar
    2. Study the system diagram and components
    3. Assemble components in correct order
    4. Get instant feedback and explanations
    5. Complete all 4 systems to become an Energy Expert!
    """)
    st.markdown('</div>', unsafe_allow_html=True)

with col2:
    # Progress tracking
    st.markdown('<div class="stats-box">', unsafe_allow_html=True)
    st.markdown(f"**Total Score:** {st.session_state.total_score}/400")
    st.markdown(f"**Systems Completed:** {len(st.session_state.systems_completed)}/4")
    
    completion_rate = (len(st.session_state.systems_completed) / 4) * 100
    st.markdown(f"**Progress:** {completion_rate:.0f}%")
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Achievement badges
    if len(st.session_state.systems_completed) >= 4:
        st.success("🏆 Energy Systems Expert!")
    elif len(st.session_state.systems_completed) >= 3:
        st.info("🥇 Advanced Energy Engineer!")
    elif len(st.session_state.systems_completed) >= 2:
        st.warning("🥈 Renewable Energy Specialist!")
    elif len(st.session_state.systems_completed) >= 1:
        st.info("🥉 Clean Energy Explorer!")

# Energy systems overview
st.markdown("## 🔋 Available Energy Systems")

col1, col2, col3, col4 = st.columns(4)

systems_data = [
    {"name": "Solar PV", "icon": "🔆", "page": "1_Solar", "color": "#FF9800"},
    {"name": "Wind Energy", "icon": "🌪️", "page": "2_Wind", "color": "#2196F3"},
    {"name": "Hydroelectric", "icon": "💧", "page": "3_Hydro", "color": "#00BCD4"},
    {"name": "Biomass", "icon": "🌱", "page": "4_Biomass", "color": "#4CAF50"}
]

for i, (col, system) in enumerate(zip([col1, col2, col3, col4], systems_data)):
    with col:
        completed = system["page"] in st.session_state.systems_completed
        status = "✅ Completed" if completed else "🔄 Available"
        
        st.markdown(f"""
        <div class="energy-option">
            <h3>{system['icon']} {system['name']}</h3>
            <p><strong>{status}</strong></p>
        </div>
        """, unsafe_allow_html=True)

# System overview with placeholder for main image
st.markdown("---")
st.markdown("## 🌟 System Overview")

# Try to load main overview image
try:
    if os.path.exists("images/renewable_energy_overview.png"):
        overview_img = Image.open("images/renewable_energy_overview.png")
        st.image(overview_img, caption="Renewable Energy Systems Overview", use_container_width=True)
    else:
        st.info("📸 **Place your main overview image here:** `images/renewable_energy_overview.png`")
except:
    st.info("📸 **Place your main overview image here:** `images/renewable_energy_overview.png`")

# Instructions
st.markdown("---")
st.markdown("## 📋 Getting Started")

col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    ### 🛠️ For Each Energy System:
    1. **Study the diagram** - Understand component layout
    2. **Read component specs** - Learn technical details
    3. **Assembly challenge** - Arrange in correct order
    4. **Get feedback** - Learn from explanations
    5. **Earn points** - Track your progress
    """)

with col2:
    st.markdown("""
    ### 🎯 Learning Objectives:
    - **Component Recognition** - Visual identification
    - **System Architecture** - Understanding layouts  
    - **Electrical Principles** - Circuit analysis
    - **Performance Metrics** - Efficiency calculations
    - **Real Applications** - Industry standards
    """)

# Footer with navigation hint
st.markdown("---")
st.info("👈 **Start your learning journey** by selecting an energy system from the sidebar!")

# Technical specifications summary
with st.expander("📊 Technical Specifications Summary"):
    specs_data = {
        "System": ["Solar PV", "Wind Turbine", "Hydroelectric", "Biomass"],
        "Typical Power": ["5-400 kW", "1.5-3 MW", "1-700 MW", "100 kW-10 MW"],
        "Efficiency": ["15-22%", "35-45%", "80-95%", "25-40%"],
        "Capacity Factor": ["15-25%", "25-40%", "40-60%", "70-85%"],
        "LCOE ($/MWh)": ["50-120", "30-80", "20-100", "60-150"]
    }
    
    import pandas as pd
    specs_df = pd.DataFrame(specs_data)
    st.dataframe(specs_df, use_container_width=True)