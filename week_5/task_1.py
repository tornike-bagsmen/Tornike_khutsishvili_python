def main():
  user_number = int(input("Choose number between 0-50: "))
 
  if not 0 < user_number < 50:
    print("Wrong number! Please, choose between 0-50")
  else:
    for i in range(1, user_number+1):
      result = f"{i} - "
      count = 0
     
      for j in range(1,i+1):
        if i % j == 0:
          if count < 3:
            result += f" {j}"
            count += 1
         
      print(result)
 
main()