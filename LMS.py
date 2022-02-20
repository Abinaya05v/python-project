print("\t\tLIBRARY MANAGEMENT")
a=[["harry potter",20],["python",30],["who will cry when you die",15],["the alchemist",30],["400 days",20],["children books",10]]
print(a)
print("enter 1 to borrow")
print("enter 2 to return")
print("enter 3 to exit")
n=int(input("enter your choice"))   
if (n==1):
    name=input("enter your name:")
    for i in range(len(a)):
        print("enter",i,"to borrow",a[i])
    m=int(input("enter your choice "))
    A=[]
    A.append(a[m])
    fare=a[m][1]
    A.append(fare)
    print(name,"borrowed book ",A[0][0],"and fare is",A[1],"and return it before 2 months from date of borrowed")
    print("you cant borrow more than one book at a time")
elif n==2:
    name=input("enter your name:")
    for i in range(len(a)):
        print("enter",i,"to return",a[i])
    m=int(input("enter your choice:"))
    print(name,"has returned the book",a[m][0]," successfully...")
    print("\t\tTHANK YOU FOR VISITING,,COME AGAIN")
elif n==3 :
    print("\t\tTHANK YOU FOR VISITING....COME AGAIN")
else:
    print("enter a valid number")
