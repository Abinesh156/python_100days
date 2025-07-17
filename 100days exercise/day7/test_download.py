import requests
import time
import sys
import os
import json
import mysql.connector

# === SETTINGS ===
url = "https://data.opensanctions.org/datasets/20250619/default/entities.ftm.json"
local_filename = "entities.ftm.json"

# === DATABASE CONFIG ===
db_config = {
    "host": "localhost",
    "user": "root",
    "password": "root",
    "database": "test"
}

# === TERMINAL UI HELPERS ===
def clear_screen():
    sys.stdout.write("\033[2J")
    sys.stdout.write("\033[H")
    sys.stdout.flush()

def move_cursor_to_bottom():
    try:
        rows = os.get_terminal_size().lines
    except OSError:
        rows = 24
    sys.stdout.write(f"\033[{rows};0H")
    sys.stdout.flush()

def print_ui_header():
    print("🔽 Downloading OpenSanctions Entity Dataset")
    print("==========================================\n")

# === DOWNLOAD FILE ===
response = requests.get(url, stream=True)
total_size = int(response.headers.get('content-length', 0))
chunk_size = 1024 * 1024
downloaded = 0
last_update = time.time()

clear_screen()
print_ui_header()

with open(local_filename, 'wb') as f:
    for chunk in response.iter_content(chunk_size=chunk_size):
        if chunk:
            f.write(chunk)
            downloaded += len(chunk)

            if time.time() - last_update >= 1:
                mb_downloaded = downloaded / (1024 * 1024)
                mb_total = total_size / (1024 * 1024)
                percent = (downloaded / total_size) * 100

                move_cursor_to_bottom()
                sys.stdout.write(f"\n📦 Progress: {mb_downloaded:.2f} MB / {mb_total:.2f} MB ({percent:.2f}%)   ")
                sys.stdout.flush()
                last_update = time.time()

# Final download line
mb_downloaded = downloaded / (1024 * 1024)
mb_total = total_size / (1024 * 1024)
percent = (downloaded / total_size) * 100
move_cursor_to_bottom()
sys.stdout.write(f"✅ Download Complete: {mb_downloaded:.2f} MB / {mb_total:.2f} MB ({percent:.2f}%)   \n")
sys.stdout.flush()

print("\n📁 File saved to:", local_filename)
print("⏳ Starting MySQL import...\n")

# === PARSE NDJSON FORMAT ===
entities = []
with open(local_filename, 'r', encoding='utf-8') as f:
    for line in f:
        try:
            obj = json.loads(line.strip())
            entities.append(obj)
        except json.JSONDecodeError as e:
            print(f"❌ Skipping malformed line: {e}")

# === CONNECT TO MYSQL ===
conn = mysql.connector.connect(**db_config)
cursor = conn.cursor()

# 🔧 Create table if not exists
create_table_query = """
CREATE TABLE IF NOT EXISTS entities (
    id VARCHAR(255) PRIMARY KEY,
    schema_name VARCHAR(100),
    name TEXT,
    country VARCHAR(10)
)
"""
cursor.execute(create_table_query)

# ✅ SQL Insert Statement
insert_query = """
    INSERT INTO entities (id, schema_name, name, country)
    VALUES (%s, %s, %s, %s)
    ON DUPLICATE KEY UPDATE name=VALUES(name), country=VALUES(country)
"""

# 🔁 Insert rows
inserted = 0
for item in entities:
    entity_id = item.get("id")
    schema_name = item.get("schema")
    name = item.get("name")
    country = item.get("countries", [None])[0]

    if entity_id:
        cursor.execute(insert_query, (entity_id, schema_name, name, country))
        inserted += 1

# ✅ Finalize
conn.commit()
cursor.close()
conn.close()

print(f"\n✅ Inserted {inserted} entities into MySQL!")
