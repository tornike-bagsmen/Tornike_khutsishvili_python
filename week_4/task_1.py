import random

def main():
        
    quantity_of_player = int(input("please, write Quantity of players: "))
    
    for i in range(quantity_of_player):
        dice_0 = random.randint(1, 6)
        dice_1 = random.randint(1, 6)
        print(dice_0, dice_1)
        quantity_of_player -= 1
        
main()

# import random

# def main():
        
#     quantity_of_player = int(input("please, write Quantity of players: "))
    
#     while  quantity_of_player>0:
#         dice_0 = random.randint(1, 6)
#         dice_1 = random.randint(1, 6)
#         print(dice_0, dice_1)
#         quantity_of_player -= 1
        
# main()