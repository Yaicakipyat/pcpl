class Manufacturer:

    def __init__(self, id, name):
        self.id = id
        self.name = name

class Part:

    def __init__(self, id, name, price, manufacturer_id):
        self.id = id
        self.name = name
        self.price = price
        self.manufacturer_id = manufacturer_id

class PartManufacturer:

    def __init__(self, part_id, manufacturer_id):
        self.part_id = part_id
        self.manufacturer_id = manufacturer_id

manufacturers = [
    Manufacturer(1, "Завод Альфа"),
    Manufacturer(2, "Завод Бета"),
    Manufacturer(3, "Фабрика Гамма"),
]

parts = [
    Part(1, "Аккумулятор", 4500, 1),
    Part(2, "Болт", 15, 1),
    Part(3, "Амортизатор", 3200, 2),
    Part(4, "Двигатель", 85000, 2),
    Part(5, "Фильтр", 700, 3),
]

parts_manufacturers = [
    PartManufacturer(1, 1),
    PartManufacturer(1, 2),
    PartManufacturer(2, 1),
    PartManufacturer(3, 2),
    PartManufacturer(3, 3),
    PartManufacturer(4, 2),
    PartManufacturer(5, 3)
]


def main():
    print("Запрос Е1")

    for manufacturer in manufacturers:
        if "завод" in manufacturer.name.lower():
            print(f"{manufacturer.name}: ", end="")

            separator = ""
            for part in parts:
                if part.manufacturer_id == manufacturer.id:
                    print(f"{separator}{part.name}", end="")
                    separator = ", "

            print()
    print()

    print("Запрос Е2")

    result = []
    for manufacturer in manufacturers:
        total_price = 0
        amount = 0

        for part in parts:
            if(part.manufacturer_id == manufacturer.id):
                total_price += part.price
                amount += 1

        average_price = round(total_price / amount, 2)
        result.append((manufacturer.name, average_price))

    result.sort(key=lambda item: item[1])
    for name, average in result:
        print(f"{name}: {average:.2f} руб.")
    print()


    print("Запрос Е3")

    for part in parts:

        if (part.name.lower().startswith("а")):
            print(f"{part.name}: ", end="")
            separator = ""

            for link in parts_manufacturers:
                if (link.part_id == part.id):

                    for manufacturer in manufacturers:
                        if (manufacturer.id == link.manufacturer_id):
                            print(f"{separator}{manufacturer.name}", end="")
                            separator = ", "
            print()

if __name__ == "__main__":
    main()