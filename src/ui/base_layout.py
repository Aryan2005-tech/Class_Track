import streamlit as st

def style_background_home():
    st.markdown("""
    <style>
        .stApp {
            background: linear-gradient(135deg, #6366f1 0%, #818cf8 40%, #a78bfa 70%, #7c3aed 100%) !important;
        }

        .stApp div[data-testid="stColumn"] {
            background: rgba(255, 255, 255, 0.92) !important;
            padding: 2.5rem !important;
            border-radius: 2.5rem !important;
            box-shadow: 0 20px 60px rgba(0, 0, 0, 0.15) !important;
        }
    </style>
    """, unsafe_allow_html=True)

def style_background_dashboard():
    st.markdown("""
        <style>
        .stApp {
            background: #ede9fe !important;
        }
        </style>
        """,
        unsafe_allow_html=True)
    
def style_base_layout():
    import streamlit as st
    st.markdown("""
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Climate+Crisis:YEAR@1979&display=swap');
        @import url('https://fonts.googleapis.com/css2?family=Outfit:wght@100..900&display=swap');

        /* Hide Top Bar of streamlit */
        #MainMenu, footer, header {
            visibility: hidden;
        }

        .block-container {
            padding-top: 1.5rem !important;
        }

        h1 {
            font-family: 'Climate Crisis', sans-serif !important;
            font-size: 3.5rem !important;
            line-height: 1.1 !important;
            margin-bottom: 0rem !important;
            color: #1e1b4b !important;
        }
        h2 {
            font-family: 'Climate Crisis', sans-serif !important;
            font-size: 2rem !important;
            line-height: 0.9 !important;
            margin-bottom: 0rem !important;
            color: #1e1b4b !important;    
        }
        h3 {
            font-family: 'Outfit', sans-serif !important;
            font-weight: 700 !important;
            color: #1e1b4b !important;
        }
        p, span, label, .stMarkdown {
            color: #334155 !important;
        }
        
        button {
            border-radius: 1.5rem !important;
            background: linear-gradient(135deg, #6366f1, #818cf8) !important;
            color: white !important;
            padding: 10px 20px !important;
            border: none !important;
            font-weight: 600 !important;
            box-shadow: 0 4px 15px rgba(99, 102, 241, 0.3) !important;
            transition: all 0.25s ease-in-out !important;
        } 
                
        button[kind="secondary"] {
            background: linear-gradient(135deg, #ec4899, #f472b6) !important;
            box-shadow: 0 4px 15px rgba(236, 72, 153, 0.3) !important;
        }

        button[kind="tertiary"] {
            border-radius: 1.5rem !important;
            background: linear-gradient(135deg, #ddd6fe, #c4b5fd) !important;
            color: #3b0764 !important;
            padding: 10px 20px !important;
            border: none !important;
            font-weight: 600 !important;
            box-shadow: 0 2px 10px rgba(196, 181, 253, 0.4) !important;
            transition: all 0.25s ease-in-out !important;
        }  
        button:hover {
            transform: scale(1.04) !important;
            filter: brightness(1.08) !important;
        }

        .stTextInput > div > div > input {
            border-radius: 0.75rem !important;
            border: 2px solid #c4b5fd !important;
            background: #f5f3ff !important;
            color: #1e1b4b !important;
            padding: 0.6rem 1rem !important;
        }
        .stTextInput > div > div > input::placeholder {
            color: #7c7c9a !important;
            opacity: 1 !important;
        }
        .stTextInput > div > div > input:focus {
            border-color: #6366f1 !important;
            box-shadow: 0 0 0 3px rgba(99, 102, 241, 0.15) !important;
            background: #ffffff !important;
        }
        .stTextInput label {
            color: #475569 !important;
            font-weight: 600 !important;
        }

        .stSelectbox label {
            color: #475569 !important;
            font-weight: 600 !important;
        }
        .stSelectbox > div > div {
            background: #f5f3ff !important;
            border-radius: 0.75rem !important;
            border: 2px solid #c4b5fd !important;
            color: #1e1b4b !important;
        }
        .stSelectbox [data-baseweb="select"] span {
            color: #1e1b4b !important;
        }
        [data-baseweb="menu"] {
            background: #faf8ff !important;
        }
        [data-baseweb="menu"] li {
            color: #1e1b4b !important;
        }
        [data-baseweb="menu"] li:hover {
            background: #e0e7ff !important;
        }

        div[data-testid="stVerticalBlockBorderWrapper"] {
            border-radius: 1.25rem !important;
            border-color: #ddd6fe !important;
            box-shadow: 0 4px 20px rgba(99, 102, 241, 0.08) !important;
            background: #faf8ff !important;
        }

        hr {
            border: none !important;
            height: 2px !important;
            background: linear-gradient(90deg, transparent, #c7d2fe, #ddd6fe, #c7d2fe, transparent) !important;
        }

        .stDataFrame {
            border-radius: 1rem !important;
        }
        .stDataFrame [data-testid="stDataFrameResizable"] {
            background: white !important;
        }
        .stDataFrame thead tr th {
            background: #f1f5f9 !important;
            color: #0f172a !important;
        }
        .stDataFrame tbody tr td {
            background: white !important;
            color: #0f172a !important;
        }
        .stDataFrame tbody tr:hover td {
            background: #f5f3ff !important;
        }
        [data-testid="stDataFrame"] canvas + div {
            background: white !important;
        }
        [data-testid="stDataFrame"] {
            background: white !important;
            border-radius: 1rem !important;
            overflow: hidden !important;
        }

        .stSubheader, [data-testid="stSubheader"] {
            color: #1e1b4b !important;
        }

        div[role="dialog"] {
            background: #faf8ff !important;
            border-radius: 1.5rem !important;
            box-shadow: 0 25px 60px rgba(0, 0, 0, 0.2) !important;
        }
        div[role="dialog"] h1,
        div[role="dialog"] h2,
        div[role="dialog"] h3,
        div[role="dialog"] p,
        div[role="dialog"] span,
        div[role="dialog"] label {
            color: #1e1b4b !important;
        }
        div[role="dialog"] .stTextInput > div > div > input {
            background: white !important;
            color: #1e1b4b !important;
            border: 2px solid #c4b5fd !important;
        }
        div[role="dialog"] .stTextInput > div > div > input::placeholder {
            color: #94a3b8 !important;
            opacity: 1 !important;
        }
        div[role="dialog"] .stSelectbox > div > div {
            background: white !important;
            color: #1e1b4b !important;
            border: 2px solid #c4b5fd !important;
        }

        .stCode, .stCodeBlock,
        pre, code,
        [data-testid="stCode"],
        .stMarkdownContainer pre {
            background: #f5f3ff !important;
            color: #1e1b4b !important;
            border-radius: 0.75rem !important;
            border: 1px solid #ddd6fe !important;
        }
        div[role="dialog"] pre,
        div[role="dialog"] code,
        div[role="dialog"] [data-testid="stCode"] {
            background: white !important;
            color: #1e1b4b !important;
            border: 1px solid #c4b5fd !important;
        }
                              
        </style>
        """,
        unsafe_allow_html=True
    )
