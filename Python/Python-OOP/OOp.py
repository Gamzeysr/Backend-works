# * gamze
# print("hello")

#! ✨Everything in Pyhton is class✨👇


# def print_types(data):
#     for i in data:
#         print(i, type(i))


# test = [122, "victor", [1, 2, 3], (1, 2, 3), {1, 2, 3}, True, lambda x: x]
# print_types(test)


# data yazan yer test demek oluyor
# 🏄‍♂️👆

#! ✨defining class✨👇
# *Pyhtonda class tanımlarken class keywordunu kullanıyoruz
# class Person:
#     name = "victor"
#     age = 33

# * 👆 Şuan burada ben pyhton da class oluşturmuş oldum.Ben bu kalıptan artık yeni objectler olusutabilirm.

# person1 = Person()
# person2 = Person()

# * 🎉👆Burada iki adet nesne yani object olusturdum.
# * Bu objeclere ✨intance✨ deniyor


# * 🎉Bu olusturmuş oldugum objectlere ✨intance ✨ de deniyor.
# * 🎉Bu nesnlere kalıptan oluşturdugum için kalıbın özelliğini tasır.
# print(person1.name)
# print(person2.age)

# * 🎉 kalıba bir özellik eklemek istersem ekleyebilirim👇
# Person.job = "developer"
# print(person1.job)

# class Meyveler:
#     name = "watermelon"
#     kg = 5


# meyve1 = Meyveler()
# meyve2 = Meyveler()
# * meryve1 ve meyve2 olarak object olusturmuş oluyoruz bu objectlerede intance diyoruz.

# print(meyve1.name)
# print(meyve2.kg)
#!   ✨class attributes vs instance attributes:
# class Person:
#     name = "victor"
#     age = 33


# person1 = Person()
# person2 = Person()
# * 👆 iki tane yine intance oluşturdum Person classında

# * Bir instancelarımıza ekleyeceğimiz özellik diğer instancelarımızı etkilemiyor 👇
# person1.location = "turkey"
# print(person1.location)
# print(person2.location)
# * Yani;Burada person1 instance ıma ✨location = turkey'i ✨eklerken person2  intsance ım bundan etkilenmedi.
# * İnstancelarımda class'dan gelen ne varsa hepsi instancelarımda oluyorken, attribute'lerim sadece hangi instanceıma attribute u ekliyorsam sadece o attribute da oluyor.❤

#! ✨SELF keyword and methods
# * SELF hangi instance dan calısıyorsa onu temsil ediyor
# * Hangi instance i cagırırsak methodu o instance ın içindeki belirten methodu bana döndürmüş olur.

# class Person:
#     company = "clarusway"

#     def test(self):
#         print("test")


# person1 = Person()
# person2 = Person()

# person1.test()
# person2.test()

# ✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨
# class Person:
#     company = "clarusway"

#     def test(self):
#         print("test")


#     def get_details(self):
#         print(f"{self.name} - {self.age}")


# person1 = Person()
# person2 = Person()

# person1.name="victor"
# person1.age=33
# person1.get_details()
# 👆 burada person1 instance ını cagırdıgımız için içinde ki methodu getirdi.


# person2.name="henry"
# person2.age=18
# person2.get_details()
# 👆 Burada da person2 instanceımızıın içindeki metyhod gelirdi

# output:victor - 33
# Ve burada ki methodlar parametre almak zorunda yoksa hata verir dikkat et
# method ların içindeki self yazısını kasdediyorum.
# ✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨

# class Person:
#     company = "clarusway"

#     def test(self):
#         print("test")

#     def set_details(self, name, age):
#         self.name = name
#         self.age = age

#     def get_details(self):
#         print(f"{self.name} - {self.age}")

# person1 = Person()
# person2 = Person()

# person2.set_details("henry", 15)
# 👆 Burada ki parametreler self,name,age  e  gitmiş oldu.
# person2.get_details()

# output:henry - 15
# ✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨
# * eger değişmeyen sabit bir method istersek ✨@staticmethod✨ yazıcaz
# * ve bu @staticmethod u yazdgımızda artık self yazmamıza gerek kalmıyor
# * Yani staticmethodlar self  parametresi almazlar.
# class Person:
#     company = "clarusway"

#     def test(self):
#         print("test")

#     def set_details(self, name, age):
#          self.name = name
#          self.age = age

#     def get_details(self):
#         print(f"{self.name} - {self.age}")

