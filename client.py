import requests

URL = 'http://127.0.0.1:8000/api/v1/reviews'
HEADERS = {'ACCEPT':'application/json'}#indica que el cliente puede aceptar como respuesta un objeto json
QUERYSET = {'page':1, 'limit':1}

#requests.get(URL)
response = requests.get(URL,headers=HEADERS,params=QUERYSET)
print(response)

if response.status_code == 200:
    print('Petición realizada de manera exitosa')
    #print(response.content)
    #print('\n')
    #print(response.headers)

    if response.headers.get('content-type') == 'application/json':
        reviews = response.json()
        for review in reviews:
            print(f"score: {review['score']} - {review['review']}" )
