import streamlit as st

def subject_card(name, code, section, stats=None, footer_callback=None):
    with st.container(border=True):

        st.markdown(f"<h3 style='margin:0; color:#1e1b4b !important; font-size:1.4rem;'>{name}</h3>", unsafe_allow_html=True)

        st.markdown(
            f"""<p style='color:#475569 !important; margin:8px 0;'>
                Code: <span style='background:#e0e7ff; color:#4338ca; padding:3px 10px; border-radius:6px; font-weight:600;'>{code}</span>
                &nbsp;&nbsp; Section: <span style='background:#f1f5f9; color:#334155; padding:3px 10px; border-radius:6px; font-weight:600;'>{section}</span>
            </p>""",
            unsafe_allow_html=True
        )

        if stats:
            stat_html = '<div style="display:flex; gap:10px; flex-wrap:wrap; margin-top:8px;">'
            for stat_item in stats:
                if len(stat_item) == 3:
                    icon, label, value = stat_item
                    stat_html += f"""
                        <div style="background:linear-gradient(135deg, #eef2ff, #e0e7ff); padding:6px 14px; 
                                    border-radius:10px; font-size:0.88rem; color:#1e1b4b; border:1px solid #c7d2fe;">
                            {icon} <b>{value}</b> {label}
                        </div>"""
                elif len(stat_item) == 2:
                    label, value = stat_item
                    stat_html += f"""
                        <div style="background:linear-gradient(135deg, #eef2ff, #e0e7ff); padding:6px 14px; 
                                    border-radius:10px; font-size:0.88rem; color:#1e1b4b; border:1px solid #c7d2fe;">
                            <b>{value}</b> {label}
                        </div>"""
            stat_html += '</div>'
            st.markdown(stat_html, unsafe_allow_html=True)

        if footer_callback:
            footer_callback()