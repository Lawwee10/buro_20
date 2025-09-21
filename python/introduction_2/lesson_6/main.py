import os
import requests
from pathlib import Path
import shutil


def save_picture(url,folder):
    payload = {"filter": "mp4,webm"}
    response = requests.get(url, params=payload).json()
    picture_link = response["url"]
    picture = requests.get(picture_link)        
    picture_extension = Path(picture_link).suffix
    filename = f"dog_0{picture_extension}"
    file_path = f"{folder}/{filename}"
    with open(file_path, 'wb') as file:
        file.write(picture.content)


def get_folder(folder):
    if os.path.isdir(folder):
        shutil.rmtree(folder)
    if not os.path.exists(folder):
        os.makedirs(folder)


if __name__ == "__main__":
    url = "https://random.dog/woof.json"
    folder = "dogs"
    get_folder(folder)
    for number in range(50): 
        save_picture(url, folder)
