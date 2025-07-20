from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response


class ProductAPIView(APIView):
    
    def get(self, request):
        return Response({"message": "Hello this view is functional",
                         "products": [
                             {"id": 1, "name": "Produto 1","description": "Amazing product", "price": 10.50,"seller": "Bob"},
                             {"id": 2, "name": "Produto 2","description": "Amazing product", "price": 11.88,"seller": "Bob"},
                             {"id": 3, "name": "Produto 3","description": "Amazing product", "price": 13.47,"seller": "Bob"},
                             {"id": 4, "name": "Produto 4","description": "Amazing product", "price": 10.59,"seller": "Bob"}
                         ]})