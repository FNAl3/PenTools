import requests
import pyfiglet
from bs4 import BeautifulSoup
import argparse
import os
from urllib.parse import urljoin, urlparse

def download_js(url, folder):
    try:
        if not os.path.exists(folder):
            os.makedirs(folder)

        print(f"[*] Crawling {url}...")
        headers = {'User-Agent': 'Mozilla/5.0'}
        response = requests.get(url, headers=headers, timeout=5)
        soup = BeautifulSoup(response.text, "html.parser")

        scripts = [script.get('src') for script in soup.find_all('script') if script.get('src')]

        print(f"[*] Found {len(scripts)} script tags.")

        for script_src in scripts:
            # Handle relative URLs
            full_url = urljoin(url, script_src)
            
            # Get filename
            parsed_url = urlparse(full_url)
            filename = os.path.basename(parsed_url.path)
            if not filename.endswith('.js'):
                filename += '.js'
                
            filepath = os.path.join(folder, filename)
            
            # Download
            try:
                print(f"    [+] Downloading {filename}...")
                js_content = requests.get(full_url, headers=headers, timeout=5).content
                with open(filepath, 'wb') as f:
                    f.write(js_content)
            except Exception as e:
                print(f"    [!] Failed to download {filename}: {e}")

        print(f"[*] Download complete. Files saved in {folder}/")

    except Exception as e:
        print(f"[!] Error: {e}")

def main():
    ascii_banner = pyfiglet.figlet_format("PenTools \n JS Crawler")
    print(ascii_banner)

    parser = argparse.ArgumentParser(description='JS Crawler - Download all .js files from a page')
    parser.add_argument('url', help='Target URL (e.g. http://example.com)')
    parser.add_argument('-o', '--output', default='js_files', help='Output directory (default: js_files)')
    
    args = parser.parse_args()
    
    download_js(args.url, args.output)

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        pass
    except SystemExit:
        pass
    except Exception as e:
        print(f"Error: {e}")
    input("\nPress Enter to exit...")
