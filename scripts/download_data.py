# Download the raw data

import os
import requests
import zipfile

# Dataset URL
url = "https://archive.ics.uci.edu/static/public/502/online+retail+ii.zip"

# Path file and extraction
raw_data_dir = os.path.join("..", "data", "raw")
zip_path = os.path.join(raw_data_dir, "online_retail_ii.zip")

os.makedirs(raw_data_dir, exist_ok=True)

# Download the file
if not os.path.exists(zip_path):
    print("Downloading dataset...")
    response = requests.get(url)
    with open(zip_path, "wb") as f:
        f.write(response.content)
    print("Download complete.")
else:
    print("ZIP file already exists. Skipping download.")

# Extract the content
with zipfile.ZipFile(zip_path, "r") as zip_ref:
    zip_ref.extractall(raw_data_dir)
    print("Extraction complete.")
