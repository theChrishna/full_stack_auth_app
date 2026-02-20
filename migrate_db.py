import sqlite3
import os

# Path to the database
db_path = os.path.join('instance', 'users.db')

# Connect to the database
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

# Check if password column exists
cursor.execute("PRAGMA table_info(user)")
columns = [column[1] for column in cursor.fetchall()]

if 'password' not in columns:
    print("Adding 'password' column to user table...")
    cursor.execute("ALTER TABLE user ADD COLUMN password VARCHAR(200)")
    conn.commit()
    print("✅ Password column added successfully!")
else:
    print("Password column already exists.")

conn.close()
print("Migration complete!")
