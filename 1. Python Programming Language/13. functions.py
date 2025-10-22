## why functions?(Interview Question)
# 1. to make code more readable
# 2. to make code more efficient
# 3. to make code more maintainable
# 4. to make code more reusable
# 5. to make code more extensible

##functions

def welcome(msg)->str:
    '''
    Description : This function is used to welcome the user

    Return : This function returns a welcome message
    '''
    return msg

msg=welcome('hello world')
print(msg + ' How are you') 



## function to add even and odd number


def even_odd_sum(lst):
    '''
     Description: This function will add even and odd number in a list
    Return : This function will return the sum of even and odd number in a list
    '''
    even_sum=0
    odd_sum=0
    for i in lst:
        if i%2==0:
            even_sum+=i
        else:
            odd_sum+=i
    return even_sum,odd_sum
    
sum1,sum2=even_odd_sum([1,2,3,34,45,2,3,8,9])
print(sum1,sum2)
