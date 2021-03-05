class Car:
    brand = None
    model = None
    color = None
    hp = None
    accidents = None
    __type = None
    __mileage = None

    def car_desc(self):
        desc = f"Marka i model: {self.brand} {self.model}. Samochód jest w kolorze {self.color}. Typ pojazdu to {self.__type}. Posiada moc w wysokości {self.hp}km. " \
               f"Przebieg pojazdu: {self.__mileage} "
        if self.accidents == 0 or self.accidents == None:
            print(desc + "Pojazd jest bezwypadkowy")
        else:
            print(desc + f"Pojazd ma zarejestrowane wypadki w wysokości: {self.accidents}")

    def register_accident(self):
        if self.accidents == None:
            self.accidents = 1
            print("Wypadek Zarejestrowany!")
        elif self.accidents >= 0:
            self.accidents += 1
            print("Wypadek Zarejestrowany!")
        else:
            print("Błąd rejstracji wypadku, zgłoś się do administratora")

    def set_type(self):
        types = ["SmallCar", "CityCar", "Compact", "Sedan", "Combi", "Minivan", "Suv", "Cabrio", "Coupe"]
        print("Wybierz typ pojazdu")
        for x in range(0, len(types)):
            print(f"{x}. {types[x]}")
        selected = int(input())
        if selected >= 0 and selected < len(types):
            self.__type = types[selected]
            print("Poprawnie ustawiono typ pojazdu")
        else:
            print("Błąd przy ustawianiu typu pojazdu")

    def set_mileage(self):
        print("Podaj nowy przebieg pojazdu: ")
        new_mileage = int(input())
        if self.__mileage == None or self.__mileage < new_mileage:
            self.__mileage = new_mileage
            print("Nowy przebieg zarejestrowany!")
        elif self.__mileage > new_mileage:
            print("Nie mozna ustawić mniejszego przebiegu niż był zarejestrowany!")


def main():
    VolvoS80 = Car()
    VolvoS80.brand = "Volvo"
    VolvoS80.model = "S80"
    VolvoS80.color = "Race Red"
    VolvoS80.hp = 136
    VolvoS80.accidents = 2
    VolvoS80._Car__mileage = 231041
    VolvoS80.set_type()
    VolvoS80.car_desc()
    VolvoS80.register_accident()
    VolvoS80.set_mileage()
    VolvoS80.car_desc()


if __name__ == "__main__":
    main()
