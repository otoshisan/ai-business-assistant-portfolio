import requests

GAS_ENDPOINT = "https://script.google.com/macros/s/AKfycbw-AlHYpie5zIoAXEzyuh3C9hsi5uEqHjY_ibaO_IujrlHi5u5I4Q-O7kryHFibXhmqDQ/exec"

res = requests.post(
    GAS_ENDPOINT,
    json={"ping": "test"},
    headers={"Content-Type": "application/json"}
)

print(res.status_code)
print(res.text)
