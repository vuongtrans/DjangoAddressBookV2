from contacts.models import Contact
from contacts.serializers import ContactSerializer
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser

contact = Contact(first_name='Scott', last_name='Tran', address='5552', city='San Jose', state='CA', zip_code='95138')
contact.save()
