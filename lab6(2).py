unique_guests = set()
print("Вводите имена гостей (каждое с новой строки). Для завершения введите пустую строку:")

while True:
    name = input().strip()
    if name == "":
        break
    unique_guests.add(name)


print(len(unique_guests))
