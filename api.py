import requests

def main():
    print("Search the Art Institute of Chicago!")
    query = input("Enter artist or topic: ")
    
    url = "https://api.artic.edu/api/v1/artworks/search"
    headers = {"User-Agent": "Mozilla/5.0"}
    query_params = {
        "q": query,
        "limit": 3
    }
    
    try:
        response = requests.get(url, headers=headers, params=query_params)
        response.raise_for_status()
        
        content = response.json()
        
        if not content["data"]:
            print("Nothing found.")
        else:
            for artwork in content["data"]:
                print(f"[*] {artwork['title']}")
            
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP Error: {http_err}")
    except Exception as err:
        print(f"Error: {err}")

main()