import requests

REVIEW_ID=4
URL = f'http://127.0.0.1:8000/api/v1/reviews/{REVIEW_ID}'
REVIEW={
    'review':'Nueva review, actualizamos el contenido',
    'score':10
}


response1=requests.put(URL, json=REVIEW)
response2=requests.delete(URL)

def update(response):
    if response.status_code==200:
        print('La reseña se actualizó de forma correcta.')
        print(response.json())

    else :
        print(response.content)



def delete(response2):
    if response2.status_code == 200:
        print('La reseña se eliminó de forma correcta.')
        print(response2.json())

    else:
        print(response2.content)


#update(response)
delete(response2)