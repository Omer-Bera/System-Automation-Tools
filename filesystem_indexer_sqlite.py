import os
import sqlite3
from tqdm import tqdm

DB_PATH = "file_index.db"
ROOT_DIR = os.path.expanduser("~")
BATCH_SIZE = 1000

def init_db():
    conn = None
    try:
        conn = sqlite3.connect(DB_PATH)
        c = conn.cursor()
        c.execute("""
            CREATE TABLE IF NOT EXISTS files (
                id INTEGER PRIMARY KEY,
                name TEXT,
                path TEXT
            )
        """)
        c.execute("DELETE FROM files")
        conn.commit()
    finally:
        if conn:
            conn.close()

def index_files():
    conn = None
    try:
        conn = sqlite3.connect(DB_PATH)
        c = conn.cursor()

        files_to_insert = []
        total = sum(len(files) for _, _, files in os.walk(ROOT_DIR))
        pbar = tqdm(total=total, desc="🔍 Scanning files")

        for dirpath, _, filenames in os.walk(ROOT_DIR):
            for name in filenames:
                full_path = os.path.join(dirpath, name)
                files_to_insert.append((name, full_path))
                pbar.update(1)

                if len(files_to_insert) >= BATCH_SIZE:
                    c.executemany("INSERT INTO files (name, path) VALUES (?, ?)", files_to_insert)
                    files_to_insert.clear()

        if files_to_insert:
            c.executemany("INSERT INTO files (name, path) VALUES (?, ?)", files_to_insert)

        conn.commit()
        pbar.close()
        print("✅ Indexing completed.")
    except Exception as e:
        print(f"💥 An error occurred: {e}")
        if conn:
            conn.rollback()
    finally:
        if conn:
            conn.close()

if __name__ == "__main__":
    init_db()
    index_files()