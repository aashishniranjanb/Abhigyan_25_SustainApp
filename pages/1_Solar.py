import streamlit as st
from PIL import Image
import os

st.set_page_config(page_title="🔆 Solar PV Energy System", layout="wide")

# Custom CSS
st.markdown("""
<style>
    .system-header {
        background: linear-gradient(90deg, #FF9800, #FF5722);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-size: 2.5rem;
        font-weight: bold;
        text-align: center;
        margin: 20px 0;
    }
    
    .component-card {
        background: linear-gradient(145deg, #fff3e0, #ffe0b2);
        padding: 20px;
        border-radius: 15px;
        box-shadow: 10px 10px 30px #d9d9d9, -10px -10px 30px #ffffff;
        margin: 15px 0;
        border-left: 5px solid #FF9800;
    }
    
    .assembly-area {
        background: linear-gradient(45deg, #f8f9fa, #e9ecef);
        padding: 25px;
        border-radius: 20px;
        border: 3px dashed #FF9800;
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
        background: #fff3e0;
        border: 2px solid #FF9800;
        border-radius: 10px;
        padding: 15px;
        margin: 10px 0;
    }
</style>
""", unsafe_allow_html=True)

# Initialize session state
if "solar_score" not in st.session_state:
    st.session_state.solar_score = 0
if "solar_completed" not in st.session_state:
    st.session_state.solar_completed = False
if "assembly_submitted" not in st.session_state:
    st.session_state.assembly_submitted = False

# Header
st.markdown('<h1 class="system-header">🔆 Solar PV Energy System</h1>', unsafe_allow_html=True)

# Progress indicator
col1, col2, col3 = st.columns(3)
with col1:
    st.metric("Solar System Score", f"{st.session_state.solar_score}/100", "Points")
with col2:
    status = "✅ Completed" if st.session_state.solar_completed else "🔄 In Progress"
    st.metric("Status", status)
with col3:
    st.metric("Difficulty", "⭐⭐⭐", "Intermediate")

# System overview
st.markdown("## 📊 System Overview")

col1, col2 = st.columns([2, 1])

with col1:
    # Main system image placeholder
    try:
        if os.path.exists("images/solar_system.png"):
            solar_img = Image.open("images/solar_system.png")
            st.image(solar_img, caption="Complete Solar PV System Architecture", use_container_width=True)
        else:
            st.info("📸 **Place your solar system diagram here:** `images/solar_system.png`")
    except:
        st.info("📸 **Place your solar system diagram here:** `images/solar_system.png`")

with col2:
    st.markdown('<div class="spec-box">', unsafe_allow_html=True)
    st.markdown("""
    ### 🔧 System Specifications
    **Power Rating:** 5-400 kW  
    **Cell Type:** Monocrystalline Si  
    **Efficiency:** 18-22%  
    **Voltage:** 24-48V DC  
    **Current:** 8-12A per panel  
    **Lifespan:** 25+ years  
    **Applications:** Grid-tie, Off-grid
    """)
    st.markdown('</div>', unsafe_allow_html=True)

# Component learning section
st.markdown("---")
st.markdown("## 🧩 Component Analysis")

