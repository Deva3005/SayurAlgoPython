def sum_to_single_digit(number:int)->int:
    if(number<=0):
        print("INVALID NUMBER TO PROCESS")
        exit(0)
    while number>=10:
        number=sum(map(int,list(str(number))))
    print(number)
    return number
sum_to_single_digit(5703)