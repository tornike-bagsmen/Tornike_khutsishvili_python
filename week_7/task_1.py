def main():
    user_input = input("write strings here: ")
    input_len = len(user_input)
    for i in range(0, input_len, 2):  
        if user_input[i] != "e" :
            print(user_input[i], end = " ")
            
main()