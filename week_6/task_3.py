def main():

    
    user_input = input("write number from 0 to 10 000: ")
    sum = 0

    if not 0 < int(user_input) <= 10000:
        print("you chose wrong number")
        exit(1)
        
    for i in user_input :
        sum += int(i)

    reverse = len(user_input)
    reversed_num = ""

    while reverse != 0:
        for i in user_input:
            na = int(user_input[reverse-1])
            reversed_num += f"{na}"
            reverse -= 1
  
    print(f"enter number: {user_input}",
          f"reverse number is: {reversed_num}",
          f"sum of digite: {sum}", sep="\n")

main()