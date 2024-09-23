import random

def main():

    num_list = []
    n_number = int(input("write number from 0 to 30: "))
    
    if 0 < n_number < 30:
        for _ in range(n_number):
            random_numbers = random.randint(0, 1000)
            num_list.append(random_numbers)
           
        print(max(num_list))

    else:
        print("you chose wrong number, sorry mate")

main()

# import random

# def main():

#     num_list = []
#     n_number = int(input("write number from 0 to 30: "))
    
#     if 0 < n_number < 30:
#         while n_number > 0 :
#             random_numbers = random.randint(0, 1000)
#             num_list.append(random_numbers)
#             n_number -= 1

#         print(max(num_list))

#     else:
#         print("you chose wrong number, sorry mate")


    

# main()
