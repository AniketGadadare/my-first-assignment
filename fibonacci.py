n =  int(input("how many terms you wnat to enter"))
n1 = 0 #1 #1 #2
n2 = 1 #1 #2 #3
count = 0 #1 #2 #3

if(n<=0):
    print("please enter positive number !")
elif(n==1):
    print(n1)
elif(n>0):
    print("it is fibonacci series-----")
    while(count<=n):#0
        print(n2,end='')#0 #1 #1 #2

        n3=n1+n2 #0+1=1 #1+1=2 #2+1=3 #2+3=5

        n1 = n2 #1 #1 #2 #3
        n2 = n3 #1 #2 #3 #5

        count=count+1