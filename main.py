#importamos requests
import requests
import json



if __name__ == '__main__':
    # si if name... geneamos una variable llamada url
    # url = 'https://www.google.com/?hl=es'

    # #con la libreria requests importada puedo ejecutar el siguiente metodo
    # # que recibe un parametro y sera la url
    # # el metodo get nos devuelve un objeto de tipo response, ese objeto lo almacenamos en esta variable
    # response = requests.get(url)

    # if response.status_code == 200:
    #     content = response.content
    #     file = open('google.html', 'wb')
    #     file.write(content)
    #     file.close()

    url = 'https://httpbin.org/get'
    args = { 'nombre': 'David', 'curso': 'Python', 'nivel': 'intermedio'}
    #con la libreria requests importada puedo ejecutar el siguiente metodo
    # que recibe un parametro y sera la url
    # el metodo get nos devuelve un objeto de tipo response, ese objeto lo almacenamos en esta variable
    response = requests.get(url, params=args)
    print(response.url)

    if response.status_code == 200:
        """
        response_json = response.json() #diccionario
        origin = response_json['origin']
        print(origin)
        """
        response_json = json.loads(response.text)
        origin = response_json['origin']
        print(origin)
        

