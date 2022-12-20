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
# * meryve1 ve meyve2 olarak object olusturmuş oluyoruz bu objectlerede intance diyoruz

# print(meyve1.name)
# print(meyve2.kg)

#!   ✨class attributes vs instance attributes:
class Person:
    name = "victor"
    age = 33


person1 = Person()
person2 = Person()
# * 👆 iki tane yine intance oluşturdum Person classında

# * Bir instancelarımıza ekleyeceğimiz özellik diğer instancelarımızı etkilemiyor 👇
person1.location = "turkey"
print(person1.location)
print(person2.location)
# * Yani;Burada person1 instance ıma ✨location = turkey'i ✨eklerken person2  intsance ım bundan etkilenmedi.
# * İnstancelarımda class'dan gelen ne varsa hepsi instancelarımda oluyorken, attribute'lerim sadece hangi instanceıma attribute u ekliyorsam sadece o attribute da oluyor.❤
