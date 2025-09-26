# try:
#     arr1 = list(map(int,input("Enter the array, sep by comma...\n").split(",")))
#     nth_place = int(input("Enter the Number[return the nth largest value]\n"))
#     if nth_place<=0:
#         raise Exception("Oh Man!...Input is Not VALID")
# except Exception as e:
#     print(e)
#     exit(0)

def find_the_nth_largest(array1:list[int],nth_largest:int)->int:
    array_without_duplicate = list(set(array1))#.........................List :: removing dups,reverse sorting
    if nth_largest==1:
        nth_largest=max(array_without_duplicate)
    else:
        for i in range(nth_largest-1):
            array_without_duplicate.remove(max(array_without_duplicate))
        # print(array_without_duplicate)
    nth_number = max(array_without_duplicate)#......................................................Finding Nth Largest with List [index]
    
    # No RULES VIOLATES, Asked not to use in-built sort function in finding max 
    # But i'd used to find the rank in sorted version...
    rank = sorted(array1,reverse=True).index(nth_number)+1#..............Finding Rank with with OLD List
    count_of_nth_number = array1.count(nth_number)#......................Finding the Nth Largest number, repeatation
    
    # PRINTING INFOS
    print(f"{nth_largest}th largest number is.......",nth_number)
    print(f"Rank of the Number..........",rank)
    print(f"Which repeated..............",count_of_nth_number-1)
    
    # RETURNING Nth Largest Number!!!
    return nth_number

# print(sorted([2,3,21,2,3,21,21,3,46,7,75,3,23],reverse=True))
# print(list(sorted(set([2,3,21,2,3,21,21,3,46,7,75,3,23]))))

for i in range(1,6):
    find_the_nth_largest([2,3,21,2,3,21,21,3,46,7,75,3,23],i)
    print("+"*10)

find_the_nth_largest([11,11,11],2)
print("+"*10)
