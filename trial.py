from sympy import *
import random


def write_numbers():
 with open('test.txt', 'w') as file:
  x = int(input("How many numbers are needed to write to the file: "))
  for i in range(x):
   random.seed()
   nums = random.randint(1, 100)
   print(nums, end=" ")
   # print(nums)
   file.write(str(nums) + " ")

 return nums

def prime_numbers():
 nums = write_numbers()
 print(type(nums))
 print(nums)
 with open('test.txt', 'r') as input:
  with open('prime.txt', 'w') as output:
   for line in input:
    output.write(line)
 

# write_numbers()
prime_numbers()

 # my_list=[]
 # my_file = open("test.txt", 'rt')
 # content = my_file.read()
 # my_file.close()
 # content = content.split()

 

 # my_list.append(content)
 # print(type(my_list))
 # print(my_list[1])
 # for i in my_list:
 #  print(i)
 #  if isprime(i) == True:
 #   print(i)
 #   with open('prime.txt', 'w') as file:
 #    file.write(str(i) + " ")




