def main():
    
    # 30 არცერთ კატეგორიაში არ იყო და SLOW-ში ჩავსვი

    car_speed = int(input("გთხოვთ, ჩაწეროთ მანქანის სიჩქარე კმ/სთ-ებში: "))
    
    if car_speed < 1 :
        print("თქვენ შეიყვანეთ არასწორი სიჩქარე! ")
        exit(1)    
        
    if car_speed > 120 :
        print("VERY FAST")
        
    elif car_speed > 60 :
        print("FAST")
        

    elif car_speed > 30 :
        print("MODERATE")
        
    else:
        print("SLOW")
    
main()