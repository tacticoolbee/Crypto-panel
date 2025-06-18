import os
# Konfig klasörünü geçici alan olarak ayarlıyoruz
os.environ["STREAMLIT_SUPPRESS_CONFIG_ERRORS"] = "1"
os.environ["STREAMLIT_RUNTIME_METRICS_ENABLED"] = "0"
os.environ["XDG_CONFIG_HOME"] = "/tmp/app_config"
os.environ["STREAMLIT_SUPPRESS_CONFIG_WARNINGS"] = "1"
os.environ["STREAMLIT_SERVER_HEADLESS"] = "true"

import streamlit as st

st.set_page_config(page_title="Crypto Panel", layout="wide")

st.title("Merhaba, Kripto Paneline Hoşgeldiniz")
st.markdown("Bu panel üzerinden canlı fiyat takibi, sinyal analizi ve alarm sistemini kullanabilirsiniz.")

# Demo örnek içerik
st.info("Sistem başarıyla yüklendi. Geliştirmeye buradan devam edebilirsin.")
