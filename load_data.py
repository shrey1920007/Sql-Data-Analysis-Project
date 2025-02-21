import sqlite3
import pandas as pd

# Load dataset (force tab delimiter if needed)
df = pd.read_csv("Superstore.csv", sep="\t")

# Rename columns for SQL compatibility (remove spaces)
df.rename(columns=lambda x: x.lower().replace(" ", "_"), inplace=True)

# Connect to SQLite database
conn = sqlite3.connect("superstore.db")
cursor = conn.cursor()

# Drop table if exists (to avoid conflicts)
cursor.execute("DROP TABLE IF EXISTS superstore")

# Create table with proper column names
df.to_sql("superstore", conn, if_exists="replace", index=False)

print("✅ Database created and data loaded successfully!")

# Close connection
conn.commit()
conn.close()
