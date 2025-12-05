import requests
import argparse
import sys
import os

def download_file(url, output_name=None):
    try:
        if not output_name:
            output_name = url.split("/")[-1]
            if not output_name:
                output_name = "downloaded_file"
        
        print(f"[*] Downloading {url}...")
        r = requests.get(url, allow_redirects=True)
        r.raise_for_status()
        
        with open(output_name, 'wb') as f:
            f.write(r.content)
            
        print(f"[+] Download completed: {output_name} saved.")
    except Exception as e:
        print(f"[-] Error: {e}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Simple File Downloader")
    parser.add_argument("url", help="URL of the file to download")
    parser.add_argument("-o", "--output", help="Name of the output file")
    
    args = parser.parse_args()
    download_file(args.url, args.output)