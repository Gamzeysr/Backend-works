from django.db import models

# Create your models here.

class Student(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=30)
    number = models.PositiveSmallIntegerField(blank=True,null=True)

    #! eğer ben bir integera blank=True dersem bu demek oluyor ki number yerini browserda bos gecebilirsin tablo yaparken demek oluyor, eger ben bu blank=Trueyu integer için dersem database dede bos gecmem gerekiyor aynı sekilde o yüzden ✨null=True✨ diyoruz.Yani database imide bos gecebilir oldugunu integer de söylemem gerekiyor
    

    def __str__(self):
       return f'{self.number} - {self.first_name} - {self.last_name}'
    #! 👆Bu method bana tablo baslıklarında number first_name last_name i göster diyor.

    class Meta:
    #  ordering = ('number',) 
    #! class meta default davranısları değiştirmek için kullanılıyor
    #!👆 mesela burada number a göre sıralamasını istedim.
    #!👇 mesela tersten sıralanmasını istersek
       ordering = ('-number',) 
       verbose_name = 'Öğrenci'
       verbose_name_plural = 'Öğrenciler'
    #  db_table = '' tablo ismini değiştirmek için kullanıyoruz.
