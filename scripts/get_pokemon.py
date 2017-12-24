
def script():
    import requests, random
    number = random.randrange(1, 500)
    url = "http://pokeapi.co/api/v2/pokemon/%s"%number
    response = requests.get(url=url)
    json_response = response.json()
    name = json_response['forms'][0]['name']
    name = str(name).title()
    image = json_response['sprites']['front_default']
    binds = {}
    binds['name'] = name
    binds['image'] = image
    return binds


if __name__ == '__main__':
    a = script()
    print a
    print '%(name)s - %(image)s' % a
