import requests

import csv

csvf = open('pokemon.csv', 'w')
csvw = csv.writer(csvf, delimiter=',')
f = open('location.csv', 'w')
w = csv.writer(f, delimiter=',')


csvw.writerow(['What are the Pokemon (up to Gen 3) in each habitat?'])
w.writerow(['How many Pokemon (up to Gen 3) are in each habitat?'])
csvw.writerow(['Location','Pokemon'])
w.writerow(['Location','# of Pokemon'])

endpoint = 'http://pokeapi.co/api/v2/'


location = 'pokemon-habitat/'

url = endpoint + location

r = requests.get(url)
print(r.url)

data = r.json()


pokehabitat = data['results']

y = 0
for habitat in pokehabitat:
    print(habitat['name'])
    print(habitat['url'])
    
    x = 0
    
    url1 = habitat['url']
    p = requests.get(url1)
    data1 = p.json()
    pokemon =  data1['pokemon_species']
    for name in pokemon:
        csvw.writerow([habitat['name'],name['name']])
        x += 1
    w.writerow([habitat['name'],x])
    y += x

w.writerow(['Total',y])

csvf.close()
f.close()