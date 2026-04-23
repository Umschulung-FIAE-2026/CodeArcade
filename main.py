import streamlit as st

# Konfiguration der Seite
st.set_page_config(
    page_title="Umschulung Projekt-Hub",
    page_icon="🎮",
    layout="wide"
)

# --- HEADER ---
st.title("🚀 Unser Spiele-Projekt-Hub")
st.markdown("""
Willkommen auf unserer gemeinsamen Startseite! Hier werden alle Spiele gesammelt, 
die wir im Rahmen unserer Umschulung entwickeln. 
Wähle eine Kachel aus, um das jeweilige Spiel zu starten.
""")

# --- MOCKUP DER SPIELE-DATEN ---
# Hier können später alle Teammitglieder ihre Spiele eintragen
spiele = [
    {"titel": "Quiz-Master", "autor": "Team A", "beschreibung": "Ein spannendes IT-Quiz.", "icon": "❓"},
    {"titel": "Snake Python", "autor": "Team B", "beschreibung": "Der Klassiker in Python.", "icon": "🐍"},
    {"titel": "Zahlenraten", "autor": "Team C", "beschreibung": "Finde die geheime Zahl.", "icon": "🔢"},
    {"titel": "Pflege-Simulator", "autor": "Deine Wenigkeit", "beschreibung": "Simulation eines Pflege-Alltags.",
     "icon": "🏥"},
]

# --- LAYOUT: KACHELN ---
# Wir erstellen ein Raster (Grid) mit 3 Spalten
cols = st.columns(3)

for i, spiel in enumerate(spiele):
    # Den Index nutzen, um die Spalte zu bestimmen (0, 1, 2, 0, 1, 2...)
    col = cols[i % 3]

    with col:
        with st.container(border=True):
            st.subheader(f"{spiel['icon']} {spiel['titel']}")
            st.caption(f"Erstellt von: {spiel['autor']}")
            st.write(spiel['beschreibung'])

            # Ein Button für jedes Spiel
            if st.button(f"Spiel starten", key=f"btn_{i}", use_container_width=True):
                st.session_state["aktuelles_spiel"] = spiel['titel']
                st.info(f"Hier würde jetzt das Spiel '{spiel['titel']}' geladen werden!")

# --- FOOTER ---
st.divider()
st.info("💡 Tipp für das Team: Um ein neues Spiel hinzuzufügen, ergänze einfach die Liste 'spiele' im Code!")