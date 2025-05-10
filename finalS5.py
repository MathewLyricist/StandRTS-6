from datetime import datetime, timedelta


class PO:
    def __init__(self, name, maker):
        self.name = name
        self.maker = maker

    def info(self):
        return f"{self.name} ({self.maker})"

    def toUse(self):
        return True


class free(PO):
    def info(self):
        return f"Свободное ПО: {super().info()}"


class halfFree(PO):
    def __init__(self, name, maker, date, userfulLife):
        super().__init__(name, maker)
        self.date = datetime.strptime(date, "%Y-%m-%d")
        self.userfulLife = timedelta(days=userfulLife)

    def info(self):
        return f"Условно-бесплатное ПО: {super().info()}, установлено {self.date.strftime('%Y-%m-%d')}, срок {self.userfulLife.days} дней"

    def toUse(self):
        return datetime.now() < self.date + self.userfulLife


class commercial(PO):
    def __init__(self, name, maker, price, date, usefulLife):
        super().__init__(name, maker)
        self.price = price
        self.date = datetime.strptime(date, "%Y-%m-%d")
        self.userfulLife = timedelta(days=usefulLife)

    def info(self):
        return f"Коммерческое ПО: {super().info()}, цена {self.price}, установлено {self.date.strftime('%Y-%m-%d')}, срок {self.userfulLife.days} дней"

    def toUse(self):
        return datetime.now() < self.date + self.userfulLife


# Создание списка ПО
programs = [
    free("Linux", "Сообщество"),
    halfFree("WinRAR", "RARLAB", "2023-01-01", 30),
    commercial("Microsoft Office", "Microsoft", 5000, "2023-05-01", 365),
    free("GIMP", "Сообщество"),
    halfFree("Antivirus", "Kaspersky", "2023-06-01", 60)
]

# Вывод информации
for prog in programs:
    print(prog.info())

# Поиск доступного ПО
print("\nДоступное на текущую дату ПО:")
for prog in programs:
    if prog.toUse():
        print(prog.info())