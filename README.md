# System Automation Tools

This repository contains Python and Shell scripts that I wrote to automate personal tasks and explore system-level interactions.

Please note that these scripts are written for educational and personal use.

## Files

* **`filesystem_indexer_sqlite.py`**: A Python script that crawls the home directory and indexes file metadata into an SQLite database for fast querying.
* **`wifi_qr_generator.py`**: Generates scannable Wi-Fi QR codes with custom logo embedding using the `qrcode` and `Pillow` libraries.
* **`macos_battery_logger.sh`**: A Zsh script that parses `ioreg` output to log real-time battery voltage and amperage data to a CSV file.

## Usage

Install the required Python packages:

```bash
pip install tqdm pillow qrcode
