import streamlit as st

# Set the title of the application (in French for users)
st.set_page_config(
    page_title="Hôtel Riviera Ramatou Plage", 
    layout="wide",
    page_icon="./assets/logo/hotel-ramatou-logo.png")
st.markdown("""
<style>
[data-testid="stSidebar"] img {
    width: 100%;
    height: auto;
}
</style>
""", unsafe_allow_html=True)
st.logo("./assets/logo/hotel-ramatou-logo.png")


st.subheader("Tableau de bord")
st.success("📈 Accédez à un tableau de bord interactif pour suivre les performances de l'hôtel, y compris les réservations et les revenus.")
