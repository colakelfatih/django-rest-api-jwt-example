from rest_framework import serializers
from school.models import Student, ClassName

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ('id','student_name', 'student_age', 'student_class')
        #fields = '__all__'

    def create(self, validated_data):
        return Student.objects.create(**validated_data)

class ClassNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClassName
        fields = ('id','name')
    
    def create(self, validated_data):
        return ClassName.objects.create(**validated_data)