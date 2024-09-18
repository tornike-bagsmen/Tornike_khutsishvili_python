import random
# import requests

def my_square_form(first_num, second_num):

    result = first_num**second_num

    print(f"რიცხვი {first_num}-ის მე-{second_num}-ე ხარისხია {result}")



def random_numbers():
    lower_num = -10000
    upper_num = 10000

    random_float = random.uniform(lower_num, upper_num)
    print(round(random_float,2))


def week_days_in_georgian(weekday):
    if weekday == "Monday":
        result = "ორშაბათი"

    elif weekday == "Tuesday":
        result = "სამშაბათი"

    elif weekday == "Wednesday":
        result = "ოთხშაბათი"

    elif weekday == "Tuesday":
        result = "ხუთშაბათი"

    elif weekday == "Friday":
        result = "პარასკევი"

    elif weekday == "Saturday":
        result = "შაბათი"

    else: result = "კვირა"

    print(f"ეს დღე იყო {result}")
