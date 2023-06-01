import psycopg2

# database connection
connection = psycopg2.connect(database='phone',
                        user='postgres',
                        password='111',
                        host='127.0.0.1',
                        port=5432)
cursor = connection.cursor()

class Telephone:
    number = '0000000'  # default number
    _counter = 0  # incoming call counter

    def set_number(self, number):  # assigns a new number
        self.number = number

    def get_incoming_calls(self):  # get the number of incoming calls
        return self._counter

    def count_calls(self):  # increases the counter of incoming calls by one
        self._counter += 1

    def save_to_database(self):  # save incoming call count to the database
        cursor.execute(f'INSERT INTO calls (phone_number, incoming_calls) VALUES ({self.number}, {self._counter})')
        connection.commit()


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

cursor.execute("CREATE TABLE IF NOT EXISTS calls (id SERIAL PRIMARY KEY,\n"
               " phone_number VARCHAR(20), incoming_calls INTEGER)")

for i in phones:
    i.save_to_database()
    print(f'Phone {i.number} has {i.get_incoming_calls()} incoming calls')

# Close connect with database
cursor.close()
connection.close()

