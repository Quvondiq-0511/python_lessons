# -*- coding: utf-8 -*-
"""
Created on Fri Feb 20 04:34:57 2026

@author: Envy-PC
"""
# print 01-dars.
#print('Assalomu aleykum')
#print (7*8)
#print(int(7/8))
#print(int(3.2+6.2))



#02-dars- print(), SINTEKS VA ARIFMETIK AMALLAR
 
# print('"Nexia","Damas","Tico" ko\'rganlar qilar havas')
# print("5 ning to'rtinchi darajasini toping:",5**4)
# print("22 ni 4 ga bo'lganda necha qoldiq qoladi:",'\n',22%4)
# print("""Tomonlari 125 ga teng bo'lgan kvadratni perimentri va yuzini toping
#       S=""",125*125,"P=",4*125)
# print("Diametri 12 teng bo'lgan doira yuzini toping",'\n',"S=",3.14*12*12)
# print("Katetlari 6 va 7 bo'lgan uchburchak gepotenuzani toping \n c=", (6*6+7*7)**(1/2))


#03-dars O'ZGARUVCHILAR

# salom = "Hello World"
# print(salom)
# xabar="Never give up"
# print(xabar)
# xabar="Quvondiq buyuklikka erishasan"
# print(xabar)
# #class="Error!"
# #print(class)
# a=3 
# b=5
# S=a*b
# print("Tomonlari 3 va 5 ga teng bo'lgan to'rtburchak yuzi=", S)

#04-darsSTRING (MATN)


# kocha="bog'bon"
# mahalla="sog'bon"
# tuman="bodomzor"
# viloyat="samarqand"
# manzil=f"{kocha.title()} ko'chasi {mahalla.title()} mahallasi {tuman.title()} tumani {viloyat.title()} viloyati"
# kocha=input("Ko'changiz nomini kiriting:\n>>>")
# mahalla=input("Mahallangiz nomini kiriting:\n>>>")
# tuman=input("Tumaningiz nomini kiriting:\n>>>")
# viloyat=input("Viloyatingiz nomini kiriting:\n>>>")
# manzil=f"{kocha.title()} ko'chasi \n {mahalla.title()} mahallasi \n {tuman.title()} tumani  \n{viloyat.title()} viloyati"
# print(manzil.upper())
# print(manzil.title())
# print(manzil.lower())
# print(manzil.capitalize())


#05- dars SONLAR.


# a=int(input("Birinchi sonni kiriting:\n>>>"))
# b=int(input("Ikkinchi sonni kiriting:\n>>>"))
# s, x, y, z =a+b, a-b, a*b, a/b
# print(a, "+", b, "=", s)
# print(a,"-",b,"=",x)
# print(a,"*",b,"=",y)
# print(a,":",b,"=",z)

# a=int(input("Istalgan sonni kiriiting:\n>>>"))
# s=a**2
# k=a**3
# print(a,"sonining kvadrati",s,"ga teng\n"+str(a),"sonining kubi esa",k,"ga teng bo'ladi")

# a=int(input("Tug'ilgan yilingizni kiriting:\n>>>"))
# yoshi=2026-a
# print("Siz",yoshi,"yoshdasiz")


#06-dars LIST


#ismlar = ["G'ayrat", "Arslon", "Jasur" ]
# print("Ishlaring qanday " + ismlar[0]  )
# print("Mening ukamni ismi "+ismlar[1])
# print("Biz bir birimizga taynchmiz "+ismlar[2]+" og'om")

# sonlar=[2, 3, -45, 3.55, 223.2323, 0.22, -232.3]
# sonlar[0]=sonlar[0]+sonlar[5]
# print(sonlar)
# sonlar[3]=sonlar[2]-1992392392392992
 
# t_shaxslar=["amir temur","Isaak nyuton","albert enshteyn","alisher navoiy",""]
# z_shaxslar=["anvar narzullayev","davronbek turdiyev","ilon mask","abror muxtor aliy"]
# t_faxr=t_shaxslar.pop(0)
# z_faxr=z_shaxslar.pop(-1)
# print("Men zamonaviy shaxslardan",t_faxr.title(),",hozirgi zamon shaxslaridan esa",z_faxr.title(),"bilan faxrlanaman")

# friends=[]
# friends.append("Ulug'bek")
# friends.append("Jasur")
# friends.append("Behruz")
# friends.append("Bunyod")
# friends.remove("Ulug'bek")
# friends.insert(0,"Bobur")
# friends.insert(2,"Sodiq")
# print(friends)
# # mehmonlar=[friends.pop(3)]
# mehmonlar.append(friends.pop(0))
# print(mehmonlar)



#07-dars.Roʻyxatlar bilan ishlash

countries=["Uzbekistan","Germany","Spain","UK","USA","Mexico","Russia","French"]
# print(len(countries))
# print(sorted(countries))
# print(sorted(countries,reverse=True))
# countries.reverse()
# print(countries)
# countries.sort()
# print(countries)
# countries.reverse()
# print(countries)
 
# juft_sonlar= list(range(120,1201,2))
# # print(juft_sonlar)
# print(sum(juft_sonlar))
# print(max(juft_sonlar)-min(juft_sonlar))
# print(len(juft_sonlar))
# print(str(juft_sonlar[:21])+","+str(juft_sonlar[270:291])+","+str(juft_sonlar[522:542]))
taomlar=["palov","manti","qozon kabob","lag'mon","qora qo'virdoq"]
nonushta=taomlar[:]
nonushta.remove("lag'mon")
nonushta.append("xonim")
nonushta.append("besh barmoq")
# print(taomlar,"\n",nonushta)


