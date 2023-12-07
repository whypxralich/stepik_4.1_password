print ("Введите пароль:")
password = input()
print ("Подтвердите пароль:")
password_conf = input()
if password == password_conf:
    print ("Пароль успешно сохранен!")
else: 
    while password != password_conf:
        print ("Пароли различаются, повторите попытку.")
        print ("Введите пароль:")
        password = input()
        print ("Подтвердите пароль:")
        password_conf = input()
        print ("Пароль успешно сохранен!")