import requests

def get_amount_of_comicses(url):
    response = requests.get(url)
    response.raise_for_status()
    amount = response.json()['num']
    return amount