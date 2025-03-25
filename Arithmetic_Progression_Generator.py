first_Number= int(input("Enter first number of AP:"))
Length_of_AP= int(input("Enter length of AP:"))
common_Difference= int(input("Enter common difference of AP:"))
def arithmetic_Progression(a, n, d):
    for i in range (n):
        term_n= a+i*d
        print (term_n)
arithmetic_Progression(first_Number, Length_of_AP, common_Difference)