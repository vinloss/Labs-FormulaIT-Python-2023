numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

# TODO заменить значение пропущенного элемента средним арифметическим

find_missed_element = 4
sum_ = sum(numbers[:find_missed_element]) + sum(numbers[find_missed_element+1:])
lenght = len(numbers)
srednee = sum_ / lenght
numbers[find_missed_element] = srednee
print("Измененный список:", numbers )
