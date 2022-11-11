import random


def isPrime(n):
    for i in range(2, n):
        if (n % i) == 0:
            return False
    else:
        return True


def assignment1():
    f = open("test.txt", "w")
    prime = open("prime.txt", "w")
    n = int(input("How many numbers are needed to write to the file: "))
    random.seed(1)
    for _ in range(n):
        # random number between 1 and 100
        r = random.randint(1, 100)
        f.write(str(r) + "\n")
        if isPrime(r):
            prime.write(str(r) + "\n")

    f.close()
    prime.close()

    # read file and show

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

    f.close()
    prime.close()


assignment1()