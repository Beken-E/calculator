
first = "Not_empty"
second = "Not_empty"
act = ""
check = "Not_empty"
res = 0


while check != '':

    while type(first) != int:
        a = input("Введите первое значение:") 
        if a.isdigit() == True:
            first = int(a)
        else:  
            print("Вводите только цифры") 

    while act != "+" or act != "-" or act != "*" or act != "/":
        b = input("Введите действие:")
        if b == "+" or b == "-" or b == "*" or b == "/":
            act = b
            break
        else:
            print("Возможные действия это +  -  *  / ")

    while type(second) != int:
        c = input("Введите второе значение:") 
        if c == "0" and act == "/":
            print("Нельзя же делить на ноль")
        elif c.isdigit() == True:
            second = int(c)
        else:  
            print("Вводите только цифры") 

    if act == "+":
        res = first + second
        
    elif act == "-":
        res = first - second
        
    elif act == "*":
        res = first * second
        
    else:
        res = first / second
            
    print(f"Результат на действие {first} {act} {second}, ровняется: {res}")
    check = input("Что делать дальше? \n Нажмите Enter чтобы закончить или любую другую кнопку что-бы продолжить:")
    first = "Not_empty"
    second = "Not_empty"
    act = ""
    res = 0
print("Калькулятор закрыт")
    
















