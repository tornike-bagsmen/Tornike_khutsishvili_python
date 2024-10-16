def main():
    user_input = input("write any word here: ")
    input_len = len(user_input)
    centre = int((input_len - 1) / 2)

    if input_len % 2 == 0 :
        middle = f"{user_input[centre]}{user_input[centre + 1]}"              
    else:
        middle =user_input[centre]

    while input_len > 0 :
        print(f"last: {user_input[-1]}   middle: {middle}   first: {user_input[0]}")
        input_len -= 1       

main()


    