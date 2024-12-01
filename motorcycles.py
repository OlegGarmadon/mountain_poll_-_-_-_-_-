motorcyles = ['honda', 'yamaha', 'suzuki']
print(motorcyles)
motorcyles[0] = 'ducati'
print(motorcyles)
motorcyles.append('ducati')
print(motorcyles)
motorcyles[0] = 'honda'
print(motorcyles)

#Составление списка если данные становяться известны только после начала программы.

motorcyles = []
motorcyles.append('honda')
motorcyles.append('yamaha')
motorcyles.append('ducati')
print(motorcyles)

# Вставка элементов в список метод insert().

motorcyles = ['honda', 'yamaha', 'suzuki']
motorcyles.insert(0, 'ducati')
print(motorcyles)

# Удаление элементов списка del

motorcyles = ['honda', 'yamaha', 'suzuki',]
print(motorcyles)
del motorcyles[0]
print(motorcyles)

# Метод pop()

motorcyles = ['honda', 'yamaha', 'suzuki',]
print(motorcyles)
poped_motorcyles = motorcyles.pop()
print(motorcyles)
print(poped_motorcyles)
motorcyles = ['honda', 'yamaha', 'suzuki',]
last_owned = motorcyles.pop()
print(f"Последний купленный мной мотоцикл {last_owned.title()}")
motorcyles = ['gt', 'yamaha', 'suzuki',]
print(motorcyles)
first_owned = motorcyles.pop(2)
print(f"Я продал этот мотоцикл {first_owned.title()}.")

# Удаление элементов по значению метод remore().

motorcyles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcyles)
motorcyles.remove('ducati')
print(motorcyles)
motorcyles = ['honda', 'yamaha', 'suzuki', 'ducati']
too_expensive = 'ducati'
motorcyles.remove(too_expensive)
print(motorcyles)
print(f"\nA {too_expensive.title()} is too expensive for me.")  # Дукати для меня слишком дорогой.