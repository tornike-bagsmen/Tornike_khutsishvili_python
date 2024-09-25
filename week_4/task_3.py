import random

def main():
    n_number = int(input("please, write number from 0 to 1000: "))
    
    if 0 < n_number < 1000:
        for i in range(1, n_number+1) :
            if n_number % i == 0:
                print(i, end= " ")
    else:
        print("wrong number!")

main()


# import random

# def main():
#     n_number = int(input("please, write number from 0 to 1000: "))
#     n = 1
#     if 0 < n_number < 1000:
#         while n_number  >= n :
#             if n_number % n == 0:
#                 print(n, end= " ")
#             n += 1
#     else:
#         print("wrong number!")

# main()
