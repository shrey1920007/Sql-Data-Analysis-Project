import sqlite3

# Connect to SQLite database
conn = sqlite3.connect("superstore.db")
cursor = conn.cursor()

# Check table structure
cursor.execute("PRAGMA table_info(superstore);")
columns = cursor.fetchall()

# Print column names
print("✅ Columns in the 'superstore' table:")
for col in columns:
    print(col)

# Close connection
conn.close()
