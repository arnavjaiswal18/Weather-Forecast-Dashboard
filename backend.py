import requests

API_Key = "0e02578ed6c05a5115943665e6b40190"


def get_data(place, forecast_days=None, option=None):
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={place}&appid={API_Key}"
    response = requests.get(url)
    data = response.json()

    return data


if __name__ == "__main__":
    print(get_data(place="Kushinagar"))
