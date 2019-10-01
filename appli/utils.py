import json

def add_Beer(response):
    filename='addBeer.json'
    with open(filename, 'w') as f:
        json.dump(response.json(), f)
def drink_Beer(response):
    filename='drinkBeer.json'
    with open(filename, 'w') as f:
        json.dump(response.json(), f)