import sqlite3
import pandas as pd
import os

# Input CSV (from your ChEMBL fetch script)
data_file = "data/ChEMBL_Compound_Info.csv"

# Connect to database
db_path = "chembl_data.db"
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

# Create table
cursor.execute("""
CREATE TABLE IF NOT EXISTS chembl_compounds (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    chembl_id TEXT UNIQUE NOT NULL,
    compound_name TEXT,
    formula TEXT,
    inchi TEXT,
    smiles TEXT,
    pubmed_id TEXT,
    doi TEXT,
    journal TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
""")

# Load data
df = pd.read_csv(data_file)

# Rename columns if needed
expected_cols = ["ChEMBL_ID", "Name", "Formula", "InChI", "SMILES", "PubMed_ID", "DOI", "Journal"]
df.columns = expected_cols[:len(df.columns)]

# Insert rows
for _, row in df.iterrows():
    cursor.execute("""
        INSERT OR IGNORE INTO chembl_compounds 
        (chembl_id, compound_name, formula, inchi, smiles, pubmed_id, doi, journal)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    """, (
        row["ChEMBL_ID"], row["Name"], row["Formula"], row["InChI"],
        row["SMILES"], row["PubMed_ID"], row["DOI"], row["Journal"]
    ))

conn.commit()
conn.close()

print(f"✅ Database created and populated successfully at {db_path}")
