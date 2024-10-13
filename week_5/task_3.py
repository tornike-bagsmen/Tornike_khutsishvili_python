def main():
  enter_number = int(input("enter number from 0 to 20: "))
   
  if not 0 < enter_number < 20:
    print("wrong number! please, choose from 0 to 20")
  else:
    first_var = 0
    second_var = 1
    count = 0
       
    while count <= enter_number:
      print(first_var, end=' ')
      next = first_var + second_var
      first_var = second_var
      second_var = next
      count += 1

main()