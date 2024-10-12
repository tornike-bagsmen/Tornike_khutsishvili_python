def main():
    user_input = int(input("Enter numberfrom 0 to 10: "))
    if not 0 < user_input < 10:
        exit(1)
    count = 1

    while True:
        if count < user_input:
            for i in range(1, count+1):
                print(i, end = "")
            print()
            count += 1
        else:
            while count > 0:
                for i in range(1, count+1):
                    print(i, end = "")
                print()
                count -= 1
            break
main()