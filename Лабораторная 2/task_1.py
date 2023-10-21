money_capital = 20000  # Подушка безопасности
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
increase = 0.05  # Ежемесячный рост цен

# TODO Посчитайте количество  месяцев, которое можно протянуть без долгов
count = 0
while money_capital >= 0:
    if count > 0:
        spend *= 1 + increase
    money_capital += salary - spend
    if money_capital < 0:
        break
    count += 1
print("Количество месяцев, которое можно протянуть без долгов:", count)
