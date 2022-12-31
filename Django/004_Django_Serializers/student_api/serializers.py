from rest_framework import serializers
from .models import Student

#! Bunlar ilkel method👇

# class StudentSerializer(serializers.Serializer):

#     first_name = serializers.CharField(max_length=50)
#     last_name = serializers.CharField(max_length=50)
#     number = serializers.IntegerField()
#     age = serializers.IntegerField()

# #? Bu yukarıdaki serializers ı yazarsam asagıdaki iki methodu yazmak zorundayım 👇


# def create(self, validated_data):
#         return Student.objects.create(**validated_data)


# def update(self, instance, validated_data):
#         instance.first_name = validated_data.get('first_name', instance.first_name)
#         instance.last_name = validated_data.get('last_name', instance.last_name)
#         instance.number = validated_data.get('number', instance.number)
#         instance.age = validated_data.get('age', instance.age)
#         instance.save()
#         return instance

#         #! ilkel method buraya kadar👆
#     #*✨✨2.adım artık serializers ım hazır ben artık view.py e gidip serializers ımı import edebilirim.


#? https://www.django-rest-framework.org/api-guide/serializers/#modelserializer 
# kullanılan seriliazers methodu👇

# class StudentSerializer(serializers.ModelSerializer):

#     class Meta:
#         model = Student
        # fields = ["id","first_name","last_name","number","age"] #!👉bunlar benim modelimden gelen fieldlar.
        # exclude = ["number"]
        #! datalarımdan number harıcındekileri getirecek exclude harıc demek.Bunu calıstırırken fieldsı kapıyoruz

#! class StudentSerializer(serializers.ModelSerializer):
#!     class Meta:
#!         model = Student
# !        fields = "__all__"
#! Bu sekilde yukarıdaki ilkel method ile yaptıgımız seyi kısaca yapabiliyoruz.
#? eger verimin hepsinin dönmesni istemeseydim  fields = ["id","first_name","last_name","number","age"] şeklinde belirterek response olarak döndürecektim.


#*👇 database den cektiğim student datasına bu seriliazares a ekstra data ekleyip frontend de dönebiliyoerum asagıdada onu yaptık.
class StudentSerializer(serializers.ModelSerializer):
   
   born_year= serializers.SerializerMethodField()
   path = serializers.StringRelatedField()
#    👆path seklinde görmek için bunu bu sekilde tanımladık




class Meta:
 


        model = Student
        fields = ["id","first_name","last_name","number","age","born_year","path"]
        # Buraya ben hangi methodları verirsem onları bana döndürüyor.👆

        def get_born_year(self,obj):
            import datetime
            current_time = datetime.datetime.now()
            return current_time.year - obj.age

class PathSerializer(serializers.ModelSerializer):
    
    students = StudentSerializer(many=True)
    students = serializers.HyperlinkedRelatedField(
        many=True,
        read_only=True,
        view_name='detail'
    )
    
    class Meta:
        model = Path
        # fields = "__all__"
        fields = ["id", "path_name", "students"]