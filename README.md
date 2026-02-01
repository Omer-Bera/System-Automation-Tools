# System Automation & Utility Tools

## Why this repo?
I believe if you have to do a task more than twice, you should automate it. This repository is a collection of scripts I wrote to handle boring daily tasks—like organizing files, sharing Wi-Fi, or monitoring hardware—so I don't have to do them manually.

It demonstrates my approach to **Python scripting, Database interactions (SQLite), and Low-level Shell scripting.**

## 📂 What's Inside?

### 1. File System Indexer (SQLite)
Indexing millions of files can be slow. I wanted a custom tool that could crawl my entire disk and store metadata efficiently.
* **File:** `filesystem_indexer_sqlite.py`
* **The "Engineer" Touch:** I used `executemany` for batch insertions instead of writing row-by-row. This drastically reduced the I/O overhead. Also added a progress bar (`tqdm`) because staring at a frozen cursor is annoying.

### 2. Wi-Fi QR Code Generator
Sharing complex Wi-Fi passwords with guests is a pain. I built this tool to generate a scan-to-connect QR code.
* **File:** `wifi_qr_generator.py`
* **The "Engineer" Touch:** It doesn't just create a QR code; it uses `Pillow` to embed a custom logo in the center and adjusts the Error Correction Level (ECC) so the code remains scannable even with the image overlay.

### 3. macOS Battery Logger (Shell Script)
I wanted to analyze my laptop's power consumption in real-time without installing heavy third-party apps.
* **File:** `macos_battery_logger.sh`
* **The "Engineer" Touch:** It parses raw `ioreg` system output using `awk` to extract precise voltage and amperage data, then calculates wattage on the fly and logs it to a CSV for analysis.

## 🚀 Usage

### Python Tools
```bash
# Install requirements
pip install tqdm pillow qrcode

# Index your files
python3 filesystem_indexer_sqlite.py

# Create a Wi-Fi QR
python3 wifi_qr_generator.py
