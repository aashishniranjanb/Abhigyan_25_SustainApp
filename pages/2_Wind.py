import streamlit as st
from PIL import Image
import os

st.set_page_config(page_title="🌪️ Wind Energy System", layout="wide")

# Custom CSS
st.markdown("""
<style>
    .system-header {
        background: linear-gradient(90deg, #2196F3, #1976D2);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-size: 2.5rem;
        font-weight: bold;
        text-align: center;
        margin: 20px 0;
    }
    
    .component-card {
        background: linear-gradient(145deg, #e3f2fd, #bbdefb);
        padding: 20px;
        border-radius: 15px;
        box-shadow: 10px 10px 30px #d9d9d9, -10px -10px 30px #ffffff;
        margin: 15px 0;
        border-left: 5px solid #2196F3;
    }
    
    .assembly-area {
        background: linear-gradient(45deg, #f8f9fa, #e9ecef);
        padding: 25px;
        border-radius: 20px;
        border: 3px dashed #2196F3;
        margin: 20px 0;
    }
    
    .correct-answer {
        background: linear-gradient(90deg, #4CAF50, #45a049);
        color: white;
        padding: 15px;
        border-radius: 10px;
        margin: 15px 0;
    }
    
    .wrong-answer {
        background: linear-gradient(90deg, #f44336, #d32f2f);
        color: white;
        padding: 15px;
        border-radius: 10px;
        margin: 15px 0;
    }
    
    .spec-box {
        background: #e3f2fd;
        border: 2px solid #2196F3;
        border-radius: 10px;
        padding: 15px;
        margin: 10px 0;
    }
</style>
""", unsafe_allow_html=True)

# Initialize session state
if "wind_score" not in st.session_state:
    st.session_state.wind_score = 0
if "wind_completed" not in st.session_state:
    st.session_state.wind_completed = False

# Header
st.markdown('<h1 class="system-header">🌪️ Wind Energy System</h1>', unsafe_allow_html=True)

# Progress indicator
col1, col2, col3 = st.columns(3)
with col1:
    st.metric("Wind System Score", f"{st.session_state.wind_score}/100", "Points")
with col2:
    status = "✅ Completed" if st.session_state.wind_completed else "🔄 In Progress"
    st.metric("Status", status)
with col3:
    st.metric("Difficulty", "⭐⭐⭐⭐", "Advanced")

# System overview
st.markdown("## 📊 System Overview")

col1, col2 = st.columns([2, 1])

with col1:
    # Main system image placeholder
    try:
        if os.path.exists("images/wind_system.png"):
            wind_img = Image.open("images/wind_system.png")
            st.image(wind_img, caption="Complete Wind Turbine System Architecture", use_container_width=True)
        else:
            st.info("📸 **Place your wind system diagram here:** `images/wind_system.png`")
    except:
        st.info("📸 **Place your wind system diagram here:** `images/wind_system.png`")

with col2:
    st.markdown('<div class="spec-box">', unsafe_allow_html=True)
    st.markdown("""
    ### 🔧 System Specifications
    **Power Rating:** 1.5-3 MW  
    **Rotor Diameter:** 80-120m  
    **Hub Height:** 80-150m  
    **Generator:** DFIG/PMSG  
    **Cut-in Speed:** 3 m/s  
    **Rated Speed:** 12 m/s  
    **Cut-out Speed:** 25 m/s
    """)
    st.markdown('</div>', unsafe_allow_html=True)

# Component learning section
st.markdown("---")
st.markdown("## 🧩 Component Analysis")

