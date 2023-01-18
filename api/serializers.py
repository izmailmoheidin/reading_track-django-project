from rest_framework import serializers
from booksapi.models import BooK

class bookSerializer(serializers.ModelSerializer):
    class Meta:
        model = BooK
        fields = '__all__'