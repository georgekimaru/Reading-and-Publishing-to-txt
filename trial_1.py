import random


def isPrime(n):
    for i in range(2, n):
        if (n % i) == 0:
            return False
    else:
        return True

# sum of digits of a number
def sumDigit(n):
    s = 0
    while n > 0:
        d = n % 10
        n = n // 10
        s += d
    return s


def assignment():
    f = open("test.txt", "w")
    prime = open("prime.txt", "w")
    n = int(input("How many numbers are needed to write to the file: "))
    # Main lab: random.seed(1)
    # Assignment 1: random.seed(2)
    random.seed(2)
    maxSumOfDigit = -1
    num=0
    for _ in range(n):
        # random number between 1 and 100
        r = random.randint(1, 100)
        f.write(str(r) + "\n")
        if isPrime(r):
            prime.write(str(r) + "\n")
        if sumDigit(r) > maxSumOfDigit:
            maxSumOfDigit = sumDigit(r)
            num=r

    f.close()
    prime.close()

    # read file and output to console

    f = open("test.txt", "r")
    prime = open("prime.txt", "r")

    print("All numbers in the file: ")
    for i in f:
        print(i.strip(), end=" ")

    print("\nThe list of prime numbers: ")
    countPrime = 0
    for i in prime:
        countPrime += 1
        print(i.strip(), end=" ")

    print("\n%d prime numbers found in this file" % countPrime)
    print("%d has a maximum sum of digits = %d" % (num, maxSumOfDigit))
    f.close()
    prime.close()


assignment()