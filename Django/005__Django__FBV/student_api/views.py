#✨✨ Bu sayfa views2 nını aynısı ama bız tek tek öğrenmek adına viewsin içindekileri buy sayfada yarıca yapıyoruz✨



from django.shortcuts import render, HttpResponse, get_object_or_404

from .models import Student, Path

from .serializers import StudentSerializer, PathSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status


@api_view() #!👉 bu function aslında,bu function bazı özellikleri yapmamızı sağlıyor en buyuk özelliği ise; POSTMANın bize basit halini sunması ve response ile json işlemlerini yapmasını sağlıyor arka tarafda #! ✨default GET✨
def home(requst):
    return Response({'home': 'This is home page...'})
    #! bu response artık bize json formatında döndüğü için 👆burada artık key value seklinde degerler yazdım.


#! http methods ----------->
#? - GET (DB den veri çağırma, public)
#? - POST(DB de değişklik, create, private)
#? - PUT (DB DE KAYIT DEĞİŞKLİĞİ, private)
#? - delete (dB de kayıt silme)
#? - patch (kısmi update)

@api_view(['GET'])
def students_list(request):
    students = Student.objects.all()
    #!👆 Student tablomdaki butun ögrencilerimi aldıyorum 
    # print(students)
    serializer = StudentSerializer(students, many=True)
    #!👆 bu cekmiş oldugum Student datasını serializersın içine koyuyorum.bu serializer'ın bana yapmış oldugu student tablomu json formatına ceviriyor.
    #* many=True dememın sebei student tablosunda birden fazla object dönecek olması.🧨🧨🧨many=true'yu belirtmezsem hata verir!!!
    # print(serializer)
    # print(serializer.data)
    return Response(serializer.data)
    #!👆 en sonda bu serializer ın içine koydugum datayı response ile frontend de döndüm.


@api_view(['POST'])
def student_create(request):
    serializer = StudentSerializer(data=request.data) #!👉burada  datam frontenden gelecek.
    if serializer.is_valid(): #!👉data valid ise databesıme kaydet, valid degilse error olarak dön.
        serializer.save()
        message = {
            "message": f'Student created succesfully....'
        }
        #!👆 basarılı olursa bu sekilde mesage dönecek 
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    #!👆 valid değilse  de buraya düsecek bu dönecek 

# Informational responses (100 – 199)-->bilgilendirme
# Successful responses (200 – 299)--> succes mesajları 200ile baslar.
# Redirection messages (300 – 399)--> 
# Client error responses (400 – 499)--> yanlış yada eksik data girilmişse yada yanlış url e gitmişse yanlış pathe istek atıldıysa bu hatayı alırız.
# Server error responses (500 – 599) --> bizim backend e yaptıgımız bır hata varsa bunlarda 500 ile baslar 


#!👇 burada databaseden tek bir obje yi cekiyoruz.
@api_view(['GET'])
def student_detail(request, pk):

    student = get_object_or_404(Student, id=pk)
    # student = Student.objects.get(id=pk)
    serializer = StudentSerializer(student)
    #!👆 many=True dememe gerek yok cükü tek bir object 
    return Response(serializer.data)


@api_view(['PUT'])
def student_update(request, pk):
    student = get_object_or_404(Student, id=pk)
    serializer = StudentSerializer(instance=student, data=request.data)
    if serializer.is_valid():
        serializer.save()
        message = {
            "message": f'Student updated succesfully....'
        }
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
def student_delete(request, pk):
    student = get_object_or_404(Student, id=pk)
    student.delete()
    message = {
        "message": 'Student deleted succesfully....'
    }
    return Response(message)


#############################################################

@api_view(['GET', 'POST'])
def student_api(request):
    if request.method == 'GET':
        students = Student.objects.all()
        serializer = StudentSerializer(students, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            data = {
                "message": f"Student {serializer.validated_data.get('first_name')} saved successfully!"}
            return Response(data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE', 'PATCH'])
def student_api_get_update_delete(request, pk):
    student = get_object_or_404(Student, pk=pk)
    if request.method == 'GET':
        serializer = StudentSerializer(student)
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'PUT':
        serializer = StudentSerializer(student, data=request.data)
        if serializer.is_valid():
            serializer.save()
            data = {
                "message": f"Student {student.last_name} updated successfully"
            }
            return Response(data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'PATCH':
        serializer = StudentSerializer(
            student, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            data = {
                "message": f"Student {student.last_name} updated successfully"
            }
            return Response(data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        student.delete()
        data = {
            "message": f"Student {student.last_name} deleted successfully"
        }
        return Response(data)