# System Automation & Utility Tools

A collection of system utility scripts designed for task automation, hardware monitoring, and file management. These tools demonstrate practical usage of Python scripting, database interactions (SQLite), and Shell scripting for system administration tasks.

**Technologies:** Python 3, SQLite, Bash/Zsh, Pillow (PIL), System I/O.

## 📂 Repository Contents

### 1. File System Indexer (SQLite Optimized)
* **File:** `filesystem_indexer_sqlite.py`
* **Description:** A high-performance file crawler that indexes the local file system into an SQLite database.
* **Key Features:**
    * Implements **batch insertion** (`executemany`) for optimized database write performance.
    * Uses `os.walk` for recursive directory traversal.
    * Features a real-time progress bar (TQDM) for user experience (UX).
    * Handles database connection lifecycles safely (try/finally blocks).

### 2. Wi-Fi QR Code Generator
* **File:** `wifi_qr_generator.py`
* **Description:** A utility to generate connectable Wi-Fi QR codes with embedded custom logos.
* **Key Features:**
    * Leverages image processing (`Pillow`) to resize and overlay logos onto QR codes.
    * Configures QR error correction levels to maintain readability despite image manipulation.

### 3. macOS Battery Logger
* **File:** `macos_battery_logger.sh`
* **Description:** A shell script for monitoring power consumption metrics on macOS devices.
* **Key Features:**
    * Parses raw `ioreg` system output using `awk` for real-time voltage and amperage data.
    * Logs power usage (Watts) to a CSV file for time-series analysis.
    * Demonstrates proficiency in Unix/Linux piping and text processing.

## 🚀 How to Run

### Python Tools
```bash
# Install dependencies
pip install tqdm pillow qrcode

# Run indexer
python3 filesystem_indexer_sqlite.py

# Generate QR
python3 wifi_qr_generator.py
