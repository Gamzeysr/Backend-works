from django.db import models

# Create your models here.
#! ben fscohort ile ilgili tablolarımı fscohort altındaki models.py dosyasında olusturucam.Yani burada


class Student(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    number = models.IntegerField(default=1111)
    # buna number girilmezse 1111 olsun dedik👆
    about = models.TextField(blank=True, null=True)
    register = models.DateTimeField(auto_now_add=True)
    # 👆 instanceımın ilk olusturdgum tarihi yazıyor.
    last_update_data = models.DateTimeField(auto_now=True)
    # 👆studentdan herhangi birsey degistirdgim zaman en sonki degistirdiğim tarihi alıyor.
    is_active = models.BooleanField()

# ? Burada ✨Student✨ ismi yakın zamanda olusturacak oldugum tablom ismine takabul ediyor.
# ? CharField da max uzunluk girilmesi zorunlu

    def __str__(self):
        return f"{self.number} + {self.first_name}"
# ? str methodu kısa benim objelerimin görüntsünü ayarladıgım methoddur.
# ? Bu method database de degisşiklik yapmıyor sadece bu databasedeki isimlerin bana göre görüntüsnü ayarlamış oluyorum

    class Meta:
        ordering = ["number"]
        verbose_name_plural = "Student_list"

    def student_year_status(self):
        "Returns the student's year status"
        import datetime
        if self.register_date < datetime.date(2019, 1, 1):
            return "Senior"
        if self.register_date < datetime.date(2021, 1, 1):
            return "Junior"
        else:
            return "Freshman"
