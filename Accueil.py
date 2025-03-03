import streamlit as st
import cloudinary
import cloudinary.uploader
import cloudinary.api
from cloudinary.utils import cloudinary_url
from datetime import datetime

cloudinary.config(
    cloud_name=st.secrets["cloudinary"]["cloud_name"],
    api_key=st.secrets["cloudinary"]["api_key"],
    api_secret=st.secrets["cloudinary"]["api_secret"],
    secure=True
)

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

#st.image("./assets/im/cover/Plage.jpg", use_container_width=True)
st.image("https://res.cloudinary.com/ddhhnrgcs/image/upload/w_800,h_400,c_fill,r_20,q_auto,f_auto/v1740948700/f79e996d_1_z0hntx.jpg", use_container_width=True)

# Application Header
st.title("Bienvenue à l'Hôtel Riviera Ramatou Plage")

# Room Reservation Section
st.subheader("Réservation de chambre")
st.write("Sélectionnez vos dates de séjour et réservez votre chambre.")

col1, col2, col3 = st.columns(3)

with col1:
    num_guests = st.number_input("Nombre de personnes", min_value=1, max_value=10, value=2)

with col2:
    date_arrival = st.date_input("Date d'arrivée", datetime.today())

with col3:
    date_departure = st.date_input("Date de départ", datetime.today())

days_stayed = (date_departure - date_arrival).days + 1


if st.button("Valider la réservation"):
    if date_arrival and date_departure:
        if date_arrival > date_departure:
            st.error("La date d'arrivée doit être avant la date de départ.")
        else:
            st.success(f"Vous avez sélectionné un séjour du {date_arrival} au {date_departure} pour {num_guests} personnes.")


# Room Information Section
st.subheader("Chambres actuellement disponibles")
st.write("Veuillez sélectionner une chambre pour voir le prix total de votre séjour.")

room_images = [
    "https://res.cloudinary.com/ddhhnrgcs/image/upload/w_600,h_400,c_fill,r_20,q_auto,f_auto/v1740948995/78896c32_zpkm3z.jpg",
    "https://res.cloudinary.com/ddhhnrgcs/image/upload/w_600,h_400,c_fill,r_20,q_auto,f_auto/v1740948994/9dec39e8_wmkdlj.jpg",
    "https://res.cloudinary.com/ddhhnrgcs/image/upload/w_600,h_400,c_fill,r_20,q_auto,f_auto/v1740948995/384593fc_1_ob01sd.jpg"
]

room_details = [
    {"name": "Suite Luxe - Vue Jardin", "description": "Chambre Deluxe, 1 très grand lit, vue jardin", "price": 70},
    {"name": "Chambre Supérieure", "description": "Chambre Double Standard, 1 lit double", "price": 54},
    {"name": "Chambre Classique", "description": "Chambre Double Standard, 1 lit double", "price": 54}
]

if "selected_room" not in st.session_state:
    st.session_state.selected_room = None
if "name" not in st.session_state:
    st.session_state.name = ""
if "email" not in st.session_state:
    st.session_state.email = ""
if "phone" not in st.session_state:
    st.session_state.phone = ""

col1, col2, col3 = st.columns(3)
cols = [col1, col2, col3]

for idx, col in enumerate(cols):
    with col:
        st.image(room_images[idx], caption=room_details[idx]["description"], use_container_width=True)
        st.write(f"**{room_details[idx]['price']} € par nuit** (taxes et frais compris)")
        if st.button(f"Réserver", key=f"reserve_{idx}"):
            st.session_state.selected_room = room_details[idx]

if st.session_state.selected_room:
    total_price = st.session_state.selected_room['price'] * days_stayed
    st.write(f"### Vous avez sélectionné : {st.session_state.selected_room['name']}")
    st.write(f"Prix total pour {days_stayed} nuit(s) : **{total_price} €** (taxes et frais compris)")
    
    st.session_state.name = st.text_input("Nom complet", st.session_state.name)
    st.session_state.email = st.text_input("Email", st.session_state.email)
    st.session_state.phone = st.text_input("Téléphone", st.session_state.phone)
    
    if st.button("Soumettre la réservation"):
        if st.session_state.name and st.session_state.email and st.session_state.phone:
            st.success(f"Merci {st.session_state.name}, votre réservation pour {st.session_state.selected_room['name']} est confirmée.")
            st.success(f"Total à payer sur place : {total_price} €")
        else:
            st.error("Veuillez remplir toutes les informations pour confirmer la réservation.")




