import requests

url = "http://localhost:8000/upload/"
file_path = "/path/to/your/file.jpg"

with open(file_path, 'rb') as f:
    files = {'file': (file_path, f)}
    response = requests.post(url, files=files)

if response.status_code == 200:
    print("Upload successful!")
    print("UUID:", response.json()['file_uuid'])
    print("Download URL:", f"http://localhost:8000/media/{response.json()['file_uuid']}")
else:
    print("Error:", response.json())