# 1-ый вариант

money=float(input('Ввести сумму вклада под процент:' ))
per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
per_cent_values = list(map (float, per_cent.values())) #создаём список значений из словаря per_cent
print (per_cent_values) #выводим список значений из словаря per_cent для наглядности
deposit =[] #создаём пустой список
for i in range (0,4):
    deposit.append(money*per_cent_values[i]/100) #добавляем в список deposit значение дохода по вкладу, рассчитанное за год
print ('deposit=', deposit) #выводим список накопленных средства за год в каждом из банков
print("Максимальная сумма, которую вы можете заработать —", max(deposit)) #выводим максимальное значение дохода по вкладу#

# 2-ий вариант

# money=float(input('Ввести сумму вклада под процент:' ))
# per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
# per_cent_values = list(map (float, per_cent.values())) #создаём список значений из словаря per_cent
# print (per_cent_values) #выводим список значений из словаря per_cent для наглядности
# for i in range (0,4):
#   per_cent_values[i]=money*per_cent_values[i]/100 #переписываем каждое значения списка per_cent_values на значения дохода по вкладу, рассчитанное по формуле
# print ('deposit=', per_cent_values) #выводим список накопленных средства за год в каждом из банков
# print("Максимальная сумма, которую вы можете заработать —", max(per_cent_values))

#3-ий вариант

# money=float(input('Ввести сумму вклада под процент:' ))
# per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
# per_cent_values = list(map (float, per_cent.values())) #создаём список значений из словаря per_cent
# print (per_cent_values) #выводим список значений из словаря per_cent для наглядности
# deposit =[] #создаём пустой список
# deposit.append(money*per_cent_values[0]/100) #добавляем в список deposit значение дохода по вкладу
# deposit.append(money*per_cent_values[1]/100)
# deposit.append(money*per_cent_values[2]/100)
# deposit.append(money*per_cent_values[-1]/100)
# print ('deposit=', deposit) #выводим список накопленных средства за год в каждом из банков
# print("Максимальная сумма, которую вы можете заработать —", max(deposit)) #выводим максимальное значение дохода по вкладу
