# number = int(input("enter number to reverse : "))
# print(f"Number is :{number}")
# reversedNum = int(str(number)[::-1])
# print(f"Reversed Number is {reversedNum}")

# a, b = 0, 1
# while a < 10:
#     print(a)
#     a, b = b, a + b

# iterative method
# n = int(input("please give a number for fibonacci series : "))
# a, b = 0, 1
# print("fibonacci series are : ")
# for i in range(0, n):
#     if i <= 1:
#         result = i
#     else:
#         result = a + b
#         a = b
#         b = result
# print(result)

# # recursive
# n = int(input("please give a number for fibonacci series : "))
# first, second = 0, 1

# def fibonacci(num):
#     if num == 0:
#         return 0
#     elif num == 1:
#         return 1
#     else:
#         return fibonacci(num-1)+fibonacci(num-2)

# print("fibonacci series are : ")
# for i in range(0, n):
#     print(fibonacci(i))

# Armstrong number program using while loop
# num = int(input("Please give a number: "))
# sum = 0
# temp = num
# count = len(str(num))
# while temp > 0:
#     digit = temp % 10
#     sum += digit ** count
#     temp //= 10 #
# if num == sum:
#     print("Given ",num, "is an Armstrong number")
# else:
#     print("Given ",num, "is not an Armstrong number")

# check prime number
# num = int(input("Enter a number : "))
# if num % 2 != 0:
#     print(f"{num} is Prime")

# n = int(input("please give a number : "))
# i, temp = 0, 0
# for i in range(2, n//2):
#     if n % i == 0:
#         temp = 1
#         break
# if temp == 1:
#     print("given number is not prime")
# else:
#     print("given number is prime")

# number = int(input("enter number : "))
# print(f"Number is :{number}")
# reversedNum = int(str(number)[::-1])

# if (number == reversedNum):
#     print(f"{number} is palindrome")
# else:
#     print(f"{number} is not palindrome")
#  using iterative method
# n = int(input("please give a number : "))
# reverse, temp = 0, n
# while temp != 0:
#     reverse = reverse*10 + temp % 10
#     temp = temp//10
# if reverse == n:
#     print("number is palindrom")
# else:
#     print("number is not palindrom")

# n1 = int(input("please give first number n1: "))
# n2 = int(input("please give second number n2: "))
# n3 = int(input("please give third number n3: "))
# if n1 <= n2 and n1 <= n3:
#     print(" n1 is smallest")
# if n2 <= n1 and n2 <= n3:
#     print(" n2 is smallest")
# if n3 <= n1 and n3 <= n2:
#     print("n3 is smallest")

# num = int(input("please give a number : "))
# while (num > 0):
#     j = num % 10
#     if j != 0 and j != 1:
#         print("num is not binary")
#         break
#     num = num//10
#     if num == 0:
#         print("num is binary")

a = int(input("please give first number a: "))
b = int(input("please give second number b: "))
a = a-b
b = a+b
a = b-a
print("After swapping")
print("value of a is : ", a)
print("value of b is : ", b)
