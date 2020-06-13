def primes_dict(n):
    #
    prime_list = []
    non_prime_list = []
    k_list = []
    number_dict = {
        i: None for i in reversed(range(n + 1))}
    #
    del number_dict[0]
    del number_dict[1]
    while True:
        # get prime
        prime, _ = number_dict.popitem()
        prime_list.append(prime)
        if prime * prime > n:
            break

        # get non primes
        non_prime_list.append(prime * prime)
        while True:
            k, _ = number_dict.popitem()
            k_list.append(k)
            if prime * k > n:
                break
            non_prime_list.append(prime * k)

        while k_list:
            number_dict[k_list.pop()] = None

        # delete non prime
        while non_prime_list:
            del number_dict[non_prime_list.pop()]

    while number_dict:
        prime, _ = number_dict.popitem()
        prime_list.append(prime)

    return prime_list

ans={}
from math import sqrt
n=846144216519
cheat_list=primes_dict(int(sqrt(n)))
if (sqrt(n)//1 == sqrt(n)):
    odd=True
else:
    odd=False
def primesearch(N):
    for p in cheat_list:
        solvd=False
        if N%p==0:
            solvd=True
            if not str(p) in ans.keys():
                ans[str(p)]=1
            else:
                ans[str(p)]=ans[str(p)]+1
            primesearch(N//p)
            break
primesearch(n)
print(ans)
if odd:
    print(sum(ans.values())*2-1)
else:
    print(sum(ans.values())*2)