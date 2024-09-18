def main():
    
    num_1 = int(input("გთხოვთ ჩაწეროთ მთელი რიცხვი 1-დან 10-მდე: "))
 
    if num_1 < 0 or num_1 > 10:
        print("თქვენ შეიყვანეთ არასწორი რიცხვი.")
        exit(1)
    
    if num_1 == 0 or num_1 == 1:
        print(f"{num_1}-ს არ აქვს მარტივი გამყოფები. ")
        exit(0)
        
    if num_1 == 2 or num_1 == 3 or num_1 == 5 or num_1 == 7:
        print(f"{num_1}- ის მარტივი გამყოფია {num_1}.")
        
    elif num_1==4 or num_1 == 8:
        print(f"{num_1}-ის მარტივი გამყოფია 2.")
        
    elif num_1 == 6:
        print(f"{num_1}-ის მარტივი გამყოფებია 2 და 3.")
        
    elif num_1 == 9:
        print(f"{num_1}-ის მარტივი გამყოფია 3.")
        
    else:
        print(f"{num_1}-ის მარტივი გამყოფებია 2 და 5.")
        
main()