import streamlit as st
import streamlit_authenticator as stauth
import yaml
from yaml.loader import SafeLoader

# Load configuration
with open('users.yaml') as file:
    config = yaml.load(file, Loader=SafeLoader)

# Create authenticator
authenticator = stauth.Authenticate(
    config['credentials'],
    config['cookie']['name'],
    config['cookie']['key'],
    config['cookie']['expiry_days'],
    config['cookie']['key']
)

# Test login
st.title("Authentication Test")
authenticator.login("Login")

if st.session_state["authentication_status"]:
    st.success(f'Welcome *{st.session_state["name"]}*')
    authenticator.logout("Logout")
elif st.session_state["authentication_status"] == False:
    st.error('Username/password is incorrect')
elif st.session_state["authentication_status"] == None:
    st.warning('Please enter your username and password')

# Display test credentials
st.sidebar.header("Test Credentials")
st.sidebar.text("Student: pes2ug20cs000 / abc")
st.sidebar.text("Faculty: sample@gmail.com / 123")
st.sidebar.text("Admin: admin / 1") 