numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

# TODO заменить значение пропущенного элемента средним арифметическим

skip_none = numbers[:4] + numbers[5:]
incorrect_number = numbers[4]
correct_number = (sum(skip_none) / len(numbers))
numbers[4] = correct_number

print("Измененный список:", numbers)
