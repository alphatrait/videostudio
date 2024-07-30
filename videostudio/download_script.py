import os
import requests

def download_file(url, folder_path):
    local_filename = url.split('/')[-1]  # Extracts the file name from the URL
    local_filepath = os.path.join(folder_path, local_filename)
    
    # Check if file already exists
    if not os.path.exists(local_filepath):
        response = requests.get(url, stream=True)
        with open(local_filepath, 'wb') as f:
            for chunk in response.iter_content(chunk_size=8192):
                f.write(chunk)
        return local_filepath
    return local_filepath  # Return the path where the file is saved

def download_assets(asset_urls, folder_path):
    # Ensure the folder exists
    os.makedirs(folder_path, exist_ok=True)
    
    # Download each asset
    for url in asset_urls:
        print(f"Downloading {url}")
        download_file(url, folder_path)