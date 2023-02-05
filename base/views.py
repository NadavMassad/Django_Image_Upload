from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework.views import APIView
from .models import Image


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = '__all__'


class imgView(APIView):
    def get(self, request, id=-1):
        if int(id) > -1:
            try:
                my_model = Image.objects.get(id=(int(id)))
            except:
                return ("Doesn't Exist")
            serializer = ImageSerializer(my_model, many=False)
        else:
            my_model = Image.objects.all()
            serializer = ImageSerializer(my_model, many=True)
        return Response(serializer.data)
    def post(self, request):
        serializer = ImageSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)
    def delete(self, request, id=-1):
        if int(id) > -1:
            del_Image = Image.objects.get(id=int(id))
            del_Image.delete()
            return Response(f'Image With ID: {id} Was Deleted')
    def put(self, request, id=-1):
        if int(id) > -1:
            my_model = Image.objects.get(id=(int(id)))
            serializer = ImageSerializer(my_model, data=request.data)   
            if serializer.is_valid():
                serializer.save()
            return Response(serializer.data)
@api_view(['GET'])
def index(r):
    return Response("Hi")

@api_view(['GET'])
def testdata(r):
    return Response({"test":20})

# # Crud for the Images model(table) with serializer
# @api_view(['GET', 'POST', 'DELETE', 'PUT'])
# def images(request, id=-1):
#     if request.method == 'GET':
#         if int(id) > -1:
#             try:
#                 my_model = Image.objects.get(id=(int(id)))
#             except:
#                 return ("Doesn't Exist")
#             serializer = ImageSerializer(my_model, many=False)
#         else:
#             my_model = Image.objects.all()
#             serializer = ImageSerializer(my_model, many=True)
#         return Response(serializer.data)
#     if request.method == 'POST':
#         serializer = ImageSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#         return Response(serializer.data)
#     if request.method == 'DELETE':
#         if int(id) > -1:
#             del_Image = Image.objects.get(id=int(id))
#             del_Image.delete()
#             return Response(f'Image With ID: {id} Was Deleted')
#     if request.method == 'PUT':
#         if int(id) > -1:
#             my_model = Image.objects.get(id=(int(id)))
#             serializer = ImageSerializer(my_model, data=request.data)   
#             if serializer.is_valid():
#                 serializer.save()
#             return Response(serializer.data)

