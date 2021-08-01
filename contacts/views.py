# from django.views.decorators.csrf import csrf_exempt
# from rest_framework import status
# from rest_framework.decorators import api_view
# from rest_framework.response import Response
# from contacts.models import Contact
# from contacts.serializers import ContactSerializer
#
# # Optional format suffixes to URLs
# # Since our responses are no longer hardwired to a single content type
# # add support for format suffixes to API endpoints. Using format suffixes
# # gives us URLs that explicitly refer to a given format and means our API
# # will be able to handle URLs
#
# @csrf_exempt
# @api_view(['GET', 'POST'])
# def contacts_list(request, format=None):
#     """
#     List all contacts, or create a new contact.
#     """
#     if request.method == 'GET':
#         contacts = Contact.objects.all()
#         serializer = ContactSerializer(contacts, many=True)
#         return Response(serializer.data)
#
#     elif request.method == 'POST':
#         serializer = ContactSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
# @csrf_exempt
# @api_view(['GET', 'PUT', 'DELETE'])
# def contact_detail(request, pk, format=None):
#     """
#     Retrieve, update or delete a contact.
#     """
#     try:
#         contact = Contact.objects.get(pk=pk)
#     except Contact.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)
#
#     if request.method == 'GET':
#         serializer = ContactSerializer(contact)
#         return Response(serializer.data)
#
#     elif request.method == 'PUT':
#         serializer = ContactSerializer(contact, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     elif request.method == 'DELETE':
#         contact.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)

from contacts.models import Contact
from contacts.serializers import ContactSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class ContactList(APIView):
    """
    List all contacts, or create a new contact.
    """
    def get(self, request, format=None):
        contacts = Contact.objects.all()
        serializer = ContactSerializer(contacts, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = ContactSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ContactDetail(APIView):
    """
    Retrieve, update or delete a contact instance.
    """
    def get_object(self, pk):
        try:
            return Contact.objects.get(pk=pk)
        except Contact.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        contact = self.get_object(pk)
        serializer = ContactSerializer(contact)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        contact = self.get_object(pk)
        serializer = ContactSerializer(contact, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        contact = self.get_object(pk)
        contact.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
