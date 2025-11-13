from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, viewsets, filters
from .models import Product
from .serialziers import GetSerializer
class ProductListView(APIView):  # Nom to'g'rilandi
    def get(self, request):
         products = Product.objects.all()
         serializer = GetSerializer(products, many=True)
         return Response(serializer.data, status=status.HTTP_200_OK)

class PostDetail(APIView):
    def post(self, request):
        serializer = GetSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class PutViewSet(APIView):
    def get_object(self, pk):
        try:
            return Product.objects.get(pk=pk)
        except Product.DoesNotExist:
            return None

    def put(self, request, pk):
        snippet = self.get_object(pk=pk)
        serializer = GetSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        snippet = self.get_object(pk=pk)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
