from rest_framework import serializers
from .models import Job, Jobtype, Category, Industry, Skill


class Jobtypeserializers(serializers.ModelSerializer):
    class Meta:
        model = Jobtype
        fields = '__all__'

class Categoryserializers(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class Skillserializers(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = '__all__'

class Industryserializers(serializers.ModelSerializer):
    class Meta:
        model = Industry
        fields = '__all__'

class jobserializers(serializers.ModelSerializer):
    jobtype = Jobtypeserializers() 
    category = Categoryserializers()
    industry = Industryserializers()
    skill = Skillserializers()
    class Meta:
        model = Job
        fields = '__all__'