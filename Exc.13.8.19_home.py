a = int(input('Кол-во билетов ', )) #кол-во билетов
list = [] #список для добавление стоимости в расчёте на возраст
i = 0 #переменная-счётчик
while i<a: #для каждого билета запрашивается возраст посетителя, в соответствии со значением которого выбирается стоимость
    v= int(input('Введите возраст ', )) #вводим возраст
    if v<18:
        list.append(0)
    elif 18<=v<25:
        list.append(990)
    elif 25<=v<100:
        list.append(1390)
    i=i+1
print (list) #вывел просто для проверки
Price = int(sum(list)) #присваиваем переменной общее значение суммы за билеты
print (Price) #выводим значение суммы (для проверки)
if a>3: #расчитываем скидку исходя из количества билетов
    Price = Price-(Price*10/100)
    print (f"Cумма с учётом скидки 10% за {a} билета(ов) составляет {Price} руб.")
else:
    print (f"Итоговая сумма к оплате за {a} билета(ов) составляет {Price} руб.")

print("---------------------------")

print ('Оплата прошла успешно! Спасибо за заказ! Ждём вас!')


