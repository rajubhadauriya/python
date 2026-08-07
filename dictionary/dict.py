# d1={"ram":56,"shyam":78,"raju":50}
# print(type(d1))
# print(len(d1))
# print(min(d1))
# print(max(d1))
# print(sorted(d1))
# print(sorted(d1,reverse=True))
# d1["shiv"]=97           for new add or update
# d1["shyam"]=100
# d2=d1.copy()
# d1.clear()
# print("d1",d1)
# print("d2",d2)
"""print(d1.values())
print(d1.items())
for i,j in d1.items():
     print(i,j)"""

d={}
for i in range(3):
    name=input("enter ur name : ")
    marks=int(input("enter marks : "))
    d[name]=marks
print(d)