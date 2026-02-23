# Python Chrome Extension Downloader

A lightweight, dependency-free Python script that allows you to download and extract the raw source code (HTML, CSS, JS, manifest, etc.) of any Chrome Extension directly from the Chrome Web Store.

## Features

- **Zero Dependencies**: Uses only standard Python libraries (`urllib`, `zipfile`, `re`, `os`). You do not need to install `requests` or any other external packages.
- **Direct Extraction**: Bypasses the proprietary `.crx` headers to directly extract the contents of the extension as a clean directory package.
- **Easy to Use**: Interactively prompts for a Web Store URL and downloads it automatically.

## Usage

1. Clone this repository or download the `downloader.py` file.
2. Open your terminal and run the script:

   ```bash
   python downloader.py
   ```

3. Paste the URL of the extension from the Chrome Web Store when prompted. For example:
   ```
   https://chromewebstore.google.com/detail/google-translate/aapbdbdomjkkjkaonhjkkikimpobigie
   ```

The script will identify the extension ID, download the `.crx` file from Google's update servers, and extract its contents into a new directory named `extension_<ID>`.

## Disclaimer
This tool is for educational purposes and personal use. Please respect the copyright and intellectual property of extension developers when reviewing their code.
