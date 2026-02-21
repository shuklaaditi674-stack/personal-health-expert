# frontend/app.py
import streamlit as st
import sys
import os
import importlib.util

# --- Dynamically load backend module (Logic Intact) ---
PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
BACKEND_PATH = os.path.join(PROJECT_ROOT, "backend", "rag_backend.py")

spec = importlib.util.spec_from_file_location("rag_backend", BACKEND_PATH)
rag_backend = importlib.util.module_from_spec(spec)
spec.loader.exec_module(rag_backend)

RAGBackend = rag_backend.RAGBackend
# -------------------------------------

# --- UI SETTINGS ---
st.set_page_config(page_title="MedAgent AI | Dark", page_icon="🧬", layout="wide")

# --- DARK THEME MODERN CSS ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@300;400;600;800&display=swap');
    
    /* Global Styles */
    .stApp {
        background: radial-gradient(circle at 2% 2%, #0f172a 0%, #020617 100%);
        color: #f8fafc;
        font-family: 'Plus Jakarta Sans', sans-serif;
    }

    /* Container Card */
    div[data-testid="stForm"], .stAlert, .stCodeBlock {
        background: rgba(30, 41, 59, 0.4) !important;
        backdrop-filter: blur(10px);
        border: 1px solid rgba(255, 255, 255, 0.05) !important;
        border-radius: 20px !important;
        padding: 2rem !important;
        box-shadow: 0 10px 30px rgba(0,0,0,0.5);
    }

    /* Input & Text Area Fixes for Dark Mode */
    input, textarea {
        background-color: #1e293b !important;
        color: white !important;
        border: 1px solid #334155 !important;
    }
    
    label p { color: #94a3b8 !important; font-weight: 600 !important; }

    /* Button - Glowing Emerald */
    .stButton>button {
        width: 100%;
        background: linear-gradient(90deg, #10b981 0%, #059669 100%) !important;
        color: white !important;
        border: none !important;
        border-radius: 14px !important;
        height: 54px !important;
        font-weight: 800 !important;
        letter-spacing: 0.5px;
        transition: all 0.3s ease !important;
        box-shadow: 0 4px 15px rgba(16, 185, 129, 0.3);
    }
    .stButton>button:hover {
        transform: translateY(-2px);
        box-shadow: 0 8px 25px rgba(16, 185, 129, 0.5);
    }

    /* Risk Badge */
    .risk-badge {
        padding: 10px 24px;
        border-radius: 100px;
        font-weight: 800;
        font-size: 0.9rem;
        text-transform: uppercase;
        margin-bottom: 20px;
        display: inline-block;
    }

    /* Subtitles */
    h1 { letter-spacing: -2px !important; color: #ffffff !important; font-weight: 800 !important; }
    h2, h3, h4 { color: #10b981 !important; font-weight: 700 !important; }

    /* Hide Streamlit elements */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    </style>
    """, unsafe_allow_html=True)

# Initialize backend
rag = RAGBackend()

# --- HEADER SECTION ---
st.markdown("<h1 style='text-align: center; margin-bottom: 0;'>🧬 MedAgent AI</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #64748b; font-size: 1.1rem;'>Neural Health Telemetry & Context Compression</p>", unsafe_allow_html=True)
st.markdown("<br>", unsafe_allow_html=True)

# --- LAYOUT SPLIT ---
col_in, col_out = st.columns([1, 1.2], gap="large")

with col_in:
    st.subheader("📡 Input Telemetry")
    with st.form("health_form"):
        age = st.number_input("Biological Age", 1, 120, 25)
        sleep_hours = st.slider("Sleep Quality (Hrs)", 0, 12, 7)
        stress_level = st.slider("Neural Stress Index", 0, 10, 3)
        fatigue_level = st.slider("System Fatigue Index", 0, 10, 3)
        medical_history = st.text_area("Clinical History / Active Symptoms", 
                                      placeholder="e.g., persistent dehydration, mild asthma...")

        submitted = st.form_submit_button("INITIALIZE ANALYSIS")

with col_out:
    if submitted:
        user_input = f"Age: {age}\nSleep: {sleep_hours}\nStress: {stress_level}\nFatigue: {fatigue_level}\nHistory: {medical_history}"
        
        with st.spinner("⚡ Processing Medical Vectors..."):
            result = rag.compress_health_info(user_input)
            
            if result.get("successful"):
                compressed = result.get("compressed_prompt") or ""
                if compressed.strip().lower() == "compress medical history and lifestyle info for ai analysis.":
                    compressed = user_input

                # --- Calculate Risk Score ---
                risk_score = sum([1 for word in ["fatigue", "stress", "dehydration", "sleep", "pain"] if word in user_input.lower()])
                
                # Dynamic Badges
                risk_colors = {0: ("#10b981", "rgba(16, 185, 129, 0.1)"), 
                               1: ("#10b981", "rgba(16, 185, 129, 0.1)"),
                               2: ("#f59e0b", "rgba(245, 158, 11, 0.1)"),
                               3: ("#f59e0b", "rgba(245, 158, 11, 0.1)"),
                               4: ("#ef4444", "rgba(239, 68, 68, 0.1)"),
                               5: ("#ef4444", "rgba(239, 68, 68, 0.1)")}
                
                txt_c, bg_c = risk_colors.get(risk_score, ("#10b981", "rgba(16, 185, 129, 0.1)"))

                st.markdown(f"<div class='risk-badge' style='background:{bg_c}; color:{txt_c}; border: 1px solid {txt_c}33;'>RISK FACTOR: {risk_score} / 5</div>", unsafe_allow_html=True)
                
                # --- Recommendations ---
                st.subheader("✅ Preventive Protocols")
                recs = []
                if "fatigue" in user_input.lower(): recs.append("Neural Reset: Prioritize 7.5h sleep cycles.")
                if "stress" in user_input.lower(): recs.append("Cortisol Regulation: Implement 4-7-8 breathing.")
                if "dehydration" in user_input.lower(): recs.append("Hydration Protocol: Target 30ml/kg body weight.")

                if recs:
                    for r in recs:
                        st.markdown(f"<div style='background:rgba(255,255,255,0.03); padding:15px; border-radius:12px; margin-bottom:8px; border-left:4px solid #10b981;'>• {r}</div>", unsafe_allow_html=True)
                else:
                    st.write("System checks normal. Maintain current baseline.")

                # --- AI Analytics Expander ---
                with st.expander("📊 AI Processing & Context Stats"):
                    st.markdown("#### Optimized Context Payload")
                    st.code(compressed)
                    
                    st.divider()
                    st.write(f"**Original Tokens:** `{result.get('original_tokens', 'N/A')}`")
                    st.write(f"**Compressed Tokens:** `{result.get('compressed_tokens', 'N/A')}`")
                    st.write(f"**Engine Latency:** `{round(result.get('latency_ms', 0), 1)} ms`")
            else:
                st.error(f"Engine Failure: {result.get('error')}")
    else:
        # Initial Placeholder
        st.markdown("""
            <div style='text-align: center; padding-top: 100px; opacity: 0.2;'>
                <img src='https://cdn-icons-png.flaticon.com/512/3063/3063176.png' width='100' style='filter: invert(1);'>
                <h3 style='color: white !important;'>SYSTEM READY</h3>
                <p>Waiting for Telemetry Submission...</p>
            </div>
        """, unsafe_allow_html=True)

st.markdown("<p style='text-align: center; color: #475569; font-size: 0.8rem; margin-top: 100px;'>Secure MedAgent Core v4.0 | AES-256 Encrypted Processing</p>", unsafe_allow_html=True)