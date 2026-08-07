"""list=[1,2,3,10,11,12]
list.append(20)
print(list[2])
print(type(list))           
list[2]="raju"
list.remove(10)   
list.pop(2)
print(list)"""
# l1=[1,2,3,4,5,6,7,8,9]
# even=[]
# odd=[]
# for i in l1:
#     if i %2==0:
#         even.append(i)
#     else:
#         odd.append(i)

# print("even",even)
# print("odd",odd)
# print(min(l1))
# print(max(l1))
# print(len(l1))
# print(sum(l1))
l1=[1,2,3,4,5,6,7]
prime=[]
notprime=[]
for i in l1:
     if i %2==0:
        notprime.append(i)
     else:
         prime.append(i)

print("prime no is :",prime)
print("not prime is :",notprime)