#     @staticmethod
#     def salute():
#         print("Hi Gamze!")


# person1 = Person()
# person2 = Person()


# person1.salute()

# ✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨

#! Special methods(Dunder methods)
#! __init__ methodu
# * daha önceden tanımlanmış methodlardır.
# class Person:
#     company = "clarusway"

#     def set_details(self, name, age):
#         self.name = name
#         self.age = age

#     def get_details(self):
#         print(f"{self.name} - {self.age}")


# person1 = Person()
# person1.set_details("victor", 33)
# person1.get_details()

# output:victor - 33

# * init methodu:instancelarımızı olusturuyorken otomatik olarak çalışır.
# *  Bu yukarıdaki methodu artık kısaca init methoduyla yapabiliriz.


# class Person:
#     company = "clarusway"

#     def __init__(self, name, age):
#             self.name = name
#             self.age = age

#     def get_details(self):
#             print(f"{self.name} - {self.age}")


# person1 = Person("victor", 33)
# person1.get_details()

# output:victor - 33

# * 👆burada yukarıda ki yaptıgımızı ✨__init__✨ methoduyla kısaca yapmış olduk.

# class Person:
#       company = "clarusway"

#       def __init__(self, name, age,gender="male"):
#               self.name = name
#               self.age = age
#               self.gender=gender

#       def get_details(self):
#               print(f"{self.name} - {self.age}")

# person1 = Person("victor", 33)
# person1.get_details()

# output:victor - 33 - male

# ✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨

#! __str__ methodu
# *  str methodlarla ben instance larımın çıktısını görüntüsünü ayarlayabiliyorum.
# * Yani ben instance larımın içine ne yazdıysam onu __str__ methoduyla görebiliyorum.
# class Person:
#            company = "clarusway"

#            def __init__(self, name, age,gender="male"):
#                    self.name = name
#                    self.age = age
#                   self.gender=gender


#            def __str__(self):
#                return f"{self.name} - {self.age}"


#            def get_details(self):
#                    print(f"{self.name} - {self.age}")

# person1 = Person("victor", 33)
# person2=Person("henry",33)

# print(person1)
# print(person2)
# output: victor - 33
#         henry - 33

#! OOP Principles (4 pillars)
# ✨#?Encapsulation
# ✨#?Abstraction
# ✨#?Inheritance
# ✨#?Polymorphism


# ✨# ?Encapsulation
# * kullanıcı tarafından classların,verilerin ve methodların ne kadarının görüntülenebileceğini, ne kadarının değiştirebileceğini belirlediğimiz yapı.

# *  public - private - protected
# *  Herkesin ulaşabildiği methodlara public,private methodlarına dışarıdan ulaşılamıyor,protected methodlarına ise; kontrollü bir sekilde ulaşılabilirz.
# *  Bu getter setter methodlarını bu methotlara göre ayarlayıp kullanabiliyoruz.Mesela;
# *  person1.name ="victor" u yukarıda gayet atadık ama name'i biz protected olarak ayarlasaydık direk değeri elimizi kolumuzu sallayarak bu sekilde atayamazdık.

# class Person:
#             company = "clarusway"

#             def __init__(self, name, age"):
#                     self.name = name
#                     self.age = age
#                     self._id = 5000
#                     # 👆Burada ✨_id✨ yapmamızın sebebi idnin basına altçizgi koymamızın sebebi idmizin private olması için
#                     # tek alt cizgi demek sadece bir uyarı değiştirirsem sıkınıt cıkarabilir uyarsı


#             def __str__(self):
#                 return f"{self.name} - {self.age}"


#             def get_details(self):
#                 print(f"{self.name} - {self.age}")

# person1 = Person("victor",33)
# print(person1._id)
# output: 5000

# person1._id = 4000
# print(person1._id)
# ✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨

# * ✨Bu tek alt cızgı nın anlamı değiştirip okuyabilirisn ama ileride sıkıntı cıkarabilir bu durum yinede sen bilirsin diyor.✨
# * ✨iki alt çizgi olursa biz dışarıdan direkt buna ulaşamayız.👇🏻
# class Person:
#                 company = "clarusway"

#                 def __init__(self, name, age"):
#                         self.name = name
#                         self.age = age
#                         self.__number = 200

#                 def __str__(self):
#                     return f"{self.name} - {self.age}"


#                 def get_details(self):
#                     print(f"{self.name} - {self.age}")


