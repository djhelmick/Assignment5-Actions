import datetime


def firstrun():
    return "success"


def area(radius):
    pi = 3.14159265359
    return (pi * (radius * radius))


def firstAndLast(collection):
    return [collection[0], collection[-1]]


def dateDifference(date1: datetime, date2: datetime):
    delta = date1 - date2
    return delta.days