# Component data with ECE focus
components_data = {
    "Aerodynamic Blades": {
        "description": "Captures kinetic energy from wind through lift and drag forces",
        "specs": "Length: 40-60m, Material: Fiberglass/Carbon, Airfoil: NACA profiles",
        "function": "Converts wind kinetic energy to mechanical rotation with optimal Cp",
        "image": "images/components/turbine_blades.png"
    },
    "Hub & Pitch System": {
        "description": "Connects blades and controls blade angle for optimization",
        "specs": "Pitch Range: 0-90°, Response: <1s, Control: Servo/Hydraulic",
        "function": "Optimizes angle of attack for maximum energy capture",
        "image": "images/components/hub_pitch.png"
    },
    "Main Shaft": {
        "description": "Low-speed shaft transmitting rotor torque to gearbox",
        "specs": "Speed: 15-50 rpm, Torque: 1-5 MNm, Material: Steel alloy",
        "function": "Transfers mechanical power from rotor to drivetrain",
        "image": "images/components/main_shaft.png"
    },
    "Gearbox": {
        "description": "Speed multiplication system for generator matching",
        "specs": "Ratio: 1:50-100, Type: Planetary, Efficiency: >95%",
        "function": "Converts low-speed high-torque to high-speed low-torque",
        "image": "images/components/gearbox.png"
    },
    "DFIG Generator": {
        "description": "Doubly Fed Induction Generator for variable speed operation",
        "specs": "Power: 1.5-3MW, Speed: 1000-1800rpm, Slip: ±30%",
        "function": "Converts mechanical energy to electrical with variable speed control",
        "image": "images/components/dfig_generator.png"
    },
    "Power Electronics": {
        "description": "Rotor-side and grid-side converters for DFIG control",
        "specs": "Converter Power: 25-30%, Switching: IGBT 2-5kHz, Control: Vector",
        "function": "Enables variable speed operation and grid synchronization",
        "image": "images/components/power_electronics.png"
    },
    "Control System": {
        "description": "Supervisory control for optimal power extraction and protection",
        "specs": "CPU: Industrial PC, I/O: 100+ points, Communication: Ethernet",
        "function": "Coordinates pitch, yaw, and generator control for optimal performance",
        "image": "images/components/control_system.png"
    },
    "Transformer": {
        "description": "Steps up generator voltage for transmission",
        "specs": "Ratio: 690V/22kV, Power: 2-3MVA, Type: Oil-filled",
        "function": "Voltage transformation for efficient power transmission",
        "image": "images/components/transformer.png"
    }
}

# Component selector
selected_component = st.selectbox(
    "🔍 Select Component for Detailed Analysis:",
    list(components_data.keys())
)

component = components_data[selected_component]

col1, col2 = st.columns([1, 1])

with col1:
    st.markdown(f'<div class="component-card">', unsafe_allow_html=True)
    st.markdown(f"### {selected_component}")
    st.markdown(f"**Description:** {component['description']}")
    st.markdown(f"**Technical Specs:** {component['specs']}")
    st.markdown(f"**Function:** {component['function']}")
    st.markdown('</div>', unsafe_allow_html=True)

with col2:
    # Component image placeholder
    try:
        if os.path.exists(component['image']):
            comp_img = Image.open(component['image'])
            st.image(comp_img, caption=f"{selected_component} - Technical Diagram", use_container_width=True)
        else:
            st.info(f"📸 **Component image:** `{component['image']}`")
    except:
        st.info(f"📸 **Component image:** `{component['image']}`")

# Assembly challenge
st.markdown("---")
st.markdown("## 🎮 Assembly Challenge: Build the Wind Energy System")

st.markdown('<div class="assembly-area">', unsafe_allow_html=True)
st.markdown("### 🛠️ Arrange Components in Correct Power Flow Order")
st.markdown("**Task:** Select components in the order of energy conversion from wind to electrical grid")

# All components for assembly
all_components = list(components_data.keys())

# Correct assembly order (wind energy flow)
correct_order = [
    "Aerodynamic Blades",
    "Hub & Pitch System",
    "Main Shaft",
    "Gearbox",
    "DFIG Generator",
    "Power Electronics",
    "Control System",
    "Transformer"
]

# Component assembly selector
st.markdown("**Select components in energy conversion order (wind-to-grid flow):**")
user_order = st.multiselect(
    "Arrange components following energy flow:",
    all_components,
    help="Think about the path from wind energy capture to electrical grid connection"
)

col1, col2 = st.columns(2)

