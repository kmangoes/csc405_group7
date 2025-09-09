import requests 

url = "https://github.com/kmangoes/csc405_group7/blob/main/data/newdata.csv"
output_file = "newdata.csv"

print(f"Downloading {url}...")

response = requests.get(url, stream=True);

if (response.status_code == 200):
    with open(output_file, "wb") as file:
        for chunk in response.iter_content(chunk_size=8192):
            file.write(chunk)
    print(f"Downloade complete! Saved as {output_file}")
else: 
    print(f"Failed to download file. Status code: {response.status_code}")