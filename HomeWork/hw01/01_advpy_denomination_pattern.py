'''
    1,3,4,10
    balance: 16
    ans
    10 x1
    3  x2
'''
def get_best_denomination(balance:int,available_denomination:list)->list:
    answer=[]
    temp_balance=balance
    temp_deno=available_denomination
    flag=True
    while True:
        if temp_balance<=0:
            break
        if temp_balance==1:
            answer.append(1)
            break
        if temp_balance<sum(available_denomination)//2 and flag:
            for i in list(reversed(available_denomination))[:len(available_denomination)-1]:
                if temp_balance%i==0:
                    temp=temp_balance//i
                    answer.extend([i]*temp)
                    temp_balance%=i
                    break
            else:
                flag=False
        else:
            if temp_balance >= max(temp_deno):
                temp=temp_balance//max(temp_deno)
                answer.extend([max(temp_deno)]*temp)
                temp_balance%=max(temp_deno)
            else:
                temp_deno.remove(max(temp_deno))
    print(balance,"--->",answer)
    flag=True
    return answer

get_best_denomination(26,[1,3,4,10])
for i in range(1,20):
    get_best_denomination(i,[1,3,4,10])