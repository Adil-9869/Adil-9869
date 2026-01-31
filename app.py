import streamlit as st
import os

# --------------------------------------------------
# PAGE CONFIG
# --------------------------------------------------
st.set_page_config(
    page_title="Adil Husain | Data Analytics Portfolio",
    page_icon="📊",
    layout="wide"
)

# --------------------------------------------------
# HARD OVERRIDE STREAMLIT LAYOUT
# --------------------------------------------------
st.markdown("""
<style>
.block-container {
    padding-top: 1.5rem !important;
    padding-bottom: 0 !important;
}
.element-container {
    margin-bottom: 0 !important;
}
hr { display: none !important; }

.stApp {
    background:
        radial-gradient(circle at 20% 10%, #111827 0%, #0b0f14 45%, #0a0d12 100%);
}

/* NAVBAR */
.navbar {
    position: sticky;
    top: 0;
    z-index: 999;
    background: rgba(11,15,20,0.92);
    backdrop-filter: blur(10px);
    padding: 12px 0;
}

.nav-items {
    display: flex;
    justify-content: center;
    gap: 42px;
}

.nav-items a {
    color: #e5e7eb;
    font-weight: 600;
    text-decoration: none;
    padding: 6px 14px;
    border-radius: 6px;
}

.nav-items a:hover {
    background-color: rgba(255,255,255,0.06);
}

/* TYPOGRAPHY */
h1, h2, h3 {
    color: #f9fafb;
    letter-spacing: 0.3px;
}
p, li {
    color: #9ca3af;
    line-height: 1.75;
}

/* CARDS */
.card {
    background: rgba(255,255,255,0.02);
    border-radius: 12px;
    padding: 24px;
    margin-top: 22px;
}

/* BUTTONS */
.icon-btn a {
    display: inline-block;
    margin-top: 8px;
    margin-right: 10px;
    padding: 8px 16px;
    border-radius: 8px;
    border: 1px solid rgba(255,255,255,0.12);
    color: #e5e7eb;
    text-decoration: none;
    font-weight: 600;
    background: rgba(0,0,0,0.2);
}
.icon-btn a:hover {
    background: rgba(255,255,255,0.08);
}

img { border-radius: 14px; }
</style>
""", unsafe_allow_html=True)

# --------------------------------------------------
# NAVBAR
# --------------------------------------------------
st.markdown("""
<div class="navbar">
    <div class="nav-items">
        <a href="#about">About</a>
        <a href="#projects">Projects</a>
        <a href="#contact">Contact</a>
    </div>
</div>
""", unsafe_allow_html=True)

# --------------------------------------------------
# HERO
# --------------------------------------------------
c1, c2 = st.columns([1, 4])

with c1:
    if os.path.exists("images/profile.jpeg"):
        st.image("images/profile.jpeg", width=150)

with c2:
    st.title("Adil Husain")
    st.subheader("Technical Analyst | Data Analytics | Python & SQL")
    st.write(
        "I work at the intersection of **engineering thinking and data analytics**, "
        "transforming operational data into clear, reliable insights that support "
        "business and IT decision-making."
    )

# ==================================================
# ABOUT
# ==================================================
st.markdown('<a id="about"></a>', unsafe_allow_html=True)
st.header("About Me")

st.write("""
I am a **Technical Analyst at HCL Technologies** with hands-on experience in
**asset management, reporting, and analytics support**.

With a background in **Mechanical Engineering**, I bring structured problem-solving
skills and apply them using **Python, SQL, Excel, and Power BI** to build
accurate reports, dashboards, and analytical datasets.
""")

st.subheader("🧠 Core Technical Skills")

st.markdown("""
### 🐍 Python — Data Analysis
- Pandas & NumPy for structured data analysis  
- Data cleaning, transformation & validation  
- Analytical automation and reporting scripts  

### 🗄️ SQL — Analytics & Reporting
- Complex joins, CTEs & subqueries  
- KPI calculation & metric validation  
- Query optimization for reporting use cases  

### 📊 Excel — Business Reporting
- Pivot tables & analytical summaries  
- Data validation & reconciliation  
- Stakeholder-ready reports  

### 📈 Power BI — Business Intelligence
- Data modeling & relationships  
- DAX measures & calculated columns  
- Executive dashboards & KPI tracking  

### 📉 Data Analytics & Business Analysis
- Translating business requirements into metrics  
- Insight generation & storytelling  
- Supporting operational and management decisions  

### 📐 Foundational Data Science
- Descriptive statistics & data exploration  
- Basic hypothesis testing  
- Practical analytical reasoning  
""")

# ==================================================
# EXPERIENCE
# ==================================================
st.header("Professional Experience")

st.markdown('<div class="card">', unsafe_allow_html=True)
st.subheader("HCL Technologies — Technical Analyst")
st.write("""
**Feb 2023 – Present | Asset Management**

- Improved IT asset tracking accuracy and reporting reliability  
- Streamlined recurring reports for faster decision-making  
- Collaborated with cross-functional IT and operations teams  
- Supported data-driven process improvements  
""")
st.markdown("</div>", unsafe_allow_html=True)

# ==================================================
# PROJECTS
# ==================================================
st.markdown('<a id="projects"></a>', unsafe_allow_html=True)
st.header("Projects")

st.markdown('<div class="card">', unsafe_allow_html=True)
st.subheader("VenomSQL — Executive Analytics Dashboard")
st.write("""
A **SQL-focused analytics project** designed to build executive-level KPIs,
structured reporting views, and decision-ready insights.
""")
st.markdown("""
<div class="icon-btn">
<a href="https://github.com/Venom-Shivu/VenomSQL-Executive-Analytics-Dashboard" target="_blank">
View Repository
</a>
</div>
""", unsafe_allow_html=True)
st.markdown("</div>", unsafe_allow_html=True)

st.markdown('<div class="card">', unsafe_allow_html=True)
st.subheader("Numerical Simulation Project — Mechanical Engineering")
st.write("""
Study of numerical simulation of staggered cylinder arrays under
different Reynolds number regimes, focusing on analytical modeling
and simulation-based insights.
""")
st.markdown("</div>", unsafe_allow_html=True)

# ==================================================
# CONTACT
# ==================================================
st.markdown('<a id="contact"></a>', unsafe_allow_html=True)
st.header("Contact & Opportunities")

st.write("""
Open to **Data Analyst, Technical Analyst, and Analytics-focused roles**
where strong SQL, reporting, and business analytics skills are valued.
""")

st.markdown("""
<div class="icon-btn">
<a href="https://www.linkedin.com" target="_blank">LinkedIn</a>
<a href="https://github.com/Venom-Shivu" target="_blank">GitHub</a>
<a href="mailto:husainadil786@gmail.com">Email</a>
</div>
""", unsafe_allow_html=True)

st.caption("© 2026 Adil Husain | Data Analytics Portfolio")
