import requests

url = "https://api.jwplayer.com/v2/sites/{{site_id}}/media/"

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
    "Authorization": "API_KEY"
}

response = requests.post(url, json=payload, headers=headers)

# Put the media
put_url = response.json()['upload_link']
requests.put(url=put_url, data=open("{{path-to-video}}", 'rb').read())
