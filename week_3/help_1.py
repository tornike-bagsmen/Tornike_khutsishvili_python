import random
import math 

def my_square_form(first_num, second_num):

    result = first_num**second_num

    print(f"რიცხვი {first_num}-ის მე-{second_num}-ე ხარისხია {result}")



def random_numbers():
    lower_num = -10000
    upper_num = 10000

    random_float = random.uniform(lower_num, upper_num)
    return(math.floor(random_float * 10) / 10)


def week_days_in_georgian(weekday):

    match weekday:
        case "Monday":
            return "ორშაბათი"
        case "Tuesday":
            return "სამშაბათი"
        case "Wednesday":
            return "ოთხშაბათი"
        case "Thursday":
            return "ხუთშაბათი"
        case "Friday":
            return "პარასკევი"
        case "Saturday":
            return "შაბათი"
        case "Sunday":
            return "კვირა"