# Accommodation Information Section
st.subheader("À propos de cet hébergement")
col1, col2, col3 = st.columns(3)

with col1:
    st.write("🏊 Piscine")
    st.write("🏖️ Sur une plage privée")
    
with col2:
    st.write("🍹 Bar")
    st.write("🥐 Petit-déjeuner disponible")

with col3:
    st.write("🛎️ Service d’étage")
    st.write("🧺 Blanchisserie")

# Additional Services in Expander
with st.expander("Afficher tous les détails de l’hébergement"):
    st.write("🌐 Internet - Disponible dans toutes les chambres : Wi-Fi gratuit")
    st.write("📶 Disponible dans certaines parties communes : Wi-Fi gratuit")
    st.write("🚗 Parking - Parking sans voiturier disponible gratuitement sur place")
    st.write("🛬 Navette - Navette vers et depuis l’aéroport disponible 24 h/24 (en supplément)")
    st.write("🍽️ Petit déjeuner - Petit déjeuner continental moyennant un supplément")
    st.write("⏰ Servi tous les jours de 07 h 30 à 11 h 00")
    st.write("💰 7 EUR pour les adultes et 7 EUR pour les enfants")
    st.write("🍔 Nourriture et boissons - 2 restaurants, snack-bar/épicerie fine, un bar/salon, un café")
    st.write("🏊 Piscine - 1 piscine extérieure et 1 piscine pour enfants (Accès : 08 h 00 - 18 h 00)")
    st.write("🚫 Animaux de compagnie - Animaux non admis")
    st.write("📺 Activités - Télévision dans les parties communes")
    st.write("👨‍👩‍👧‍👦 Pour les familles - Chambres insonorisées, laverie, piscine pour enfants")
    st.write("🔐 Commodités - Casiers, consigne à bagages, réception ouverte 24 h/24")
    st.write("🌍 Services aux voyageurs - Personnel polyglotte, service de ménage quotidien")
    st.write("🏢 Services professionnels - 2 salles de réunion, 250 m² d’espace de conférence")
    st.write("🏕️ Extérieur - Aire de pique-nique, barbecue, jardin, terrasse, plage privée")
    st.write("♿ Accessibilité - Chemin d’accès bien éclairé, pas d’ascenseur, salles de réunion avec assistance auditive")



# Restaurant Information Section
st.subheader("Restaurant de l'hôtel")
st.write("Dégustez une cuisine raffinée préparée par nos chefs étoilés.")
st.image("https://res.cloudinary.com/ddhhnrgcs/image/upload/w_600,h_400,c_fill,r_20,q_auto,f_auto/v1740949163/foodcarousel10_qxebpi.jpg", caption="Restaurant gastronomique", use_container_width=True)

# Event Booking Section
st.subheader("Événements et Réservations de salles")
st.write("Organisez vos événements privés ou professionnels dans un cadre prestigieux. Nous offrons des services pour mariages, conférences et séminaires.")
col1, col2 = st.columns(2)
with col1:
    st.image("https://res.cloudinary.com/ddhhnrgcs/image/upload/w_600,h_400,c_fill,r_20,q_auto,f_auto/v1740960169/Table_Romantique_en_Bord_de_Mer_yzq03y.avif", caption="🌿 Table Romantique en Bord de Mer – Mariage ou Dîner Privé", use_container_width=True)

with col2:
    st.image("https://res.cloudinary.com/ddhhnrgcs/image/upload/w_600,h_400,c_fill,r_20,q_auto,f_auto/v1740960168/Salle_de_R%C3%A9ception_%C3%89l%C3%A9gante_wrbnyk.webp", caption="🍽️ Salle de Réception Élégante – Idéale pour Dîners et Événements", use_container_width=True)




# Footer
st.write("---")
st.write("📍 Hôtel Riviera Ramatou Plage, Lomé, Togo")
st.map(data={'latitude': [6.151954701940698], 'longitude': [1.3012933984910968]})
st.write("☎️ Contact: +228 90 87 44 44 / +228 92 70 00 10")
st.write("✉️ Email: hotelriviera19@gmail.com")

# Copyright Footer
current_year = datetime.today().year
st.write(f"© {current_year} Hôtel Riviera Ramatou Plage")
