def linecount(filename):
    count = 0
    for line in open(filename):
        count += 1
    return count


if _name_ == '__main__'
    print(linecount('wc.py'))