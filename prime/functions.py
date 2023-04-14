def is_prime(num):
    if num < 2:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True
    
            


def prime_range(num):
    for i in range(2, num):
        if is_prime(i):
            yield i


def prime_factors(num):
    ls = []
    while num > 1:
        for i in range(2, num):
            if num % i == 0:
                ls.append(i)
                num //= i
                break
        else:
            ls.append(num)
            return ls
    
        

            


                
            

            

    



        