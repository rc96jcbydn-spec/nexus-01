import streamlit as st
from datetime import datetime
import pandas as pd
import random
import json
import os

# 1. SAYFA YAPILANDIRMASI
st.set_page_config(
    page_title="NEXUS-01 | Kalıcı Bellekli Otonom Çekirdek",
    page_icon="⚛️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- KALICI BELLEK (JSON NOT DEFTERİ) YÖNETİMİ ---
STATE_FILE = "nexus_state.json"

def load_state():
    """Eğer daha önce kaydedilmiş dosya varsa onu oku, yoksa ilk değerleri ver."""
    if os.path.exists(STATE_FILE):
        try:
            with open(STATE_FILE, "r", encoding="utf-8") as f:
                return json.load(f)
        except:
            pass
    return {
        "evolution_gen": 7,
        "vector_nodes": 1920,
        "agent_fitness": 97.2,
        "system_logs": [f"[{datetime.now().strftime('%H:%M:%S')}] Sistem sıfırdan ve kalıcı hafızayla başlatıldı."]
    }

def save_state():
    """O anki güncel verileri otomatik olarak nexus_state.json dosyasına kaydet."""
    state_data = {
        "evolution_gen": st.session_state.evolution_gen,
        "vector_nodes": st.session_state.vector_nodes,
        "agent_fitness": st.session_state.agent_fitness,
        "system_logs": st.session_state.system_logs
    }
    with open(STATE_FILE, "w", encoding="utf-8") as f:
        json.dump(state_data, f, ensure_ascii=False, indent=4)

# Dosyadan gelen verileri hafızaya yükle
saved_data = load_state()

if "evolution_gen" not in st.session_state:
    st.session_state.evolution_gen = saved_data["evolution_gen"]
if "vector_nodes" not in st.session_state:
    st.session_state.vector_nodes = saved_data["vector_nodes"]
if "agent_fitness" not in st.session_state:
    st.session_state.agent_fitness = saved_data["agent_fitness"]
if "system_logs" not in st.session_state:
    st.session_state.system_logs = saved_data["system_logs"]

# 2. ARAYÜZ TASARIMI VE METİNLER
st.markdown("""
    <style>
    .stApp { background-color: #0b0f19; color: #f3f4f6; font-family: sans-serif; }
    .hero-container { padding: 2rem; background: #111827; border-radius: 10px; border: 1px solid #1f2937; margin-bottom: 2rem; }
    </style>
""", unsafe_allow_html=True)

st.markdown("""
    <div class="hero-container">
        <h1>⚛️ NEXUS-01 Kalıcı Bellek Paneli</h1>
        <p>Bu panel artık sayfa yenilense (F5 çekilse) bile verilerini kaybetmez, dosyaya kaydeder.</p>
    </div>
""", unsafe_allow_html=True)

# İSTATİSTİKLER
col1, col2, col3 = st.columns(3)
with col1:
    st.metric("Evrimsel Nesil (Gen)", f"Gen {st.session_state.evolution_gen}")
with col2:
    st.metric("Vektör Düğümleri", f"{st.session_state.vector_nodes} Düğüm")
with col3:
    st.metric("Ajan Başarısı", f"%{st.session_state.agent_fitness:.1f}")

st.divider()

# 3. İŞLEM BUTONU (Kalıcılığı Test Etme Yeri)
if st.button("🧬 Eğitimi İlerlet ve Dosyaya Kaydet"):
    # Değerleri artır
    st.session_state.evolution_gen += 1
    st.session_state.vector_nodes += 50
    st.session_state.agent_fitness = min(99.9, st.session_state.agent_fitness + 0.5)
    
    # Log ekle
    zaman = datetime.now().strftime('%H:%M:%S')
    st.session_state.system_logs.insert(0, f"[{zaman}] Yeni eğitime geçildi. Gen {st.session_state.evolution_gen} oldu.")
    
    # İŞTE EN ÖNEMLİ KISIM: Değişen verileri hemen dosyaya yaz!
    save_state()
    
    st.success(f"Başarıyla Gen {st.session_state.evolution_gen}'e geçildi ve diske kaydedildi! Şimdi sayfayı yenileyebilirsin.")

st.subheader("🛡️ Sistem Günlükleri (Loglar)")
log_box = st.container(height=200)
with log_box:
    for log in st.session_state.system_logs:
        st.text(log)
