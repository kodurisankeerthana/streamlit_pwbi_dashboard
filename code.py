# Import necessary libraries
import pandas as pd
import streamlit as st 

# Display information on the Streamlit app
st.text('{this is streamlit generated}')
st.title(':blue[PWBI_Dashboard]')
st.info('Displaying PWBI Dashboard in Streamlit')
st.subheader(':rainbow[new way of demonstrating your dashboards through Streamlit]')

# Users database (for demo authentication)
users_db = {
    'admin': {'password': 'admin', 'c_br_code': None},
    'keeru': {'password': 'pass1', 'c_br_code': 612},
    'rajeev': {'password': 'pass2', 'c_br_code': 613},
    'veena': {'password': 'pass3', 'c_br_code': 614},
    'krishna': {'password': 'pass4', 'c_br_code': 615}
}

# Power BI base URL (your report embed URL)
base_power_bi_url = "https://app.powerbi.com/reportEmbed?reportId=2b33ec73-95e5-418e-86c4-19e5f8b0cdd2&autoAuth=true&ctid=1e3bab2c-ff49-4d6c-827a-5017e6fd859c"

# Function to authenticate users
def authenticate(username, password):
    if username in users_db and users_db[username]['password'] == password:
        return True, users_db[username]['c_br_code']
    return False, None

# Function to generate Power BI URL with filter and hidden filters pane
def generate_power_bi_url(c_br_code):
    # Construct filter for the Power BI report
    filter_url = f"&$filter=sales_table/c_br_code eq {c_br_code}&filterPaneEnabled=false"
    return base_power_bi_url + filter_url

# User input fields for username and password
username = st.text_input('Username')
password = st.text_input('Password', type='password')

# Login button logic
if st.button('Login'):
    is_authenticated, user_c_br_code = authenticate(username, password)
    
    if is_authenticated:
        st.success(f"Welcome {username}, you have access to data for c_br_code: {user_c_br_code}")
        
        # Generate the Power BI URL with the user's c_br_code filter
        power_bi_filtered_url = generate_power_bi_url(user_c_br_code)
        
        # Embed the filtered Power BI report using an iframe
        st.markdown(f'''
            <iframe width="130%" height="1500px" src="{power_bi_filtered_url}" frameborder="0" allowFullScreen="true"></iframe>
        ''', unsafe_allow_html=True)
    else:
        st.error('Invalid username or password')

# Logout button logic
if st.button('Logout'):
    st.write('Logged out')
