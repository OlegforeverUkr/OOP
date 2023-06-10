import datetime


class EmailAlreadyExistsException(Exception):
    pass


try:
    raise EmailAlreadyExistsException

except EmailAlreadyExistsException:
    time = datetime.datetime.now()
    error = f"{time} | EmailAlreadyExistsException\n"

    with open('logs.txt', 'a') as file:
        file.write(error)

    print("Email error. This email already exists.")
