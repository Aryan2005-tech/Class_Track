import streamlit as st

def header_home():
    logo_url = "https://i.ibb.co/YTYGn5qV/logo.png"

    st.markdown(f"""
        <div style="display:flex; flex-direction:column; align-items:center; justify-content:center; margin-bottom:30px; margin-top:30px;">
            <img src='{logo_url}' style='height:100px; filter: drop-shadow(0 4px 12px rgba(0,0,0,0.2));' />
            <h1 style='text-align:center; color:white !important; text-shadow: 0 2px 15px rgba(0,0,0,0.2);'>CLASS<br>TRACK</h1>
        </div>
    """, unsafe_allow_html=True)

def header_dashboard():
    logo_url = "https://i.ibb.co/YTYGn5qV/logo.png"

    st.markdown(f"""
        <div style="display:flex; align-items:center; justify-content:center; gap:12px; margin-top:30px;">
            <img src='{logo_url}' style='height:85px; filter: drop-shadow(0 2px 8px rgba(0,0,0,0.1));' />
            <h2 style='text-align:center; color:#4f46e5 !important; margin:0;'>CLASS<br>TRACK</h2>
        </div>
    """, unsafe_allow_html=True)    
