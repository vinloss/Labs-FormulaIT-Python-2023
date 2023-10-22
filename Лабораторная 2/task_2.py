salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
months = 10  # Количество месяцев, которое планируется протянуть без долгов
increase = 0.03  # Ежемесячный рост цен

# TODO Рассчитайте подушку безопасности, чтобы протянуть 10 месяцев без долгов
money_capital = 0

for _ in range(months):
    money_capital += salary  # Добавляем зарплату в подушку безопасности
    money_capital -= spend   # Вычитаем расходы на проживание
    spend *= (1 + increase)  # Увеличиваем расходы на следующий месяц

money_capital = round(money_capital, 2)
print(f"Подушка безопасности, чтобы протянуть {months} месяцев без долгов:", abs(money_capital))
