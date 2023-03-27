import re
from datetime import datetime

class Car:
    def __init__(self, owner, car, license_plate, entry_date, exit_date=None):
        self.owner = owner
        self.car = car
        self.license_plate = license_plate
        self.entry_date = entry_date
        self.exit_date = exit_date

def add_car(owner, car, license_plate, entry_date, car_list):
    if not validate_license_plate(license_plate):
        print("Placa inválida. A placa deve ter o formato NN-NN-LL ou NN LL NL.")
        return
    # Converte a data de entrada para um objeto datetime para facilitar a manipulação
    entry_date = datetime.strptime(entry_date, "%d/%m/%Y")
    new_car = Car(owner, car, license_plate, entry_date)
    car_list.append(new_car)
    print("Carro adicionado com sucesso!")

def remove_car(license_plate, car_list):
    for car in car_list:
        if car.license_plate == license_plate:
            car_list.remove(car)
            print("Carro removido com sucesso!")
            return
    print("Carro não encontrado.")

def search_license_plate(license_plate, car_list):
    for car in car_list:
        if re.search('^'+license_plate, car.license_plate):
            return car
    return None

def validate_license_plate(license_plate):
    pattern = '^(\d{2}[ -]?){2}[a-zA-Z]{2}$'
    return re.match(pattern, license_plate) is not None

def print_car_list(car_list):
    print("Lista de carros:")
    for car in car_list:
        print(f"Proprietário: {car.owner} | Carro: {car.car} | Placa: {car.license_plate} | Entrada: {car.entry_date.strftime('%d/%m/%Y')} | Saída: {car.exit_date or 'N/A'}")

def main():
    car_list = []
    while True:
        print("\nO que você deseja fazer?")
        print("1 - Adicionar carro")
        print("2 - Remover carro")
        print("3 - Procurar carro pela placa")
        print("4 - Imprimir lista de carros")
        print("5 - Sair")

        option = input("Opção escolhida: ")
        if option == "1":
            owner = input("Digite o nome do proprietário: ")
            car = input("Digite o modelo do carro: ")
            license_plate = input("Digite a placa do carro (no formato NN-NN-LL ou NN LL NL): ")
            entry_date = input("Digite a data de entrada (no formato DD/MM/YYYY): ")
            add_car(owner, car, license_plate, entry_date, car_list)
        elif option == "2":
            license_plate = input("Digite a placa do carro a ser removido: ")
            remove_car(license_plate, car_list)
        elif option == "3":
            license_plate = input("Digite a placa do carro a ser procurado: ")
            car = search_license_plate(license_plate, car_list)
            if car:
                print(f"Proprietário: {car.owner} | Carro: {car.car} | Placa: {car.license_plate} | Entrada: {car.entry_date.strftime('%d/%m/%Y')} | Saída: {car.exit_date