# Component data with ECE focus
components_data = {
    "PN Junction (Silicon Cell)": {
        "description": "Core semiconductor device - converts photons to electron-hole pairs",
        "specs": "Bandgap: 1.12 eV, Voc: 0.6V, Isc: 9A/cm²",
        "function": "Photovoltaic effect - light → electrical energy conversion",
        "image": "images/components/pn_junction.png"
    },
    "Anti-Reflective Coating": {
        "description": "Optical coating to minimize reflection losses",
        "specs": "Material: Si₃N₄, Thickness: 70-80nm, Refractive Index: 2.0",
        "function": "Reduces reflection from 30% to <2% - increases light absorption",
        "image": "images/components/ar_coating.png"
    },
    "Front Contact Grid": {
        "description": "Silver conductive fingers for current collection",
        "specs": "Width: 100-150μm, Resistance: <5mΩ, Coverage: 3-5%",
        "function": "Collects generated current with minimal shading loss",
        "image": "images/components/front_contact.png"
    },
    "Back Surface Field": {
        "description": "Heavily doped p+ layer for electron reflection",
        "specs": "Doping: 10¹⁹ cm⁻³, Thickness: 0.5μm, Material: Al-Si",
        "function": "Creates electric field to repel minority carriers",
        "image": "images/components/back_surface.png"
    },
    "MPPT Controller": {
        "description": "Maximum Power Point Tracking for optimal energy harvesting",
        "specs": "Efficiency: >98%, Algorithm: P&O/InCond, Response: <1s",
        "function": "Dynamic impedance matching - maintains MPP under varying conditions",
        "image": "images/components/mppt_controller.png"
    },
    "DC-AC Inverter": {
        "description": "Power electronics for grid synchronization",
        "specs": "THD: <3%, Efficiency: >96%, Switching: PWM 20kHz",
        "function": "Converts DC to AC with grid-quality waveform",
        "image": "images/components/inverter.png"
    },
    "Battery Storage": {
        "description": "Energy storage system for load balancing",
        "specs": "Type: Li-ion, Capacity: 100-400Ah, Voltage: 48V",
        "function": "Stores excess energy, provides power during low irradiance",
        "image": "images/components/battery.png"
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
st.markdown("## 🎮 Assembly Challenge: Build the Solar PV System")

st.markdown('<div class="assembly-area">', unsafe_allow_html=True)
st.markdown("### 🛠️ Arrange Components in Correct Assembly Order")
st.markdown("**Task:** Select components in the order they would be assembled/connected in a complete solar PV system")

# All components for assembly
all_components = [
    "PN Junction (Silicon Cell)",
    "Anti-Reflective Coating", 
    "Front Contact Grid",
    "Back Surface Field",
    "MPPT Controller",
    "DC-AC Inverter",
    "Battery Storage"
]

# Correct assembly order (from light entry to power output)
correct_order = [
    "Anti-Reflective Coating",
    "Front Contact Grid", 
    "PN Junction (Silicon Cell)",
    "Back Surface Field",
    "MPPT Controller",
    "Battery Storage",
    "DC-AC Inverter"
]

# Component assembly selector
st.markdown("**Select components in assembly order (light-to-power flow):**")
user_order = st.multiselect(
    "Drag and arrange components:",
    all_components,
    help="Think about the path from sunlight entering to electricity output"
)

col1, col2 = st.columns(2)

with col1:
    if st.button("🚀 Submit Assembly", type="primary"):
        st.session_state.assembly_submitted = True
        
        if user_order == correct_order:
            st.session_state.solar_score = 100
            st.session_state.solar_completed = True
            if "1_Solar" not in st.session_state.systems_completed:
                st.session_state.systems_completed.append("1_Solar")
                st.session_state.total_score += 100
            
            st.markdown('<div class="correct-answer">', unsafe_allow_html=True)
            st.markdown("""
            🎉 **Perfect Assembly!** You've correctly built the Solar PV system!
            
            **Explanation:** Your assembly follows the optimal light-to-electricity conversion path:
            1. **Anti-Reflective Coating** - First contact with sunlight, minimizes losses
            2. **Front Contact Grid** - Collects photogenerated current  
            3. **PN Junction** - Core conversion element (photovoltaic effect)
            4. **Back Surface Field** - Improves collection efficiency
            5. **MPPT Controller** - Optimizes power extraction
            6. **Battery Storage** - Stores energy for later use
            7. **DC-AC Inverter** - Converts to usable AC power
            """)
            st.markdown('</div>', unsafe_allow_html=True)
            
            st.balloons()
            
        else:
            st.markdown('<div class="wrong-answer">', unsafe_allow_html=True)
            st.markdown(f"""
            ❌ **Assembly needs adjustment!** 
            
            **Your order:** {' → '.join(user_order)}
            
            **Hint:** Think about the energy conversion flow:
            - Start with **light entry** components
            - Then the **semiconductor conversion** 
            - Finally **power conditioning** systems
            
            **Key principle:** Follow the electron flow from photon absorption to AC output!
            """)
            st.markdown('</div>', unsafe_allow_html=True)

with col2:
    if st.button("💡 Get Hint"):
        st.info("""
        🔍 **Assembly Hint:**
        
        **Light Entry Stage:** What touches sunlight first?
        **Conversion Stage:** Where do photons become electrons?
        **Collection Stage:** How is current gathered?  
        **Conditioning Stage:** How is power optimized and converted?
        
        Think: **Photon → Electron → Current → Power → Grid**
        """)

st.markdown('</div>', unsafe_allow_html=True)

# Technical deep dive
if st.session_state.solar_completed:
    st.markdown("---")
    st.markdown("## 🔬 Advanced Engineering Analysis")
    
    with st.expander("📈 Performance Characteristics"):
        st.markdown("""
        ### I-V Characteristic Analysis
        **Short Circuit Current (Isc):** Isc = IL - I0(e^(qVoc/nkT) - 1) ≈ IL
        **Open Circuit Voltage (Voc):** Voc = (nkT/q) × ln(IL/I0 + 1)  
        **Maximum Power Point:** Pmax = Vmp × Imp
        **Fill Factor:** FF = (Vmp × Imp)/(Voc × Isc)
        **Efficiency:** η = Pmax/(Pin × Area)
        
        ### Temperature Effects
        - **Voltage coefficient:** -0.4%/°C
        - **Current coefficient:** +0.05%/°C  
        - **Power coefficient:** -0.45%/°C
        """)
    
    with st.expander("⚡ Circuit Analysis"):
        st.markdown("""
        ### Equivalent Circuit Model
        **Single Diode Model:** I = IL - I0(e^((V+IRs)/nVt) - 1) - (V+IRs)/Rsh
        
        **Parameters:**
        - IL: Light-generated current
        - I0: Dark saturation current  
        - Rs: Series resistance (1-5Ω)
        - Rsh: Shunt resistance (>1000Ω)
        - n: Ideality factor (1-2)
        
        ### MPPT Algorithms
        **Perturb & Observe:** Simple, 95-98% efficiency
        **Incremental Conductance:** Better performance, 98-99% efficiency
        **Fuzzy Logic:** Adaptive, handles rapid changes
        """)

# Navigation and progress
st.markdown("---")
col1, col2, col3 = st.columns(3)

with col1:
    if st.button("🏠 Home"):
        st.switch_page("app.py")

with col2:
    if st.button("➡️ Next: Wind Energy"):
        st.switch_page("pages/2_Wind.py")

with col3:
    if st.session_state.solar_completed:
        st.success("✅ Solar System Mastered!")
    else:
        st.info("🎯 Complete assembly to proceed")

# Footer
st.markdown("---")
st.markdown("**🔆 Solar PV System** | Photovoltaic Energy Conversion | ECE Engineering Focus")