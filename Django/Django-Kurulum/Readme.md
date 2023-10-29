## DRF_Class Base Views

### Django proje kurulumu:

```py
- python -m venv env
-source env/Scripts/activate 👈benimki bu komutile calısıyor (./env/Scripts/activate )
- pip install djangorestframework
- pip install python-decouple
- pip freeze > requirements.txt
- django-admin startproject main .
- python manage.py runserver
```

###### Repodan çektiğimiz bir projeyi requirements deki indirilen paket/versiyonları ile birlikte install etmek için kullanılacak komut ->

```py
- python -m venv env
- ./env/Scripts/activate
- pip install -r requirements.txt
```

- .gitignore ve .env dosyalarını oluştur.
- settings.py daki SECRET_KEY ' i config ile .env ye ekle

settings.py

```py
from decouple import config
SECRET_KEY = config('SECRET_KEY')
```

.env

```py
SECRET_KEY =django-insecure-&2_9wl^*c1v&z-x0g121-qceca2nm&tys+=a_!$9(6x28vech&
```

- bir app oluştur ->

```powershell
- python manage.py startapp student_api
```

- ilk iş app i ve rets_framework paketini settings.py daki INSTALLED_APP e ekle ->

settings.py

```py
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # myapp
    'student_api',
    # 3rd party packages
    'rest_framework',
]
```

- urls configurasyonunu oluştur ->
  main/urls.py

```py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('student_api/', include('student_api.urls')),
]

```

student_api/urls.py

```py
from django.urls import path
from .views import (
    home,
)


urlpatterns = [
    path('', home),
]
```

- views.py da home view ini yaz ->
  views.py

```py
from rest_framework.response import Response
from rest_framework.decorators import api_view

@api_view()
def home(request):
    return Response(
        {
            'message': 'Hello World'
        }
    )
```

- model oluştur ->
  models.py

```py
from django.db import models

# Create your models here.
class Student(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    number = models.IntegerField()

    def __str__(self):
        return self.first_name + ' ' + self.last_name
```

- makemigrations ve migrate komutları çalıştır.

```powershell
- python manage.py makemigrations
- python manage.py migrate
```

- modeli admin.py' a register et.
  admin.py

```py
from django.contrib import admin
from .models import Student

# Register your models here.
admin.site.register(Student)
```

- superuser oluştur ve db ye veri girişi yap ->

```powershell
- python manage.py createsuperuser
- python manage.py runserver
```

- model için serializer yaz ->
  student_api/serializers.py

```py
from rest_framework import serializers
from .models import Student


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'
```

```text
 HTTP Request Types:
        GET -> Public verilerdir. Listeleme/Görüntüleme işlemlerinde kullanılır.
        POST -> Private verilerdir. Kayıt oluşturma işlemlerinde kullanılır. (ID’ye ihtiyaç duymaz.)


        * PUT -> Kayıt güncelleme işlemlerinde kullanılır. (Veri bir bütün olarak güncellenir.) (ID’ye ihtiyaç duyar.)
        * PATCH -> Kayıt güncelleme işlemlerinde kullanılır. (Verinin sadece ilgili kısmı güncellenir.) (ID’ye ihtiyaç duyar.)
        * DELETE -> Kayıt silme işlemlerinde kullanılır. (ID’ye ihtiyaç duyar.)
```

- List - Create ->
- student_api/views.py ->

```py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Student
from .serializers import StudentSerializer

# List - Create
class StudentListCreate(APIView):
    # List (GET Method)
    def get(self, request):
        students = Student.objects.all()
        serializer = StudentSerializer(instance=students, many=True)
        return Response(serializer.data)

    # Create (Post Method)
    def post(self, request):
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
```

- student_api/urls.py ->

```py
from django.urls import path
from .views import (
    StudentListCreate,
)

urlpatterns = [
    path('student-list-create/', StudentListCreate.as_view()),
]
```

- Detail - Update - Delete ->
- student_api/views.py ->

```py
from django.shortcuts import get_object_or_404

class StudentDetailUpdateDelete(APIView):

    # Tek kayıt görüntüleme:
    def get(self, request, pk):
        student = get_object_or_404(Student, pk=pk)
        serializer = StudentSerializer(instance=student)
        return Response(serializer.data)

    # Tek kayıt güncelleme:
    def put(self, request, pk):
        student = get_object_or_404(Student, pk=pk)
        serializer = StudentSerializer(instance=student, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # Tek kayıt sil:
    # def delete(self, request, pk):
    #     student = get_object_or_404(Student, pk=pk)
    #     student.delete()
    #     return Response({'message': 'Deleted'}, status=status.HTTP_204_NO_CONTENT)

    def delete(self, request, pk):
        student = get_object_or_404(Student, pk=pk)
        serializer = StudentSerializer(student)
        student.delete()
        return Response({
            'message': 'Deleted',
            'data': serializer.data
            }, status=status.HTTP_204_NO_CONTENT)

```

- student_api/urls.py ->

```py
from django.urls import path
from .views import (
    StudentListCreate,
    StudentDetailUpdateDelete,
)

urlpatterns = [
    path('student-list-create/', StudentListCreate.as_view()),
    path('student-detail-update-delete/<int:pk>', StudentDetailUpdateDelete.as_view()),
]
```

- List - Create - Detail - Update - Delete ->
- student_api/views.py ->

