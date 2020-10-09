from flask_restful import Resource, reqparse

lista_hoteis = [
    {"hotel_id": 1, "nome": "Alpha hotel", "estrelas": 4.3, "diaria": 430, "cidade": "Fortaleza"},
    {"hotel_id": 2, "nome": "Bravo hotel", "estrelas": 5.2, "diaria": 820, "cidade": "São Paulo"},
    {"hotel_id": 3, "nome": "Charloe hotel", "estrelas": 2.3, "diaria": 130, "cidade": "Bahia"}
]


class Hoteis(Resource):

    def get(self):
        return {"hoteis": lista_hoteis}


class Hotel(Resource):

    @staticmethod
    def retornar_hotel(self, hotel_id):
        for hotel in lista_hoteis:
            if hotel["hotel_id"] == hotel_id:
                return hotel

    def get(self, hotel_id):
        for hotel in lista_hoteis:
            if hotel["hotel_id"] == hotel_id:
                return hotel
        return {"Error": "Hotel not found."}, 404 #status http not found

    def delete(self, hotel_id):
        for hotel in lista_hoteis:
            if hotel["hotel_id"] == hotel_id:
                lista_hoteis.remove(hotel)
                return 1
        return {"error": "Impossible Delete hotel"}, 400 #status code bad request

    def post(self, hotel_id):
        #Pega os elementos do JSON
        argumentos = reqparse.RequestParser()
        argumentos.add_argument("nome")
        argumentos.add_argument("estrelas")
        argumentos.add_argument("diaria")
        argumentos.add_argument("cidade")

        #Retorna os elementos com chave:valor
        dados = argumentos.parse_args()


        novo_hotel = {
            "hotel_id": len(lista_hoteis) + 1,
            "nome": dados["nome"],
            "estrelas": dados["estrelas"],
            "diaria": dados["diaria"],
            "cidade": dados["cidade"]
        }
        lista_hoteis.append(novo_hotel)
        return novo_hotel, 201 # status code http created

    def put(self, hotel_id):
        pass





