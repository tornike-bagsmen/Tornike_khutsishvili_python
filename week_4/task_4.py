def main():
    
    first_var = 1
    second_var = 0
    n = first_var + second_var

    enter_number = int(input("write number: "))

    if 0 < enter_number <20:

        for i in range(1, enter_number):
            first_var = second_var
            second_var = n
            n = first_var + second_var
            enter_number -= 1

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