# person1=Person("victor",33)
# print(person.__number)
# *  output: hata alrırız . çünkü iki alt çizgi olunca ulaşamıyoruz.
# print(person1._Person__number)👈 ama dediğimde ulaşabiliriz.
# ✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨


# ✨#?Abstraction

# liste = [2, 3, 1, 4]
# liste.sort()
# print(liste)
# * Burada output: [1,2,3,4,5] burada sort methodu listenin içindekileri sıralıyor onu biliyoruz aslında arkada ne fonksiyonlarla calısdgını detaylı bilmyioruz işte Abstraction  bize yapıların yeteri kadar ne işe yaracagını bilmemiz yeterli diyor.
# * Yani kullanıcıya greksiz detaylardan ve bilmesne ihtiyaç olmayan yapıdan uzaklaştırarak yormamak- soyutlama

#! Bir örnek olarak, bir telefonu düşünebilirsiniz. Telefon, çeşitli özelliklere ve davranışlara sahiptir(örneğin mesaj gönderme, arama yapma, alarm kurma gibi) ancak kullanıcıların bu özellikleri ve davranışları kullanabilmeleri için telefonun nasıl çalıştığını bilmeleri gerekmez. Telefonun kullanımı için gerekli olan özellikler ve davranışlar, telefonun arayüzünde gösterilir ve kullanıcılar bu arayüzü kullanarak telefonu kullanabilirler. Bu durumda, telefonun içinde yer alan özellikler ve davranışlar encapsulation ile gizlenmiştir ve sadece kullanıcıların ihtiyaç duydukları özellikler ve davranışlar abstraction ile ortaya çıkarılmıştır.

# ✨#?Inheritance
# * Miras kalıtım.
# * Bir takım özellikleri, methodları, attributelari o classdan üretilmiş başka classlara aktarma.Miras bırakmaya ✨Parent✨ classı diyoruz.
# * Bu özellikleri Parenttan alan class ada ✨child✨ diyoruz.Bunlara örnek parent-child-kalıtım imagesi na bak


# class Person:
#     company = "clarusway"

#     def __init__(self,name,age)
#       self.name = name
#       self.age = age

#     def __str__(self):
#         return f"{self.name}"

#     def get_details(self):
#         print(self.name,self.age)

# class Employe(Person):
#     pass

#  emp1 = Employe("barry",20)
#  emp1.get_details()

# *👆  Person classından Employe classı ürettik ve intance olusturduk.
# * Burada Person classının içindekileri de miras alarak bir employee classı meydana geldi.
#
# print(emp1.company) dediğimizde 👉 output:clarusway olucak cünkü kalıtım olrak Person clasını da almış oldugundan
# ✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨

# ✨#? Polymorphism
# * Overriding
# parenttan aldıgımız bir methodu yeni işlevsellik ekleyerek tekrardan tanımlamaya overriding deniliyor.


# class Person:
#     company = "clarusway"

#     def __init__(self, name, age):
#       self.name = name
#       self.age = age

#     def __str__(self):
#         return f"{self.name}"

#     def get_details(self):
#         print(self.name, self.age)


# class Employe(Person): 👉Burada person classından employe classını olusturdum.


#     def __init__(self,name,age,path):
#      self.name = name
#      self.age = age
#      self.path = path
# * 👆 Burada Overriding yapmış olduk.Yani parenttan aldıgımız methodu yeni işlevsellik kazandırarak ekledik.
# *     Bu overriding işlemini  kısaca ✨super() ✨keywordu ile yapabilirz.👇
#!def __init__(self, name, age, path):
#!super().__init__(name,age)
#! self.path= path
#      def get_details(self):
#         print(self.name, self.age, self.path)
# * 👆Burasınıda kısaca super() keywordu ile yapabilirim 👇
#!   def get_details(self):
#!    super().get_details()
#!   print(self.path)


#  emp1 = Employe("barry",20,"FS")
#  emp1.get_details()
# ✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨
# * 🎀Employe classına ben overriding de yapabilirim ya da yeni bir class da oluşturabilirim 🎀
# Yukarıdaki overriding'i super() keywordu ile clear bi sekilde yazalım şimdi👇
# class Person:
#     company = "clarusway"

#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def __str__(self):
#         return f" {self.name}"

#     def get_details(self):
#         print(self.name, self.age)

# class Employe(Person):
#     def __init__(self,name,age,path):
#      super().__init__(name,age)
#      self.path = path

