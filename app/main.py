import requests

GAS_ENDPOINT = "https://script.google.com/macros/s/AKfycbzYFncM2krub5I6aa9iM090TPFJUbmlXkEhny7PVP2VXLfITwPe9ej_jyVHsqBd7sgqbQ/exec"

res = requests.post(
    GAS_ENDPOINT,
    json={"ping": "test"},
    headers={"Content-Type": "application/json"}
)

print(res.status_code)
print(res.text)
