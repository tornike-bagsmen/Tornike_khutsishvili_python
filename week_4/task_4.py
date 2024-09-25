def main():
    
    first_var = 0
    second_var = 1
    n = first_var + second_var

    enter_number = int(input("write number from 0 to 20: "))

    if 0 < enter_number <20:

        for _ in range(2, enter_number):
            first_var = second_var
            second_var = n
            n = first_var + second_var

        print(n)
    else:
        print("you chose non valid number.")
        
main()

# def main():
    
#     first_var = 1
#     second_var = 0
#     n = first_var + second_var

#     enter_number = int(input("write number: "))

#     if 0 < enter_number <20:

#         while enter_number > 1:
            

#             first_var = second_var
#             second_var = n
#             n = first_var + second_var
#             enter_number -= 1
#         print(n)
#     else:
#         print("you chose non valid number.")

# main()