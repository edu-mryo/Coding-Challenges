# Description: Write a function that takes an integer as input and returns True if it's prime,
# and False otherwise. A prime number is a number greater than 1 that is only divisible by 1 and itself.


def check_prime():
    n = int(input("Give me number: "))
    if n > 1:
        for i in range(2,(n//2)+1):
            if (n % i)==0:
                return False, 
        else:
            return True, 
    else:
        return False, 


        
def main():
    if check_prime():
         print("The given number is  a prime number")
    else:
        print("The given number is not a prime number")


if __name__== '__main__':
    main()

        
