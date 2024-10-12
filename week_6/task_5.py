

def main():
  user_input = int(input("Enter number: "))

  if not 0 < user_input < 10:
    exit(1)

  count = 0

  while count <= user_input:
    spaces = ' ' * (user_input - count)
    print(spaces, end='')
   
    count2 = count
    while count2 >= 0:
      print(count2, end = '')
      count2 -= 1
   
    count3 = 1
    while count3 <= count:
      print(count3, end = '')
      count3 += 1
   
    print()
    count += 1
main()
