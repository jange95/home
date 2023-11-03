
import streamlit as st
import pandas as pd
import mariadb

# Function to establish a MySQL connection and execute a query
@st.cache(ttl=600)
def get_data_from_database():
    conn = mariadb.connect(
        host="192.168.0.243",
        user="root",
        password="esp22",
        database="home"
    )
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM temperature')
    data = cursor.fetchall()
    columns = [i[0] for i in cursor.description]
    conn.close()
    df = pd.DataFrame(data, columns=columns)
    return df

# Retrieve data from the database
df = get_data_from_database()

# Print results
for index, row in df.iterrows():
    st.write(f"{row['wert']}")
