import mysql.connector


class Model:
    def __init__(self):
        self.connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='password',
            database='друзья человека'
        )
        self.cursor = self.connection.cursor()
        self.animal_cursor = self.connection.cursor()

    def add_home_animal(self, animal_type, animal_name, birth_date):
        correct_types = ['кошка', 'собака', 'хомяк']
        if animal_type in correct_types:
            self.cursor.execute("INSERT INTO `домашние_животные` (`тип`, `кличка`, `дата_рождения`) VALUES (%s, %s, %s)",
                                (animal_type, animal_name, birth_date))
            self.connection.commit()
        else:
            raise ValueError('Указан неверный тип домашнего животного')

    def add_worker_animal(self, animal_type, animal_name, birth_date):
        correct_types = ['лошадь', 'осел']
        if animal_type in correct_types:
            self.cursor.execute("INSERT INTO `вьючные_животные` (`тип`, `кличка`, `дата_рождения`) VALUES (%s, %s, %s)",
                                (animal_type, animal_name, birth_date))
            self.connection.commit()
        else:
            raise ValueError('Указан неверный тип домашнего животного')

    def __del__(self):
        self.cursor.close()
        self.animal_cursor.close()
        self.connection.close()
