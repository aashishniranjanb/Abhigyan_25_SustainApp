import streamlit as st
from PIL import Image
import os

st.set_page_config(page_title="🌱 Biomass Energy System", layout="wide")

# Custom CSS
st.markdown("""
<style>
    .system-header {
        background: linear-gradient(90deg, #4CAF50, #388E3C);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-size: 2.5rem;
        font-weight: bold;
        text-align: center;
        margin: 20px 0;
    }
    
    .component-card {
        background: linear-gradient(145deg, #e8f5e8, #c8e6c9);
        padding: 20px;
        border-radius: 15px;
        box-shadow: 10px 10px 30px #d9d9d9, -10px -10px 30px #ffffff;
        margin: 15px 0;
        border-left: 5px solid #4CAF50;
    }
    
    .assembly-area {
        background: linear-gradient(45deg, #f8f9fa, #e9ecef);
        padding: 25px;
        border-radius: 20px;
        border: 3px dashed #4CAF50;
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
        background: #e8f5e8;
        border: 2px solid #4CAF50;
        border-radius: 10px;
        padding: 15px;
        margin: 10px 0;
    }
    
    .completion-celebration {
        background: linear-gradient(45deg, #FFD700, #FFA500);
        color: black;
        padding: 20px;
        border-radius: 15px;
        text-align: center;
        margin: 20px 0;
        font-weight: bold;
    }
</style>
""", unsafe_allow_html=True)

# Initialize session state
if "biomass_score" not in st.session_state:
    st.session_state.biomass_score = 0
if "biomass_completed" not in st.session_state:
    st.session_state.biomass_completed = False

# Header
st.markdown('<h1 class="system-header">🌱 Biomass Energy System</h1>', unsafe_allow_html=True)

# Progress indicator
col1, col2, col3 = st.columns(3)
with col1:
    st.metric("Biomass System Score", f"{st.session_state.biomass_score}/100", "Points")
with col2:
    status = "✅ Completed" if st.session_state.biomass_completed else "🔄 In Progress"
    st.metric("Status", status)
with col3:
    st.metric("Difficulty", "⭐⭐⭐⭐", "Advanced")

# System overview
st.markdown("## 📊 System Overview")

col1, col2 = st.columns([2, 1])

with col1:
    # Main system image placeholder
    try:
        if os.path.exists("images/biomass_system.png"):
            biomass_img = Image.open("images/biomass_system.png")
            st.image(biomass_img, caption="Complete Biomass Energy System Architecture", use_container_width=True)
        else:
            st.info("📸 **Place your biomass system diagram here:** `images/biomass_system.png`")
    except:
        st.info("📸 **Place your biomass system diagram here:** `images/biomass_system.png`")

with col2:
    st.markdown('<div class="spec-box">', unsafe_allow_html=True)
    st.markdown("""
    ### 🔧 System Specifications
    **Power Rating:** 100 kW - 10 MW  
    **Feedstock:** Organic waste, crops  
    **Gas Yield:** 300-600 m³/tonne  
    **Methane Content:** 55-70%  
    **Engine Efficiency:** 35-42%  
    **Operating Temp:** 35-55°C  
    **Retention Time:** 15-30 days
    """)
    st.markdown('</div>', unsafe_allow_html=True)

# Component learning section
st.markdown("---")
st.markdown("## 🧩 Component Analysis")