#08-dars. for takrorlash operatori

# ismlar=["ali","vali","husan","hasan","bobur"]
# for ism in ismlar:
#     print(f"Tizimga hush kelibsiz {ism.title()}")
# print("Kod",len(ismlar),"marta takrorlandi")

# toq_sonlar=range(11,100,2)
# kvadrati=[]
# for son in toq_sonlar:
#     kvadrati.append(son**2)
# print(list(toq_sonlar))
# print(kvadrati)

# kinolar=[]
# print("5 ta eng sevimli kinoyingizni kiriting:")
# for n in range(5):
#     kinolar.append(input(f"{n+1}-kino nomi:"))
# print(f"Sevimli kinolaringiz ro'yxati:\n>>> {kinolar}")

#09 if else

# cars = ['toyota', 'mazda', 'hyundai', 'gm', 'kia']
# for car in cars:
#     if car != 'gm' :
#         print(car.title())
#     else:
#         print(car.upper())


# login=input("Loginingizni kiriting:")
# if login.lower() == "admin" :
#     print("Xush kelibsiz, Admin. Foydalanuvchilar ro'yxatini ko'rasizmi?")
# else :
#   print("Xush kelibsiz, ", login)    

# x=input("Birinchi son:")
# y=input("Ikkinchi son:")
# if x==y:
#     print(x,"va",y,"sonlari teng")

# x=int(input("Istalgan sonni kiriting:"))
# if x<0:
#     print("Bu manfiy son")
# else :
#       print("Bu musbat son")    

# x=int(input("Istalgan sonni kiriting:"))
# if x>=0:
#     print(x**0.5)
# else:
#     print("Manfiy bo'lmagana son kiriting:")




#10-dars. Bir nechta shartlar

# x=int(input("juft son kiriting:"  ))
# if x<=0 or x % 2:
#     print("Juft son kirting")
# else :
#   print("rahmat")
"----------------------------------------------------"
# yosh=int(input("Yoshingizni kiriting:  "))
# if yosh>=60 or yosh<=4:
#     narh=0
# elif yosh <= 18:
#     narh=10000
# else:
#     narh=20000
# print(f"Sizga kirish {narh} so'm")
"---------------------------------------------------"   
# print("Ikkita son kiriting:")
# son1=int(input("Birinchi son: "))
# son2=int(input("Ikkinchi son: "))
# if son1 == son2:
#     print("Bu sonlar teng!")
# elif son1>=son2 :
#     print("Birinchi son katta!")
# else:
#    print("Ikkinchi son katta!")    
"---------------------------------------------------"
# mahsulotlar=['olma','o\'rik','un','novot','shaftoli','tuxum','anjir','pecheniya','suv','muzqaymoq']
# savat=[]
# print("Nechta mahsulot kiritmoqchilingizni belgilang")  
# mahsulot_soni=int(input(">>> "))
# for n in range(mahsulot_soni):
#     savat.append(input("Mahsulotingiz nomi: "))
# if savat:
#     for mahsulot in savat:
#         if mahsulot in mahsulotlar:
#             print(f"{mahsulot} nomli buyutmangiz qabul qilindi")
#         else:
#             print(f"{mahsulot} mahsulot do'konimizda yo'q")
            
# else:
#   print("Savatingiz bo'sh")         
"___________________________________________________________________"

# mahsulotlar=['olma','o\'rik','un','novot','shaftoli','tuxum','anjir','pecheniya','suv','muzqaymoq']
# savat=[]
# bor_mahsulotlar=[]
# mavjud_emas=[]
# print("Nechta mahsulot kiritmoqchilingizni belgilang")  
# mahsulot_soni=int(input(">>> "))
# for n in range(mahsulot_soni):
#     savat.append(input("Mahsulotingiz nomi: "))
# if savat:
#     for mahsulot in savat:
#         if mahsulot in mahsulotlar:
#             bor_mahsulotlar.append(mahsulot)
#         else:
#            mavjud_emas.append(mahsulot)
#     if mavjud_emas==0:
#             print("Siz so'ragan barcha mahsulotlar do'konimizda bor")
#     else:
#         print(f"siz so'ragan mahsulotlar ichida yo'qlar ro'yxati: {mavjud_emas}")
# else:
#   print("Savatingiz bo'sh")         
"--------------------------------------------------------------------"

# Loginlar=["azog","thorin","quvondiq","einshteyn","durin"]
# new_login=input("Yangi login kiriting:\n>>>> ")
# if new_login in Loginlar:
    
#         print("Bu logan band, iltimos boshqa login kiriting!")
# else:
#    print("Xush kelibsiz")
#    Loginlar.append(new_login)
"------------------------------------------------------------------"
# son=int(input("Biror butun son kiriting:"))
# boluvchilar=range(2,11)
# for boluvchi in boluvchilar:
#   if not(son % boluvchi):
#       print(f"{son}  {boluvchi} ga qoldiqsiz bo'linadi")        

"____________________________________________________________________"


# 11- dars xatolar bilan ishlash


    print ("Hello World!")






















