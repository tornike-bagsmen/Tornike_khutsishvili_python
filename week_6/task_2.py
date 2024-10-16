def main():
    enter_num = int(input("enter number from 0 to 1000: "))

    if not 0 < enter_num <= 1000 :
        print("wrong number mate.")
        exit(1)

    while enter_num != 1:

        if enter_num % 2 == 0:
            enter_num = enter_num / 2

        else:  
            enter_num = enter_num * 3 + 1
            
        if enter_num != 1:
            print(int(enter_num),end=" -> ")
        else:
            print(int(enter_num))
        
        

main()