#      def get_details(self):
#       super().get_details()
#       print(self.path)


# emp1=Employe("barry",20,"FS")
# emp1.get_details()


# ✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨

# * Overloading:
# * aynı methodan birden fazla olmasına dayanıyor.
# *Overloading:aynı methodu farklı parametrelerle çalıştırmaya dayanıyor.


# class Person:
#     company = "clarusway"

#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def __str__(self):
#         return f" {self.name}"

#     def get_details(self):
#         print(self.name, self.age)


# class Employe(Person):
#     def __init__(self, name, age, path):
#         super().__init__(name, age)
#         self.path = path

#         def get_details(self):
#             super().get_details()
#             print(self.path)

#         def get_details(self, salary):
#             super().get_details()
#             print(self.path)

#         def get_details(self, salary, duration):
#             super().get_details()
#             print(self.path)


# emp1 = Employe("barry", 20, "FS")
# emp1.get_details()

# 👆 Tabi kullanım bu python da yok..Java gibi dillerde var ama pythoo da yok.Python en son tanımladıgımız methodu görğyor diğerlerini görmüyor bu da pythonun özelliği.
# pythonda multipledispatch package var bunu yüklerrsek o zama overloading özelliği gelebiliyor.


# ✨#?multiple inheritance
# * Birden fazla classımızı inheritance edebiliriz.


# class Person:
#     company = "clarusway"

#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def __str__(self):
#         return f" {self.name}"

#     def get_details(self):
#         print(self.name, self.age)


# class Lang:
#     def __init__(self, langs):
#         self.langs = langs

#     def display_langs(self):
#         print(self.langs)


# *👇🏻 Burada ki Employe classında birden fazla class inheritance etmiş olduk Django da da bu sekilde.
# class Employe(Person, Lang):
#     def __init__(self, name, age, path, langs):
#         super().__init__(name, age)
#         Lang.__init__(self, langs)
#         self.path = path
#         # self.langs = langs

#         def get_details(self):
#             super().get_details()
#             print(self.path)


# emp1 = Employe("barry", 20, "FS", "JavaScript")
# emp1.get_details()
# print(emp1.company)
# emp1.display_langs()

# ? other topics

# print(Employe.mro()) #*mro : method resolution order
# *👆 Bu method Employe classı bize arka tarafda hangi inharitancelardan üretildiğini gösteren methoddur.


# print(help(Employe)) 👉 #*help de bize employe classının bize bütün bilgisini döküyor.


# print(emp1.__dict__)👇🏻
# * output:{'name':'barry' 'age':20 'langs':'Javascript' 'path':'FS'}

# print(isinstance(emp1, Employe))👇🏻
# * Bu methptta benim Employe classım emp1 demi diye döndürüyor.emp1 de ise true değilse false dönüyor.

# print(issubclass(Lang,Person))👇🏻
# * Person classı Lang classını kapsıyor mu kapsıyorsa true kapsamıyorsa False,Bunların ikisde bagımsız class oldgundan false
# * Burada output:False

# print(issubclass(Employe,Person))👇🏻
# * Employe classı Person classını kapsıyor mu kapsıyorsA true kapsamıyorsa False
# * output:True


#! getattr (instanece, attribute) : returns attribute value of instance
#! setattr (instanece, attribute, new value) : update attribute  of instance
#! hasattr (instanece, attribute):return boolean
#! delattr (instanece, attribute): delete attribute of instance

# print(getattr(emp1,"name"))👉bu bana iki tane parametre kullanmamı sağlar.ilki✨ instance✨ ı alır,ikincisi attribute alır. sonucu👇🏻Bu sekilde instancelarımızın attrıbutelerını cekebliyoruz.
# *output:barry
# ya da 👇🏻👇🏻
# x = getattr(emp1, "name")
# print(x)


# print(setattr(emp1, "name", "qadir"))
# print(getattr(emp1,"name"))
# output:qadir

# print(hasattr(emp1, "name"))👉Bizim instance ımızın böğle bir parametresi var mı yokmu onu döndürüyor.
# * output:True


# print(delattr(emp1,"age"))
# print(emp1.__dict__)
# * output:{'name':'barry', 'langs':'Javascript', 'path': 'FS'}


# ? inner class

# from django.db import models


# class Makale(models.Model):
#     name = models.CharFiels(max_length=50)
#     author = models.CharField(max_length=50)

#     class Meta:
#         ordering = ["name"]
#         verbose_name = "makaleler"
