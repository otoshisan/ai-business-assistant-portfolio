import requests

GAS_ENDPOINT = "https://script.google.com/macros/s/AKfycbw-AlHYpie5zIoAXEzyuh3C9hsi5uEqHjY_ibaO_IujrlHi5u5I4Q-O7kryHFibXhmqDQ/exec"

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
