from model import Model
from view import View


class Program:
    def __init__(self, model, view):
        self.model = model
        self.view = view

    def run(self):
        while True:
            self.view.main_menu()
            choice = self.view.get_choice()

            if choice == '1':
                animal_type, animal_name, birth_date = self.view.get_animal_data()
                self.model.add_home_animal(animal_type, animal_name, birth_date)
            elif choice == '2':
                animal_type, name, birth_date = self.view.get_animal_data()
                self.model.add_worker_animal(animal_type, name, birth_date)
            elif choice == '3':
                print("add soon")
            elif choice == '4':
                break
            else:
                print("Incorrect input. Try again")


def main():
    model = Model()
    view = View()
    program = Program(model, view)
    program.run()


if __name__ == '__main__':
    main()
