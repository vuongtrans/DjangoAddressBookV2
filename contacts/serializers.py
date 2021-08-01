from rest_framework import serializers
from contacts.models import Contact, LANGUAGE_CHOICES, STYLE_CHOICES

# Validation flags
# - required, max_length, default
# Can use the Serializer and ModelSerializer classes

class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = ['id', 'first_name', 'last_name', 'address', 'city', 'state', 'zip_code']
