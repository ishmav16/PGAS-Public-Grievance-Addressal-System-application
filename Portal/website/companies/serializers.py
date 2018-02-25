from rest_framework import serializers
from .models import Stock1

class StockSerializer(serializers.ModelSerializer):
	class Meta:
		model=Stock1
		fields=('data',)
		#fields='_all_'


class StockSerializer1(serializers.ModelSerializer):
	class Meta:
		model=Stock1
		fields=('desc','id')
class ProbSerializer(serializers.ModelSerializer):

    class Meta:
        model=Stock1
        fields=('id','status','priority','email1','desc')
