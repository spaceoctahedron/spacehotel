import streamlit as st
import pandas as pd
import plotly.express as px
from datetime import datetime, timedelta
import numpy as np

colors = ['#8b76e9','#EA2081','#52BCFF','#EEA705','#00923f']


# Set the title of the application (in French for users)
st.set_page_config(
    page_title="Tableau de bord", 
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


st.title("Tableau de bord")

# Create three columns
col1, col2, col3 = st.columns([1, 2, 1])

# Column 1: Revenue Data
with col1:
    st.subheader("Revenus par Catégorie")
    data = {
        "Catégorie": ["Chambres", "Nourriture & Boissons", "Téléphone", "Autres", "Total"],
        "Revenus (FCFA)": [213549000, 86755930, 3041000, 130891290, 434237220]
    }
    df_revenues = pd.DataFrame(data).set_index("Catégorie")

    def style_dataframe(df):
        return df.style.format({
            'Revenus (FCFA)': lambda x: f"{x:,.0f}".replace(",", " ").replace(".", ",")
        }).set_properties(**{
            'text-align': 'right',
            'font-family': 'monospace',
            'font-size': 'smaller'
        }).apply(lambda x: ['font-weight: bold' if x.name == 'Total' else '' for i in x], axis=1)

    styled_df = style_dataframe(df_revenues)
    st.write(styled_df.to_html(escape=False), unsafe_allow_html=True)

# Column 2: Ring Diagram
with col2:
    st.markdown("<h3 style='text-align: center;'>Sources de Réservation</h3>", unsafe_allow_html=True)
    data = {
        'Source': ['Autre', 'Hors ligne (téléphone)', 'Répétition', 'En ligne', 'Ami/Référence'],
        'Pourcentage': [1, 28, 6, 62, 3]
    }

    fig = px.pie(
        data,
        values='Pourcentage',
        names='Source',
        hole=0.5,
        color_discrete_sequence=colors
    )

    fig.update_layout(
        font=dict(size=18),
        showlegend=False,
        annotations=[dict(text='Total des<br>réservations<br>180', x=0.5, y=0.5, showarrow=False)]
    )

    fig.update_traces(textposition='outside', textinfo='percent+label')

    st.plotly_chart(fig, use_container_width=True)


# Column 3: Average Ratios
with col3:
    st.subheader("Ratios Moyens")
    data = {
        "Indicateur": ["TRM", "RevPAR", "Taux d'occupation"],
        "Valeur": ["111 512 FCFA", "63 627 FCFA", "53 %"]
    }

    df_ratios = pd.DataFrame(data).set_index("Indicateur")

    styled_df = style_dataframe(df_ratios)
    st.write(styled_df.to_html(escape=False), unsafe_allow_html=True)
    st.caption("TRM = Tarif Moyen Journalier")
    st.caption("RevPAR = Revenu par Chambre Disponible")


# Set random seed for reproducibility
np.random.seed(2025)

# Generate daily data for March 2025
start_date = datetime(2025, 3, 1)
end_date = datetime(2025, 3, 31)
date_range = [start_date + timedelta(days=x) for x in range((end_date - start_date).days + 1)]

# Generate realistic daily amounts
chambres_daily = np.random.normal(213549000 / 31, 1000000, 31)
nourriture_boissons_daily = np.random.normal(86755930 / 31, 500000, 31)
autres_daily = np.random.normal((130891290) / 31, 300000, 31)

# Create a DataFrame
df = pd.DataFrame({
    'Date': date_range,
    'Chambres': chambres_daily,
    'Nourriture & Boissons': nourriture_boissons_daily,
    'Autres': autres_daily
})

# Set the Date column as the index
df.set_index('Date', inplace=True)

# Create the Streamlit line chart
st.subheader('Revenus Journaliers par Catégorie - Mars 2025')
st.line_chart(df, use_container_width=True, color = colors[:3])


