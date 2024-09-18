def main():

    num_1 = int(input("გთხოვთ ჩაწეროთ პირველი რიცხვი: "))
    num_2 = int(input("გთხოვთ ჩაწეროთ მეორე რიცხვი: "))
        
    if num_1 == 0 or num_2 == 0:
        print("ერთერთი რიცხვი ნულია.")
        exit(1)
    
            
    if (num_1 < 0 and num_2 < 0 ) or (num_1 > 0 and num_2 > 0 ):
        if num_1 % num_2 == 0:
            print(f"{num_1} არის {num_2} ის ჯერადი რიცხვი.")
        else:
            print(f"{num_1} არ არის {num_2} ის ჯერადი რიცხვი.")
        
    else:
        print("ორივე რიცხვი უნდა იყოს დადებითი ან უარყოფითი!")

main()
    