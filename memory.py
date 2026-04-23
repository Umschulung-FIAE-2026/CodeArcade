import streamlit as st

def open_memory():
    st.header("❓ Memory")
    st.write("Finde die passenden Paare!")

    # Hier kommt deine Spiellogik rein
    # Beispiel für den Anfang:
    if st.button("Klick mich für Spiel-Action"):
        st.confetti()