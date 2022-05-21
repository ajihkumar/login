'''
from rest_framework import serializers
#from rest_framework.decorators import serializers
from .models import upload_image

class FileSerializer(serializers.ModelSerializer):
   
    class Meta():
        model=upload_image
        fields=['image']
'''