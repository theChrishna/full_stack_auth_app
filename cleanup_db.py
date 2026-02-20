import os
import time

# Wait a moment for any processes to release the file
time.sleep(1)

db_files = ['instance/users.db', 'instance/database.db']

for db_file in db_files:
    if os.path.exists(db_file):
        try:
            os.remove(db_file)
            print(f"✅ Deleted {db_file}")
        except Exception as e:
            print(f"❌ Could not delete {db_file}: {e}")
    else:
        print(f"ℹ️  {db_file} does not exist")

print("\n✅ Database cleanup complete!")
