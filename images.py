import requests
import base64
import os

def create_from_data(data, output_dir):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    image_number = 0
    for element in data:
        if element["type"] != "image":
            continue
        image_number += 1
        image_name = f"image_{image_number}.webp"
        generate(element["description"] + ". Vertical image, fully filling the canvas.", os.path.join(output_dir, image_name))

def generate(prompt, output_file, size="1024x1792"):
    response = requests.post("http://localhost:5000/sdapi/v1/txt2img", json={
        "prompt": prompt,
        "width": int(size.split("x")[0]),
        "height": int(size.split("x")[1]),
        "steps": 25
    })
    response.raise_for_status()

    image_b64 = response.json()["images"][0]

    with open(output_file, "wb") as f:
        f.write(base64.b64decode(image_b64))
