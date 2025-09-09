import requests
import os
from urllib.parse import urlparse
import uuid

def main():
    print("🌍 Welcome to the Ubuntu Image Fetcher")
    print("A tool for mindfully collecting images from the web\n")
    url = input("Please enter the image URL: ").strip()
    
    try:
        
        os.makedirs("Fetched_Images", exist_ok=True)
        
        response = requests.get(url, timeout=10)
        response.raise_for_status()  
        
        
        parsed_url = urlparse(url)
        filename = os.path.basename(parsed_url.path)
        if not filename or "." not in filename:
            filename = f"image_{uuid.uuid4().hex}.jpg"
        filepath = os.path.join("Fetched_Images", filename)
        with open(filepath, 'wb') as f:
            f.write(response.content)
            
        print(f"✓ Successfully fetched: {filename}")
        print(f"✓ Image saved to {filepath}")
        print("\n🤝 Connection strengthened. Community enriched.")
        
    except requests.exceptions.MissingSchema:
        print("✗ Invalid URL. Please include http:// or https://")
    except requests.exceptions.Timeout:
        print("✗ Request timed out. Please try again.")
    except requests.exceptions.HTTPError as e:
        print(f"✗ HTTP error: {e}")
    except requests.exceptions.RequestException as e:
        print(f"✗ Connection error: {e}")
    except Exception as e:
        print(f"✗ Unexpected error: {e}")

if __name__ == "__main__":
    main()
