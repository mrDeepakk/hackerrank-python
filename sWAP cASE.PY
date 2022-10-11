def swap_case(s):
    result=""
    for i in s:
        if i.isupper():
            i=i.lower()
        else:
            i=i.upper()
        result+="".join(i)
    return result
    # other wise 
    #s.swapcase()
if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)