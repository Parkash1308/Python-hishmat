a= int(input("Enter any number: "))
b= input("Enter any Operato: ")
c= int(input("Enter 2nd number: "))
if b=='+':
    print("sum is: ",a+c)
elif b=='-':
    print("subtraction is: ",(a-c))
elif b=='*':
    print("Multiplication is: ",(a*c))
elif b=='/':
    if c==0:
        print("Envalid")
    else:
        print("subtraction is: ",(a/c))



    