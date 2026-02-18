import streamlit as st

# Configuration de la page
st.set_page_config(page_title="CV - El Hadji Oumar Ndiaye", page_icon="📍")

# Sidebar - Contact
st.sidebar.title("Contact")
st.sidebar.write("📧 elhadjioumarndiaye338@gmail.com")
st.sidebar.write("📞 77 240 25 20")
st.sidebar.write("📍 Hann Maristes 2, Dakar")

# Corps du CV
st.title("El Hadji Oumar Ndiaye")
st.subheader("Étudiant en BTS Géomatique")

st.markdown("---")
st.write("### 🎯 Objectif Professionnel")
st.write("Motivé, rigoureux et orienté résultats, je souhaite contribuer efficacement aux projets d'aménagement et de gestion territoriale.")

st.write("### 🎓 Formation")
st.write("**BTS Géomatique (En cours)** - CEDT Le G15")
st.write("- Cartographie numérique, SIG, Topographie.")
st.write("**Baccalauréat (2024)** - Collège Notre Dame du Liban")

st.write("### 🛠 Compétences Techniques")
col1, col2 = st.columns(2)
with col1:
    st.write("- **QGIS / ArcGIS**")
    st.write("- **AutoCAD**")
with col2:
    st.write("- **Collecte GPS**")
    st.write("- **Analyse spatiale**")