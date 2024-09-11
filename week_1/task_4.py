def main():
    fahren = float(input("გთხოვთ ჩაწეროთ ტემპერატურა ფარენჰეიტში"))
    cel = int((fahren-32)*(5/9))
    print(f"{fahren} ფარენჰეიტი უდრის {cel} ცელსიუსს")
main()