def split_and_join(line):
    word=line.split(" ")
    c='-'.join(word)
    return c
if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)