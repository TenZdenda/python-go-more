import json_handler
import helper


print("There are 3 commands - C = Create, R = Date, S = Search")
cmd = input("Choose a command: ")
code = cmd[0].upper()

if code == "C":

    from_city = input("From city: ")
    to_city = input("To city: ")
    date = input("Date (Y-m-d): ")
    number_of_seats = input("Number of seats: ")

    if helper.check_date_format(date) or helper.check_seat(number_of_seats):
        json_ride = {"from": from_city, "to": to_city, "date": date, "seats": number_of_seats}
        json_handler.write_ride(json_ride)

elif code == "R":

    date = input("Date (Y-m-d): ")
    if helper.check_date_format(date):
        json_handler.search_date(date)

elif code == "S":

    print("Note: All inputs are optional. If you have no data for a given input just smash enter")

    from_city = input("From city: ")
    to_city = input("To city: ")
    from_date = input("From date (Y-m-d): ")
    to_date = input("To date (Y-m-d): ")
    min_number_of_seats = input("Min. number of seats: ")

    json_handler.search_ride(from_city, to_city, from_date, to_date, min_number_of_seats)

else:
    print("This command not exist!")