```py
# Yukarıdaki işlemleri tek class'da yazmaya çalışalım

class StudentGPPD(APIView):

    def get(self, request, pk=0):
        if pk:
        # Tek kayıt görüntüle:
            student = get_object_or_404(Student, id=pk)
            serializer = StudentSerializer(instance=student)
            return Response(serializer.data)
        else:
        # Kayıtları listele:
            students = Student.objects.all()
            serializer = StudentSerializer(instance=students, many=True)
            return Response(serializer.data)

    # Yeni Kayıt (POST Method)
    def post(self, request):
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # Tek kayıt güncelle:
    def put(self, request, pk):
        student = get_object_or_404(Student, id=pk)
        serializer = StudentSerializer(instance=student, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # Tek kayıt sil:
    def delete(self, request, pk):
        student = get_object_or_404(Student, id=pk)
        student.delete()
        return Response({ "message": "Deleted" }, status=status.HTTP_204_NO_CONTENT)

```

- student_api/urls.py ->

```py
from django.urls import path
from .views import (
    StudentListCreate,
    StudentDetailUpdateDelete,
    StudentGPPD,
)

urlpatterns = [
    path('student-list-create/', StudentListCreate.as_view()),
    path('student-detail-update-delete/<int:pk>', StudentDetailUpdateDelete.as_view()),
    path('student_gppd/', StudentGPPD.as_view()),
    path('student_gppd/<int:pk>', StudentGPPD.as_view()),
]
```

### GenericAPIView

- views.py ->

```py
# GenericAPIView

from rest_framework.generics import GenericAPIView
from rest_framework import mixins

class StudentGenericListCreate(mixins.ListModelMixin, mixins.CreateModelMixin, GenericAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    # List
    def get(self, request, *args, **kwargs):
        return self.list(*args, **kwargs)

    # Create
    def post(self, request, *args, **kwargs):
        return self.create(*args, **kwargs)

```

- urls.py

```py
from django.urls import path
from .views import (
    StudentListCreate,
    StudentDetailUpdateDelete,
    StudentGPPD,
    StudentGenericListCreate,
)

urlpatterns = [
    path('student-list-create/', StudentListCreate.as_view()),
    path('student-detail-update-delete/<int:pk>', StudentDetailUpdateDelete.as_view()),
    path('student_gppd/', StudentGPPD.as_view()),
    path('student_gppd/<int:pk>', StudentGPPD.as_view()),
    path('student_generic-list-create', StudentGenericListCreate.as_view()),
]
```

### ListCreateAPIView

### RetrieveUpdateDestroyAPIView

- views.py ->

```py
# ListCreateAPIView
# RetrieveUpdateDestroyAPIView
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
# List - Create
class StudentListCreateAPIView(ListCreateAPIView):
    queryset =Student.objects.all()
    serializer_class = StudentSerializer

# Detail - Update - Delete
class StudentRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset =Student.objects.all()
    serializer_class = StudentSerializer

```

- urls.py

```py
from django.urls import path
from .views import (
    StudentListCreate,
    StudentDetailUpdateDelete,
    StudentGPPD,
    # Generic
    StudentGenericListCreate,
    StudentListCreateAPIView,
    StudentRetrieveUpdateDestroyAPIView
)

urlpatterns = [
    path('student-list-create/', StudentListCreate.as_view()),
    path('student-detail-update-delete/<int:pk>', StudentDetailUpdateDelete.as_view()),
    path('student_gppd/', StudentGPPD.as_view()),
    path('student_gppd/<int:pk>', StudentGPPD.as_view()),
    # Generic mixins
    path('student_generic-list-create', StudentGenericListCreate.as_view()),
    # APIView
    path('student-list-create-api', StudentListCreateAPIView.as_view()),
    path('student-get-put-delete-api', StudentRetrieveUpdateDestroyAPIView.as_view()),

]
```

### ModelViewSet

- views.py

```py
from rest_framework.viewsets import ModelViewSet

class StudentModelViewSet(ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
```

- urls.py (router yapısını kullanacağız.)

```py
from django.urls import path
from .views import (
    StudentListCreate,
    StudentDetailUpdateDelete,
    StudentGPPD,
    # Generic mixins
    StudentGenericListCreate,
    # APIViews
    StudentListCreateAPIView,
    StudentRetrieveUpdateDestroyAPIView,
)

urlpatterns = [
    path('student-list-create/', StudentListCreate.as_view()),
    path('student-detail-update-delete/<int:pk>', StudentDetailUpdateDelete.as_view()),
    path('student_gppd/', StudentGPPD.as_view()),
    path('student_gppd/<int:pk>', StudentGPPD.as_view()),
    # Generic mixins
    path('student_generic-list-create', StudentGenericListCreate.as_view()),
    # APIView
    path('student-list-create-api', StudentListCreateAPIView.as_view()),
    path('student-get-put-delete-api', StudentRetrieveUpdateDestroyAPIView.as_view()),
]


# ModelViewSet
from rest_framework import routers
from .views import StudentModelViewSet

router = routers.DefaultRouter()
router.register('students', StudentModelViewSet)

urlpatterns += router.urls

```

#### MVS action() method

views.py

```py
# ModelViewSet
# Tüm işlemler
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action

class StudentMVS(ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    @action(methods=["GET"], detail=False)
    def count(self, request):
        return Response({
            'count': Student.objects.count()
        })
```
