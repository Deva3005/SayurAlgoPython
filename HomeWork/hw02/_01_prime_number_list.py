# Prime Numbers Challenge
#     Write a program to:
#         Check if input number N is prime..................[ok]
#         Print all prime numbers up to N...................[ok]
#         Find the sum of all prime numbers less than N.....[ok]

def is_prime(number:int)->bool:
    try:
        if (number <= 0):
            raise Exception("Prime Number should be Greater than 0")
    except Exception as e:
        print(e)
    if number==1:
        return False
    if number==2:
        return True
    for i in range(2,int(number**0.5)+1): #....For Optimization...number**0.5
        if number%i==0:
            return False
        pass
    else:
        return True
    
def prime_list_collection(number:int)->str|tuple:
    print("\nThe Number is ",number)
    if is_prime(number):
        answer_list=[]   
        for i in range(1,number+1):
            if is_prime(i):
                answer_list.append(i)
        return answer_list[:-1],f"The Sum is {sum(answer_list[:-1])}"
    else:
        return f"{number} -> This is not a PRIME Number...."
        

print(prime_list_collection(10))
print(prime_list_collection(5))
print(prime_list_collection(53))
print(prime_list_collection(101))