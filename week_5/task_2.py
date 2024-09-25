
def main():
    user_number = int(input("Choose number between 1-9: "))
   
    if not 1 <= user_number <= 9:
        print("Wrong number! Please, choose between 1-9.")
    else:
        for i in range(1, user_number + 1):
            line = ""
            for j in range(1, i + 1):
                result = i * j
                line += f"{i} * {j} = {result}"
                if j < i:
                    line += "   "
            print(line)

main()