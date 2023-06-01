class Telephone:
    number = ''
    _counter = 0

    def set_number(self, number):
        self.number = number

    def get_incoming_calls(self):
        return self._counter

    def count_calls(self):
        self._counter += 1


my_phone = Telephone()
my_phone.number = '214124'

print(my_phone.number)



