import json
import helper


def write_ride(json_ride):
    data = read_rides()

    data.append(json_ride)

    with open('data.json', 'w') as file:
        json.dump(data, file, indent=4)


def read_rides():
    with open('data.json') as file:
        data = json.load(file)
    return data


def search_date(date):
    rides = read_rides()
    if not rides:
        print("No trips were found :(")

    ride = rides[-1]

    json_ride = {"from": ride['to'], "to": ride['from'], "date": date, "seats": ride['seats']}
    write_ride(json_ride)


def search_ride(start, end, date_from, date_to, min_seats):
    rides = read_rides()

    if min_seats == "":
        min_seats = "1"

    for ride in rides:
        has_start = False
        has_end = False
        has_date_from = False
        has_date_to = False
        has_min_seats = False

        if start.lower() == ride['from'].lower() or start == "":
            has_start = True
        if end.lower() == ride['to'].lower() or end == "":
            has_end = True
        if date_from != "":
            has_date_from = True
        if date_to != "":
            has_date_to = True
        if int(min_seats) <= int(ride['seats']):
            has_min_seats = True

        string = "{} | {} | {} | {}".format(ride['from'], ride['to'], ride['date'], ride['seats'])

        if has_start and has_end and has_min_seats:
            if has_date_from and not has_date_to:
                if helper.format_date(ride['date']) == helper.format_date(date_from):
                    print(string)
            if has_date_to and not has_date_from:
                if helper.format_date(ride['date']) == helper.format_date(date_to):
                    print(string)
            if not has_date_to and not has_date_from:
                print(string)
            if has_date_from and has_date_to:
                if helper.format_date(date_from) <= helper.format_date(ride['date']) <= helper.format_date(date_to):
                    print(string)
