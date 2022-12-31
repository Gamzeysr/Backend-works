
from django.shortcuts import render,HttpResponse, get_object_or_404


from .models import Student
from .serializers import StudentSerializer
#*✨✨✨ 3.adım olarak StudentSerializer ımı import ettim.Şimdi 4. adım olarak da endpointlarımı olusturucam urls.pymda 


from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status



# Create your views here.

def home(request):
    return HttpResponse('<h1>API Page</h1>' )

#! get ve post isteklerine cevap veren bir fonk 👇
#!👇 Bu viewlarımı ben Serializers i import ettiğim için kullanabilirim.Artık urls.py ye gidip çağırıyorum
@api_view(['GET', 'POST']) #?👈bu öğrenci listeleme ve öğrenci create etmeye yarıyor 
def student_api(request):
    if request.method == 'GET':
        students = Student.objects.all()
        #! 👆bu komut tablodaki butun öğrencileri çekiyor.yani butun instanceları çekip studends degiskenine atanmış.
        serializer = StudentSerializer(students, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        #!👆 frontendden bana post methodu ile veri gelmiş 
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            data = {
                "message": f"Student {serializer.validated_data.get('first_name')} saved successfully!"}
            return Response(data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE', 'PATCH']) #? 👈özel bi öğrenci cekiyor sonra onu update ediyor sonra delete ya da patch ediyor.
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
        serializer = StudentSerializer(student, data=request.data,partial=True)
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
    

@api_view(['GET', 'POST'])
def path_api(request):
    # from rest_framework.decorators import api_view
    # from rest_framework.response import Response
    # from rest_framework import status

    if request.method == 'GET':
        paths = Path.objects.all()
        serializer = PathSerializer(paths, many=True, context={'request': request})
        return Response(serializer.data)
    elif request.method == 'POST':
        # from pprint import pprint
        # pprint(request)
        serializer = PathSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            data = {
                "message": f"Path saved successfully!"}
            return Response(data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)