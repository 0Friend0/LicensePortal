from django.http import Http404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from licenses.models import Client, License
from api.serializers import ClientSerializer, ClientDetailSerializer, LicenseSerializer, LicenseDetailSerializer


class apiHome(APIView):
    """
    Welcome to License Portal API
    """
    
    def get(self, request):
        api_url ={
            'Licenses List': '/licenses',
            'License Details': '/licenses/<str:pk>',
            'Clients List': '/clients',
            'Client Details': '/clients/<str:pk>',
        }

        return Response(api_url)


class clients(APIView):
    """
    List or add Clients
    """
    
    def get(self, request):
        clients = Client.objects.all()
        serializer = ClientSerializer(clients, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ClientSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class clientDetails(APIView):
    """
    View of selected Client.
    """

    def get_object(self, pk):
        try:
            return Client.objects.get(pk=pk)
        except Client.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        clients = self.get_object(pk)
        serializer = ClientSerializer(clients, many=False)
        return Response(serializer.data)

    def put(self, request, pk):
        client = self.get_object(pk)
        serializer = ClientDetailSerializer(client, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        client = self.get_object(pk)
        client.delete()
        return Response(f"Client was deleted: {client.name}")


class licenses(APIView):
    """
    List or add License
    """
    
    def get(self, request):
        license = License.objects.all()
        serializer = LicenseSerializer(license, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = LicenseSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class licenseDetails(APIView):
    """
    View of selected License.
    """


    def get_object(self, pk):
        try:
            return License.objects.get(pk=pk)
        except License.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        license = self.get_object(pk)
        serializer = LicenseSerializer(license, many=False)
        return Response(serializer.data)

    def put(self, request, pk):
        client = self.get_object(pk)
        serializer = LicenseDetailSerializer(client, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        license = self.get_object(pk)
        license.delete()
        return Response(f"License was deleted: {license.name}")