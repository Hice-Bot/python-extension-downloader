import sys
import re
import urllib.request
import urllib.error
import zipfile
import os
import io

def download_extension_source(store_url, output_dir=None):
    # Extract extension ID from the URL using regex (32 characters, a-p)
    match = re.search(r'([a-p]{32})', store_url)
    if not match:
        print("Could not find a valid Chrome Extension ID in the URL.")
        return False
    
    ext_id = match.group(1)
    print(f"Found Extension ID: {ext_id}")
    
    # Standard URL for downloading CRX files from Google
    download_url = f"https://clients2.google.com/service/update2/crx?response=redirect&prodversion=114.0.0.0&acceptformat=crx2,crx3&x=id%3D{ext_id}%26uc"
    
    print("Downloading extension package (CRX)...")
    req = urllib.request.Request(
        download_url, 
        headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'}
    )
    
    try:
        with urllib.request.urlopen(req) as response:
            crx_data = response.read()
    except urllib.error.URLError as e:
        print(f"Failed to download the extension: {e}")
        return False

    if not output_dir:
        output_dir = f"extension_{ext_id}"
        
    os.makedirs(output_dir, exist_ok=True)
    
    print(f"Extracting source files to folder: {output_dir}...")
    
    try:
        # CRX files are basically ZIP files with a custom header prepended.
        # We need to find the start of the standard ZIP file by looking for the 'PK' magic number.
        zip_start = crx_data.find(b'PK\x03\x04')
        if zip_start == -1:
            print("Could not find ZIP header in the downloaded package.")
            return False
            
        zip_data = crx_data[zip_start:]
        
        # Extract the contents into memory and write to the output directory
        with zipfile.ZipFile(io.BytesIO(zip_data)) as zstream:
            zstream.extractall(output_dir)
            
        print(f"✅ Successfully downloaded and extracted extension to: {output_dir}")
        return True
    except zipfile.BadZipFile:
        print("Failed to extract the extension. The downloaded file might be corrupt.")
        return False
    except Exception as e:
        print(f"An error occurred during extraction: {e}")
        return False

if __name__ == "__main__":
    print("-" * 50)
    print("Chrome Extension Source Downloader")
    print("-" * 50)
    
    # Ask the user for the web store url
    url = input("Enter the Chrome Web Store URL of the extension:\n> ")
    download_extension_source(url.strip())
