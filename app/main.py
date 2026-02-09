import requests

GAS_ENDPOINT = "https://script.google.com/macros/s/AKfycbxyZkOkQUYE0M7aIyRz0SrXTYM9XS11gT7NrEkcijaD12yE-E_tYyKrLQbERrk6a3PY3A/exec"

def create_reservation(data: dict):
    response = requests.post(
        GAS_ENDPOINT,
        json=data,
        headers={"Content-Type": "application/json"}
    )
    return response.text


if __name__ == "__main__":
    reservation = {
        "name": "テスト太郎",
        "date": "2026-02-15",
        "time": "19:00",
        "people": 2,
        "note": "カウンター希望"
    }

    result = create_reservation(reservation)
    print(result)
