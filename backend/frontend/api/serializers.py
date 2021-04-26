from rest_framework import serializers
from frontend.models import users
class DataSerializer(serializers.ModelSerializer):
    class Meta:
        model=users
        fields=('username','email','pwd')