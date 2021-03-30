def sumOfDigit(n):
    assert n>=0 or int(n)==n;"Bhaag vha se"
    if n==0:
        return 0
    else:
        return int(n)%10+sumOfDigit(int(n)/10)
print(sumOfDigit(1111112))
