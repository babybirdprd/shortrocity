import subprocess
import os

def create(data, output_folder):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    n = 0
    for element in data:
        if element["type"] != "text":
            continue

        n += 1
        output_file = os.path.join(output_folder, f"narration_{n}.wav")
        
        subprocess.run(["melo", element["content"], output_file, "--language", "EN", "--speaker", "EN-US"])

