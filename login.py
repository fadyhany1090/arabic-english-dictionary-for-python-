# سطر كويس لواجهه تسجيل الدخول
print("hello ")
user_name=input("user name\n").capitalize().strip()
password=input("creat password\n")

print()
#تسجيل الدخول باستخدام الباسورد واليوزر الخاص بالمستخدم
print("good ,please login in")
user_name0=input("user name\n").capitalize().strip()
pass0=input("your password\n")
if user_name0==user_name and password==pass0:
    print("okay, you are login now ")
    print("welcome "+user_name.capitalize())
    print("this web site for "" info  of website ")
    #دى حته تتحقق فيها من العمر لو عايز عمر معين يدخل الموقع 
    age=int(input("how old are you"))
    if age>=18  :
     print("good")
     print("now, you are submint succsesfully")
    else:
     print("sorry, You are under the minimum age for entry")
     input()
     #سطر ال input(), هنا عشان يدى المستخدم وقت يقرا رساله انو تحت السن او يعرف السبب من غير مالبرنامج يخرج بسرعه 
else:
 print("wrong username or password")
 checker=input("if you want try again write 'try again' if not 'press enter'").upper().strip()
 while checker == "try again".upper():
     print("please login in")
     user_name1=input("user name\n").capitalize().strip()
     pass1=input("your password\n")
     if  user_name1!=user_name or pass1!=password:
        checker2=input("if you want try again write 'try again' if not 'press enter'").upper()
        if len(checker2)==0:
          break
     elif   user_name1==user_name or pass1==password:
       print()
       print("okay, you are login now ")
       print("welcome "+user_name.capitalize())
       print("this web site for "" info  of website ")
#دى حته تتحقق فيها من العمر لو عايز عمر معين يدخل الموقع 
       age=int(input("how old are you"))
       if age>=18  :
         print("good")
         print("now, you are submint succsesfully")
         break
#كد بعد ميتحقق الشرط هيقف اللوب 
       else:
            print("sorry, You are under the minimum age for entry")
            input()
            break
# هنا نفس الكلام بردو 
# الانبت الفاضى هنا بيدى للمستخدم وقت يقرا فى سبب عدم دخوله او نجاحه فالتسجيل (انو تحت السن )       
         






#الكود كد بدون اختصار 
#  لانو بيديك معلومه المستخدم سجل دخول صح بعد كام مرا غلط 
#تفيد لو حبيت تظهرلو بعد التحققات عشان تتاكد انو المالك الفعلى 
#وممكن تنصحو بالتغير لو كرر الغلط  لعدد معين 











       

























#  print("please login in")
# user_name1=input("user name\n").capitalize()
# pass1=input("your password\n")
# while user_name1!=user_name or pass1!=password:
#        print("wrong, user or password")
#        check=input("if you want contine write yes (if you press enter you exit)")
#        if check :
#           user_name1=input("user name\n").capitalize
#           pass1=input("your password\n")
#        else:
#           exit()   
 
    
 
 

    # دا بق سطر لو سجل اليوزر والباسورد غلط غير اللى كان كاتبهم 
    #هيفضل يسجل هنا لحد ميسجل صح ويبدء يدخل للموقع او زى معايزو يتوجه بعد يدخل صح
      
                          
