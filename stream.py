import streamlit as st
st.set_page_config(page_title="Multistore - Dashboards", 
                   page_icon="📊", 
                   layout="wide")
import stream_arribos
import stream_arribos_historico
import stream_pendientes_facturar
from streamlit_option_menu import option_menu
from streamlit_cookies_manager import EncryptedCookieManager
import os

# Estilo
with open("styles.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

USERNAMES = ["administracion", "Facu", "operativo"]
PASSWORDS = ["1234", "123", "12345"]

def login(username, password):
    if username in USERNAMES and password in PASSWORDS:
        return True
    return False

# Initialize cookies manager
cookies = EncryptedCookieManager(prefix="multistore_", password="your_secret_password")

if not cookies.ready():
    st.stop()


# Check if user is already logged in
if 'logged_in' not in st.session_state:
    st.session_state.logged_in = cookies.get("logged_in", False)
if 'username' not in st.session_state:
    st.session_state.username = cookies.get("username", "")

if not st.session_state['logged_in']:
    st.title("Login")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    if st.button("Login"):
        if login(username, password):
            st.session_state['logged_in'] = True
            st.session_state.username = username
            cookies["logged_in"] = str(True)  # Convert to string
            cookies["username"] = username  # Username is already a string
            cookies.save()  # Persist the changes
            st.success("Usuario logeado")
            st.rerun()
        else:
            st.error("Usuario o clave invalidos")
else:
    page_selection = option_menu(
            None,  # No menu title
            ["Arribos", "Arribos - histórico", "Items pendientes de Facturar", "Logout"],  
            icons=["arrow-down-circle", "book", "file-earmark-excel", "box-arrow-right"],   
            menu_icon="cast",  
            default_index=0, 
            orientation="horizontal")
    if page_selection == "Arribos":
        stream_arribos.show_page_arribos()  
    elif page_selection == "Arribos - histórico":
        stream_arribos_historico.show_page_arribos_historico()
    elif page_selection == "Items pendientes de Facturar":
        stream_pendientes_facturar.show_page_pendientes_facturar()
    elif page_selection == "Logout":
        cookies.pop("logged_in", None)
        cookies.pop("username", None)
        cookies.save()
        st.session_state['logged_in'] = False
        st.session_state['username'] = ""
        st.rerun()
