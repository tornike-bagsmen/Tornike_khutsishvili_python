
def main():
    n = int(input("Choose number from 0 to 50: "))
   
    if not 0 < n <= 50:
        print("Wrong number! Please, choose from 0 to 50")
    else:
      print(" " * (n - 1) + "*")

      for i in range(1, n):
        print(" " * (n - i - 1) + "/"*i + "|" + "\\"*i)

   
      print(" " * (n - 1) + "|")

main()