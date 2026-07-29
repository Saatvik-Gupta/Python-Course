# Jug with water problem
Max_P=4
Max_Q=3

P,Q=0,0
print("Water Jug Problem (Goal 2L : water to be filled in Jug A (P) )\n")
print("Initial state considered P=0,Q=0 \n ")
while True:

    print("Current state : P=",P,"Q=",Q)
    if P==2:
        print("Goal Achieved! Jug A is filled upto 2 L\n")
        break

    print("Choose an action!\n")
    print("0. Stop (Exit Program)")
    print("1. Fill Jug A (P=4)")
    print("2. Fill Jug B (Q=3)")
    print("3. Empty Jug A (P)")
    print("4. Empty Jug B (Q)")
    print("5. Complete Transfer of water from Jug B-> Jug A")
    print("6. Complete Transfer of water from Jug A-> Jug B")
    print("7. Transfer of water from Jug B-> Jug A until Jug A is full")
    print("8. Transfer of water from Jug A-> Jug B until Jug B is full")

    choice=int (input("Enter the Choice\n"))

    if(choice==0):
                
                print("Exit the code!")
                break
                      
    elif choice ==1:
                 P=Max_P
    elif choice==2:
                 Q=Max_Q
    elif choice==3:
                P=0
    elif choice==4:
                Q=0
    elif choice==5:
                total=P+Q
                if total <= Max_P:
                    P=total
                    Q=0
                else:
                    print("Not enough space in JuG A for complete TRansfer:")
    elif choice==6:
                total=P+Q
                if total<=Max_Q:
                    Q=total
                    P=0
                else:
                    print("Not enough space in JuG B for complete TRansfer:")
    elif choice ==7:
                if P+Q<=Max_P:
                    P=P+Q
                    Q=0
                else:
                    Q=Q-(Max_P-P)
                    P=Max_P
    elif choice ==8:
                 if P+Q<=Max_Q:
                    Q=P+Q
                    P=0
    else:
        print("Invalid Choice!")