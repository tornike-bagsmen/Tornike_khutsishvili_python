import random

def main():
    guessing_num = random.randint(0, 100)
    counter = 10
    cou = "last"

    while counter > 0:

        count = counter

        if count == 1:
            count = cou

        guess_num = int(input(f"try to guess the num, you have {count} try: "))       
        counter -= 1      

        if not 0 < guess_num < 100:
            continue

        if guess_num == guessing_num:
            result = "you are winner"

        elif counter == 0 :
            result = "computer is winner"

        elif guess_num < guessing_num:
            result = "low"

        elif guess_num > guessing_num:
            result = "high"
        
        print(result)

        

main()