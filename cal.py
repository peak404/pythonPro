
active = True
print("wanna using calculator ? yes or no")

while active:
    
    tag = input().lower()
    if tag == 'yes':
        try:

            print("enter the first number")
            num1 = float(input())
            print("enter the second number")
            num2 = float(input())
                        

            print("enter + - * / only one")
            op = input()

            if op == '+':
                print(num1+num2)
            elif op == '-':
                print(num1-num2)
            elif op == '*':
                print(num1*num2)
            elif op == '/':
                if num2 == 0:
                    print("cant  be  diveide by 0 ")
                else:
                    print(num1/num2)
            else:
                print("invalid op")
        except ValueError:
            print("must be number not str")
        
        

        
    elif tag == 'no':
        print("have fun")
        active = False
        break
    
    print("wanna retry again? yes or no")
        
        


