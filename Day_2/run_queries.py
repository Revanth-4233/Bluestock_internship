import sqlite3
import re

conn = sqlite3.connect('bluestock_mf.db')

with open('queries.sql', 'r') as f:
    sql_script = f.read()

# Remove comment lines (lines starting with --) from the whole script first
lines = sql_script.split('\n')
clean_lines = [line for line in lines if not line.strip().startswith('--')]
clean_script = '\n'.join(clean_lines)

# Now split into individual queries by semicolon
queries = [q.strip() for q in clean_script.split(';') if q.strip()]

print(f"Found {len(queries)} queries\n")

for i, q in enumerate(queries, 1):
    print(f"--- Query {i} ---")
    try:
        cursor = conn.execute(q)
        rows = cursor.fetchall()
        cols = [desc[0] for desc in cursor.description]
        print(cols)
        for row in rows[:5]:
            print(row)
    except Exception as e:
        print("ERROR:", e)
    print()

conn.close()