import datetime
from help_1 import week_days_in_georgian

def main():
    print("პროგრამა ითვლის თარიღის მიხედვით კვირის დღეს")
    year = int(input("ჩაწერეთ წელი: "))
    month = int(input("ჩაწერეთ თვე: "))
    number = int(input("ჩაწერეთ რიცხვი: "))
    time = datetime.datetime(year, month, number)
    time = time.strftime("%A")

    week_days_in_georgian(time)

main()