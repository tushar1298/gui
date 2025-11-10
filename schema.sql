-- schema.sql
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
