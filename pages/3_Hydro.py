import streamlit as st
from PIL import Image
import os

st.set_page_config(page_title="💧 Hydroelectric System", layout="wide")

# Custom CSS
st.markdown("""
<style>
    .system-header {
        background: linear-gradient(90deg, #00BCD4, #0097A7);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-size: 2.5rem;
        font-weight: bold;
        text-align: center;
        margin: 20px 0;
    }
    
    .component-card {
        background: linear-gradient(145deg, #e0f7fa, #b2ebf2);
        padding: 20px;
        border-radius: 15px;
        box-shadow: 10px 10px 30px #d9d9d9, -10px -10px 30px #ffffff;
        margin: 15px 0;
        border-left: 5px solid #00BCD4;
    }
    
    .assembly-area {
        background: linear-gradient(45deg, #f8f9fa, #e9ecef);
        padding: 25px;
        border-radius: 20px;
        border: 3px dashed #00BCD4;
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
        background: #e0f7fa;
        border: 2px solid #00BCD4;
        border-radius: 10px;
        padding: 15px;
        margin: 10px 0;
    }
</style>
""", unsafe_allow_html=True)

# Initialize session state
if "hydro_score" not in st.session_state:
    st.session_state.hydro_score = 0
if "hydro_completed" not in st.session_state:
    st.session_state.hydro_completed = False

# Header
st.markdown('<h1 class="system-header">💧 Hydroelectric System</h1>', unsafe_allow_html=True)

# Progress indicator
col1, col2, col3 = st.columns(3)
with col1:
    st.metric("Hydro System Score", f"{st.session_state.hydro_score}/100", "Points")
with col2:
    status = "✅ Completed" if st.session_state.hydro_completed else "🔄 In Progress"
    st.metric("Status", status)
with col3:
    st.metric("Difficulty", "⭐⭐⭐⭐⭐", "Expert")

# System overview
st.markdown("## 📊 System Overview")

col1, col2 = st.columns([2, 1])

with col1:
    # Main system image placeholder
    try:
        if os.path.exists("images/hydro_system.png"):
            hydro_img = Image.open("images/hydro_system.png")
            st.image(hydro_img, caption="Complete Hydroelectric Power Plant Architecture", use_container_width=True)
        else:
            st.info("📸 **Place your hydro system diagram here:** `images/hydro_system.png`")
    except:
        st.info("📸 **Place your hydro system diagram here:** `images/hydro_system.png`")

with col2:
    st.markdown('<div class="spec-box">', unsafe_allow_html=True)
    st.markdown("""
    ### 🔧 System Specifications
    **Power Rating:** 1-700 MW  
    **Head Height:** 50-200m  
    **Flow Rate:** 100-1000 m³/s  
    **Turbine Type:** Francis/Kaplan/Pelton  
    **Generator:** Synchronous  
    **Efficiency:** 80-95%  
    **Grid Voltage:** 11-22 kV
    """)
    st.markdown('</div>', unsafe_allow_html=True)

# Component learning section
st.markdown("---")
st.markdown("## 🧩 Component Analysis")

