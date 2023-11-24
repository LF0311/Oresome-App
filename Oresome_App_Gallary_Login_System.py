import yaml
from yaml.loader import SafeLoader
import streamlit as st
import streamlit_authenticator as stauth


st.set_page_config(page_title='Oresome App Gallary Login System',
                   layout='centered', initial_sidebar_state='auto')

with open('config.yaml') as file:
    config = yaml.load(file, Loader=SafeLoader)

authenticator = stauth.Authenticate(
    config['credentials'],
    config['cookie']['name'],
    config['cookie']['key'],
    config['cookie']['expiry_days'],
    config['preauthorized']
)

name, authentication_status, username = authenticator.login('Oresome App Gallary Login System', 'main')

if authentication_status:
    st.header("Oresome Technology App Gallary")
    st.markdown(
        '<nobr><p style="text-align: left;font-family:arial; color:Black; font-size: 23px;">'
        'Welcome to the app gallary. We share the past and most <br> '
        'exciting IoT apps that have been deployed by our team. <br>'
        'Simply click on each app’s URL to view the app.<br>'
        ' We would love to hear your feedback.</p></nobr>',
        unsafe_allow_html=True)
    # st.subheader("Welcome to the app gallary. We share the past and most exciting IoT apps that have been deployed by "
    #              "our team. Simply click on each app’s URL to view the app. We would love to hear your feedback.")

    st.markdown("---")

    st.markdown(
        '<nobr><p style="text-align: left;font-family:arial; color:Black; font-size: 25px; font-weight: bold">'
        'Dexing Copper 34FT SAG Mill</p></nobr>',
        unsafe_allow_html=True)
    st.write(
        '<style>a {text-decoration: underline; color: blue; font-size: 18px}</style><a target="_blank" '
        'href="https://dexingcopper34ftsag22.onrender.com/">https://dexingcopper34ftsag22.onrender.com/</a>',
        unsafe_allow_html=True)
    st.markdown("")
    st.image("pics/example1.png")

    st.markdown("---")

    st.markdown(
        '<nobr><p style="text-align: left;font-family:arial; color:Black; font-size: 25px; font-weight: bold">'
        'Dexing Copper 34FT SAG Mill</p></nobr>',
        unsafe_allow_html=True)
    st.write(
        '<style>a {text-decoration: underline; color: blue; font-size: 18px}</style><a target="_blank" '
        'href="https://dexingcopper34ftsag22.onrender.com/">https://dexingcopper34ftsag22.onrender.com/</a>',
        unsafe_allow_html=True)
    st.markdown("")
    st.image("pics/example2.png")

    st.markdown("---")

elif authentication_status is False:
    st.error('Username/password is incorrect')
elif authentication_status is None:
    st.warning('Please enter your username and password')

hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """

st.markdown(hide_streamlit_style, unsafe_allow_html=True)
