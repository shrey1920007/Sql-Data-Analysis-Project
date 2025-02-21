import sqlite3
import pandas as pd

# Connect to SQLite database
conn = sqlite3.connect("superstore.db")
cursor = conn.cursor()

# Count total records
query_1 = "SELECT COUNT(*) FROM superstore;"
total_records = cursor.execute(query_1).fetchone()[0]
print(f"Total Records: {total_records}")

# Find total and average sales
query_2 = "SELECT SUM(sales), AVG(sales) FROM superstore;"
total_sales, avg_sales = cursor.execute(query_2).fetchone()
print(f"Total Sales: {total_sales:.2f}, Average Sales: {avg_sales:.2f}")

#  Filter dataset (Sales > 500)
query_3 = "SELECT * FROM superstore WHERE sales > 500;"
filtered_data = pd.read_sql(query_3, conn)
print(f"Filtered Records (sales > 500):\n{filtered_data}")

# Save query results to CSV
filtered_data.to_csv("filtered_results.csv", index=False)

# Close connection
conn.close()
