from horizontal_fragmentation import PHorizontalFragmentation

# Define predicates to segment sales data in Addis Ababa by amount and district
predicates = [
    ["amount <= 200", "amount > 200"],
    ["district = 'Bole'", "district = 'Yeka'", "district = 'Arada'", 
     "district = 'Lideta'", "district = 'Kirkos'", "district = 'Gullele'", "district = 'Nifas Silk'"]
]

# Initialize the PHorizontalFragmentation class with Addis Ababa-specific predicates
phf = PHorizontalFragmentation(predicates)

# Query the MySQL database and print results for each miniterm
results = phf.query_database(
    host="localhost",            # MySQL server host
    user="root",        # MySQL username
    password="IObed8528@",    # MySQL password
    database="addis_ababa_sales" # MySQL database name
)

# Print results for each miniterm query
for miniterm, rows in results.items():
    print(f"Results for: {miniterm}")
    if rows:
        for row in rows:
            print(row)
    else:
        print("No matching records found.")
    print("-" * 30)
