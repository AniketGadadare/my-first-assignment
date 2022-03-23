n = int(input("enter the numbers :"))
list = []
even_count=0
odd_count=0
for i in range(1,n+1):
    list.append(i)
    #print(a)
print('sample numbers:',list)
for num in list:
    if(num%2==0):
        even_count=even_count+1
    elif(num%2 !=0):
        odd_count=odd_count+1
    print("number of even numbers:",even_count)
    print("number of odd numbers:",odd_count)