import datetime


def check_date_format(date):
    try:
        datetime.datetime.strptime(date, "%Y-%m-d")
        return True
    except ValueError:
        print("This is the incorrect date string format. It should be YYYY-MM-DD")
        return False


def check_seat(seat):
    if seat.isnumeric():
        return True
    else:
        print("This seat number is not a number!")
        return False


def format_date(date):
    return datetime.datetime.strptime(date, "%Y-%m-%d").date()