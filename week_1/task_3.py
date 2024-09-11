def main():
    size_1 = int(input("ჩაწერე სამკუთხედის პირველი გვერდის სიგრძე სმ_ებში"))
    size_2 = int(input("ჩაწერე სამკუთხედის მეორე გვერდის სიგრძე სმ_ებში"))
    size_3 = int(input("ჩაწერე სამკუთხედის მესამე გვერდის სიგრძე სმ_ებში"))
    p_triangle = (size_1 + size_2 + size_3)/2
    
    s_triangle = p_triangle*(p_triangle-size_1)*(p_triangle-size_2)*(p_triangle-size_3)
    s_triangle = round(s_triangle **(1/2), 2)
    print(f"სამკუთხედის პერიმეტრია {p_triangle} სმ")
    print(f"სამკუთხედის ფართობია {s_triangle} სმ²") 
    
main()