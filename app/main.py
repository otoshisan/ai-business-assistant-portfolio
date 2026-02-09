import requests

GAS_ENDPOINT = "https://script.google.com/macros/s/AKfycbw3o0gE839mO2_-46dTgbUNrVTtEj68vYe_IWOhihpMtv3fVyQFUmITqgRNMu3of7XyLw/execsqBd7sgqbQ/exec"

res = requests.post(
    GAS_ENDPOINT,
    json={"ping": "test"},
    headers={"Content-Type": "application/json"}
)

print(res.status_code)
print(res.text)
