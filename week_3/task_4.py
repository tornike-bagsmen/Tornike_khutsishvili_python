import random

def main():
    color_list = ["ყვავი", "ჯვარი", "გული", "აგური"]
    card_value_list = ["A", "K", "Q", "J", "10", "9", "8", "7", "6", "5", "4", "3", "2"]
    
    color_value = random.choice(color_list)
    card_value = random.choice(card_value_list)

    print(card_value, color_value)


main()