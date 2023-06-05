import psycopg2

class DatabaseManager:
    def __init__(self, database='phone', user='postgres', password='111', host='127.0.0.1', port=5432):
        self.connection = psycopg2.connect(database=database, user=user, password=password, host=host, port=port)
        self.cursor = self.connection.cursor()

    def create_table(self):
        self.cursor.execute("CREATE TABLE IF NOT EXISTS calls (id SERIAL PRIMARY KEY, "
                            "phone_number VARCHAR(20), incoming_calls INTEGER)")
        self.connection.commit()

    def save_to_database(self, number, counter):
        self.cursor.execute(f"INSERT INTO calls (phone_number, incoming_calls) VALUES ('{number}', {counter})")
        self.connection.commit()

    def close_connection(self):
        self.cursor.close()
        self.connection.close()


class Telephone:
    def __init__(self, number='0000000', counter=0):
        self.number = number  # default number
        self.counter = counter  # incoming call counter

    def __str__(self):
        return f'Create Class Telephone with number - {self.number}'

    def set_number(self, number):  # assigns a new number
        self.number = number

    def get_incoming_calls(self):  # get the number of incoming calls
        return self.counter

    def count_calls(self):  # increases the counter of incoming calls by one
        self.counter += 1


db_manager = DatabaseManager()

my_phone = Telephone()
my_phone1 = Telephone()
my_phone2 = Telephone()
my_phone3 = Telephone
my_phone.number = '1111111111'
my_phone1.number = '222222222'
my_phone2.number = '333333333'
my_phone.count_calls()
my_phone1.count_calls()
my_phone2.count_calls()
my_phone.count_calls()
my_phone1.count_calls()
my_phone2.count_calls()
my_phone.count_calls()
my_phone1.count_calls()
my_phone2.count_calls()
my_phone.count_calls()
my_phone1.count_calls()
my_phone2.count_calls()
my_phone1.count_calls()
my_phone2.count_calls()
phones = [my_phone, my_phone1, my_phone2]

db_manager.create_table()

for phone in phones:
    phone.save_to_database(phone.number, phone.get_incoming_calls())
    print(f'Phone {phone.number} has {phone.get_incoming_calls()} incoming calls')

db_manager.close_connection()
