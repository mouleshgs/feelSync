import requests

def get_spotify_token(client_id, client_secret):
    url = "https://accounts.spotify.com/api/token"
    data = {"grant_type": "client_credentials"}
    response = requests.post(url, data=data, auth=(client_id, client_secret))
    return response.json().get("access_token")

def search_playlist_by_genre(genre, access_token):
    url = f"https://api.spotify.com/v1/search?q={genre}&type=playlist&limit=1"
    headers = {"Authorization": f"Bearer {access_token}"}
    response = requests.get(url, headers=headers)
    playlists = response.json().get("playlists", {}).get("items", [])
    
    if playlists:
        playlist = playlists[0]
        playlist_url = playlist["external_urls"]["spotify"]
        image_url = playlist["images"][0]["url"] if playlist["images"] else None
        return playlist_url, image_url
    
    return None, None
