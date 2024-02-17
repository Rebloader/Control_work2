class View:
    def main_menu(self):
        print("\nМеню:")
        print("1. Завести новое домашнее животное")
        print("2. Завести новое вьючное животное")
        print("3. Показать список команд")
        print("4. Выход")

    def get_choice(self):
        return input("Выберите действие: ")

    def get_animal_data(self):
        animal_type = input("Тип животного: ")
        animal_name = input("Кличка: ")
        birth_date = input("Дата рождения (гггг-мм-дд): ")
        return animal_type, animal_name, birth_date
