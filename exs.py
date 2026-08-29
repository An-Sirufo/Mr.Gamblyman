""" #### ex1
num1 = int(input("First num: "))
num2 = int(input("Second num: "))
if num1 * num2 <= 1000:
   print(num1 * num2)
else:
   print (num1 + num2)


#### ex2
j = 0
for i in range(10):
   print(f"previous num: {j}")
   print(f"current num: {i}")
   print(f"sum: {i+j}")
   j = i


#### ex3
p = "mesmerizing"
for i in range(len(p)):
   if i % 2 == 0:
       print(p[i])


## ex4
def remove_chars(word, upto):
   print('Original string:', word)
   ans = word[upto:]
   return ans
print(remove_chars("saymyname", 5))
 """
 
## ex5
a = 1
b = 2
print(f"a = {a}, b = {b}")
a, b = b, a
print(f"a = {a}, b = {b}")
