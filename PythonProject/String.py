#
# a = "Sangeethavani Subramanian"
# print(a[::-1])
#
# b = "madam"
# print(b)
# b1 = b[::-1]
# print(b1)
# if b == b1:
#     print("Palindrome")
# else:
#     print("Not Palindrome")
#
# vowels = 0
# consonants =0
# a = "Sangeethavani"
# a.lower()
# for i in a:
#     if i =='a' or i == 'e' or i =='i' or i == 'o' or i == 'u':
#         print(i, end ="")
#         vowels = vowels+1
#     else:
#         consonants = consonants+1
# print(consonants)
# print(vowels)
#
#
# a = "sa ng e et   h a"
# a1 = a.replace(" ","")
# print(a1)
#
# a = "sangeetha"
# a1 = a.capitalize()
# print(a1)
#
#
# str1 = "Listen"
# str2 = "Silent"
#
# a = str1.lower()
# b = str2.lower()
# if sorted(a) == sorted(b):
#     print("Anagram")
# else:
#     print("not Anagram")
#
#
#
# a = "i love python but not java but i am interested to learn java"
# a1 = a.replace("java", "javascript")
# print(a1)
#
#
# a = "sangeethavani"
# dict ={}
# for i in a:
#     dict1 = dict.keys()
#     if i in dict1:
#         dict[i] = dict[i] + 1
#     else:
#         dict[i] = 1
# print(dict)
#
# a ="sangee1326"
# digits = ''.join(char for char in a if char.isdigit())
# print(digits)
#
#
# a ="sangeetha1326"
# for i in a :
#     if i.isdigit():
#         print(i, end ="")
#
# a = "sangeetha1326"
# for i in a:
#     if not i.isdigit():
#         print(i, end =" ")
# #
#
# a = "ssangeethavani"
# for i in a:
#     if a.count(i) == 1:
#         break
# print(i)
#
a = "Ha y"
b = "Ho l i da y"
# a+b = Hapy Holiday
a1 = a.replace(" ",'p')
b1 = b.replace(" ","")
c= a1+b1
print(c)

#
a = "Sangeethavani Subramanian"
a1 = a[0:13]
a2 = a[14:]
a3 = a2[::-1]
print(a1)
print(a3)
print(a1, " ", a3)
#
# a = input("Enter the name: ")
# a1 = a.find(" ")
# b = a[0:a1]
# c = a[a1:]
# d = c[::-1]
# print(b, " ", d)
#
#
# a = input("Enter the name: ")
#
# # Find space position without using .find()
# i = 0
# while i < len(a):
#     if a[i] == ' ':
#         break
#     i += 1
#     print(a)
#
# # Get first name
# b = ""
# j = 0
# while j < i:
#     b += a[j]
#     j += 1
#
# # Get and reverse last name
# c = ""
# k = len(a) - 1
# while k > i:
#     c += a[k]
#     k -= 1
#
# # Print result
# print(b + " " + c)
#
#