# Component data with ECE focus
components_data = {
    "Dam & Reservoir": {
        "description": "Water retention structure creating hydraulic head pressure",
        "specs": "Height: 50-200m, Volume: 10⁶-10⁹ m³, Material: Concrete/Earth",
        "function": "Converts flowing water kinetic energy to potential energy storage",
        "image": "images/components/dam_reservoir.png"
    },
    "Intake Structure": {
        "description": "Controlled water entry with debris screening and flow regulation",
        "specs": "Gate Type: Radial/Vertical, Flow Control: Servo actuators, Capacity: 500-2000 m³/s",
        "function": "Regulates water flow into penstock with debris protection",
        "image": "images/components/intake.png"
    },
    "Penstock": {
        "description": "Large pressure pipeline delivering water to turbine",
        "specs": "Diameter: 3-8m, Pressure: 5-20 bar, Material: Steel/Concrete",
        "function": "Maintains hydraulic pressure and directs flow to turbine",
        "image": "images/components/penstock.png"
    },
    "Hydraulic Turbine": {
        "description": "Converts hydraulic energy to mechanical rotation",
        "specs": "Type: Francis/Kaplan, Efficiency: 85-95%, Speed: 100-750 rpm",
        "function": "Extracts kinetic and pressure energy from water flow",
        "image": "images/components/hydraulic_turbine.png"
    },
    "Synchronous Generator": {
        "description": "Large AC generator for electrical power production",
        "specs": "Power: 1-700MW, Voltage: 11-22kV, Frequency: 50/60Hz, Poles: 20-60",
        "function": "Converts mechanical rotation to three-phase electrical power",
        "image": "images/components/sync_generator.png"
    },
    "Governor System": {
        "description": "Hydraulic control system for turbine speed and power regulation",
        "specs": "Type: Digital/Hydraulic, Response: <5s, Accuracy: ±0.1%, Control: PID",
        "function": "Maintains frequency and controls power output via wicket gate positioning",
        "image": "images/components/governor.png"
    },
    "Excitation System": {
        "description": "Generator field control for voltage and reactive power regulation",
        "specs": "Type: Static/Brushless, Response: <0.1s, Voltage Reg: ±0.5%, Range: 0-130%",
        "function": "Controls generator field current for voltage regulation and grid stability",
        "image": "images/components/excitation.png"
    },
    "Step-up Transformer": {
        "description": "Voltage transformation for efficient power transmission",
        "specs": "Ratio: 11kV/220kV, Power: 100-800MVA, Type: Oil-immersed, Efficiency: >99%",
        "function": "Steps up generator voltage for high-voltage transmission",
        "image": "images/components/step_up_transformer.png"
    },
    "Protection & Control": {
        "description": "Comprehensive protection and SCADA control systems",
        "specs": "Relays: Digital multifunction, Communication: IEC 61850, HMI: SCADA",
        "function": "Protects equipment and provides remote monitoring/control capabilities",
        "image": "images/components/protection_control.png"
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
st.markdown("## 🎮 Assembly Challenge: Build the Hydroelectric System")

st.markdown('<div class="assembly-area">', unsafe_allow_html=True)
st.markdown("### 🛠️ Arrange Components in Correct Water-to-Power Flow Order")
st.markdown("**Task:** Select components following the complete water flow and energy conversion path")

# All components for assembly
all_components = list(components_data.keys())

# Correct assembly order (water flow and energy conversion)
correct_order = [
    "Dam & Reservoir",
    "Intake Structure", 
    "Penstock",
    "Hydraulic Turbine",
    "Synchronous Generator",
    "Governor System",
    "Excitation System",
    "Step-up Transformer",
    "Protection & Control"
]

# Component assembly selector
st.markdown("**Select components in energy conversion order (water-to-grid flow):**")
user_order = st.multiselect(
    "Arrange components following water and energy flow:",
    all_components,
    help="Think about the complete path from water storage to electrical grid"
)

col1, col2 = st.columns(2)

with col1:
    if st.button("🚀 Submit Assembly", type="primary"):
        if user_order == correct_order:
            st.session_state.hydro_score = 100
            st.session_state.hydro_completed = True
            if "3_Hydro" not in st.session_state.systems_completed:
                st.session_state.systems_completed.append("3_Hydro")
                st.session_state.total_score += 100
            
            st.markdown('<div class="correct-answer">', unsafe_allow_html=True)
            st.markdown("""
            🎉 **Perfect Assembly!** You've correctly built the Hydroelectric system!
            
            **Explanation:** Your assembly follows the optimal water-to-grid conversion path:
            1. **Dam & Reservoir** - Creates potential energy through water elevation
            2. **Intake Structure** - Controls water entry with flow regulation
            3. **Penstock** - Maintains pressure and directs flow to turbine
            4. **Hydraulic Turbine** - Converts hydraulic energy to mechanical rotation
            5. **Synchronous Generator** - Converts mechanical to electrical energy
            6. **Governor System** - Controls speed and power through flow regulation
            7. **Excitation System** - Regulates voltage and reactive power
            8. **Step-up Transformer** - Voltage transformation for transmission
            9. **Protection & Control** - System protection and remote operation
            """)
            st.markdown('</div>', unsafe_allow_html=True)
            
            st.balloons()
            
        else:
            st.markdown('<div class="wrong-answer">', unsafe_allow_html=True)
            st.markdown(f"""
            ❌ **Assembly needs adjustment!** 
            
            **Your order:** {' → '.join(user_order[:3])}{'...' if len(user_order) > 3 else ''}
            
            **Hint:** Think about the energy conversion chain:
            - Start with **water storage** (potential energy)
            - Then **water flow control** (kinetic energy)
            - Then **mechanical conversion** (turbine)
            - Finally **electrical generation & control** (generator systems)
            
            **Key principle:** Follow water flow from storage to electrical grid!
            """)
            st.markdown('</div>', unsafe_allow_html=True)

with col2:
    if st.button("💡 Get Hint"):
        st.info("""
        🔍 **Assembly Hint:**
        
        **Water Storage:** Where is potential energy stored?
        **Flow Control:** How is water flow regulated?
        **Energy Conversion:** How is hydraulic energy converted?
        **Electrical Systems:** How is power generated and controlled?
        **Grid Interface:** How is power transmitted?
        
        Think: **Storage → Control → Conversion → Generation → Transmission**
        """)

st.markdown('</div>', unsafe_allow_html=True)

# Technical deep dive
if st.session_state.hydro_completed:
    st.markdown("---")
    st.markdown("## 🔬 Advanced Engineering Analysis")
    
    with st.expander("📈 Hydroelectric Power Analysis"):
        st.markdown("""
        ### Power Output Calculation
        **Theoretical Power:** P = ρgQH (where ρ=1000kg/m³, g=9.81m/s², Q=flow, H=head)
        **Actual Power:** P = ρgQHηt ηg (ηt=turbine efficiency, ηg=generator efficiency)
        **Turbine Efficiency:** Francis: 85-95%, Kaplan: 90-95%, Pelton: 85-92%
        **Overall Efficiency:** Typically 80-90% for complete system
        
        ### Governor Control System
        **Speed Regulation:** Δn/n = -1/R × ΔP/Prated (R = regulation constant)
        **Wicket Gate Control:** Position controls flow area and turbine power
        **Response Time:** Mechanical: 5-20s, Electrical: 0.1-1s
        **Stability:** Requires proper tuning of PID parameters
        """)
    
    with st.expander("⚡ Electrical System Design"):
        st.markdown("""
        ### Synchronous Generator Analysis
        **EMF Equation:** E = 4.44fΦZKw (f=frequency, Φ=flux, Z=turns, Kw=winding factor)
        **Power Equation:** P = (EV/Xs)sinδ (δ=load angle, Xs=synchronous reactance)
        **Voltage Regulation:** VR = (Enl - Vfl)/Vfl × 100%
        **Power Factor Control:** Via field excitation adjustment
        
        ### Protection Systems
        **Generator Protection:** Differential, over/under voltage, frequency
        **Transformer Protection:** Differential, gas relay, temperature
        **System Protection:** Distance relays, directional overcurrent
        **Backup Protection:** Independent systems for critical components
        """)

# Navigation
st.markdown("---")
col1, col2, col3 = st.columns(3)

with col1:
    if st.button("⬅️ Back: Wind"):
        st.switch_page("pages/2_Wind.py")

with col2:
    if st.button("➡️ Next: Biomass"):
        st.switch_page("pages/4_Biomass.py")

with col3:
    if st.session_state.hydro_completed:
        st.success("✅ Hydro System Mastered!")
    else:
        st.info("🎯 Complete assembly to proceed")

st.markdown("---")
st.markdown("**💧 Hydroelectric System** | Mechanical-Electrical Energy Conversion | Power System Engineering")