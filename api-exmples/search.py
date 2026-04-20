# import requests

# def main():
#     user_input = input("Artist: ")
#     artists = get_artist(query=user_input, limit=3)
#     print(artists)

# def get_artist(query, limit):
#     response = requests.get(
#         "https://api.artic.edu/api/v1/artists/search",
#         params={
#             "q": query,
#             "limit": limit,
#         }
#     )
        
#     content = response.json()
#     return [artist["title"] for artist in content["data"]]

# main()
