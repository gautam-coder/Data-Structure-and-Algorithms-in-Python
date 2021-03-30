def power(base,exp):
    assert exp>=0 or int(base)==base;"Fialed to load"
    if exp ==0:
        return 1
    return base*power(base,exp-1)
print(power(-2,4))
