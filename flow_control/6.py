def cap(str):
    if len(str) >= 10:
        return str.upper()
    else:
        return str
    
print(cap('hi')) # hi
print(cap('i am longer than 10 characters')) # I AM LONGER THAN 10 CHARACTERS