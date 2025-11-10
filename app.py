import streamlit as st
import sqlite3
import pandas as pd

DB_PATH = "chembl_data.db"

st.title("🧬 ChEMBL Compound Database Browser")

@st.cache_data
def load_data():
    conn = sqlite3.connect(DB_PATH)
    df = pd.read_sql_query("SELECT * FROM chembl_compounds", conn)
    conn.close()
    return df

df = load_data()

search = st.text_input("🔍 Search compound (by ChEMBL ID, Name, or Formula)")
if search:
    df = df[df.apply(lambda row: search.lower() in str(row).lower(), axis=1)]

st.dataframe(df)

csv = df.to_csv(index=False).encode("utf-8")
st.download_button("⬇️ Download Filtered Results as CSV", csv, "filtered_compounds.csv", "text/csv")