# Component data with ECE focus
components_data = {
    "Feedstock Preparation": {
        "description": "Organic matter processing for optimal digestion conditions",
        "specs": "C/N Ratio: 25-30:1, Moisture: 40-60%, Size: <50mm, pH: 6.8-7.2",
        "function": "Prepares organic substrate for efficient anaerobic digestion process",
        "image": "images/components/feedstock_prep.png"
    },
    "Mixing & Heating": {
        "description": "Substrate homogenization and temperature control system",
        "specs": "Mixer Power: 5-15kW, Heating: 35-55°C, Control: PID, Sensors: Temperature/pH",
        "function": "Maintains optimal temperature and mixing for bacterial activity",
        "image": "images/components/mixing_heating.png"
    },
    "Anaerobic Digester": {
        "description": "Sealed reactor vessel for biogas production via bacterial decomposition",
        "specs": "Volume: 100-5000m³, Pressure: 1-3 bar, Material: Steel/Concrete, HRT: 15-30 days",
        "function": "Converts organic matter to biogas through anaerobic bacterial processes",
        "image": "images/components/digester.png"
    },
    "Gas Processing": {
        "description": "Biogas purification and conditioning for engine compatibility",
        "specs": "H2S Removal: <1000ppm, CO2 Separation: Optional, Drying: <60% RH, Filtration: 5μm",
        "function": "Removes impurities and conditions biogas for combustion engines",
        "image": "images/components/gas_processing.png"
    },
    "Gas Engine": {
        "description": "Internal combustion engine optimized for biogas fuel",
        "specs": "Power: 100kW-5MW, Speed: 1500rpm, Fuel: CH4 55-70%, Efficiency: 35-42%",
        "function": "Converts chemical energy in biogas to mechanical rotation",
        "image": "images/components/gas_engine.png"
    },
    "Synchronous Generator": {
        "description": "AC generator for electrical power production from engine",
        "specs": "Power: 100kW-5MW, Voltage: 400V-11kV, Frequency: 50/60Hz, Efficiency: >95%",
        "function": "Converts mechanical rotation to three-phase electrical power",
        "image": "images/components/biomass_generator.png"
    },
    "PLC Control System": {
        "description": "Programmable logic controller for automated process control",
        "specs": "I/O Points: 100-500, HMI: Touchscreen, Communication: Ethernet/Modbus, Memory: 1MB+",
        "function": "Monitors and controls digester parameters, safety systems, and power output",
        "image": "images/components/plc_control.png"
    },
    "Power Conditioning": {
        "description": "Generator synchronization and grid interface electronics",
        "specs": "Sync Unit: Automatic, Protection: Over/Under freq, THD: <5%, Power Factor: 0.8-1.0",
        "function": "Synchronizes generator with grid and maintains power quality",
        "image": "images/components/power_conditioning.png"
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
st.markdown("## 🎮 Final Assembly Challenge: Build the Biomass Energy System")

st.markdown('<div class="assembly-area">', unsafe_allow_html=True)
st.markdown("### 🛠️ Arrange Components in Correct Process Flow Order")
st.markdown("**Task:** Complete the biomass energy conversion process from organic waste to electrical power")

# All components for assembly
all_components = list(components_data.keys())

# Correct assembly order (process flow)
correct_order = [
    "Feedstock Preparation",
    "Mixing & Heating",
    "Anaerobic Digester",
    "Gas Processing", 
    "Gas Engine",
    "Synchronous Generator",
    "PLC Control System",
    "Power Conditioning"
]

# Component assembly selector
st.markdown("**Select components in process flow order (waste-to-electricity conversion):**")
user_order = st.multiselect(
    "Arrange components following the complete conversion process:",
    all_components,
    help="Think about the complete path from organic waste to electrical grid connection"
)

col1, col2 = st.columns(2)

with col1:
    if st.button("🚀 Submit Final Assembly", type="primary"):
        if user_order == correct_order:
            st.session_state.biomass_score = 100
            st.session_state.biomass_completed = True
            if "4_Biomass" not in st.session_state.systems_completed:
                st.session_state.systems_completed.append("4_Biomass")
                st.session_state.total_score += 100
            
            st.markdown('<div class="correct-answer">', unsafe_allow_html=True)
            st.markdown("""
            🎉 **Perfect Final Assembly!** You've mastered the Biomass Energy system!
            
            **Explanation:** Your assembly follows the optimal waste-to-power conversion:
            1. **Feedstock Preparation** - Optimizes organic matter for digestion
            2. **Mixing & Heating** - Creates ideal conditions for bacterial activity
            3. **Anaerobic Digester** - Biological conversion of organic matter to biogas
            4. **Gas Processing** - Purifies biogas for engine compatibility
            5. **Gas Engine** - Converts chemical energy to mechanical power
            6. **Synchronous Generator** - Converts mechanical to electrical energy
            7. **PLC Control System** - Automates and optimizes entire process
            8. **Power Conditioning** - Ensures grid-quality electrical output
            """)
            st.markdown('</div>', unsafe_allow_html=True)
            
            st.balloons()
            
            # Check if all systems completed
            if len(st.session_state.systems_completed) >= 4:
                st.markdown('<div class="completion-celebration">', unsafe_allow_html=True)
                st.markdown("""
                🏆 **CONGRATULATIONS! SUSTAINABLE ENERGY EXPERT ACHIEVED!** 🏆
                
                You have successfully mastered all 4 renewable energy systems:
                ✅ Solar PV Energy  
                ✅ Wind Energy  
                ✅ Hydroelectric Energy  
                ✅ Biomass Energy  
                
                **Total Score: 400/400 Points**
                
                You now understand the complete spectrum of sustainable energy technologies
                and their electrical engineering principles. You're ready to contribute to 
                the clean energy revolution! 🌍⚡
                """)
                st.markdown('</div>', unsafe_allow_html=True)
            
        else:
            st.markdown('<div class="wrong-answer">', unsafe_allow_html=True)
            st.markdown(f"""
            ❌ **Assembly needs adjustment!** 
            
            **Your order:** {' → '.join(user_order[:3])}{'...' if len(user_order) > 3 else ''}
            
            **Hint:** Think about the biological and mechanical process flow:
            - Start with **organic matter preparation**
            - Then **biological conversion** (anaerobic digestion)
            - Then **gas processing** and **combustion**
            - Finally **electrical generation & control**
            
            **Key principle:** Follow the energy conversion from biological to electrical!
            """)
            st.markdown('</div>', unsafe_allow_html=True)

with col2:
    if st.button("💡 Get Final Hint"):
        st.info("""
        🔍 **Final Assembly Hint:**
        
        **Preparation Stage:** How is organic matter prepared?
        **Biological Stage:** Where does anaerobic digestion occur?
        **Processing Stage:** How is biogas purified?
        **Conversion Stage:** How is chemical energy converted?
        **Control Stage:** How is the process automated?
        
        Think: **Prepare → Digest → Process → Convert → Control → Grid**
        """)

st.markdown('</div>', unsafe_allow_html=True)

# Technical deep dive
if st.session_state.biomass_completed:
    st.markdown("---")
    st.markdown("## 🔬 Advanced Engineering Analysis")
    
    with st.expander("📈 Biomass Process Analysis"):
        st.markdown("""
        ### Biogas Production Kinetics
        **Hydrolysis Rate:** k1 = 0.1-0.3 day⁻¹ (rate-limiting step)
        **Methanogenesis:** CH3COOH → CH4 + CO2 (acidogenesis → methanogenesis)
        **Gas Yield:** 300-600 m³/tonne volatile solids (depends on C/N ratio)
        **Methane Content:** 55-70% CH4, 30-45% CO2, <1% H2S
        **Temperature Effect:** Mesophilic (35°C) vs Thermophilic (55°C)
        
        ### Power Generation Efficiency
        **Overall Efficiency:** ηoverall = ηdigester × ηengine × ηgenerator
        **Typical Values:** 35% digester × 40% engine × 95% generator ≈ 13% overall
        **CHP Systems:** Combined heat and power can reach 80% total efficiency
        """)
    
    with st.expander("⚡ Control System Engineering"):
        st.markdown("""
        ### PLC Control Architecture
        **Process Variables:** Temperature, pH, gas flow, pressure, H2S content
        **Control Loops:** PID temperature control, flow regulation, safety interlocks
        **HMI Functions:** Real-time monitoring, alarm management, data logging
        **Communication:** Modbus RTU/TCP, Ethernet, wireless sensors
        
        ### Safety & Protection Systems
        **Gas Detection:** CH4, H2S, CO2 monitoring with alarm levels
        **Pressure Relief:** Automatic venting systems for overpressure
        **Fire Suppression:** CO2/foam systems for electrical equipment
        **Emergency Shutdown:** Fail-safe systems for process isolation
        """)

# Final navigation
st.markdown("---")
col1, col2, col3 = st.columns(3)

with col1:
    if st.button("⬅️ Back: Hydro"):
        st.switch_page("pages/3_Hydro.py")

with col2:
    if st.button("🏠 Home - View Progress"):
        st.switch_page("app.py")

with col3:
    if st.session_state.biomass_completed:
        if len(st.session_state.systems_completed) >= 4:
            st.success("🏆 ALL SYSTEMS MASTERED!")
        else:
            st.success("✅ Biomass System Mastered!")
    else:
        st.info("🎯 Complete assembly to finish")

st.markdown("---")
st.markdown("**🌱 Biomass Energy System** | Chemical-Electrical Energy Conversion | Process Control Engineering")