with col1:
    if st.button("🚀 Submit Assembly", type="primary"):
        if user_order == correct_order:
            st.session_state.wind_score = 100
            st.session_state.wind_completed = True
            if "2_Wind" not in st.session_state.systems_completed:
                st.session_state.systems_completed.append("2_Wind")
                st.session_state.total_score += 100
            
            st.markdown('<div class="correct-answer">', unsafe_allow_html=True)
            st.markdown("""
            🎉 **Perfect Assembly!** You've correctly built the Wind Energy system!
            
            **Explanation:** Your assembly follows the optimal wind-to-grid conversion path:
            1. **Aerodynamic Blades** - Capture wind kinetic energy through aerodynamics
            2. **Hub & Pitch System** - Optimizes blade angle for maximum energy capture
            3. **Main Shaft** - Transfers low-speed, high-torque mechanical power
            4. **Gearbox** - Speed multiplication for generator compatibility
            5. **DFIG Generator** - Mechanical to electrical energy conversion
            6. **Power Electronics** - Variable speed control and grid synchronization
            7. **Control System** - Coordinates all subsystems for optimal operation
            8. **Transformer** - Voltage step-up for efficient transmission
            """)
            st.markdown('</div>', unsafe_allow_html=True)
            
            st.balloons()
            
        else:
            st.markdown('<div class="wrong-answer">', unsafe_allow_html=True)
            st.markdown(f"""
            ❌ **Assembly needs adjustment!** 
            
            **Your order:** {' → '.join(user_order)}
            
            **Hint:** Think about the energy conversion chain:
            - Start with **wind capture** (aerodynamics)
            - Then **mechanical transmission** (speed conversion)  
            - Finally **electrical conversion** (generation & conditioning)
            
            **Key principle:** Follow the energy flow from kinetic wind energy to AC grid power!
            """)
            st.markdown('</div>', unsafe_allow_html=True)

with col2:
    if st.button("💡 Get Hint"):
        st.info("""
        🔍 **Assembly Hint:**
        
        **Wind Capture Stage:** How is wind energy captured?
        **Mechanical Stage:** How is rotational speed/torque converted?
        **Electrical Stage:** How is mechanical energy converted to electricity?
        **Grid Interface:** How is power conditioned for the grid?
        
        Think: **Wind → Rotation → Speed Change → Generation → Control → Grid**
        """)

st.markdown('</div>', unsafe_allow_html=True)

# Technical deep dive
if st.session_state.wind_completed:
    st.markdown("---")
    st.markdown("## 🔬 Advanced Engineering Analysis")
    
    with st.expander("📈 Wind Turbine Performance"):
        st.markdown("""
        ### Power Output Calculation
        **Available Wind Power:** P = ½ρAV³
        **Turbine Power Output:** P = ½ρAV³Cp
        **Power Coefficient:** Cp = f(λ, β) where λ = tip speed ratio
        **Optimal λ:** λopt = ΩR/V ≈ 7-8 for most turbines
        
        ### DFIG Control Strategy
        **Rotor Side Converter:** Controls rotor current for speed/power
        **Grid Side Converter:** Maintains DC link voltage, reactive power
        **Slip Power:** Ps = sP where s = slip, P = stator power
        **Speed Range:** n = (1±s)ns for ±30% slip range
        """)
    
    with st.expander("⚡ Electrical System Analysis"):
        st.markdown("""
        ### DFIG Equivalent Circuit
        **Stator:** Direct grid connection at synchronous frequency
        **Rotor:** Fed through slip rings via power electronics
        **Slip Calculation:** s = (ns - nr)/ns
        **Power Flow:** Mechanical → Stator (75%) + Rotor (25%) → Grid
        
        ### Control Algorithms
        **Vector Control:** Decoupled control of torque and flux
        **MPPT:** Maximum power point tracking Popt = ½ρAV³Cpmax
        **Pitch Control:** β adjustment for power regulation above rated
        **Grid Code Compliance:** LVRT, frequency response, reactive support
        """)

# Navigation
st.markdown("---")
col1, col2, col3 = st.columns(3)

with col1:
    if st.button("⬅️ Back: Solar"):
        st.switch_page("pages/1_Solar.py")

with col2:
    if st.button("➡️ Next: Hydro"):
        st.switch_page("pages/3_Hydro.py")

with col3:
    if st.session_state.wind_completed:
        st.success("✅ Wind System Mastered!")
    else:
        st.info("🎯 Complete assembly to proceed")

st.markdown("---")
st.markdown("**🌪️ Wind Energy System** | Electromagnetic Energy Conversion | Advanced Power Electronics")