# a="python"
# print("I love",a)
# v_count=0
# c_count = 0
# v="sangeethavani"
# for i in v:
#   if i=="a" or i=="e" or i=="i" or i=="o"or i=="u":
#     v_count = v_count+1
#
#   else:
#       c_count = c_count+1
#
# print("v=", v_count)
# print("c=",c_count)
a=int(input())
if a>1 and a<10 :
    if a%2==0:
        print("even")
    else:
        print("odd")
elif a>10 and a<40:
  if a%2==0 :
     print("even 10")
  else:
     print("odd 10")
else:
    if a%2==0 :
        print("even 40")
    else:
        print("odd 40")

# i=1
# while i<6:
#     print(i, end =",")
#     i=i+1
# b="python"
# a="I love python"
# print(a)
# print("I love {}".format(b))
# print(f"I like {b} very much")

# a="madhu sangeetha"
# print(a[0:5])
# print(a[6:15])
# print(a[::-1])

# num=[1,2,3,4,5]
# print(num)
# num.append(4)
# print(num)
# num.remove(3)
# print(num)
# num_1=tuple(num)
# print(num_1)
# num_2=list(num_1)
# print(num_2)
# num_2.append(7)
# print(num_2)

student={"name":"madhu","age":20,"course":"python"}
print(student)
print(student.keys())
print(student.values())
