import requests

url = "https://api.jwplayer.com/v2/sites/CivsmZGh/media/"

payload = {
    "upload": {
        "method": "direct",
    },
    "metadata": {
        "tags": ["thisTag", "ThatTag"],
        "title": "My video",
        "description": "some information",
        "author": "Jonny",
        "category": "Careers",
        "language": "en"
    }
}
headers = {
    "Accept": "application/json",
    "Content-Type": "application/json",
    "Authorization": "TG5D7vab8RU8Q8W0y9h2tWInYWpoellsVkpPRk5aWTBWM1Z6aEdOMHhVWjJwNVltRTQn"
}

response = requests.post(url, json=payload, headers=headers)

# Put the media
put_url = response.json()['upload_link']
requests.put(url=put_url, data=open("/home/fuel/Videos/test.mp4", 'rb').read())