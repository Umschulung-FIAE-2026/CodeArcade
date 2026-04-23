import streamlit as st
import memory

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
    {"titel": "Memory", "autor": "Simon Vinu", "beschreibung": "Ein Memory Spiel", "icon": "❓"},
    {"titel": "Snake Python", "autor": "Team B", "beschreibung": "Der Klassiker in Python.", "icon": "🐍"},
]

# 1. WICHTIG: Wir müssen die 'wahl' ganz oben abfragen, BEVOR wir etwas zeichnen!
wahl = st.session_state.get("aktuelles_spiel")

# --- LAYOUT: KACHELN ---
# 2. Die Kacheln werden NUR gezeichnet, wenn KEIN Spiel gewählt ist
if not wahl:

    cols = st.columns(3)

    for i, spiel in enumerate(spiele):
        col = cols[i % 3]

        with col:
            with st.container(border=True):
                st.subheader(f"{spiel['icon']} {spiel['titel']}")
                st.caption(f"Erstellt von: {spiel['autor']}")
                st.write(spiel['beschreibung'])

                # Ein Button für jedes Spiel
                if st.button(f"Spiel starten", key=f"btn_{i}", use_container_width=True):
                    st.session_state["aktuelles_spiel"] = spiel['titel']
                    st.rerun()  # <--- HIER das rerun() statt st.info()

# --- NAVIGATION ---
# 3. Wenn ein Spiel gewählt ist, wird dieser Teil hier unten aktiv
if wahl == "Memory":
    if st.button("⬅️ Zurück zur Übersicht"):
        st.session_state["aktuelles_spiel"] = None
        st.rerun()
    st.divider()
    memory.open_memory()

elif wahl == "Snake Python":
    if st.button("⬅️ Zurück zur Übersicht"):
        st.session_state["aktuelles_spiel"] = None
        st.rerun()
    st.divider()
    st.title("🐍 Snake Python")
    st.info("Hier entsteht bald das Snake-Spiel!")

# --- FOOTER ---
st.divider()
st.info("💡 Tipp für das Team: Um ein neues Spiel hinzuzufügen, ergänze einfach die Liste 'spiele' im Code!")