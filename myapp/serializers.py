from rest_framework import serializers
from .models import Demonstrate

class DemonstrateSerializer(serializers.ModelSerializer):
	class Meta:
		model=Demonstrate
		fields=('id','postId','name','email','body')
